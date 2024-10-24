import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def add_times(time1: data.Time, time2: data.Time) -> data.Time:
    total_seconds = (time1.hour * 3600 + time1.minute * 60 + time1.second) + \
                    (time2.hour * 3600 + time2.minute * 60 + time2.second)

    hours = (total_seconds // 3600) % 24
    minutes = (total_seconds // 60) % 60
    seconds = total_seconds % 60

    return data.Time(hours, minutes, seconds)

# Part 4
def is_descending(numbers: list[float]) -> bool:
    if len(numbers) <= 1:
        return True
    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[i - 1]:
            return False

    return True

# Part 5
def largest_between(nums:list[int], lower:int, upper:int ):
    if lower > upper:
        return None
    if lower < 0:
        lower = 0
    if upper >= len(nums):
        upper = len(nums) - 1
    max_value = nums[lower]
    max_index = lower
    for i in range(lower, upper + 1):
        if nums[i] > max_value:
            max_value = nums[i]
            max_index = i

    return max_index

# Part 6

def furthest_from_origin(points):
    if not points:
        return None
    max_index = 0
    max_distance_squared = points[0].x ** 2 + points[0].y ** 2
    for index in range(1, len(points)):
        distance_squared = points[index].x ** 2 + points[index].y ** 2
        if distance_squared > max_distance_squared:
            max_distance_squared = distance_squared
            max_index = index
    return max_index
