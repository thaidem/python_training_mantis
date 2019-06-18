from sys import maxsize


class Project:
    def __init__(self, id=None, name=None, description=None, path=None):
        self.id = id
        self.name = name
        self.description = description
        self.path = path

    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id, self.name, self.description, self.path)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
