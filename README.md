# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The games purpose is to create a random number and give a certain number of attempts to the user who will try to get the correct number. The user could pick various difficulties with the number of tries and the number range changing according to the difficulty.
- [ ] Detail which bugs you found.
The secret number changes with every user interaction, the hints gave the wrong information, and with every even guess, the secret number was converted into a string.
- [ ] Explain what fixes you applied.
Using st.session_state, the secret number was stored and wasn't regenerated with every user interaction. The hints were changed to display the right number depending on the secret number. Th string conversion with every even guess was also removed.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
![alt text](<Screenshot 2026-03-14 at 3.16.41 PM.png>)



## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
