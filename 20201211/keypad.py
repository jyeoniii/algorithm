# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

def solution(numbers, hand):
    is_left = True if hand == "left" else False
    left_numbers, right_numbers = [1, 4, 7], [3, 6, 9]
    pos = [
        [3, 1],  # 0
        [0, 0], [0, 1], [0, 2],  # 1, 2, 3
        [1, 0], [1, 1], [1, 2],  # 4, 5, 6
        [2, 0], [2, 1], [2, 2],  # 7, 8, 9
        [3, 0], [3, 2]  # * #
    ]
    left_cursor, right_cursor = 10, 11
    for i, num in enumerate(numbers):
        if num in left_numbers:
            numbers[i] = 'L'
            left_cursor = num
        elif num in right_numbers:
            numbers[i] = 'R'
            right_cursor = num
        else:
            left_distance = abs(pos[left_cursor][0] - pos[num][0]) + abs(pos[left_cursor][1] - pos[num][1])
            right_distance = abs(pos[right_cursor][0] - pos[num][0]) + abs(pos[right_cursor][1] - pos[num][1])
            if left_distance > right_distance:
                right_cursor = num
                numbers[i] = 'R'
            elif left_distance < right_distance:
                left_cursor = num
                numbers[i] = 'L'
            else:  # Equal
                if is_left:
                    left_cursor = num
                    numbers[i] = 'L'
                else:
                    right_cursor = num
                    numbers[i] = 'R'

    return ''.join(numbers)