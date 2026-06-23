# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the Streamlit app, the sidebar settings did not agree with the actual game. On Easy, the sidebar showed a range of 1 to 20, but the app still asked me to guess from 1 to 100 and the debug panel showed a secret of 41. I also noticed that every difficulty began with one attempt already used. The hints and score logic also needed inspection because the code could compare a number with a string and return misleading results.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Select Easy difficulty | Game range is 1 to 20, the secret is within that range, and six attempts are available. | The main message still said 1 to 100, the debug secret was 41, and only five attempts were left. | none |
| Select Normal difficulty | Eight attempts are available before the first guess. | The app showed seven attempts left and the debug panel already showed Attempts: 1. | none |
| Select Hard difficulty | The main instruction says 1 to 50 and the app starts with five attempts. | The sidebar said 1 to 50, but the main instruction still said 1 to 100 and only four attempts were left. | none |
| Enter 60 when the secret is 41 | The game should say the guess is too high and suggest a lower number. | The starter logic returned “Go HIGHER!”, which is the opposite direction. | none |

---

## 2. How did you use AI as a teammate?

I used ChatGPT as an AI teammate to help read the starter code, identify state and comparison bugs, and plan a small refactor. A correct suggestion was to keep the secret number, attempts, score, history, and status in `st.session_state`, then reset all of them together for a new game or difficulty change. I verified this by changing difficulty and starting a new game while checking the Developer Debug Info panel. One misleading setup suggestion was to install every dependency again, but the installation process was killed and I confirmed that Streamlit was already available by successfully running `python -m streamlit run app.py`.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed only after checking both the code and the running Streamlit app. I added pytest tests for the difficulty ranges, input parsing, high/low outcomes, and scoring so that the core logic can be checked without clicking through the UI every time. I also manually tested a guess above and below the debug secret number to confirm that the displayed hint points in the correct direction. AI helped me turn the observed bugs into small, specific test cases.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the script from top to bottom whenever the user changes a widget or clicks a button. A normal Python variable can therefore appear to reset on every interaction. `st.session_state` is like a small memory for one browser session, so it keeps values such as the secret number and attempt count stable between reruns. The game also needs an intentional reset function so related state values do not get out of sync.

---

## 5. Looking ahead: your developer habits

I want to reuse the habit of writing down a reproducible bug case before changing the code. This makes it easier to ask an AI a focused question and to verify whether the answer actually solved the problem. Next time, I will check AI-generated changes in smaller pieces instead of assuming the first suggestion is correct. This project showed me that AI can speed up debugging, but I still need to run the program, inspect the state, and test the logic myself.
