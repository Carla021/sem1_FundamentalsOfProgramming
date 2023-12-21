class Rental:
    idGen = 0

    def __init__(self, movie_id, client_id, rented_date, due_date, returned_date):
        """
        Create the Rental
        :param movie_id:
        :param client_id:
        :param rented_date:
        :param due_date:
        :param returned_date:
        """
        Rental.idGen += 1
        self._rental_id = Rental.idGen
        self._movie_id = movie_id
        self._client_id = client_id
        self._rented_date = rented_date
        self._due_date = due_date
        self._returned_date = returned_date

    @property
    def id(self):
        return self._rental_id

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def client_id(self):
        return self._client_id

    @property
    def rented_date(self):
        return self._rented_date

    @property
    def due_date(self):
        return self._due_date

    @property
    def returned_date(self):
        return self._returned_date

    def __str__(self):
        return "Rental Id: " + str(self._rental_id) + ", Movie Id: " + str(self._movie_id) + ", Client Id: " + str(
            self._client_id) + ", Rented Date: " + str(self._rented_date) + ", Due Date: " + str(
            self._due_date) + ", Returned Date: " + str(self._returned_date)

    def match_search(self, search: str):
        """
        Search the rentals by one of their fields
        :param search:
        :return:
        """
        search = search.lower()
        for attr in [self._rental_id, self.movie_id, self.client_id, self.rented_date, self.due_date,
                     self.returned_date]:
            if search in str(attr):
                return True

        return False
