import sys
from datetime import datetime, date
from six import iteritems

def sanitize_for_serialization(obj):
    """
    Builds a JSON object ready for serialization.

    If obj is None, return None.
    If obj is str, int, float, bool, return directly.
    If obj is datetime.datetime, datetime.date
        convert to string in iso8601 format.
    If obj is list, sanitize each element in the list.
    If obj is dict, return the dict.
    If obj is swagger model, return the properties dict.

    :param obj: The data to serialize.
    :return: The serialized form of data.
    """
    types = (str, int, float, bool, tuple)
    if sys.version_info < (3,0):
        types = types + (unicode,)
    if isinstance(obj, type(None)):
        return None
    elif isinstance(obj, types):
        return obj
    elif isinstance(obj, list):
        return [sanitize_for_serialization(sub_obj)
                for sub_obj in obj]
    elif isinstance(obj, (datetime, date)):
        return obj.isoformat()
    else:
        if isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `swagger_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
                        for attr, _ in iteritems(obj.swagger_types)
                        if getattr(obj, attr) is not None}

        return {key: sanitize_for_serialization(val)
                for key, val in iteritems(obj_dict)}
