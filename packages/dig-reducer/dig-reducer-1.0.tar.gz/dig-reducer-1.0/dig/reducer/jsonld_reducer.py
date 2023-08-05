from dig.reducer.jsonld_comparator import JSONLDComparator
from dig.utils.data_types import *
from dig.io.adapter import MemoryAdapter, HBaseAdapter


class JSONLDReducer(object):

    def __init__(self, **kwargs):
        """
          Initializer to setup variables

          Args:
          **kwargs: Arbitrary keyword arguments

          Returns:
            None
        """
        self._kwargs = kwargs

        if 'provenance_properties' in self._kwargs:
            (self._provenance_props) = self._kwargs['provenance_properties']
        else:
            self._provenance_props = {}

        self._comparator = JSONLDComparator()

        if 'adapter' in self._kwargs:
            self._adapter = self._kwargs['adapter']
        else:
            self._adapter = MemoryAdapter()

    def merge_json_objects(self, left, right):
        self._merge_json_objects_inner(left, right)
        return left

    def merge_json_object(self, object):
        object_id = self._get_object_id(object)
        if object_id is not None:
            cached_obj = self._adapter.get(object_id)
            if cached_obj is not None:
                self._merge_json_objects_inner(cached_obj, object)
                self._adapter.set(object_id, cached_obj)
            else:
                self._adapter.set(object_id, object)
        return object

    def load_json_object(self, object):
        object_id = self._get_object_id(object)
        if object_id is not None:
            self._adapter.set(object_id, object)

    def _get_object_id(self, object):
        object_id = self._comparator.get_id(object)
        if object_id is not None:
             return object_id.encode('utf-8', 'ignore')
        return None
    
    def _merge_json_objects_inner(self, left, right):
        right_added = False

        #Move provenance properties to the end so we know if we need to combine them
        keys = list(right.keys())
        for prov_prop in self._provenance_props:
            if prov_prop in keys:
                keys.remove(prov_prop)
                keys.append(prov_prop)

        #Start merging into left
        for key in keys:
            # print("Start key", key)
            is_prov_key = self._is_prov_key(key)
            if not key in left:     #If key not in left, get the object from right and add it
                value = right[key]
                left[key] = value
                if is_str(value) and not is_prov_key:
                    right_added = True

            else:
                #It exists in both left and right, convert to array and then merge them
                value_left = to_list(left[key])
                value_right = to_list(right[key])
                new_added = self._merge_arrays(left, key, right_added, value_left, value_right)
                if not is_prov_key:
                    right_added = right_added | new_added
            # print(right_added, left)
        return right_added

    def _merge_arrays(self, left, key, new_addded, value_arr_left, value_arr_right):
        prov_date_prop = False
        is_prov_key = self._is_prov_key(key)

        #If it is a provenance property and no new information is added, we do not need to add the property
        if is_prov_key and not new_addded:
            prov_type = self._provenance_props[key]
            if prov_type == "date":
                #For dates we still need the min/max dates
                prov_date_prop = True
            else:
                return False

        left_idx = 0
        right_idx = 0
        right_added = False
        final_arr = []

        while left_idx < len(value_arr_left) and right_idx < len(value_arr_right):
            result = self._comparator.compare(value_arr_left[left_idx], value_arr_right[right_idx])
            if result < 0:
                final_arr.append(value_arr_left[left_idx])
                left_idx += 1
            elif result == 0:
                #the strings or objects are the same
                object_left = value_arr_left[left_idx]
                left_idx += 1
                object_right = value_arr_right[right_idx]
                right_idx += 1
                (is_right_added, merged_obj) = self._merge_strings_and_json_objects(object_left, object_right)
                right_added = right_added | is_right_added
                final_arr.append(merged_obj)
            else:
                if is_str(value_arr_right[right_idx]):
                    right_added = True
                final_arr.append(value_arr_right[right_idx])
                right_idx += 1


        while left_idx < len(value_arr_left):
            final_arr.append(value_arr_left[left_idx])
            left_idx += 1

        while right_idx < len(value_arr_right):
            if is_str(value_arr_right[right_idx]):
                right_added = True
            final_arr.append(value_arr_right[right_idx])
            right_idx += 1

        if len(final_arr) > 1 or key == "a":
            if not prov_date_prop:
                left[key] = final_arr
            else:
                min = None
                max = None
                for s in final_arr:
                    if min is None or str_compare(s, min) < 0:
                        min = s
                    if max is None or str_compare(s, max) > 0:
                        max = s
                    min_max = [min]
                    if max is not None:
                        min_max.append(max)
                    left[key] = min_max
        elif len(final_arr) == 1:
            left[key] = final_arr[0]
        return right_added

    def _merge_strings_and_json_objects(self, left, right):
        right_added = False
        merged_object = None

        if is_str(left) and is_str(right):
            merged_object = left
        elif is_dict(left) and is_str(right):
            merged_object = left
        elif is_str(left) and is_dict(right):
            merged_object = right
            right_added = False  #/We add right, but since its an object, the object will contain prov and we dont need to count it as merged
        elif is_dict(left) and is_dict(right):
            self._merge_json_objects_inner(left, right)
            merged_object = left
            right_added = False #We add right, but since its an object, the object will contain prov and we dont need to count it as merged
        else:
            if is_str(left):
                merged_object = right.encode('utf-8', 'ignore')
                if is_str(right):
                    right_added = True
            else:
                merged_object = left.encode('utf-8', 'ignore')

        return right_added, merged_object

    def _is_prov_key(self, key):
        return key in self._provenance_props


if __name__ == '__main__':
    # reducer = JSONLDReducer()

    # obj1 = {"a": "Class", "uri": "Class1", "value": "hello"}
    # obj2 = {"a": "Class", "uri": "Class1", "value": "hello2"}
    # result = reducer.merge_json_objects(obj1, obj2)
    # print(result)
    #
    # obj3 = {"a": "Class", "uri": "Class1", "value": "hello",  "nested": {"a": "NestedObject", "name": "obj1"}}
    # obj4 = {"a": "Class", "uri": "Class1", "value": "hello2", "nested": {"a": "NestedObject", "name": "obj2"}}
    # result = reducer.merge_json_objects(obj3, obj4)
    # print(result)

    # reducer = JSONLDReducer(provenance_properties={'source': 'str', 'dateRecorded': 'date'})
    # obj5 =  {"a": ["Class"], "uri": "Class1", "value": "hello", "source":"s1", "dateRecorded":["2018-06-01", "2018-06-09"]}
    # obj6 = {"a": ["Class"], "uri": "Class1", "value": "hello", "source":"s2", "dateRecorded":"2018-06-15"}
    # result = reducer.merge_json_objects(obj5, obj6)
    # print(result)

    reducers = [JSONLDReducer(), JSONLDReducer(adapter=HBaseAdapter(host="127.0.0.1", table="dig-reducer"))]
    for reducer in reducers:
        obj1 = {"a": "Class", "uri": "Class1", "value": "hello"}
        result = reducer.merge_json_object(obj1)
        print(result)
        obj2 = {"a": "Class", "uri": "Class1", "value": "hello2"}
        result = reducer.merge_json_object(obj2)
        print(result)
        obj3 = {"a": "Class", "uri": "Class1", "value": "hello", "nested": {"a": "NestedObject", "name": "obj1"}}
        result = reducer.merge_json_object(obj3)
        print(result)
        obj4 = {"a": "Class", "uri": "Class1", "value": "hello2", "nested": {"a": "NestedObject", "name": "obj2"}}
        result = reducer.merge_json_object(obj4)
        print(result)
        obj5 = {"uri": "Class1", "value": "x", "attr":True}
        result = reducer.merge_json_object(obj5)
        print(result)
        print("==========================================================================================")
    
