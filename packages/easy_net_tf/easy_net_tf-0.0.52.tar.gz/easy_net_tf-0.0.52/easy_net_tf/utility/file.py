import random
import os

from pathlib import Path


class UtilityFile:
    @staticmethod
    def _line_generator(file_path):
        """
        get a line generator of a file
        :param file_path:
        :return:
        """
        with file_path.open('r') as file:
            while True:
                line = file.readline()
                if line:
                    yield line
                else:
                    return

    @staticmethod
    def _line_shuffle(file_path):
        """
        first get all lines in file, then shuffle, finally save to file again.
        :param file_path:
        :return:
        """
        # read
        with file_path.open('r') as file:
            info_list = file.readlines()

        # shuffle
        random.shuffle(info_list)

        # write
        with file_path.open('w') as file:
            for info in info_list:
                file.write(info)

    @staticmethod
    def get_file_list(files_dir, shuffle):
        """

        :param files_dir:
        :param shuffle:
        :return:
        """

        file_list = os.listdir(files_dir.__str__())

        if shuffle:
            random.shuffle(file_list)

        return file_list

    @staticmethod
    def get_line_generator(file_path,
                           shuffle):
        """

        :param file_path:
        :param shuffle: True: first shuffle and save, then return generator; False: return generator
        :return:
        """

        if shuffle:
            UtilityFile._line_shuffle(file_path)

        return UtilityFile._line_generator(file_path)

    @staticmethod
    def list_2_file(file_path,
                    info_list,
                    mode='w'):
        """
        save a list of info to a file
        :param file_path: Path
        :param info_list: a list of info to save
        :param mode: file mode
        :return:
        """
        with file_path.open(mode) as file:
            for info in info_list:
                file.write(str(info) + '\n')


if __name__ == '__main__':
    save_list = ['net',
                 0.88,
                 128,
                 'hello',
                 False,
                 True,
                 None]

    UtilityFile.list_2_file(Path('test.txt'), save_list)
