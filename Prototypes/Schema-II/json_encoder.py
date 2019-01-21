import json
import numpy as np

class CustomEncoder(json.JSONEncoder):
    """
        Use this class to serialize different types of data which is unsuported by the default json encoder

        In this case will serialize int32 from numpy.
    """
    def default(self, obj):
        if isinstance(obj,np.int32):
            return int(obj)
        return json.JSONEncoder.default(self, obj)
