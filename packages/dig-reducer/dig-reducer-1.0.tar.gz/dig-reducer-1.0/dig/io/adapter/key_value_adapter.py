
class KeyValueAdapter(object):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def get(self, record_id):
        raise NotImplementedError

    def set(self, record_id, record):
        raise NotImplementedError

    def __iter__(self):
        return self.__next__()

    def __next__(self):
        """iterator is not required in adapter"""
        pass
