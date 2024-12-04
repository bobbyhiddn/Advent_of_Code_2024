import sys
import re

def read_input():
    dataset = sys.argv[1]
    with open(dataset) as f:
        # Read raw lines, strip whitespace
        return [line.strip() for line in f]
    

def part_1(data):
    collected_data = []
    
    # Pattern matches mul followed by two numbers in parentheses
    pattern = r'mul\((\d+),(\d+)\)'
    
    for line in data:
        # Find all matches in the line
        matches = re.finditer(pattern, line)
        for match in matches:
            # Get the full match
            full_match = match.group(0)
            # Get the two numbers
            num1, num2 = match.groups()
            collected_data.append((full_match, int(num1), int(num2)))

    print("Collected data:", collected_data[:10])

    counter = 0

    for line in collected_data:
        counter += line[1] * line[2]

    print("Counter:", counter)


def part_2(data):
    counter = 0
    active = True  # Start active until first don't()

    # Patterns for matching
    mul_pattern = r'mul\((\d+),(\d+)\)'
    do_pattern = r'do\(\)'
    dont_pattern = r"don'?t\(\)"

    for line in data:
        position = 0
        line_length = len(line)
        while position < line_length:
            # Find the next events from the current position
            mul_match = re.search(mul_pattern, line[position:])
            do_match = re.search(do_pattern, line[position:])
            dont_match = re.search(dont_pattern, line[position:])
            
            # Collect matches with their adjusted positions
            matches = []
            if mul_match:
                matches.append((mul_match.start() + position, 'mul', mul_match))
            if do_match:
                matches.append((do_match.start() + position, 'do'))
            if dont_match:
                matches.append((dont_match.start() + position, 'dont'))

            if not matches:
                break  # No more events in this line

            # Get the earliest event
            matches.sort(key=lambda x: x[0])
            event_pos, event_type, *match = matches[0]
            position = event_pos + 1  # Move past the event

            if event_type == 'do':
                active = True
            elif event_type == 'dont':
                active = False
            elif event_type == 'mul':
                num1, num2 = map(int, match[0].groups())
                if active:
                    counter += num1 * num2

    print(f"Final counter: {counter}")
    return counter


def main():
    data = read_input()
    print("Data:", data)
    part_1(data)
    part_2(data)

if __name__ == "__main__":
    main()