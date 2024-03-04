def solution(N):
    # Define all lowercase letters
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    num_letters = min(N, len(letters))
    num_repetitions = N // num_letters
    
   
    result = letters[:num_letters] * num_repetitions
    
    if N % num_letters != 0:
        result += letters[:N % num_letters]
    print(result)
    return result
solution(3)