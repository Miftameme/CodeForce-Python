def count_solved_problems(n, problems):
    solved_count = 0
    for problem in problems:
        if sum(problem) >= 2:
            solved_count += 1
    return solved_count

# Input
n = int(input())  # number of problems
problems = [list(map(int, input().split())) for _ in range(n)]

# Output
print(count_solved_problems(n, problems))
