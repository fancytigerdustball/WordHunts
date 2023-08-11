''' Module that creates crossword puzzles '''

from string import ascii_uppercase as auc
import random

DIRECTS = [-1, 0, 1]

def print_matrix(matrix):
    ''' Print the given matrix '''

    print()
    for y in matrix:
        for x in y:
            print(' ' + x, end='')
        print()

words = []
word = 'a'
while True:
    try:
        word = input('> ')
        if not word.isalpha():
            raise EOFError
        words.append(word.upper())
    except (KeyboardInterrupt, EOFError):
        pass

    if not word.isalpha():
        break

width = int(input('Width: '))
height = int(input('Height: '))
matrix = list([''] * width for _ in range(height))

for word in words:
    length = len(word)

    while True:
        # Make word index
        while True:
            # Make x and y
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            # Choice direction
            plusx = random.choice(DIRECTS)
            plusy = random.choice(DIRECTS)
            # Check if word is OK
            if x + (plusx * length):
                continue
            if y + (plusy * length):
                continue
            if plusx == 0 and plusy == 0:
                continue
            break

        # Draw word on matrix
        for i in range(length):
            letter = word[i]
            if matrix[y][x]:
                continue
            matrix[y][x] = letter
            x += plusx
            y += plusy
        break

# Fill in matrix
for yi, y in enumerate(matrix):
    for xi, x in enumerate(y):
        if not x:
            matrix[yi][xi] = random.choice(auc)

# Print matrix
print_matrix(matrix)

while True:
    pass
