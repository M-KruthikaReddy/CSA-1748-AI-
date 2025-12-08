from itertools import permutations
def solve_cryptarithmetic(puzzle):
    words = puzzle.replace("=", "+").split("+")
    words = [w.strip() for w in words]    
    w1, w2, res = words
    letters = set(w1 + w2 + res)
    if len(letters) > 10:
        return None 
    letters = list(letters)
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if mapping[w1[0]] == 0 or mapping[w2[0]] == 0 or mapping[res[0]] == 0:
            continue
        def word_to_num(word):
            num = 0
            for c in word:
                num = num * 10 + mapping[c]
            return num
        n1 = word_to_num(w1)
        n2 = word_to_num(w2)
        n3 = word_to_num(res)
        if n1 + n2 == n3:
            return mapping
    return None
puzzle = "SEND + MORE = MONEY"
solution = solve_cryptarithmetic(puzzle)
if solution:
    print("Solution:", solution)
    print("Numeric form:", puzzle.translate(str.maketrans({c: str(solution[c]) for c in solution})))
else:
    print("No solution found.")