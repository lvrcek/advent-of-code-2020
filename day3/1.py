with open('in.txt') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

right = 1
down = 2 # write this in a loop

x, y = 0, 0
end = len(lines)
length = len(lines[0])
counter = 0

while True:
    x = (x + right) % length
    y += down
    if y >= end:
        break

    if lines[y][x] == '#':
        counter += 1

print(counter)