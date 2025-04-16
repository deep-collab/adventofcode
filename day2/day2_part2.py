def is_safe(levels):
    if len(levels) < 2:
        return False

    direction = None

    for i in range(len(levels) - 1):
        a = int(levels[i])
        b = int(levels[i + 1])
        diff = b - a

        if diff == 0 or abs(diff) > 3:
            return False

        if direction is None:
            direction = "increasing" if diff > 0 else "decreasing"
        elif (direction == "increasing" and diff < 0) or \
             (direction == "decreasing" and diff > 0):
            return False

    return True

# Read and parse input
with open("input.txt", "r") as f:
    lines = f.read().strip().splitlines()
print(lines)

arrays = [line.split() for line in lines]
print(arrays)

safe_count = 0

for levels in arrays:
    # First check the original list
    print(levels)
    if is_safe(levels):
        print(f"safe levels: {levels}")
        safe_count += 1
        continue

    # Try removing each element one-by-one
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        print(f"new levels {new_levels}")
        if is_safe(new_levels):
            safe_count += 1
            break  # no need to try more removals if already safe

print(safe_count)
