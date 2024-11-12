def count_numbers(numbers):
    count_dict = {}

    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1

        else:
            count_dict[num] = 1

    return count_dict


numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
