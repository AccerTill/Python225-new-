from view_films import UserInterface
from model_films import FilmModel


class Controller:
    def __init__(self):
        self.MODEL_films = FilmModel()
        self.VIEW_films = UserInterface()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.VIEW_films.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            film = self.VIEW_films.add_user_film_1()
            self.MODEL_films.add_film(film)

        elif answer == '2':
            articles = self.MODEL_films.get_all_films()
            self.VIEW_films.show_all_filmes_2(articles)

        elif answer == '3':
            film_title = self.VIEW_films.get_user_film_3()
            try:
                film = self.MODEL_films.get_singe_film(film_title)
            except KeyError:
                self.VIEW_films.show_incorrect_title_error(film_title)
            else:
                self.VIEW_films.show_single_film(film)

        elif answer == '4':
            film_title = self.VIEW_films.get_user_film_3()
            try:
                title = self.MODEL_films.remove_film(film_title)
            except KeyError:
                self.VIEW_films.show_incorrect_title_error(film_title)
            else:
                self.VIEW_films.remove_single_film(title)

        elif answer == 'q':
            self.MODEL_films.save_data()
        else:
            self.VIEW_films.show_incorrect_answer_error(answer)








