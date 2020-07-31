from datasets.BaseDataset import BaseDataset


class RHD(BaseDataset):
    @classmethod
    def get_class_colors(*args):
        return [[255, 0, 0], [0, 0, 255]]

    @classmethod
    def get_class_names(*args):
        # class counting(gtFine)
        return ['Left', 'Right']
