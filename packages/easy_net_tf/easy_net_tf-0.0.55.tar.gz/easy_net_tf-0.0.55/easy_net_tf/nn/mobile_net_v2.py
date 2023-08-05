import numpy
import tensorflow as tf

from easy_net_tf.utility.variable import UtilityVariable


class MobileNetV2:
    VALID = 'VALID'
    SAME = 'SAME'

    def __init__(self,
                 batch_input,
                 dilate_number,
                 filter_size,
                 channels_out,
                 stride,
                 add_bias,
                 add_residual=False,
                 padding=SAME,
                 dilate_active_func=tf.nn.leaky_relu,
                 depth_active_func=tf.nn.leaky_relu,
                 name=''):
        """
        :param batch_input: a Tensor [batch, height, width, channel]
        :param dilate_number: if 'None', become MobileNet V1 without output activation
        :param filter_size:
        :param channels_out:
        :param stride:
        :param add_bias: True: add; False: not add
        :param add_residual: be sure input [height, width] = output [height, width]. stride=1 and padding='SAME'
        :param padding:
        :param dilate_active_func: active function for dilatation.
        :param depth_active_func: active function for depth-wise.
        :param name: layer name
        """

        """
        prepare
        """
        if batch_input is None:
            assert 'Error: [%s.%s] batch_image can not be ''None''.' % (MobileNetV2.__name__,
                                                                        MobileNetV2.__init__.__name__)
        else:
            _, _height_in, _width_in, _channels_in = batch_input.shape

            self.height_in = _height_in.value
            self.width_in = _width_in.value
            self.channels_in = _channels_in.value
            assert self.channels_in is not None, '[%s,%s] ' \
                                                 'the channels of input must be explicit, ' \
                                                 'otherwise filters can not be initialized.' % (MobileNetV2.__name__,
                                                                                                MobileNetV2.__init__.__name__)

        self.channels_out = channels_out

        self.dilate_number = dilate_number

        self.filter_size = filter_size

        self.dilate_active_func = dilate_active_func
        self.dilate_active_func_name = 'None' \
            if self.dilate_active_func is None \
            else self.dilate_active_func.__name__

        self.depth_active_func = depth_active_func
        self.depth_active_func_name = 'None' \
            if self.depth_active_func is None \
            else self.depth_active_func.__name__

        self.stride = stride

        if add_residual \
                and (stride != 1
                     or padding is not MobileNetV2.SAME):
            add_residual = False
            print('Error: '
                  '[%s.%s] '
                  'if residual added, '
                  'be sure stride = 1 and padding = %s.%s' % (MobileNetV2.__name__,
                                                              MobileNetV2.__init__.__name__,
                                                              MobileNetV2.__name__,
                                                              MobileNetV2.SAME))
        self.add_residual = add_residual

        self.add_bias = add_bias
        self.padding = padding

        """
        initialize filter
        """
        self.dilate_filter, \
        self.depth_filter, \
        self.compress_filter, \
        self.residual_filter, \
        self.bias = self._initialize_variable(name=name)

        """
        calculation
        """
        self.features = self._calculate(batch_input)

    def _initialize_variable(self, name):
        """
        initialize variable
        :return:
        """

        channel_multiplier = 1

        """
        dilatation_filter
        """
        if self.dilate_number is None:
            dilatation_filter = None
            self.dilate_number = self.channels_in
        else:
            dilatation_filter = UtilityVariable.initialize_weight(
                [1,
                 1,
                 self.channels_in,
                 self.dilate_number],
                name='%s_mn/dilate' % name
            )

        """
        depth-wise_filter
        """
        depthwise_filter = UtilityVariable.initialize_weight(
            [self.filter_size,
             self.filter_size,
             self.dilate_number,
             channel_multiplier],
            name='%s_mn/depth' % name
        )

        """
        compress_filter
        """
        compress_filter = UtilityVariable.initialize_weight(
            [1,
             1,
             self.dilate_number * channel_multiplier,
             self.channels_out],
            name='%s_mn/compress' % name
        )

        """
        residual_filter
        """
        if self.add_residual and self.channels_in != self.channels_out:
            residual_filter = UtilityVariable.initialize_weight(
                [1,
                 1,
                 self.channels_in,
                 self.channels_out],
                name='%s_mn/residual' % name
            )
        else:
            residual_filter = None

        """
        bias
        """
        if self.add_bias:
            bias = UtilityVariable.initialize_bias(
                [self.channels_out],
                name='%s_mn/bias' % name
            )
        else:
            bias = None

        return dilatation_filter, \
               depthwise_filter, \
               compress_filter, \
               residual_filter, \
               bias

    def _calculate(self,
                   batch_input):
        """
        No activation function applied on output.
        :param batch_input:
        :return:
        """

        """
        dilate
        """
        if self.dilate_filter is not None:

            dilatation_o = tf.nn.conv2d(input=batch_input,
                                        filter=self.dilate_filter,
                                        strides=[1, 1, 1, 1],
                                        padding='SAME')

            if self.depth_active_func is not None:
                dilatation_o = self.dilate_active_func(dilatation_o)

        else:
            dilatation_o = batch_input

        """
        depth-wise
        """
        convolution_o = tf.nn.depthwise_conv2d(input=dilatation_o,
                                               filter=self.depth_filter,
                                               strides=[1, self.stride, self.stride, 1],
                                               padding=self.padding)
        if self.depth_active_func is not None:
            convolution_o = self.depth_active_func(convolution_o)

        """
        compress
        """
        compress_o = tf.nn.conv2d(input=convolution_o,
                                  filter=self.compress_filter,
                                  strides=[1, 1, 1, 1],
                                  padding='SAME')

        """
        residual block
        """
        if self.add_residual is True:
            if self.residual_filter is not None:
                batch_input = tf.nn.conv2d(input=batch_input,
                                           filter=self.residual_filter,
                                           strides=[1, 1, 1, 1],
                                           padding='SAME')

            batch_output = tf.add(compress_o, batch_input)
        else:
            batch_output = compress_o

        """
        bias
        """
        if self.bias is not None:
            batch_output += self.bias

        return batch_output

    def get_features(self):
        """
        :return: image out
        """
        return self.features

    def get_variables(self, sess=None, save_dir=None):
        """
        :return: variable
        """
        if sess is None:
            return self.dilate_filter, \
                   self.depth_filter, \
                   self.compress_filter, \
                   self.residual_filter, \
                   self.bias
        else:
            dilate_filter = None if self.dilate_filter is None else sess.run(self.dilate_filter)
            depth_filter = None if self.depth_filter is None else sess.run(self.depth_filter)
            compress_filter = None if self.compress_filter is None else sess.run(self.compress_filter)
            residual_filter = None if self.residual_filter is None else sess.run(self.residual_filter)
            bias = None if self.bias is None else sess.run(self.bias)

            if save_dir is not None:
                if dilate_filter is not None:
                    shape = '[%d,%d,%d,%d]' % dilate_filter.shape
                    numpy.savetxt(fname='%s/mn-dilate-%s.txt' % (save_dir, shape),
                                  X=numpy.reshape(dilate_filter, [-1]),
                                  header='%s: dilatation filter' % MobileNetV2.__name__,
                                  footer='shape: %s' % shape)

                    numpy.save(file='%s/mn-dilate-%s.npy' % (save_dir, shape),
                               arr=dilate_filter)

                if depth_filter is not None:
                    shape = '[%d,%d,%d,%d]' % depth_filter.shape
                    numpy.savetxt(fname='%s/mn-depthwise-%s.txt' % (save_dir, shape),
                                  X=numpy.reshape(depth_filter, [-1]),
                                  header='%s: depthwise filter' % MobileNetV2.__name__,
                                  footer='shape: %s' % shape)

                    numpy.save(file='%s/mn-depthwise-%s.npy' % (save_dir, shape),
                               arr=depth_filter)

                if compress_filter is not None:
                    shape = '[%d,%d,%d,%d]' % compress_filter.shape
                    numpy.savetxt(fname='%s/mn-compress-%s.txt' % (save_dir, shape),
                                  X=numpy.reshape(compress_filter, [-1]),
                                  header='%s: compress filter' % MobileNetV2.__name__,
                                  footer='shape: %s' % shape)

                    numpy.save(file='%s/mn-compress-%s.npy' % (save_dir, shape),
                               arr=compress_filter)

                if residual_filter is not None:
                    shape = '[%d,%d,%d,%d]' % residual_filter.shape
                    numpy.savetxt(fname='%s/mn-residual-%s.txt' % (save_dir, shape),
                                  X=numpy.reshape(residual_filter, [-1]),
                                  header='%s: residual filter' % MobileNetV2.__name__,
                                  footer='shape: %s' % shape)

                    numpy.save(file='%s/mn-residual-%s.npy' % (save_dir, shape),
                               arr=residual_filter)

                if bias is not None:
                    shape = '[%d]' % bias.shape
                    numpy.savetxt(fname='%s/mn-bias-%s.txt' % (save_dir, shape),
                                  X=bias,
                                  header='%s: bias' % MobileNetV2.__name__,
                                  footer='shape: %s' % shape)

                    numpy.save(file='%s/mn-bias-%s.npy' % (save_dir, shape),
                               arr=bias)

            return dilate_filter, \
                   depth_filter, \
                   compress_filter, \
                   residual_filter, \
                   bias

    def get_config(self):
        """
        export config as a list
        :return:
        """

        """
        multiplication calculation
        """
        multiplication_dilate, \
        multiplication_depth, \
        multiplication_compress, \
        multiplication_residual = self.get_multiplication_amount(height_in=self.height_in,
                                                                 width_in=self.width_in,
                                                                 dilate_number=self.dilate_number,
                                                                 channels_in=self.channels_in,
                                                                 channels_out=self.channels_out,
                                                                 filter_size=self.filter_size,
                                                                 stride=self.stride,
                                                                 add_residual=self.add_residual,
                                                                 padding=self.padding)

        config = [
            '- MobileNet V2\n',
            '- filter size: %d\n' % self.filter_size,
            '- channels in: %d\n' % self.channels_in,
            '- channels out: %d\n' % self.channels_out,
            '- dilatation: %d\n' % self.dilate_number,
            '- dilate active function: %s\n' % self.dilate_active_func_name,
            '- depth-wise active function: %s\n' % self.depth_active_func_name,
            '- stride: %d\n' % self.stride,
            '- add residual: %s\n' % self.add_residual,
            '- add bias: %s\n' % self.add_bias,
            '- padding: %s\n' % self.padding,
            '- multiplicative amount: %d\n' % (multiplication_dilate
                                               + multiplication_depth
                                               + multiplication_compress
                                               + multiplication_residual),
            '   - dilatation: %d\n' % multiplication_dilate,
            '   - depth-wise: %d\n' % multiplication_depth,
            '   - compress: %d\n' % multiplication_compress,
            '   - residual: %d\n' % multiplication_residual
        ]

        return config

    @staticmethod
    def get_multiplication_amount(height_in,
                                  width_in,
                                  dilate_number,
                                  channels_in,
                                  channels_out,
                                  filter_size,
                                  stride,
                                  add_residual,
                                  padding):

        if height_in is None or width_in is None:
            return -1, -1, -1, -1

        else:
            if padding == MobileNetV2.VALID:
                height_out = round((height_in - filter_size + 1) / stride)
                width_out = round((width_in - filter_size + 1) / stride)
            elif padding == MobileNetV2.SAME:
                height_out = round(height_in / stride)
                width_out = round(width_in / stride)
            else:
                height_out = 0
                width_out = 0
                print('Error: '
                      '[%s.%s] '
                      'wrong padding mode.' % (MobileNetV2.__name__,
                                               MobileNetV2.__init__.__name__))
            if dilate_number is None:
                dilate = 0
                depth = height_out * width_out * filter_size * filter_size * channels_in
                compress = height_out * width_out * channels_in * channels_out
            else:
                dilate = height_in * width_in * channels_in * dilate_number
                depth = height_out * width_out * filter_size * filter_size * dilate_number
                compress = height_out * width_out * dilate_number * channels_out

            if add_residual and channels_in != channels_out:
                residual = height_in * width_out * channels_in * channels_out
            else:
                residual = 0

            return dilate, depth, compress, residual


if __name__ == '__main__':
    from easy_net_tf.utility.file import UtilityFile
    from pathlib import Path

    image = numpy.array([[[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                          [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                          [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                          [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                          [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]]],
                        dtype=numpy.float32)

    image_ph = tf.placeholder(dtype=tf.float32, shape=[None, None, None, None])

    mn = MobileNetV2(batch_input=image_ph,
                     dilate_number=1,
                     filter_size=3,
                     channels_out=15,
                     dilate_active_func=tf.nn.relu6,
                     depth_active_func=tf.nn.leaky_relu,
                     stride=1,
                     add_residual=True,
                     add_bias=False,
                     padding=MobileNetV2.SAME)

    UtilityFile.save_str_list(Path('test-mn.md'), mn.get_config())
