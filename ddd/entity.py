class Entity:
    def __init__(self, id_):
        self._id = id_

    def __eq__(self, other: "Entity"):
        return self._id == other.id

    def __ne__(self, other: "Entity"):
        return self != other

    @property
    def id(self):
        return self._id
