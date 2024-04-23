
def countSeeablePeople(heights):
    def sees(i: int, j: int) -> bool:
        # print(i, j, heights[i+1:j+1], [heights[i], heights[j]], min([heights[i], heights[j]]), max(heights[i+1:j]))
        return i < j and min([heights[i], heights[j]]) >= max(heights[i+1:j])

    seen_count = 1 
    for position in range(2, len(heights)):
        if sees(0, position):
            seen_count += 1
    return seen_count

print(countSeeablePeople([10, 2, 2, 2, 2, 2, 2, 2, 2]))
print(countSeeablePeople([10, 2, 2, 2]))
print(countSeeablePeople([10, 2, 2, 10, 9]))

# Does not work
print(countSeeablePeople([10, 9, 8, 7, 6, 6]))
print(countSeeablePeople([1, 2, 3, 4, 5, 7]))
print(countSeeablePeople([1, 1, 1, 2, 3, 4, 5, 6]))
print(countSeeablePeople([10, 4, 5, 1, 1, 1, 4]))

