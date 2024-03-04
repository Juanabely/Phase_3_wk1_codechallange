## Readme file for phase3 wk1 codechallange 
## 1:bricks.py
This function first checks if it’s possible to have exactly 10 bricks in every box. If not, it returns -1. Then it calculates the minimum number of moves needed to end up with exactly 10 bricks in every box. It does this by iterating over each box and moving bricks from or to the next box until there are exactly 10 bricks in the current box. The number of moves is then returned. 
## 2: Letter.py
This function first calculates the number of different letters (num_letters) and the number of repetitions (num_repetitions). Then it creates a string (result) by repeating the first num_letters letters num_repetitions times. If N is not a multiple of num_letters, it adds the remaining letters to result. Finally, it returns result.

For example, if you call solution(3), the function will return "abc". Each of these strings contains three different letters with the same number of occurrences.
## 3:num.py
This function first Initialize a dictionary to store the sums of digits and then Iterate over each number in the array,then Calculate the sum of digits of the current number and finally  Updates the dictionary with the maximum number that has the current sum of digits.