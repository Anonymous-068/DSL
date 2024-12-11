# Function to perform Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Main Program
def main():
    # Input: first-year percentages of students
    percentages = []
    n = int(input("Enter the number of students: "))

    print("Enter the percentages:")
    for _ in range(n):
        percentages.append(float(input()))

    print("\nOriginal array:", percentages)

    # Sorting using Quick Sort
    quick_sorted = quick_sort(percentages)
    print("\nArray sorted using Quick Sort:", quick_sorted)

    # Display top five scores
    top_five = quick_sorted[-5:][::-1]
    print("\nTop five scores:", top_five)

# Run the program
if __name__ == "__main__":
    main()