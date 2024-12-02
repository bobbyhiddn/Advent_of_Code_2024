So we have the function for finding out if the list is greater than or less than, now we need to figure out how to track that info to tell if the list contained one or the other throughout. So the logic right now is:

for row in rows
    for iteration in length of row -1
        if the rows iteration is greater than it's next iteration, print greater than
    else if the rows iteration is less than it's next iteration, print less than


So we need to modify the loop so that it adds to a temporary counter until the end of the row, then prints the result. So the logic would be:

greaterthan = []
lessthan = []

for row in rows
    for iteration in length of row -1
        if the rows iteration is greater than it's next iteration, append to row in greaterthan

    else if the rows iteration is less than it's next iteration, append to row in lessthan

Then we need to return the number of rows in either of the new arrays that the same number of elements as their entry in the original array. 

So really the logic should go that the loop only adds the row to the greaterthan or lessthan arrays if the length of the row is the same as the length in the original array. It should stop iterating once it finds a row doesn't continue in the same order, add it to a sorting array, and then continue to the next row.


The second part is kicking my butt.

I need to get a violation counter for sure, and one way to do it would be to remove a number at a time from a row at a time and run the first part, only taking the rows that are able to pass in only one way. That might be the move. I would just need to figure out the logic for one more loop where we run against the array minus the element at the current index.