# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looked like a number guessing game. It had 3 difficulties: easy, medium, and hard. What changed between each difficulty was the number of tries allowed to the player with easy having 6 (which i assumed was supposed to be 10) and supposed to have a range of 1 -20, normal having 8 and a range of 1-50, and hard having 5 and a range of 1 -100. it had submit, new game, and hint under the interface with the buttons or checkbox supposed to perform what was it was named.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. The New game button didn't work, the page had to be manually refreshed to start again.
  2. The Normal difficulty had more attempts than the Easy difficulty.
  3. The hints were wrong, when the user inputted a number less than 10, it said that the guess should be lower and when a numbe rgreater than 80 was inputted, it said go higher.
  4. Numbers greater than 100 could be inputted

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
1. The AI gave me a suggestion on how to fix the wrong hint and secret number. The hints were reversed and showed too high for a low number and too low for a high number. Furthermore, the code turned the guesses into srings causing further problems.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I didn't really catch any misleading or incorrect suggestions from the AI. It answered and gave me suggestions as I intended. However, the first fix implemented didn't work completely as the high and low messages were still swapped for secret number.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
After I had identified and fixed it with the AI, I ran it on the browser and tested it from a user's perspective. If I saw that the bug was still active, I would check back with the AI. If the bug was fixed I would move on to the next.
- Describe at least one test you ran (manual or using pytest)
For the bug involving the hints, I would try to guess the number on my own and compare it to what the hints said. The hints previously would tell you that you needed to go lower if your number was 10 or below and to go higher if you rnumber was above 80. Once I tested 80 and 10, if the results were consistent, I would move on to the mid range number and compare my guesses with the final result.
- Did AI help you design or understand any tests? How?
It helped me create a test that compares the guess to a dummy answer, an outcome, and the intended message. If they are the same, the outcome is "correct" and the message should be "correct", if the guess is larger than the answer, the outcome should be too high and a corresponding message should be said, vice versa for a smaller answer.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
In streamlit, every interaction with widgets causes the entire code to run from the start. A random number generator was used in the code, meaning that for every refresh, a new random number was generated. This prevented the user from getting a win.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns are a feature that makes it that every variable initialized gets reinitalized whenever the user interacts with it. Getting input, pressing a button, etc. makes the entire code re-execute. This feature makes it so that a randomly generated number can never be stored.
- What change did you make that finally gave the game a stable secret number?
The random number generator was removed from its original position. Furthermore, it was stored in st.session_state. This change made it so that the same number was kept throughout the entire execution.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
Getting test cases from the AI. This makes it that future edits to the code still pass those initial expectations for the code. I also liked the habit of using copilot to giev suggestions to fix bugs while coding.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
I will give clearer prompts on specific segments instead of asking it to just "fix the entire code". I find that clearly stating the bug that needs fixing makes the edits to the code much more accurate. I will also ask for clear explanations after edits have been made.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI generated code can execute the wrong logic depending on how vauge the prompts might be. The AI generated code should be screened manually as you might have context on the code that the AI might not have.
