def mean(numbers):
    if not numbers:
        raise ValueError("mean() arg is an empty list")
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        raise ValueError("median() arg is an empty list")
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def mode(numbers):
    if not numbers:
        raise ValueError("mode() arg is an empty list")
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_count = max(freq.values())
    modes = [num for num, count in freq.items() if count == count]
    return min(modes)  

if __name__ == "__main__":
    sample = [1, 2, 2, 3, 4]
print("Numbers:", sample)
print("Mean:", mean(sample))
print("Median:", median(sample))
print("Mode:", mode(sample))
