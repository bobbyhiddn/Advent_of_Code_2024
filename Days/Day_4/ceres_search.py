import sys

def read_input():
    dataset = sys.argv[1]
    with open(dataset) as f:
        # Read raw lines, strip whitespace
        return [line.strip() for line in f]

def part_1(data):
    xmas_counter = 0

    directions = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1),  (1, 0), (1, 1)]

    word = "XMAS"

    row_count = len(data)
    col_count = len(data[0]) if data else 0

    for row_index, row in enumerate(data):
        for col_index, char in enumerate(row):
            if char == "X":
                for dx, dy in directions:
                    x, y = row_index, col_index
                    found = True
                    for letter in word[1:]:
                        x += dx
                        y += dy
                        if 0 <= x < row_count and 0 <= y < col_count and data[x][y] == letter:
                            continue
                        else:
                            found = False
                            break
                    if found:
                        xmas_counter += 1

    print("XMAS Counter:", xmas_counter)

def part_2(data):
    x_counter = 0
    diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    row_count = len(data)
    col_count = len(data[0]) if data else 0

    for row_index, row in enumerate(data):
        for col_index, char in enumerate(row):
            if char == "A":
                for dx1, dy1 in diagonal_directions:
                    x_m1, y_m1 = row_index + dx1, col_index + dy1
                    if 0 <= x_m1 < row_count and 0 <= y_m1 < col_count and data[x_m1][y_m1] == 'M':
                        # Calculate first S position (opposite to first M)
                        x_s1, y_s1 = row_index - dx1, col_index - dy1
                        
                        # Calculate perpendicular direction for second M
                        dx2, dy2 = dy1, -dx1  # Rotate 90 degrees
                        x_m2, y_m2 = row_index + dx2, col_index + dy2
                        
                        # Calculate second S position
                        x_s2, y_s2 = row_index - dx2, col_index - dy2
                        
                        if (0 <= x_s1 < row_count and 0 <= y_s1 < col_count and data[x_s1][y_s1] == 'S' and
                            0 <= x_m2 < row_count and 0 <= y_m2 < col_count and data[x_m2][y_m2] == 'M' and
                            0 <= x_s2 < row_count and 0 <= y_s2 < col_count and data[x_s2][y_s2] == 'S'):
                            x_counter += 1

    print("XMAS Counter:", x_counter)

def main():
    data = read_input()
    part_1(data)
    part_2(data)

if __name__ == "__main__":
    main()