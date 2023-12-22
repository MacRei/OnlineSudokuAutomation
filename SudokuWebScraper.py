from bs4 import BeautifulSoup
import requests

def GetPuzzle():
    url = "https://www.menneske.no/sudoku/eng/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    soup.prettify()

    data = soup.find("div", {"class": "grid"}).text #Retrieves Puzzle
    data = data[2:] #Removes first two elements of puzzle because they are just \n
    data = data.replace("\xa0", "") #Removes \xa0 from puzzle because I don't know why they are there, I think its a break sequence, do research.

    #Following loop removes the new line element after every character
    dataCheck = data[0]
    dataCount = 0
    while dataCheck != "S":
        if data[dataCount] != "\n":
            data = data[:dataCount + 1] + data[dataCount + 2:] #Removing characters using translation
        dataCount += 1
        dataCheck = data[dataCount]

    #Turns puzzle into a nested loop that can be altered
    sudokuPuzzle = []
    puzzleRow = []
    for i in range(9):
        for ii in range(9):
            if data[ii] != "\n":
                puzzleRow.append(data[ii])
            else:
                puzzleRow.append("_")
        sudokuPuzzle.append(puzzleRow)
        puzzleRow = []
        data = data[11:]

    puzzleNumber = data[22:29]
    return sudokuPuzzle, puzzleNumber