def solution(A):
    # Initialize a dictionary to store the sums of digits
    sums = {}
    max_sum = -1

    # Iterate over each number in the array
    for num in A:
        # Calculate the sum of digits of the current number
        digit_sum = sum(int(digit) for digit in str(num))

        # If the sum of digits is already in the dictionary, update the max_sum
        if digit_sum in sums:
            max_sum = max(max_sum, sums[digit_sum] + num)

        # Update the dictionary with the maximum number that has the current sum of digits
        sums[digit_sum] = max(sums.get(digit_sum, 0), num)
    print(max_sum)
    return max_sum
solution([51, 71, 17, 42])