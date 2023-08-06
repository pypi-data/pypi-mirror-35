import dateutil.parser

class Service(object):
    def __init__(self, dict):
        self.uid = dict.get('uid', None)
        self.name = dict.get('name', None)
        self.description = dict.get('description', None)

        self.created = dict.get('created', None)
        if self.created is not None:
            self.created = dateutil.parser.parse(self.created)

        self.updated = dict.get('updated', None)
        if self.updated is not None:
            self.updated = dateutil.parser.parse(self.updated)

    def __str__(self):
        return str(self.__dict__)
