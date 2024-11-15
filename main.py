def longest_box_sequence(boxes):
    # Sort the boxes based on all three dimensions in ascending order
    # Sorting by (l, b, h) ensures that each box fits within the next in sorted order
    boxes.sort(key=lambda box: (box[0], box[1], box[2]))
    print(boxes)
    # Initialize DP array where dp[i] will store the maximum sequence length ending with the i-th box
    n = len(boxes)
    dp = [1] * n

    # Apply DP to find the longest fitting sequence
    for i in range(1, n):
        for j in range(i):
            # Check if box[j] can fit into box[i]
            if boxes[j][0] < boxes[i][0] and boxes[j][1] < boxes[i][1] and boxes[j][2] < boxes[i][2]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(dp)
    # The longest sequence length will be the maximum value in dp
    max_length = max(dp)
    return max_length
