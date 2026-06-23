# 🎮 Game Glitch Investigator: The Impossible Guesser

## Purpose

This is a Streamlit number-guessing game. The goal is to guess the secret number before the allowed attempts run out. I used this project to investigate AI-generated bugs, refactor the game logic, and verify fixes with pytest.

## Bugs Found and Fixed

- The difficulty sidebar range did not match the main game instructions or the secret number.
- The game started with one attempt already used.
- The hints were backwards: a guess that was too high told the player to go higher.
- The game sometimes compared an integer guess with a string secret number.
- New Game did not reset all important state values.

I moved the pure game functions into `logic_utils.py`, used `st.session_state` for the secret number and progress, reset the whole game when needed, and added automated tests in `tests/test_game_logic.py`.

## Setup

```bash
python -m streamlit run app.py
```

Run tests with:

```bash
python -m pytest tests -q
```

## Demo Walkthrough

1. Select **Easy** difficulty. The app displays the correct range, 1 to 20, and six attempts.
2. Open Developer Debug Info to confirm the secret number stays within the selected range.
3. Enter a guess above the secret number. The game returns **Too High** and tells the player to try a lower number.
4. Enter a guess below the secret number. The game returns **Too Low** and tells the player to try a higher number.
5. Enter the correct number. The game shows a win message and calculates the final score.
6. Click **New Game**. The secret, attempts, history, score, and game status reset correctly.

## Test Results

Run this command in the project folder before submitting:

```bash
python -m pytest tests -q
```

The tests cover difficulty ranges, valid and invalid input, correct high/low hints, and consistent score behavior.
