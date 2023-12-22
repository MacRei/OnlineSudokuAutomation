import time
def SolvePuzzle(puzzle):
    iterations = 0
    while iterations <= 10:
        alterableSquares = []
        distanceOfSquares = 0
        #while "_" in puzzle:
        ySquare = 0
        for row in puzzle:
            xSquare = 0
            for square in row:
                if square == "_":
                    distanceOfSquares += 1
                    options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    erase = []
                    block = puzzle[((ySquare // 3) * 3):(((ySquare // 3) * 3) + 3), ((xSquare // 3) * 3):(((xSquare // 3) * 3) + 3)]
                    column = [puzzle[0][xSquare], puzzle[1][xSquare], puzzle[2][xSquare], puzzle[3][xSquare], puzzle[4][xSquare],
                              puzzle[5][xSquare], puzzle[6][xSquare], puzzle[7][xSquare], puzzle[8][xSquare]]
                    for number in options:
                        if number in row or number in block or number in column:
                            erase.append(number)
                    options = list(set(options) - set(erase))
                    if len(options) == 1:
                        puzzle[ySquare][xSquare] = options[0] 
                    #if len(options) == 0:
                    #    print("Ligma")
                    #else:
                    #    puzzle[ySquare][xSquare] = options[0] 
                    #print(options)
                else:
                    alterableSquares.append(distanceOfSquares)
                    distanceOfSquares = 0
                xSquare += 1
            ySquare += 1
        #print(alterableSquares)
        #print(puzzle)
        #print(iterations)
        iterations += 1
        if "_" not in puzzle:
            break
    return puzzle
    #puzzleCompleted = False
    #while not puzzleCompleted:
    #    puzzleCompleted = True
    #    squareY = 0
    #    for row in puzzle:
    #        squareX = 0
    #        for square in row:
    #            block = puzzle[((squareY // 3) * 3):(((squareY // 3) * 3) + 3), ((squareX // 3) * 3):(((squareX // 3) * 3) + 3)] #Makes a block
    #            print(square)
    #            print(block)
    #            erase = []
    #            if square == "_":
    #                options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    #                for number in options:
    #                    if number in row: #Disregarding characters in the same row
    #                        erase.append(number)
    #                        print(f"{number} in Row")
    #                    if number in block and number not in erase:
    #                        print(f"{number} in Block")
    #                        erase.append(number)
    #                for number in puzzle:
    #                    if number[squareX] in options and number[squareX] not in erase: #Disregarding characters in the same column
    #                        print(f"{number[squareX]} in Column")
    #                        erase.append(number[squareX])
    #                if len(erase) == 8:
    #                    options = list(set(options) - set(erase))
    #                    puzzle[squareX][squareY] = options[0]
    #                    puzzleCompleted = False
    #            print()
    #            squareX += 1
    #        squareY += 1
    #    break
    #        
    #print(puzzle)