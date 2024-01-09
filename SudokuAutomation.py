print("Importing modules...")
import SudokuWebScraper, SudokuSolver
import numpy as np
from time import sleep
import pyautogui as robot

print("Retrieving puzzle...")
puzzle, puzzleID = SudokuWebScraper.GetPuzzle()
puzzle = np.array(puzzle)
print(f"Puzzle from \"https://www.menneske.no/sudoku/eng/\"\nPuzzle ID is {puzzleID}.\nPuzzle:")
print(puzzle, "\nSolving puzzle...")
puzzle = SudokuSolver.SolvePuzzle(puzzle)
print("Solved")

robot.moveTo(1050, 1030) #This code will not work as it should on other computers because of dimensions of screen and location of apps on taskbar.
robot.click()
sleep(2)
robot.typewrite(f"https://www.menneske.no/sudoku/eng/solve.html?number={puzzleID}")
robot.press("enter")
sleep(4) #This 4 second sleep function is used to allow the webpage time to load.
robot.moveTo(1900, 200)
robot.dragTo(1900, 350, 1, button="left")
rowX = 0
columnY = 0
for row in puzzle:
    rowX = 0
    for square in row:
        robot.moveTo(660 + (rowX * 65), 260 + (columnY * 65))
        robot.click()
        robot.typewrite(square)
        rowX += 1
    columnY += 1
robot.press("enter")
