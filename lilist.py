class LiList(list):
    def __getitem__(self, item):
        try:
            return list.__getitem__(self, item)
        except TypeError:
            if not isinstance(item, float):
                raise
            return (1. - item % 1) * self[int(item)] + (item % 1) * self[int(item + 1)]
