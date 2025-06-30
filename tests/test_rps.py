from rps import get_winner

def test_get_winner():
    assert get_winner("rock", "scissors") == "player"
    assert get_winner("rock", "paper") == "computer"
    assert get_winner("scissors", "scissors") == "draw"
