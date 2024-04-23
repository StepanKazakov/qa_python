import pytest
from main import BooksCollector


@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    return collector


@pytest.fixture(scope='function')
def my_books(collector):
    my_books = collector.get_books_genre()
    return my_books


@pytest.fixture(scope='function')
def my_favorite(collector):
    my_favorite = collector.get_list_of_favorites_books()
    return my_favorite
