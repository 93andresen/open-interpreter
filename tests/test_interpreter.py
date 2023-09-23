import interpreter
# interpreter.reset()
interpreter.auto_run = True
# interpreter.local = True
interpreter.model = "gpt-4"
#interpreter.model = "gpt-3.5-turbo-16k"
interpreter.model = "codellama-13b-instruct.Q3_K_S"
# interpreter.debug_mode = True
interpreter.temperature = 0

import os
path = r"C:\_\Auto-GPT\Music_Recomentation_Engine"
os.chdir(path)
# Confirm the current working directory
print("Current directory:", os.getcwd())

with open('C:\_\Text\Music_Recomentation_Engine.txt', 'r') as file:
    prompt = file.read()

i = 0
while i < 100:
    interpreter.chat(prompt)
    interpreter.chat("Continue working on the current step")
    interpreter.chat()
    print(i)
    i += 1

i = 1
while i != 1:
    interpreter.chat()
    print(i)
    i += 1

i = 0
while i < 100:
    interpreter.chat("""""")
    print(i)
    i += 1

i = 1
while i != 0:
    interpreter.chat()
    print(i)
    i += 1







exit



    interpreter.chat(r"""make spotify automaticly pause playback when youtube starts playing in Firefox and vice verca. I obviously don't want to listen to multiple songs at the same time. Continue until your goal is reached. do not ask user for any help. you have full administrator access to do and install anything you want. Find a solution instead of making one yourself. run "spt --help" to see command line options for spotify. GOOGLE_API_KEY="AIzaSyBJlmSWyNB2OMJYxX_wgKxwnvmSHkNCApg" and GOOGLE_CUSTOM_SEARCH_ENGINE_ID="0337977ff4c214604". Then Test that it works as expected. Continue Until you are finished. Here is some code:"// Check if Firefox is playing mediafunction isFirefoxPlayingMedia() {  // Get all media elements on the page  var mediaElements = document.querySelectorAll("video, audio");  // Iterate through each media element  for (var i = 0; i < mediaElements.length; i++) {    var mediaElement = mediaElements[i];    // Check if the media element is playing    if (!mediaElement.paused) {      return true; // Firefox is playing media    }  }  return false; // Firefox is not playing media}// Usage exampleif (isFirefoxPlayingMedia()) {  console.log("Firefox is playing media.");} else {  console.log("Firefox is not playing media.");}".If you are finnished, then run a script that waits for 100000000 seconds.""")




interpreter.chat("""""")
interpreter.chat("""Asking for human input is forbidden. Continue with Follow the instructions. Execute code in every response""")








interpreter.chat("""""")
interpreter.chat("""""")

#interpreter.chat("""I am using windows, so do not use bash. Use python or powershell. Make a list of all the files in my computer. Then make a list of all symlinks. Then for hardlinks. The for eve file you think i may need or tgink is valubale. Then Make a list of all log files. All files should be saved to c:\_\{{filename}}.txt. Do not store the filepaths in memory, append to file for each file""")
#interpreter.chat("""What files on my computer has my settings in Resident Evil Village? Make a copy and tell me where you stored the copy. DO NOT CHANGE ANY FILES!!! If you encounter an issue with the execution, then find another way""")
#interpreter.chat("""The directory "C:\_\Powershell\open-interpreter\Text_LOCAL_TEST" contains a lit of different types of textfiles. Convert them all to txt-files. After That, Make a list with references of all files that contains "Rebekka" either in the filename or in the file content.""")
#interpreter.chat("""""")

interpreter.chat("""continue""")
interpreter.chat("""continue""")
interpreter.chat("""continue""")
interpreter.chat("""continue""")
interpreter.chat("""continue""")
interpreter.chat("""continue""")
interpreter.chat("""continue""")
interpreter.chat("""continue""")
interpreter.chat("""continue""")
interpreter.chat("""continue""")
interpreter.chat("""continue""")
interpreter.chat("""continue""")
interpreter.chat("""continue""")
interpreter.chat("""continue""")
interpreter.chat("""continue""")



interpreter.chat()



def test_hello_world():
    #interpreter.reset()
    messages = interpreter.chat("""Please reply with just the words "Hello, World!" and nothing else. Do not run code.""", return_messages=True)
    assert messages == [{'role': 'user', 'content': 'Please reply with just the words "Hello, World!" and nothing else. Do not run code.'}, {'role': 'assistant', 'content': 'Hello, World!'}]

def test_math():
    #interpreter.reset()
    messages = interpreter.chat("""Please perform the calculation 27073*7397 then reply with just the integer answer with no commas or anything, nothing else.""", return_messages=True)
    assert "200258981" in messages[-1]["content"]

def test_delayed_exec():
    #interpreter.reset()
    interpreter.chat("""Can you write a single block of code and run_code it that prints something, then delays 1 second, then prints something else? No talk just code. Thanks!""", return_messages=True)

def test_nested_loops_and_multiple_newlines():
    #interpreter.reset()
    interpreter.chat("""Can you write a nested for loop in python and shell and run them? Also put 1-3 newlines between each line in the code. Thanks!""", return_messages=True)

def test_markdown():
    #interpreter.reset()
    interpreter.chat("""Hi, can you test out a bunch of markdown features? Try writing a fenced code block, a table, headers, everything. DO NOT write the markdown inside a markdown code block, just write it raw.""")

def evolution_game():
    #interpreter.reset()
    interpreter.chat("""Create an engaging text-based game centered around evolution using python. The game is an RPG with branching storylines so that the player's choices and actions within the game lead to significantly different storylines or outcomes. Begin as the initial life form and progress towards the future. Each decision you make including the first decicion at the start significantly impacts the future outcome. Make the story meaningful and make sure the consequenses of decicions surprises the player. Make the game deceptivly unfair. Make the players life a living hell after the first part of the game. Note that while the game aims to create a sense of unfairness, it is essential to balance it with meaningful choices and opportunities for redemption or growth. The goal is to engage the player and encourage reflection on the consequences of their decisions rather than making the game frustrating or discouraging. The Game should be text-based. The players decicions dictate what happens next so every playthrough should be unique with all the branching storylines and how the players choices affact the story. Use the players choices to create difficult situations so they feel like they barely survived. The game has no failure state. There are consequenses on the story but never a game ending in game over. If the players health gets too low, there Here’s a list of traits and skills that the player can develop in the game. Strength - Increases the player’s physical power and ability to overcome challenges. Intelligence - Enhances problem-solving skills and the player’s ability to make strategic decisions. Agility - Improves the player’s speed and reflexes, allowing them to evade danger or perform quick actions. Adaptability - Increases the player’s ability to adjust to new environments and situations. Stealth - Enhances the player’s ability to move silently and remain undetected by enemies. Communication - Improves the player’s ability to interact and communicate with other organisms or characters in the game. Camouflage - Allows the player to blend into their surroundings, making it harder for enemies to spot them. Regeneration - Enhances the player’s ability to heal and recover from injuries or damage. Perception - Improves the player’s senses, allowing them to detect hidden objects or spot potential dangers. Leadership - Enhances the player’s ability to lead and influence other organisms or characters in the game. Cooperation - Improves the player’s ability to work together with other organisms or characters towards a common goal. Resourcefulness - Enhances the player’s ability to find and utilize resources effectively. Resilience - Increases the player’s ability to withstand adverse conditions or recover from setbacks. Charisma - Improves the player’s ability to persuade or influence others through charm and charisma. Problemsolving - Enhances the player’s ability to solve puzzles or overcome obstacles through logical thinking. These traits and skills can be developed and improved throughout the game based on the player’s choices and actions. They can have a significant impact on the player’s success and the outcome of different storylines. The player can find items that has various clever uses. Perception helps him find more useful items.""")
    interpreter.chat()

def evolution_game2():
    #interpreter.reset()
    interpreter.chat("""Create an engaging text-based game centered around evolution using python. The game is an RPG with branching storylines so that the player's choices and actions within the game lead to significantly different storylines or outcomes. Begin as the initial life form and progress towards the future. Each decision you make including the first decicion at the start significantly impacts the future outcome. Make the story meaningful and make sure the consequenses of decicions surprises the player. Make the game deceptivly unfair. Make the players life a living hell after the first part of the game. Note that while the game aims to create a sense of unfairness, it is essential to balance it with meaningful choices and opportunities for redemption or growth. The goal is to engage the player and encourage reflection on the consequences of their decisions rather than making the game frustrating or discouraging. The Game should be text-based. The players decicions dictate what happens next so every playthrough should be unique with all the branching storylines and how the players choices affact the story. Use the players choices to create difficult situations so they feel like they barely survived. The game has no failure state. There are consequenses on the story but never a game ending in game over.""")
    interpreter.chat()

def evolution_game3():
    #interpreter.reset()
    interpreter.chat("""Create an engaging text-based game centered around evolution using python. The game is an RPG with branching storylines so that the player's choices and actions within the game lead to significantly different storylines or outcomes. Begin as the initial life form and progress towards the future. Each decision you make including the first decicion at the start significantly impacts the future outcome. Make the story meaningful and make sure the consequenses of decicions surprises the player. Make the game deceptivly unfair. Make the players life a living hell after the first part of the game. Note that while the game aims to create a sense of unfairness, it is essential to balance it with meaningful choices and opportunities for redemption or growth.""")
    interpreter.chat()

def evolution_game4():
    #interpreter.reset()
    interpreter.chat("""Create a text-based game centered around evolution using python. Every response should start with a block of python code that will print output.""")
    interpreter.chat()

def evolution_game5():
    #interpreter.reset()
    interpreter.chat("""Create an engaging text-based game centered around evolution using python. The game is an RPG with branching storylines so that the player's choices and actions within the game lead to significantly different storylines or outcomes. Begin as the initial life form and progress towards the future. Each decision you make including the first decicion at the start significantly impacts the future outcome. Make the story meaningful and make sure the consequenses of decicions surprises the player. Make the game deceptivly unfair. Make the players life a living hell after the first part of the game. Note that while the game aims to create a sense of unfairness, it is essential to balance it with meaningful choices and opportunities for redemption or growth. Every response should start with a block of python code that will print output.""")
    #interpreter.reset()
    interpreter.chat()

def turbo_test():
    #interpreter.reset()
    interpreter.chat("""create a snake game""")
    #interpreter.reset()
    interpreter.chat("""if you are finished, then run the game, else continue""")
    interpreter.chat()

def stuff():
    #interpreter.reset()
    interpreter.chat("""Write a program to calculate the factorial of a given number.""")
    interpreter.chat("""Create a function that reverses a string without using any built-in functions or libraries.""")
    interpreter.chat("""Implement a binary search algorithm to find the index of a target element in a sorted list.""")
    interpreter.chat("""Design a class hierarchy for different types of vehicles, including cars, motorcycles, and bicycles.""")
    interpreter.chat("""Develop a program that generates a random password with a specified length and complexity.""")
    interpreter.chat("""Write a function to check if a given string is a palindrome.""")
    interpreter.chat("""Create a web scraping script to extract data from a specific website and save it to a file.""")
    interpreter.chat("""Implement a sorting algorithm of your choice (e.g., bubble sort, merge sort, quicksort) and analyze its time complexity.""")
    interpreter.chat("""Design a simple chatbot that can answer basic questions or engage in a conversation.""")
    interpreter.chat("""Develop a program that simulates a game of tic-tac-toe between two players.""")
    interpreter.chat()


# test_hello_world()
# test_delayed_exec()
# test_nested_loops_and_multiple_newlines()
# test_markdown()
# test_math()
# evolution_game()
# evolution_game2()
# evolution_game3()
# evolution_game4()
# evolution_game5()
#stuff()






