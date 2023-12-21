class Movie:
    def __init__(self, movie_id, title, description, genre):
        """
        Create the Movie
        :param movie_id:
        :param title:
        :param description:
        :param genre:
        """
        self._movie_id = movie_id
        self._title = title
        self._description = description
        self._genre = genre

    @property
    def id(self):
        return self._movie_id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def genre(self):
        return self._genre

    def __str__(self):
        return "Id: " + str(self._movie_id) + ", title: " + self._title + ", description: " + self._description + ", genre: " + self._genre

    def match_search(self, search: str):
        """
        Search movies by one of their fields
        :param search:
        :return:
        """
        search = search.lower()
        for attr in [self._movie_id, self.title, self.description, self.genre]:
            if search in str(attr).lower():
                return True

        return False


def test_movie():
    new_movie = Movie(12, "Titanic", "popular", "drama")
    assert new_movie.id == 12, "error!"
    assert new_movie.title == "Titanic", "error!"
    assert new_movie.description == "popular", "error!"
    assert new_movie.genre == "drama", "error!"


if __name__ == "__main__":
    test_movie()
