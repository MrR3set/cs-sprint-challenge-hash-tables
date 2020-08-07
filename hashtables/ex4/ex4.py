def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    a.sort()
    pairs = {}
    for nums in a:
        if nums<0:
            pairs[abs(nums)] = False
        else:
            if nums in pairs:
                pairs[nums] = True


    result=[key for key, value in pairs.items() if value == True]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
