"""Pure game logic for the Game Glitch Investigator project."""


def get_range_for_difficulty(difficulty: str):
    """Return the inclusive guessing range for the selected difficulty."""
    ranges = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 50),
    }
    return ranges.get(difficulty, (1, 100))


def parse_guess(raw: str):
    """
    Parse a text input as a whole-number guess.

    Returns:
        (ok, guess_int, error_message)
    """
    if raw is None or not raw.strip():
        return False, None, "Enter a guess."

    try:
        guess = int(raw.strip())
    except ValueError:
        return False, None, "Enter a whole number."

    return True, guess, None


def check_guess(guess: int, secret: int):
    """
    Compare an integer guess with an integer secret.

    Returns:
        (outcome, message), where outcome is "Win", "Too High", or "Too Low".
    """
    # FIX: Keep both values as integers so comparisons are numeric, not alphabetical.
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Too high — try a lower number."

    return "Too Low", "📈 Too low — try a higher number."


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Return a consistent score after a valid guess."""
    if outcome == "Win":
        points = max(10, 100 - (attempt_number * 10))
        return current_score + points

    if outcome in {"Too High", "Too Low"}:
        return current_score - 5

    return current_score
