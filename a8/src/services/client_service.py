import copy
import random
from a8_Carla021.src.domain.client import Client
from a8_Carla021.src.repository.repository import Repository


class ClientService:
    def __init__(self, repo: Repository):
        self._repo = repo
        #self.__changes = 0
        #self.__history = []
        #self.__history.append(copy.deepcopy((self._repo.get_all())))

    def add(self, client: Client):
        """
        this function adds a new client and saves the changes
        :param client:
        :return:
        """
        self._repo.add(client)

    def get_all(self):
        """
        this function gets all the clients as a list
        :return:
        """
        return self._repo.get_all()

    def remove(self, client_id: int):
        """
        this function removes the client with the given id
        :param client_id:
        :return:
        """
        self._repo.delete(client_id)

    def update(self, client):
        """
        this function updates the client given
        :param client:
        :return:
        """
        self._repo.update(client.id, client)

    def find(self, client_id: int):
        """
        this function searches a client with a given id
        :param client_id:
        :return:
        """
        return self._repo.find(client_id)

    def most_active_clients(self, rentals: list):
        rented_days = {}

        for rental in rentals:
            rented_days[rental.client_id] = 0

        for rental in rentals:
            if rental.returned_date is None:
                continue
            days = (rental.returned_date - rental.rented_date).days
            if rented_days[rental.client_id] == 0:
                rented_days[rental.client_id] = days
            else:
                rented_days[rental.client_id] += days

        sorted_active_clients = sorted(rented_days.items(), key=lambda x: x[1], reverse=True)

        return sorted_active_clients



def generate_clients(n: int):
    """
    Generates n clients instances
    :param n: int
    :return: A list of n clients
    """

    name = ["Elena", "Vlad", "Carla", "Lorena", "Ioana", "Luiza", "Daria", "Dan", "David"]
    result = []

    while n > 0:
        #client_id = random.randint(1, 900)
        client_name = name[random.randint(0, 8)]
        result.append(Client(n, client_name))
        n -= 1

    return result