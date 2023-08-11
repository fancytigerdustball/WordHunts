''' Module that solves crossword puzzles

It solves by looping through each cell.
If the cell is the first letter of the word checking for,
check the cell's neighbors for the next letter in the word.
If one is found continue in that direction.
If the whole word is found, show result. '''

matrix = []

row = 'a'
while True:
    try:
        row = input('> ')
        if not row.isalpha():
            raise EOFError
        matrix.append(list(row))
    except (KeyboardInterrupt, EOFError):
        pass

    if not row.isalpha():
        break

is_complete = False

# Create list for holding tuples to find neighboring cells
editions = []
for plusx in range(-1, 2):
    for plusy in range(-1, 2):
        if plusx or plusy: # As long as they aren't both 0
            editions.append((plusx, plusy))

while True:
    word = input('Find word: ')
    is_complete = False
    
    for yi, y in enumerate(matrix):
        for xi, x in enumerate(y):
            index = 0 # Letter index currently checking for
            if x == word[index]:

                index += 1
                for plusx, plusy in editions:
                    try:
                        if matrix[yi + plusy][xi + plusx] == word[index]:
                            # Check for completed word
                            index = 0
                            x = xi
                            y = yi
                            is_complete = True
                            while index < len(word):
                                try:
                                    if matrix[y][x] == word[index]:
                                        x += plusx
                                        y += plusy
                                        index += 1
                                    else:
                                        is_complete = False
                                        break
                                except IndexError:
                                    pass
                                
                            if is_complete:
                                print(f'{word.upper()}> (x:{xi + 1}, y:{yi + 1})')
                            break
                        
                    except IndexError:
                        pass
                    
            if is_complete:
                break
            
        if is_complete:
            break
