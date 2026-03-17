import pytest

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_get_range_for_normal_mode():
    assert get_range_for_difficulty("Normal") == (1, 100)


@pytest.mark.parametrize(
    ("raw", "expected_error"),
    [
        ("-1", "Guess must be between 1 and 100."),
        ("0", "Guess must be between 1 and 100."),
        ("101", "Guess must be between 1 and 100."),
        ("", "Enter a guess."),
    ],
)
def test_parse_guess_rejects_invalid_normal_range_inputs(raw, expected_error):
    assert parse_guess(raw, low=1, high=100) == (False, None, expected_error)


def test_parse_guess_accepts_valid_integer_in_range():
    assert parse_guess("42", low=1, high=100) == (True, 42, None)


def test_winning_guess_returns_win_message():
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")


def test_guess_too_high_tells_player_to_go_lower():
    assert check_guess(60, 50) == ("Too High", "📉 Go LOWER!")


def test_guess_too_low_tells_player_to_go_higher():
    assert check_guess(40, 50) == ("Too Low", "📈 Go HIGHER!")


def test_update_score_increases_for_too_low_guess():
    assert update_score(0, "Too Low", 1) == 5


def test_update_score_increases_for_too_high_guess():
    assert update_score(0, "Too High", 1) == 5


def test_update_score_rewards_any_too_high_attempt():
    assert update_score(0, "Too High", 2) == 5


def test_update_score_rewards_win_based_on_attempt_number():
    assert update_score(5, "Win", 1) == 95
