from bs4 import BeautifulSoup
import requests

def GetPuzzle():
    url = "https://www.menneske.no/sudoku/eng/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    soup.prettify()

    data = soup.find("div", {"class": "grid"}).text
    data = data[2:] #Removes first two elements of puzzle because they are just "\n" new line elements.
    data = data.replace("\xa0", "") #Removes "\xa0" elements from puzzle.

    dataCheck = data[0]
    dataCount = 0
    while dataCheck != "S": #Loop removes the new line element after every character.
        if data[dataCount] != "\n":
            data = data[:dataCount + 1] + data[dataCount + 2:]
        dataCount += 1
        dataCheck = data[dataCount]

    sudokuPuzzle = []
    puzzleRow = []
    for i in range(9): #Loop turns puzzle into a nested list so that it can be easily altered and inspected.
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
