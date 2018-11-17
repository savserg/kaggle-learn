def count_negatives1(nums):
    return len([num for num in nums if num < 0])

def count_negatives2(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of 
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])
