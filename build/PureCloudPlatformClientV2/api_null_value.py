def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class ApiNullValue(object):
    """
    NOTE: This is a custom class to represent Json Nullable value in models
    """

    def __init__(self):
        """
        Constructor
        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    def to_dict(self):
        """
        Returns None
        """
        return None

    def to_json(self):
        """
        Returns None
        """
        return None
    
