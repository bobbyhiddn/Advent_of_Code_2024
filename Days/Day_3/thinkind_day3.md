# Alright, let's do better today. 
A little scared at how long it took me yesterday.

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

Ok, so part 1 is fairly easy, it essentiallly just requires us to break the line into rows that start with an m.


So we need to go: 

dataset = read from file
build-a-row = []

for each character in row:
    if character is m:
        append the row starting from that character to the end of the line.
    
for each row in build-a-row:
    

Then we need to go through the rows and split them into the function and the arguments.