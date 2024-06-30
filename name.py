def group_names(names):
    # Create a list of 6 empty lists
    groups = []
    for _ in range(6):
        groups.append([])

    # Iterate over the names
    for i in range(len(names)):
        group_index = i // 6
        if group_index < 6:
            groups[group_index].append(names[i])
    return groups

# Askes the user for names
input_names = input("Enter You like to group and seperate it with commas: ").split(',')

# Removes space before and after from the names
input_names = [name.strip() for name in input_names]

# Group the names into 6 pairsg
grouped_names = group_names(input_names)

# Print the groups
for i in range(len(grouped_names)):
    print(f"Group {i+1}: {grouped_names[i]}")