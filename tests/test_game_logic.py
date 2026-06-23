from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_get_range_for_each_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_parse_valid_whole_number():
    assert parse_guess("42") == (True, 42, None)


def test_parse_blank_input():
    assert parse_guess("") == (False, None, "Enter a guess.")


def test_parse_rejects_decimal_input():
    assert parse_guess("4.5") == (False, None, "Enter a whole number.")


def test_check_guess_win():
    assert check_guess(41, 41) == ("Win", "🎉 Correct!")


def test_check_guess_too_high_has_lower_hint():
    outcome, message = check_guess(60, 41)
    assert outcome == "Too High"
    assert "lower" in message.lower()


def test_check_guess_too_low_has_higher_hint():
    outcome, message = check_guess(20, 41)
    assert outcome == "Too Low"
    assert "higher" in message.lower()


def test_score_penalty_is_consistent_for_wrong_guess():
    assert update_score(0, "Too High", 1) == -5
    assert update_score(0, "Too Low", 1) == -5


def test_score_rewards_faster_win_more():
    assert update_score(0, "Win", 1) == 90
    assert update_score(0, "Win", 8) == 20
