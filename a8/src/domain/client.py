
class Client:

    def __init__(self, client_id, name):
        """
        Create the Client
        :param client_id:
        :param name:
        """
        self._client_id = client_id
        self._name = name

    @property
    def id(self):
        return self._client_id

    @property
    def name(self):
        return self._name

    def __str__(self):
        return "Id: " + str(self._client_id) + ", name: " + self._name

    def match_search(self, search: str):
        """
        Search clients by one of their fields
        :param search:
        :return:
        """
        if search.lower() in str(self.id):
            return True
        if search.lower() in self.name.lower():
            return True
        return False

def test_client():
    new_client = Client(12, "Ioana")
    assert new_client._client_id == 12, "error!"
    assert new_client._name == "Ioana", "error!"


if __name__ == "__main__":
    test_client()
