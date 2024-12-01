
# import sys

# def part_1():

#     dataset = sys.argv[1]

#     with open(dataset) as f:
#         list = [line.split() for line in f]


#     sorted_array1 = []
#     sorted_array2 = []

#     for set in list:
#         # strip first number from second number in pairs
#         # sort them into two arrays
#         sorted_array1.append(int(set[0]))
#         sorted_array2.append(int(set[1]))

#     # sort the arrays from smallest to largest
#     sorted_array1.sort()
#     sorted_array2.sort()

#     diff = 0

#     for i in range(len(sorted_array1)):
#         if sorted_array1[i] > sorted_array2[i]:
#             diff += (sorted_array1[i] - sorted_array2[i])
#         else:
#             diff += (sorted_array2[i] - sorted_array1[i])

#     print(diff)

# def main():
#     part_1()

# if __name__ == "__main__":
#     main()


import sys

def read_input():

    dataset = sys.argv[1]

    with open(dataset) as f:
        data = [line.split() for line in f]

    return data

def part_1(data):

    sorted_array1 = []
    sorted_array2 = []

    for set in data:
        # strip first number from second number in pairs
        # sort them into two arrays
        sorted_array1.append(int(set[0]))
        sorted_array2.append(int(set[1]))

    # sort the arrays from smallest to largest
    sorted_array1.sort()
    sorted_array2.sort()

    diff = 0

    for i in range(len(sorted_array1)):
        if sorted_array1[i] > sorted_array2[i]:
            diff += (sorted_array1[i] - sorted_array2[i])
        else:
            diff += (sorted_array2[i] - sorted_array1[i])

    print(diff)

def part_2(data):

    sorted_array1 = []
    sorted_array2 = []

    for set in data:
        # strip first number from second number in pairs
        # sort them into two arrays
        sorted_array1.append(int(set[0]))
        sorted_array2.append(int(set[1]))

    # sort the arrays from smallest to largest
    sorted_array1.sort()
    sorted_array2.sort()

    # Find the number of similar numbers in the two arrays, comparing left to how many similar numbers are in the right
    # Create a multidimensional array to store the number of similar numbers in the two arrays
    # So if there are 3 counts of 3, the array would look like [3[3]]
    sim_counter = []
    for i in range(len(sorted_array1)):
        sim_counter.append(0)

    for i in range(len(sorted_array1)):
        for j in range(len(sorted_array2)):
            if sorted_array1[i] == sorted_array2[j]:
                sim_counter[i] += 1

    # Create multidimensional array with [number, count] pairs
    multi_array = []
    for i in range(len(sorted_array1)):
        multi_array.append([sorted_array1[i], sim_counter[i]])

    # Multiply the number by the count and add it to the total
    total = 0
    for i in range(len(multi_array)):
        total += (multi_array[i][0] * multi_array[i][1])

    print(total)

def main():
    data = read_input()
    part_1(data)
    part_2(data)

if __name__ == "__main__":
    main()