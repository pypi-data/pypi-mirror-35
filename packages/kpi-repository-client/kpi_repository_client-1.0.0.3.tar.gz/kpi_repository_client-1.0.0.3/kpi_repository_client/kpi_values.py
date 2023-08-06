
import json
from datetime import date, datetime


class KpiValues(object):
    def __init__(self, timestamp, values):
        self.__dict__ = dict(values)
        self.timestamp = timestamp

    def __str__(self):
        return str(self.__dict__)


class KpiValuesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, KpiValues):
            return obj.__dict__
        elif isinstance(obj, (datetime, date)):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)
