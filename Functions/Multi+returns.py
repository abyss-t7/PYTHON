def min_max(numbers):
    return min(numbers), max(numbers)   # guys it will returns a tuple

lo, hi = min_max([3, 1, 4, 1, 5, 9])
print(lo, hi)   # 1 9

# You can also explicitly return a dict for clarity
def analyze(numbers):
    return {
        "min":  min(numbers),
        "max":  max(numbers),
        "mean": sum(numbers) / len(numbers),
        "count": len(numbers)
    }

stats = analyze([3, 1, 4, 1, 5, 9])
print(stats["mean"])   