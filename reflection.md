# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

When I first run the game, I was not able to make any guesses. I ran into broken code. 


- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

ImportError: C extension: None not built. If you want to import pandas from the source directory, you may need to run 'python setup.py build_ext' to build the C extensions first.

ran into this error 

after fixing this i got the bug on guessing number as whatever number I guess it says go lower 
also show hint is not working 
Since our guess number should be positive numbers between 1 t0 100, there are few negative numbers displayed 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  
I used github copilot . 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

When i first run the game , there were few bugs that I noticed and when I told AI to go through #file:app.py and check and suggest how to fix bug when you cannot start the game 
and copilot was able to fix that. I was able to restart or start the new game . 


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  
  On the debugging info the secret was revealed, I told AI to fix that but was not able to fix that. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  
First , I went through the web app and tried myself. And later , I wrote test cases for each of the function on the logic utils which helped me to test my logic without browsing the app. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I used this test to see if our guess lies in which range: 

test_guess_too_low_tells_player_to_go_higher
and verified with pytest and streaming through app 


- Did AI help you design or understand any tests? How?
Yes, AI helped me design test cases . It suggested me to check the behavior of the function of the logic and try to implement that . It also created boilertemplate for test cases .TBH it helped me writing test cases in proper way . 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would explain Streamlit reruns as the app running the whole script again every time we click a button or change an input. At first, this was confusing because it felt like the game was resetting every time I guessed a number. Session state is what helps Streamlit remember important values like the secret number, attempts, score, and whether the game is won or lost. So in simple words, reruns are the refresh, and session state is the memory that keeps the app from forgetting everything.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

Figuring out how to give proper command to agent so that we can implement our feature or debigging the bugs . 

  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
  
  I would give proper prompt not only copy pasting the whole code, I would try to be more efficient in explaining what agent should do and where should it do . 

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  
Before this course, I was using AI as just a regular LLM tool without thinking too much about the prompt and conextt like just copy pasting stuffs without proper instructions. After this course and the project, i got better idea on how AI take the instructions and agent do the task. 
