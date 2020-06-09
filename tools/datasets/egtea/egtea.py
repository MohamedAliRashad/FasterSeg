from datasets.BaseDataset import BaseDataset


class EGTEA(BaseDataset):
    @classmethod
    def get_class_colors(*args):
        return [[255, 255, 255]]

    @classmethod
    def get_class_names(*args):
        return ['Hands']
