
def solve(target):
    for idx, spell in enumerate(target[:len(target)//2]):
        if spell != target[-1-idx]:
            return "false"
        else:
            continue
    return "true"

print(solve(input()))
