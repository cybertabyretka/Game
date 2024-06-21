import random

from Utils.Settings.DataStructures.Stack import Stack


def partition(start_index: int, end_index: int, current_index: int, saves, indexes) -> int:
    while start_index < end_index:
        start_date, start_time = saves[start_index].get_date_and_time_as_tuples()
        current_date, current_time = saves[current_index].get_date_and_time_as_tuples()
        end_date, end_time = saves[end_index].get_date_and_time_as_tuples()
        if start_date < current_date:
            start_index += 1
        elif start_date == current_date:
            if start_time < current_time:
                start_index += 1
        if end_date > current_date:
            end_index -= 1
        elif end_date == current_date:
            if end_time > current_time:
                end_index -= 1
        elif start_index < end_index and start_date >= current_date >= end_date:
            saves[start_index], saves[end_index] = saves[end_index], saves[start_index]
            indexes[start_index], indexes[end_index] = indexes[end_index], indexes[start_index]
            if start_index == current_index:
                current_index = end_index
                start_index += 1
            elif end_index == current_index:
                current_index = start_index
                end_index -= 1
            else:
                start_index, end_index = start_index + 1, end_index - 1
    return current_index


def saves_indexes_quick_sort(saves, indexes):
    if len(saves) in [0, 1]:
        return
    stack = Stack((0, len(saves) - 1))
    while not stack.is_empty():
        left, right = stack.peek()[0], stack.pop()[1]
        current_index = random.randint(left, right)
        current_index = partition(left, right, current_index, saves, indexes)
        if current_index + 1 < right:
            stack.push((current_index + 1, right))
        if left < current_index - 1:
            stack.push((left, current_index - 1))