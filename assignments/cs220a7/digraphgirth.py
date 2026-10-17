import sys

def main():
    lines = sys.stdin.read().strip().splitlines()

    current_node = 0
    seen = []
    girth = 0

    for line in lines:
        if line.strip() == "":
            continue

        outneigbours = line.split(" ")
        seen = [current_node]
        result = find_girth(seen, outneigbours, current_node)
        if result:
            girth = result
            break
        current_node += 1
    print(girth)

def find_girth(seen, outneighbours, current_node):
    if current_node in outneighbours:
        return len(seen)
    else:
        for neighbour in outneighbours:
            if neighbour not in seen:
                seen.append(neighbour)
                result = find_girth(seen, outneighbours, neighbour)
                if result:
                    return result
    return False
