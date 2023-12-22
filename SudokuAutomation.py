print("Importing modules...")
import SudokuWebScraper
import SudokuSolver
import numpy as np
from time import sleep
import pyautogui as robot

print("Retrieving puzzle...")
puzzle, puzzleID = SudokuWebScraper.GetPuzzle()
puzzle = np.array(puzzle)
print(f"Puzzle from \"https://www.menneske.no/sudoku/eng/\"\nPuzzle ID is {puzzleID}.\nPuzzle:")
print(puzzle)
puzzle = SudokuSolver.SolvePuzzle(puzzle)
if "_" in puzzle:
    print("Can't Solve")
else:
    print("Solved")
    robot.moveTo(1050, 1030)
    robot.click()
    sleep(2)
    robot.typewrite(f"https://www.menneske.no/sudoku/eng/solve.html?number={puzzleID}")
    robot.press("enter")
    sleep(2)
    robot.moveTo(1900, 200)
    robot.dragTo(1900, 350, 1, button="left") #640 240
    rowX = 0
    columnY = 0
    for row in puzzle:
        rowX = 0
        for square in row:
            robot.moveTo(640 + (rowX * 65), 240 + (columnY * 65))
            robot.click()
            robot.typewrite(square)
            rowX += 1
            #sleep(1)
        columnY += 1
    robot.press("enter")