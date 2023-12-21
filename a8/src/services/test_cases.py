import unittest

from a8_Carla021.src.domain.movie import Movie
from a8_Carla021.src.repository.repository import Repository
from a8_Carla021.src.services.movie_service import MovieService, generate_movies


class Tests(unittest.TestCase):

    def setUp(self) -> None:
        print("set up")

        self._service = MovieService(Repository())
        movies = generate_movies(5)
        for movie in movies:
            self._service.add(movie)

    def tearDown(self) -> None:
        print("tear down")

    def test_add_length(self):
        print("test")
        leng = len(self._service.get_all())
        self.assertEqual(leng, 5)
        self._service.add(Movie(10, "Ion", "emotional", "drama"))
        leng = len(self._service.get_all())
        self.assertEqual(leng, 6)

    def test_add_item(self):
        print("test")
        movie = Movie(123, "Florica", "emotional", "drama")
        self._service.add(movie)
        self.assertTrue(movie in self._service.get_all())

    def test_remove_length(self):
        print("test")
        leng = len(self._service.get_all())
        self.assertEqual(leng, 5)
        self._service.remove(4)
        leng = len(self._service.get_all())
        self.assertEqual(leng, 4)

    def test_remove_item(self):
        print("test")
        first_movie = self._service.get_all()[0]
        self._service.remove(first_movie.id)
        self.assertFalse(first_movie in self._service.get_all())

    def test_update(self):
        print("test")
        first_movie = self._service.get_all()[0]
        new_movie = Movie(first_movie.id, "Ion", "emotional", "drama")
        self._service.update(new_movie)
        self.assertTrue(new_movie in self._service.get_all())
