# Online Sudoku Automation

# About The Project
Program Demonstration:
https://youtu.be/J4sAI-ql00A

This project is 3 python files that work together to scrape a random sudoku puzzle from the website, "https://www.menneske.no/sudoku/eng/," solve the puzzle, and then take control of the mouse and keyboard to then go to the website to solve the puzzle. 

One of the reasons I made this project was to learn how to use beautiful soup and requests to retrieve data from the web. Web scraping is useful because of how it can be used for many different purposes to create interesting projects. I wanted to make a sudoku solving algorithm because it seemed like a challenge that required lots of skill and a deep understanding of computer science concepts like implementation of loops and indexing and managing of lists. I was also wanted to learn how to automate with python using pyautogui, even though automating a computer to solve a sudoku puzzle isn't particularly helpful, creating these projects has made me into a much stronger programmer.

The first part of this project was creating a program to retrieve a puzzle from the web using beautiful soup and requests, this was difficult because first I had to find a website that would easily allow for me to scrape it's data. Then I had to parse through the HTML to get the individual numbered squares and empty squares of the puzzle and allocate it in a way that would be easy for me to manipulate. I stored the puzzle as a nested array using numpy so I could easily view and change the puzzle.

The second part of this project was creating the algorith to solve the puzzle. I wanted the code to be original so I wrote it without any help, I only researched ways that programs solved sudoku puzzles and found the backtracking method where the program will enter a 1 into an empty square and if it interferes with any other squares in its row, column, or block, going up by 1 value. Then repeating this until it either finds a value that does not conflict with other squares or getting past 9, it which case the program will go to the previous alterable square and repeat the process of finding a value that does not conflict or going further back in the puzzle. Creating this algorithm was the part of the project that took the most time and was the most complex but I learned a lot about concepts like how to debug to solve complex issues and managing arrays. I hope to remake the program one day using recursion.

The final part of the project was using pyautogui to automate my computer solving the puzzle. This part was pretty straight foward of giving the computer specific instructions of where to move the mouse what to type in the keyboard to go to the website and solve the puzzle. Unfortunately, other users will have to enter different coordinates into the code for the program to work on their computer, and because of connection times and ad sizes, occasionaly the program will not enter the squares into the correct location of the puzzle on the website.

# Using The Program
First you will have to have certain libraries installed on your computer, these libraries are, BeautifulSoup, requests, numpy, and pyautogui. These libraries can be installed on your computer by entering these commands into your terminal, "pip install beautifulsoup4," "pip install requests," "pip install numpy," and "pip install pyautogui."

Next you will have to alter the coordinates of where you pyautogui will move your mouse in the end of the "SudokuAutomation" file so that it fits your computer. First it must click the search engine on your task bar, then it must drag your scroll bar to the right level. And finally it must enter all squares of the puzzle correctly.
