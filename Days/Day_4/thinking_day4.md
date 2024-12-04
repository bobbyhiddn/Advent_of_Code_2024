Ok so this is definitely more complicated than yesterday, but I think I know where to start. It's a crossword puzzle, so we need to think through out procedural generation brain and remember how we built sudoku.

First:

xmas_counter = 0

for row in rows:
    for i, char in enumerate(row):
        if char == "X":
            check space to all diagonal and orthoganal positions for 'M'
            then determine what space that M came from and continue in that direction to see is there is an A
            Same for S. 

            Break on any missing letters, but return a count if we find an S. 

I knew sudoku would come in handy. Ok, now we need to check for A's and do the same thing but we are only making the phrase MAS twice to form an X like this:

M.S
.A.
M.S

So we need to perform the same logic for A instead of X, but only at the diagonal positions, and looking for an M on one side and an S on the other.