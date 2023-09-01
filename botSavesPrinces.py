def displayPathtoPrincess(N, grid):
    # Find the positions of the bot and princess
    bot_position = (0, 0)
    princess_position = (0, 0)

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'm':
                bot_position = (i, j)
            elif grid[i][j] == 'p':
                princess_position = (i, j)

    # Calculate row and column differences
    row_diff = princess_position[0] - bot_position[0]
    col_diff = princess_position[1] - bot_position[1]

    # Output moves to reach the princess
    while row_diff != 0:
        if row_diff < 0:
            print("UP")
            row_diff += 1
        else:
            print("DOWN")
            row_diff -= 1

    while col_diff != 0:
        if col_diff < 0:
            print("LEFT")
            col_diff += 1
        else:
            print("RIGHT")
            col_diff -= 1

# Read input
N = int(input())
grid = [list(input()) for _ in range(N)]

# Call the function to rescue the princess
displayPathtoPrincess(N, grid)
