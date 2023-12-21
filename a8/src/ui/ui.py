from datetime import date

from a8_Carla021.src.domain.client import Client
from a8_Carla021.src.domain.movie import Movie
from a8_Carla021.src.repository.repository_exception import RepositoryException
from a8_Carla021.src.services.movie_rental_exception import MovieRentalException
from a8_Carla021.src.ui.ui_exception import UIException


class UI:

    def __init__(self, client_service, movie_service, rental_service):
        self._client_service = client_service
        self._movie_service = movie_service
        self._rental_service = rental_service

    def add_clients(self, client: Client):
        try:
            self._client_service.add(client)
        except MovieRentalException as e:
            print(e.msg)

    def add_movies(self, movie: Movie):
        try:
            self._movie_service.add(movie)
        except MovieRentalException as e:
            print(e.msg)

    def display_clients(self):
        for client in self._client_service.get_all():
            print(str(client))

    def display_movies(self):
        for movies in self._movie_service.get_all():
            print(str(movies))

    def remove_clients(self, client_id):
        self._client_service.remove(client_id)

    def remove_movies(self, movie_id):
        self._movie_service.remove(movie_id)

    def update_client(self, client):
        self._client_service.update(client)

    def update_movie(self, movie):
        self._movie_service.update(movie)

    @staticmethod
    def _print_menu():
        print("1. Manage clients and movies. You can add, remove, update, and list both clients and movies")
        print("2. Rent or return a movie.")
        print("3. Search for clients or movies using any one of their fields")
        print("4. Create statistics")
        print("0. Exit the program\n")

    @staticmethod
    def print_statistics_menu():
        print("a. Most rented movies. This will provide the list of movies, sorted in descending order of the number of days they were rented")
        print("b. Most active clients. This will provide the list of clients, sorted in descending order of the number of movie rental days they have (e.g. having 2 rented movies for 3 days each counts as 2 x 3 = 6 days)")
        print("c. Late rentals. All the movies that are currently rented, for which the due date for return has passed, sorted in descending order of the number of days of delay")

    @staticmethod
    def menu_manage_clients_or_movies():
        print("Choose between clients and movies: ")

    @staticmethod
    def menu_add_remove_update_list():
        print("Choose to add, remove, update or list the object chosen: ")

    @staticmethod
    def menu_rent_or_return_movie():
        print("Rent or Return a movie. List the rentals: ")

    @staticmethod
    def _input_command():
        command = input(">")
        return command

    def get_input(self):
        try:
            return int(input(">"))
        except ValueError as ve:
            print(ve)
            return self.get_input()

    def start(self):
        while True:
            self._print_menu()
            option = self.get_input()
            try:
                if option == 1:

                    self.menu_manage_clients_or_movies()

                    choice = input()

                    if choice == "clients":

                        self.menu_add_remove_update_list()
                        action = input()

                        if action == "add":
                            id = int(input("id: "))
                            name = input("name: ")
                            self._client_service.add(Client(id, name))
                        elif action == "remove":
                            id = int(input("id: "))
                            self._client_service.remove(id)
                        elif action == "update":
                            id = int(input("id: "))
                            name = input("name: ")
                            self._client_service.update(Client(id, name))
                        elif action == "list":
                            for client in self._client_service.get_all():
                                print(client)
                        else:
                            raise UIException("Invalid input!")

                    elif choice == "movies":

                        self.menu_add_remove_update_list()
                        action = input()

                        if action == "add":

                            id = int(input("id: "))
                            title = input("title: ")
                            description = input("description: ")
                            genre = input("genre: ")

                            self._movie_service.add(Movie(id, title, description, genre))

                        elif action == "remove":

                            id = int(input("id: "))

                            self._movie_service.remove(id)

                        elif action == "update":

                            id = int(input("id: "))
                            title = input("title: ")
                            description = input("description: ")
                            genre = input("genre: ")

                            self._movie_service.update(Movie(id, title, description, genre))

                        elif action == "list":
                            for rental in self._movie_service.get_all():
                                print(rental)
                        else:
                            raise UIException("Invalid input!")

                    else:
                        raise UIException("Invalid input!")

                elif option == 2:

                    self.menu_rent_or_return_movie()

                    choice = input()

                    if choice == "rent":

                        #rental_id = input("rental id: ")
                        movie_id = int(input("movie id: "))
                        client_id = int(input("client id: "))

                        rented_day = int(input("rented day: "))
                        rented_month = int(input("rented month: "))
                        rented_year = int(input("rented year: "))

                        due_day = int(input("due day: "))
                        due_month = int(input("due month: "))
                        due_year = int(input("due year: "))

                        movie_ids = []
                        for movie in self._movie_service.get_all():
                            movie_ids.append(movie.id)

                        if movie_id not in movie_ids:
                            raise UIException('Movie is not existing!')

                        client_ids = []
                        for client in self._client_service.get_all():
                            client_ids.append(client.id)

                        if client_id not in client_ids:
                            raise UIException("Client is not existing!")

                        rented_date = date(rented_year, rented_month, rented_day)
                        due_date = date(due_year, due_month, due_day)

                        self._rental_service.rent_a_movie(movie_id, client_id, rented_date, due_date)

                    elif choice == "return":

                        rental_id = int(input("rental id: "))
                        returned_day = int(input("return day: "))
                        returned_month = int(input("return month: "))
                        returned_year = int(input("return year: "))
                        returned_date = date(returned_year, returned_month, returned_day)

                        rental_ids = []
                        for rental in self._rental_service.get_all():
                            rental_ids.append(rental.id)

                        if rental_id not in rental_ids:
                            raise UIException('Rental is not existing!')

                        self._rental_service.return_a_movie(rental_id, returned_date)

                    elif choice == "list rentals":
                        for rental in self._rental_service.get_all():
                            print(rental)

                    else:
                        raise UIException("Invalid input!")

                elif option == 3:

                    search = input("enter your search: ")

                    for client in self._client_service.get_all():
                        if client.match_search(search):
                            print(client)

                    for movie in self._movie_service.get_all():
                        if movie.match_search(search):
                            print(movie)

                elif option == 4:

                    self.print_statistics_menu()
                    choice = input()

                    if choice == "a":

                        sorted_rented_movies = dict(self._movie_service.most_rented_movies(self._rental_service.get_all()))

                        for sorted in sorted_rented_movies.items():
                            print(self._movie_service.find(sorted[0]), sorted[1])

                    elif choice == "b":

                        sorted_active_clients = dict(self._client_service.most_active_clients(self._rental_service.get_all()))

                        for sorted in sorted_active_clients.items():
                            print(self._client_service.find(sorted[0]), sorted[1])

                    elif choice == "c":

                        sorted_delay_days = dict(self._rental_service.late_rentals(self._rental_service.get_all()))

                        for sorted in sorted_delay_days.items():
                            print(self._rental_service.find(sorted[0]), sorted[1])

                    else:
                        raise UIException("Invalid input!")

                elif option == 0:
                    print("Exiting...")
                    return

                else:
                    raise UIException("Invalid input!")

            except UIException as e:
                print(e.msg)
            except RepositoryException as e:
                print(e.get_message())

