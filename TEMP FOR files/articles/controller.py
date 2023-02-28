from view import UserInterface
from model import ArticleModel


class Controller:
    def __init__(self):
        self.MODEL_article_model = ArticleModel()  # model
        self.VIEW_user_interface = UserInterface()  # view

    def run(self):
        answer = None
        while answer != "q":
            answer = self.VIEW_user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            article = self.VIEW_user_interface.add_user_article_1()
            self.MODEL_article_model.add_article(article)

        elif answer == '2':
            articles = self.MODEL_article_model.get_all_articles()
            self.VIEW_user_interface.show_all_articles_2(articles)

        elif answer == '3':
            article_title = self.VIEW_user_interface.get_user_article_3()
            try:
                article = self.MODEL_article_model.get_singe_article(article_title)
            except KeyError:
                self.VIEW_user_interface.show_incorrect_title_error(article_title)
            else:
                self.VIEW_user_interface.show_single_article(article)

        elif answer == '4':
            article_title = self.VIEW_user_interface.get_user_article_3()
            try:
                title = self.MODEL_article_model.remove_article(article_title)
            except KeyError:
                self.VIEW_user_interface.show_incorrect_title_error(article_title)
            else:
                self.VIEW_user_interface.remove_single_article(title)

        elif answer == 'q':
            self.MODEL_article_model.save_data()
        else:
            self.VIEW_user_interface.show_incorrect_answer_error(answer)