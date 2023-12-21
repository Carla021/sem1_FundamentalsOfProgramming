import random
from datetime import datetime, date

from a8_Carla021.src.domain.rental import Rental
from a8_Carla021.src.services.movie_rental_exception import MovieRentalException


class RentalService:

    def __init__(self, rental_repo, movie_repo, client_repo):
        self._rental_repo = rental_repo
        self._movie_repo = movie_repo
        self._client_repo = client_repo

    def get_all(self):
        return self._rental_repo.get_all()

    def find(self, rental_id: int):
        return self._rental_repo.find(rental_id)

    def rent_a_movie(self, movie_id, client_id, rented_date, due_date):

        good_client = True

        for rental in self._rental_repo.get_all():
            if rental.client_id == client_id:
                if rental.returned_date is not None:
                    if rental.due_date < rental.returned_date:
                        good_client = False
                else:
                    today = date.today()
                    if rental.due_date < today:
                        good_client = False

        if good_client:
            returned_date = None
            for rental in self._rental_repo.get_all():
                if rental.movie_id == movie_id:
                    if rental.returned_date == None:
                        raise MovieRentalException("Movie not returned!")


            rental = Rental(movie_id, client_id, rented_date, due_date, returned_date)
            self._rental_repo.add(rental)

    def return_a_movie(self, rental_id, return_date):

        for rental in self._rental_repo.get_all():

            if rental.id == rental_id:

                if rental.rented_date == None:
                    raise MovieRentalException("Movie not rented!")

                rental._returned_date = return_date

    def late_rentals(self, rentals: list):
        delay_days = {}
        today_date = datetime.today()
        for rental in rentals:
            if rental.returned_date is None and rental.due_date < today_date:
                delay_days[rental.id] = 0

        for rental in rentals:
            if rental.returned_date is None and rental.due_date < today_date:
                days = (today_date - rental.due_date).days
                delay_days[rental.id] += days

        sorted_delay_days = sorted(delay_days.items(), key=lambda x: x[1], reverse=True)
        return sorted_delay_days


def generate_rentals(n: int, movies: list, clients: list):
    dates = [datetime(2017, 2, 1), datetime(2018, 6, 3), datetime(2019, 8, 2), datetime(2019, 9, 13), datetime(2020, 11, 8), datetime(2020, 12, 5), datetime(2020, 12, 10), datetime(2020, 12, 11), datetime(2020, 12, 13), datetime(2020, 12, 14)]
    result = []

    while n > 0:
        movie_index = random.randint(0, len(movies) - 1)
        movie_id = movies[movie_index].id
        client_index = random.randint(0, len(clients) - 1)
        client_id = clients[client_index].id
        dates_index = random.randint(0, len(dates) - 3)
        rented_date = dates[dates_index]
        delay_index = random.randint(1, 2)
        returned_date = dates[dates_index + delay_index]
        second_delay_index = random.randint(1, 2)
        due_date = dates[dates_index + second_delay_index]
        if 3 < random.randint(0, 10):
            returned_date = None

        result.append(Rental(movie_id, client_id, rented_date, due_date, returned_date))
        n -= 1

    return result
