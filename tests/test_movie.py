import pytest
from viewing_party.movie import Movie

def test_update_rating():
    # Arrange
    horror1=Movie("It was Horror", "comedy", 3.3, "netflix")
    # Act
    horror1.update_rating(4.0)
    # Assert
    assert horror1.title=="It was Horror"
    assert horror1.genre=="comedy"
    assert horror1.host=="netflix"
    assert horror1.rating==4.0