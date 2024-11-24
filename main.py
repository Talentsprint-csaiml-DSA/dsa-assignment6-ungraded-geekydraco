def can_pack(box_a, box_b):
    return all(a < b for a, b in zip(box_a, box_b))

def box_packing(boxes):
    boxes.sort(key=lambda x: (x[0], x[1], x[2]))

    n = len(boxes)
    dp = [1] * n  

    for i in range(n):
        for j in range(i):
            if can_pack(boxes[j], boxes[i]):
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp) 
