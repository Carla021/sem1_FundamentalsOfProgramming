import copy
import random
from a8_Carla021.src.domain.movie import Movie
from a8_Carla021.src.repository.repository import Repository


class MovieService:

    def __init__(self, repo: Repository):
        self._repo = repo
        #self.__changes = 0
        #self.__history = []
        #self.__history.append(copy.deepcopy((self._repo.get_all())))

    def add(self, movie: Movie):
        """
        this function adds a new movie and saves the changes
        :param movie:
        :return:
        """
        self._repo.add(movie)

    def find(self, movie_id: int):
        """
        this function searches a movie with a given id
        :param movie_id:
        :return:
        """
        return self._repo.find(movie_id)

    def get_all(self):
        """
        this function gets all the movies as a list
        :return:
        """
        return self._repo.get_all()

    def remove(self, movie_id: int):
        """
        this function removes the movie with the given id
        :param movie_id:
        :return:
        """
        self._repo.delete(movie_id)

    def update(self, movie):
        """
        this function updates the movie given
        :param movie:
        :return:
        """
        self._repo.update(movie.id, movie)

    def most_rented_movies(self, rentals: list):
        rented_days = {}

        for rental in rentals:
            rented_days[rental.movie_id] = 0

        for rental in rentals:
            if rental.returned_date == None:
                continue
            days = (rental.returned_date - rental.rented_date).days
            rented_days[rental.movie_id] += days

        sorted_rented_movies = sorted(rented_days.items(), key=lambda x: x[1], reverse=True)

        return sorted_rented_movies


def generate_movies(n: int):
     """
     Generates n movies instances
     :param n: int
     :return: A list of n movies
     """

     title = ["The Godfather", "Citizen Kane", "La Dolce Vita", "Seven Samurai", "In the Mood for love", "There will be blood", "Singin' in the Rain", "Goodfellas", "North by Northwest", "Mulholland Drive", "Bicycle Thieves", "The Dark Knight", "City Lights", "Grand Illusion", "His Girl Friday", "The Red Shoes", "Vertigo", "Beau Travail", "The Searchers", "Persona"]
     description = ["emotional", "casual viewing", "feel-good", "critically acclaimed"]
     genre = ["romantic", "horror", "drama", "comedy"]
     result = []

     while n > 0:
          #movie_id = random.randint(1, 900)
          movie_title = title[random.randint(0, 9)]
          movie_description = description[random.randint(0, 3)]
          movie_genre = genre[random.randint(0, 3)]
          result.append(Movie(n, movie_title, movie_description, movie_genre))
          n -= 1

     return result
