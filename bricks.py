A = [7, 15, 10, 8]
def solution(A):
    total_bricks = sum(A)
    total_boxes = len(A)
    target_bricks_per_box = 10

    # Check if it's possible to have exactly 10 bricks in every box
    if total_bricks % total_boxes != 0 or total_bricks // total_boxes != target_bricks_per_box:
        return -1

    moves = 0
    for i in range(len(A)):
        if A[i] < target_bricks_per_box:
            moves += target_bricks_per_box - A[i]
            A[i+1] -= target_bricks_per_box - A[i]
        elif A[i] > target_bricks_per_box:
            moves += A[i] - target_bricks_per_box
            A[i+1] += A[i] - target_bricks_per_box
    
    print(moves)
    return moves
solution([7, 15, 10, 8])   

