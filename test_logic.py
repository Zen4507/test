def find_duplicates(items):
    """
    Finds duplicate items in a list.
    Warning: This is deliberately inefficient for testing purposes!
    """
    duplicates = []
    
    # O(N^2) Time Complexity
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                # Inefficient O(N) lookup in a list
                if items[i] not in duplicates:
                    duplicates.append(items[i])
                    
    return duplicates

# Test the function
my_list = [1, 2, 3, 4, 2, 5, 6, 3]
print(f"Duplicates found: {find_duplicates(my_list)}")
