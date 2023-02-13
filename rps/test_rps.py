from rps import rock_paper_scissors


def test_rock_paper_scissors():
    ties = [("rock", "rock"), ("paper", "paper"), ("scissors", "scissors")]
    player1wins = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]
    player2wins = [("rock", "paper"), ("paper", "scissors"), ("scissors", "rock")]
    for game in ties:
        assert rock_paper_scissors(*game) == -1
    for game in player1wins:
        assert rock_paper_scissors(*game) == 0
    for game in player2wins:
        assert rock_paper_scissors(*game) == 1
