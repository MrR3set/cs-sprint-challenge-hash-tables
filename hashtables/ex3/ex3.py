def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # We use intersect to find the numbers of the first 2 arrays, inside this group of numbers there will be the numbers that repeat in all the arrays
    
    numbers = {}

    # Count all the numbers
    for array in arrays:
        for num in array:
            if num not in numbers:
                numbers[num]=1
            else:
                numbers[num]+=1





    # Only return thos numbers that length is == len(arrays)
    result = [ key for key, value in numbers.items() if value == len(arrays) ]



    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])


    print(intersection(arrays))
