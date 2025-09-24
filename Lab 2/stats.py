# Filename: stats.py
# Faythe Magsombol
# Description: Module to compute mean, median, and mode of a list of numbers.

from collections import Counter

def mean(numbers):
    """Return the average of the numbers in the list. Return 0 if list is empty."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Return the median of the numbers in the list. Return 0 if list is empty."""
    if not numbers:
        return 0
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        # Even number of elements
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        # Odd number of elements
        return sorted_nums[mid]

def mode(numbers):
    """Return the mode of the numbers in the list. Return 0 if list is empty.
       If multiple modes exist, return the smallest one."""
    if not numbers:
        return 0
    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    return min(modes)  # Return smallest mode if tie

def main():
    """Testing"""
    sample_data = [4, 1, 2, 2, 5, 3, 3, 3, 4, 2]
    
    print("Sample Data:", sample_data)
    print("Mean:", mean(sample_data))
    print("Median:", median(sample_data))
    print("Mode:", mode(sample_data))

if __name__ == "__main__":
    main()