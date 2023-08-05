from dig.utils.data_types import *


class JSONLDComparator(object):

    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def compare(self, object1, object2):
        if is_str(object1) and is_str(object2):
            return str_compare(object1, object2)

        if is_dict(object1) and is_str(object2):
            if "uri" in object1:
                return str_compare(object1["uri"], object2)
            elif "@id" in object1:
                return str_compare(object1["@id"], object2)
            else:
                return str_compare(str(object1), object2)

        if is_str(object1) and is_dict(object2):
            if "uri" in object2:
                return str_compare(object1,  object2["uri"])
            elif "@id" in object2:
                return str_compare(object1, object2["@id"])
            else:
                return str_compare(object1, str(object2))

        if is_dict(object1) and is_dict(object2):
            if "uri" in object1 and "uri" in object2:
                return str_compare(object1["uri"], object2["uri"])
            elif "@id" in object1 and "@id" in object2:
                return str_compare(object1["@id"], object2["@id"])
            else:
                return str_compare(str(object1), str(object2))

        return 0

    def get_id(self, object):
        if "uri" in object:
            return object["uri"]
        elif "@id" in object:
            return object["@id"]
        return None