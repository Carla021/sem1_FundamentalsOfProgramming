from a8_Carla021.src.repository.repository_exception import RepositoryException


class Repository(object):
    """
    repository for storing instances
    """
    def __init__(self):
        self._objects = []

    def add(self, obj):
        """
        adds a new object to a repository, if it doesn't already exist
        :param obj: the object wanted to be added
        :return:
        """
        if self.find(obj.id) is not None:
            raise RepositoryException("Object already in repository!")
        else:
            self._objects.append(obj)

    def find(self, objId):
        """
        finds an object in the repository according to its id, if it exists
        :param objId: the object's id to be searched for
        :return: the object wanted
        """
        for obj in self._objects:
            if obj.id == objId:
                return obj
        return None

    def delete(self, objectId):
        """
        Remove the object with given objectId from repository
        :param objectId: the object that will be removed
        :return: the object that will be removed
        raises RepositoryException if object with given pbjectId is not contained in the repository
        """
        object = self.find(objectId)
        if object is not None:
            self._objects.remove(object)
        else:
            raise RepositoryException("Object is not in repository!")

    def get_all(self):
        """
        gets all the objects as a list of instances
        :return: the list of objects
        """
        return self._objects

    def __len__(self):
        return len(self._objects)

    def update(self, id, obj):
        """
        updates the object with the given id to the object given
        :param id: the object wanted to be updated id
        :param obj: the object that will replace the searched for one
        :return:
        """
        found = False

        for i in range(len(self._objects)):
            if self._objects[i].id == id:
                self._objects[i] = obj
                found = True

        if not found:
            raise RepositoryException("Object is not in repository!")

