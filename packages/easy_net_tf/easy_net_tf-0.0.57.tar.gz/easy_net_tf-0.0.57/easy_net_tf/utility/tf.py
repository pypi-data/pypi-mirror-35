import os
from pathlib import Path
import tkinter
import tkinter.filedialog
import tkinter.dialog

import tensorflow as tf
from tensorflow.python import pywrap_tensorflow

from easy_net_tf.utility.dialog import UtilityDialog
from easy_net_tf.utility.file import UtilityFile


class UtilityTf:
    @staticmethod
    def latest_checkpoint(model_dir=None, initial_dir='', hint=''):
        """

        :param model_dir:
        :param initial_dir:
        :param hint:
        :return:
        """
        if model_dir is None:

            model_dir = UtilityDialog.tk_avoid(func=tkinter.filedialog.askdirectory,
                                               hint=hint,
                                               initial_dir=initial_dir)
            if type(model_dir) == tuple:
                model_dir = ''

        return tf.train.latest_checkpoint(model_dir)

    @staticmethod
    def select_checkpoint(initial_dir='', hint=''):
        path = UtilityDialog.tk_avoid(tkinter.filedialog.askopenfilename,
                                      hint=hint,
                                      initial_dir=initial_dir)
        path = Path(path)
        path = path.parent / path.stem

        return path.__str__()

    @staticmethod
    def get_variables(checkpoint_path):
        """

        :param checkpoint_path:
        :return:
        """
        reader = pywrap_tensorflow.NewCheckpointReader(checkpoint_path)
        var_to_shape_map = reader.get_variable_to_shape_map()

        result = list()
        for key in var_to_shape_map:
            result.append('%s' % key)
            result.append(reader.get_tensor(key))

        return result

    @staticmethod
    def save_checkpoint(sess,
                        saver_ob,
                        new_merits,
                        save_dir,
                        net_name,
                        global_step,
                        number=5):
        """
        save a better checkpoint according to comparison of a list of merits
        :param sess:
        :param saver_ob: tensorflow model saver object: tf.train.Saver()
        :param new_merits: a list of merits for comparing
        :param save_dir: Path format
        :param net_name:
        :param global_step:
        :param number:
        :return: True: a new model saved; False: new model is not saved
        """

        # .model_comparison not exist
        if (save_dir / '.model_comparison').exists() is False:

            # update .model_comparision file
            with (save_dir / '.model_comparison').open('w') as file:
                file.write('%s-%d;' % (net_name, global_step) + ';'.join(map(str, new_merits)) + '\n')

            # save new model
            saver_ob.save(
                sess=sess,
                save_path=(save_dir / net_name).__str__(),
                global_step=global_step
            )
            return True
        # .model_comparison exist
        else:
            with (save_dir / '.model_comparison').open('r') as file:
                caches = file.readlines()

            if len(caches) < number:

                # update .model_comparison file
                with (save_dir / '.model_comparison').open('a') as file:
                    file.write('%s-%d;' % (net_name, global_step) + ';'.join(map(str, new_merits)) + '\n')

                # save new model
                saver_ob.save(
                    sess=sess,
                    save_path=(save_dir / net_name).__str__(),
                    global_step=global_step
                )
                return True

            else:
                for cache_index, cache in enumerate(caches):
                    records = cache.strip().split(';')
                    old_name = records.pop(0)
                    old_merits = list(map(float, records))

                    """
                    if all new merits greater than old merits
                    """
                    replace = True
                    for i, old_merit in enumerate(old_merits):
                        if new_merits[i] <= old_merit:
                            replace = False
                            break

                    if replace:
                        """
                        update .model_comparison file
                        """
                        caches[cache_index] = '%s-%d;' % (net_name, global_step) + ';'.join(map(str, new_merits)) + '\n'
                        UtilityFile.save_str_list(file_path=save_dir / '.model_comparison',
                                                  info_list=caches,
                                                  mode='w')

                        """
                        update checkpoint file
                        """
                        # read checkpoint file
                        with (save_dir / 'checkpoint').open('r') as file_checkpoint:
                            checkpoints = file_checkpoint.readlines()

                        for index_cp in range(len(checkpoints)):
                            if index_cp == 0:
                                continue

                            if checkpoints[index_cp].find(old_name) >= 0:
                                checkpoints.pop(index_cp)
                                break

                        # rewrite checkpoint file
                        UtilityFile.save_str_list(file_path=save_dir / 'checkpoint',
                                                  info_list=checkpoints,
                                                  mode='w')

                        """
                        delete records file
                        """
                        file_list = UtilityFile.get_file_list(files_dir=save_dir,
                                                              shuffle=False)
                        for filename in file_list:
                            if filename.find(old_name) >= 0:
                                os.remove((save_dir / filename).__str__())

                        """
                        save new model
                        """
                        saver_ob.save(
                            sess=sess,
                            save_path=(save_dir / net_name).__str__(),
                            global_step=global_step
                        )

                        return True

                return False


if __name__ == '__main__':
    # path = UtilityTf.latest_checkpoint(hint='hello world')

    checkpoint_path = UtilityTf.select_checkpoint(hint='Select a checkpoint file')
    variables = UtilityTf.get_variables(checkpoint_path=checkpoint_path)

    print(variables)
