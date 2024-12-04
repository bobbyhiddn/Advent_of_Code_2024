import sys

def read_file(file_path):
    with open(file_path, 'r') as file:
        rows = []
        for line in file:
            # Convert strings to integers during initial read
            row = [int(x) for x in line.strip().split()]
            rows.append(row)
    return rows

def part_1(rows):
    
    print(rows)

    ascending_rows = []
    descending_rows = []
    
    for row in rows:
        is_ascending = True
        is_descending = True
        has_equals = False
        has_large_diff = False
        
        # Check pattern, equals, and differences
        for i in range(len(row) - 1):
            diff = abs(row[i] - row[i+1])
            
            if diff > 3:
                has_large_diff = True
                break
            elif row[i] == row[i+1]:
                has_equals = True
                break
            elif row[i] > row[i+1]:
                is_ascending = False
            elif row[i] < row[i+1]:
                is_descending = False
            
            # Break if neither pattern holds
            if not is_ascending and not is_descending:
                break
        
        # Only add valid complete rows
        if not has_equals and not has_large_diff:
            if is_ascending:
                ascending_rows.append(row)
            elif is_descending:
                descending_rows.append(row)

    
    print("Ascending rows:", ascending_rows)
    print("Descending rows:", descending_rows)

    print("Valid rows:", len(ascending_rows) + len(descending_rows))

# Built this after part 1
def is_valid_sequence(sequence):
    if len(sequence) < 2:
        return False
        
    is_ascending = True
    is_descending = True
    
    for i in range(len(sequence) - 1):
        diff = abs(sequence[i] - sequence[i+1])
        
        if diff > 3 or sequence[i] == sequence[i+1]:
            return False
            
        if sequence[i] > sequence[i+1]:
            is_ascending = False
        elif sequence[i] < sequence[i+1]:
            is_descending = False
        
        if not is_ascending and not is_descending:
            return False
            
    return True

def part_2(rows):
    violation_count = 0
    
    for row in rows:
        # Try removing each number and check if sequence becomes valid
        for i in range(len(row)):
            # Create new sequence without current number
            test_sequence = row[:i] + row[i+1:]
            if is_valid_sequence(test_sequence):
                violation_count += 1
                break
    
    print("Rows that can be fixed by removing one number:", violation_count)

def main():
    rows = read_file(sys.argv[1])
    part_1(rows)
    part_2(rows)

if __name__ == "__main__":
    main()