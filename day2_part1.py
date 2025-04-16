with open("input.txt", "r") as f:
    input = f.read()
    array = input.split("\n")

arrays = []
for i in range(len(array)):
    arrays.append(array[i].split())

def if_safe(levels):
    if(len(levels) < 2):
        return False
    
    direction = None

    for i in range(len(levels)-1):
        diff = int(levels[i+1]) - int(levels[i])

        if(diff == 0 or (abs(diff) > 3)):
            return False

        if direction is None:
            direction = "increasing" if diff > 0 else "decreasing"
        else:
            if(direction == "increasing" and diff < 0) or (direction == "decreasing" and diff > 0):
                return False

    return True
count = 0

for i in range(len(arrays)):
    if if_safe(arrays[i]):
        count += 1


print(count)