from dig.utils.jsonld_util import JSONLDUtil
from dig.io.adapter import MemoryAdapter, HBaseAdapter
import requests
import json
from os.path import exists


class JSONLDFramer(object):
    def __init__(self, **kwargs):
        self._kwargs = kwargs

        if 'adapter' in self._kwargs:
            self._adapter = self._kwargs['adapter']
        else:
            self._adapter = MemoryAdapter()

        if 'contextUrl' in self._kwargs:
            self._context = self.__load_context(json.loads(self.__get_request(self._kwargs['contextUrl'])))
        elif 'contextFile' in self._kwargs:
            self._context = self.__load_context(json.loads(self.__read_file(self._kwargs['contextFile'])))
        elif 'context' in self._kwargs:
            self._context = self._kwargs['context']


        if 'frames' in self._kwargs:
            self._frames = self._kwargs['frames']
        elif 'frameUrls' in self._kwargs:
            self._frames = []
            for f in self._kwargs['frameUrls']:
                self._frames.append(json.loads(self.__get_request(f)))
        elif 'frameFiles' in self._kwargs:
            self._frames = []
            for f in self._kwargs['frameFiles']:
                self._frames.append(json.loads(self.__read_file(f)))

        if not self._frames:
            raise ValueError('Frames not provided. Please provide attribute frames or framUrls or frameFiles')

        self._types = {}
        for frame in self._frames:
            frame_types = self.__get_types_in_frame(frame)
            for type in frame_types:
                self._types[type] = True

        self._types_arr = []
        for type in self._types:
            url = type
            if self._context is not None:
                url = self._context[type]
                self._types_arr.append({"name": type, "uri": url})

    def generate_frames(self, data):
        types_partitioned_data = self._partition_data_on_types(data)
        for frame in self._frames:
            self._frame_json(frame, types_partitioned_data)

    def _frame_json(self, frame, types_partitioned_data):
        document_type = frame["@type"]
        document_type_data = types_partitioned_data[document_type]["data"]

        if len(frame.items()) > 1:
            if "@explicit" in frame and frame["@explicit"] == True:
                document_type_data = list(map(lambda json: JSONLDUtil.frame_include_only_values(json, frame), document_type_data))
            for key, val in frame.items():
                if key[0] == "@":
                    continue
                if isinstance(val, dict) and not "@type" in val:
                    continue
                if isinstance(val, dict) and "@embed" in val and val["@embed"] == False:
                    continue
                # should this be every value?
                child_rdd = self._frame_json(val, types_partitioned_data)
                document_type_data = self._merge_json(document_type_data, key, child_rdd)
        return document_type_data

    def _merge_json(self, input_json, json_path, to_merge_json):
        to_merge_dict = {}
        for json_doc in to_merge_json:
            uri = JSONLDUtil.get_object_id(json_doc)
            to_merge_dict[uri] = json_doc

        result = []
        for json_doc in input_json:
            new_doc = JSONLDUtil.replace_values_at_path_batch(json_doc, json_path, to_merge_dict, [])
            result.append(new_doc)
        return result

    def _partition_data_on_types(self, data):
        type_to_json = {}

        for type in self._types_arr:
            def filter_on_type(tuple, class_short_name, class_long_name):
                # print "FIlter on:", class_name
                # key = tuple[0]
                value = tuple[1]
                # print "GOt value", value
                if type(value) is dict:
                    if "a" in value:
                        a_value = value["a"]
                        if type(a_value) is tuple or type(a_value) is list:
                            if class_short_name in a_value or class_long_name in a_value:
                                return True
                        else:
                            if a_value == class_short_name or a_value == class_long_name:
                                return True
                return False

            def create_data_for_type(input_data, type):
                type_name = type["name"]
                type_full = type["uri"]

                type_to_json[type_name] = {}
                type_to_json[type_name]["data"] = list(filter(lambda x:
                                                              filter_on_type(x, type_name, type_full), input_data))

            create_data_for_type(data, type)
        return type_to_json

    def __get_types_in_frame(self, frame):
        types = {}
        for attr in frame:
            value = frame[attr]
            if attr == "@type":
                types[value] = True
            elif type(value) == dict:
                inner_types = self.__get_types_in_frame(value)
                for t in inner_types:
                    types[t] = True

        return types

    def __read_file(self, filename):
        content = None
        if exists(filename):
            with open(filename, 'r') as content_file:
                content = content_file.read()

        return content

    def __get_request(self, url):
        response = requests.get(url, verify=False)
        if response.status_code == requests.codes.ok:
            return str(response.content)
        return None

    def __load_context(self, context_json):
        context_dict = {}
        if "@context" in context_json:
            contexts = context_json["@context"]
            for class_name in contexts:
                definition = contexts[class_name]
                #print class_name, definition
                if type(definition) == dict and "@id" in definition:
                    context_dict[class_name] = definition["@id"]

        # print context_dict
        return context_dict