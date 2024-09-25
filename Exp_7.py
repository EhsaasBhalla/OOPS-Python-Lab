def dups(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

lst = [1, 2, 3, 4, 5, 3, 2, 6]
print("Duplicates:", dups(lst))
