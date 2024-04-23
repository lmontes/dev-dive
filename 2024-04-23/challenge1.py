def countSeeablePeople(heights):
    def sees(i: int, j: int) -> bool:
        # print(i, j, heights[i+1:j+1], [heights[i], heights[j]], min([heights[i], heights[j]]), max(heights[i+1:j]))
        return i < j and min([heights[i], heights[j]]) > max(heights[i+1:j])

    seen_count = 1 
    for position in range(2, len(heights)):
        if sees(0, position):
            seen_count += 1
    return seen_count


print(countSeeablePeople([10, 3, 4, 5, 6, 10, 9]))
print(countSeeablePeople([6, 6, 5, 5, 5, 6, 5]))
print(countSeeablePeople([6, 5, 4, 5, 5, 6, 5, 10]))