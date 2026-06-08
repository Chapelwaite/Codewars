def snail(array):
    if array == [[]]:
        return []

    result = []

    top = 0
    bottom = len(array) - 1
    left = 0
    right = len(array[0]) - 1

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            result.append(array[top][i])
        top += 1

        # მარჯვენა სვეტი ↓
        for i in range(top, bottom + 1):
            result.append(array[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(array[bottom][i])
            bottom -= 1


        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(array[i][left])
            left += 1

    return result


# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python