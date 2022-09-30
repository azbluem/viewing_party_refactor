import pytest
from viewing_party.person import Person

def test_add_1_movie():
    # Arrange
    sarah=Person("Sarah",[],[],["netflix","hulu"])
    margaret=Person("Margaret",[],[sarah],["amazon","hulu"])
    alyssa=Person("Alyssa",[],[sarah,margaret],["crave","netflix"])
    # Act
    sarah.add_watched_movie("It came from outer space")
    # Assert
    assert sarah.watched==["It came from outer space"]
    assert sarah.get_num_watched()==1

def test_add_2_movies():
    # Arrange
    sarah=Person("Sarah",[],[],["netflix","hulu"])
    margaret=Person("Margaret",[],[sarah],["amazon","hulu"])
    alyssa=Person("Alyssa",[],[sarah,margaret],["crave","netflix"])
    # Act
    sarah.add_watched_movie("It came from outer space")
    sarah.add_watched_movie("It came from inner space")
    # Assert
    assert sarah.watched==["It came from outer space","It came from inner space"]
    assert sarah.get_num_watched()==2