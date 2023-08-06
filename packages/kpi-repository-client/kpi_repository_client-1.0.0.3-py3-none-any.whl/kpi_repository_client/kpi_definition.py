
import json
import dateutil.parser


class KpiDefinition(object):
    STORAGE_TYPE_MINUTE = 'minute'
    STORAGE_TYPE_HOUR = 'hour'
    STORAGE_TYPE_DAY = 'day'

    CHART_TYPE_LINE = 'line'
    CHART_TYPE_COLUMN = 'column'

    def __init__(self, dict):
        self.uid = dict.get('uid', None)
        self.charttype = dict.get('charttype', None)
        self.color = dict.get('color', None)
        self.datatype = dict.get('datatype', None)
        self.description = dict.get('description', None)
        self.isSelected = dict.get('isSelected', None)
        self.label = dict.get('label', None)
        self.name = dict.get('name', None)
        self.storagetype = dict.get('storagetype', None)
        self.isSystem = dict.get('isSystem', None)
        self.index = dict.get('index', None)
        self.type = dict.get('type', None)

        self.created = dict.get('created', None)
        if self.created is not None:
            self.created = dateutil.parser.parse(self.created)

        self.updated = dict.get('updated', None)
        if self.updated is not None:
            self.updated = dateutil.parser.parse(self.updated)

    def to_json(self):
        selfDict = {
            'name': self.name,
            'label': self.label,
            'description': self.description,
            'datatype': self.datatype,
            'storagetype': self.storagetype,
            'isSelected': self.isSelected,
            'color': self.color,
            'charttype': self.charttype
        }

        return json.dumps(selfDict)

    def __str__(self):
        return str(self.__dict__)

    @classmethod
    def create(cls, name, label, description, isSelected, color, index=100, storagetype=STORAGE_TYPE_DAY, charttype=CHART_TYPE_LINE):
        return cls({
            'name': name,
            'label': label,
            'description': description,
            'datatype': 'number',
            'storagetype': storagetype,
            'isSelected': isSelected,
            'index': index,
            'color': color,
            'charttype': charttype
        })
