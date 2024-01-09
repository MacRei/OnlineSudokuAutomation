def SolvePuzzle(puzzle):
    alterableSquares = []
    position = 0
    alter = False
    while position != 81:
        square = puzzle[(position // 9)][(position % 9)]
        block = puzzle[(((position // 9) // 3) * 3):((((position // 9) // 3) * 3) + 3), (((position % 9) // 3) * 3):((((position % 9) // 3) * 3) + 3)]
        column = [puzzle[0][(position % 9)], puzzle[1][(position % 9)], puzzle[2][(position % 9)], puzzle[3][(position % 9)], puzzle[4][(position % 9)],
                puzzle[5][(position % 9)], puzzle[6][(position % 9)], puzzle[7][(position % 9)], puzzle[8][(position % 9)]]
        row = puzzle[(position // 9)]
        if square == "_":
            alterableSquares.append(position)
            options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for option in options:
                if option not in block and option not in row and option not in column:
                    puzzle[(position // 9)][(position % 9)] = option
                    break
            if puzzle[(position // 9)][(position % 9)] == "_":
                alter = True
                alterableSquares.pop((-1))
                position = alterableSquares[-1]
                continue
            else:
                alter = False
        elif alter:
            option = int(square)
            option += 1
            while option != 10:
                if str(option) not in block and str(option) not in row and str(option) not in column:
                    puzzle[(position // 9)][(position % 9)] = str(option)
                    alter = False
                    break
                option += 1
            if option == 10:
                puzzle[(position // 9)][(position % 9)] = "_"
                alterableSquares.pop((-1))
                position = alterableSquares[-1]
                continue
        position += 1
    return puzzle
