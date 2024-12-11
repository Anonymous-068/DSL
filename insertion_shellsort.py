# Function to perform Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Function to perform Shell Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Main Program
def main():
    # Input: first-year percentages of students
    percentages = []
    n = int(input("Enter the number of students: "))

    print("Enter the percentages:")
    for _ in range(n):
        percentages.append(float(input()))

    print("\nOriginal array:", percentages)

    # Sorting using Insertion Sort
    insertion_sorted = percentages.copy()
    insertion_sort(insertion_sorted)
    print("\nArray sorted using Insertion Sort:", insertion_sorted)

    # Sorting using Shell Sort
    shell_sorted = percentages.copy()
    shell_sort(shell_sorted)
    print("\nArray sorted using Shell Sort:", shell_sorted)

# Run the program
if __name__ == "__main__":
    main()