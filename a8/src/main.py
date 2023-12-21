from a8_Carla021.src.repository.repository import Repository
from a8_Carla021.src.services.client_service import generate_clients, ClientService
from a8_Carla021.src.services.movie_service import generate_movies, MovieService
from a8_Carla021.src.services.rental_service import RentalService, generate_rentals
from a8_Carla021.src.ui.ui import UI

if __name__ == "__main__":

    client_repo = Repository()
    for client in generate_clients(20):
        client_repo.add(client)

    movie_repo = Repository()
    for movie in generate_movies(20):
        movie_repo.add(movie)

    rental_repo = Repository()
    for rental in generate_rentals(20, movie_repo.get_all(), client_repo.get_all()):
        rental_repo.add(rental)

    client_services = ClientService(client_repo)
    movie_services = MovieService(movie_repo)
    rental_services = RentalService(rental_repo, movie_repo, client_repo)

    ui = UI(client_services, movie_services, rental_services)

    ui.start()
