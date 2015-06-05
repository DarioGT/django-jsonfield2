import datetime
import decimal
import types
import json
import uuid


from django.db.models.query import QuerySet
from django.utils import six, timezone
from django.utils.encoding import force_text
from django.utils.functional import Promise

from django.core.serializers.json import DjangoJSONEncoder

class JSONEncoder( DjangoJSONEncoder ):

    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)

        elif isinstance(obj, datetime.timedelta):
            return six.text_type(total_seconds(obj))
 
        elif isinstance(obj, decimal.Decimal):
            # Serializers will coerce decimals to strings by default.
            return float(obj)
 
        elif isinstance(obj, uuid.UUID):
            return six.text_type(obj)
 
        elif isinstance(obj, QuerySet):
            return tuple(obj)
        elif hasattr(obj, 'tolist'):
            # Numpy arrays and array scalars.
            return obj.tolist()

        elif hasattr(obj, '__getitem__'):
            try:
                return dict(obj)
            except:
                pass
        elif hasattr(obj, '__iter__'):
            return tuple(item for item in obj)

        return super(JSONEncoder, self).default(obj)



def default(o):
    if hasattr(o, 'to_json'):
        return o.to_json()
    if isinstance(o, Decimal):
        return str(o)
    if isinstance(o, datetime.datetime):
        if o.tzinfo:
            return o.strftime('%Y-%m-%dT%H:%M:%S%z')
        return o.strftime("%Y-%m-%dT%H:%M:%S")
    if isinstance(o, datetime.date):
        return o.strftime("%Y-%m-%d")
    if isinstance(o, datetime.time):
        if o.tzinfo:
            return o.strftime('%H:%M:%S%z')
        return o.strftime("%H:%M:%S")
    if isinstance(o, set):
        return list(o)

    raise TypeError(repr(o) + " is not JSON serializable")
