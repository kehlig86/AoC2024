import csv

def parse_rules_from_csv(file_path):
    rules = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            x, y = row[0].split('|')
            rules.append((int(x), int(y)))
    return rules

def parse_updates_from_csv(file_path):
    updates = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            updates.append(list(map(int, row)))
    return updates

def is_correct_order(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def correct_order(update, rules):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    indegree = defaultdict(int)
    
    for x, y in rules:
        graph[x].append(y)
        indegree[y] += 1
        if x not in indegree:
            indegree[x] = 0
    
    queue = deque([node for node in update if indegree[node] == 0])
    ordered_update = []
    
    while queue:
        node = queue.popleft()
        ordered_update.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # Ensure all nodes are included in the ordered update
    remaining_nodes = set(update) - set(ordered_update)
    ordered_update.extend(remaining_nodes)
    
    return ordered_update

def find_middle_page_numbers_of_incorrect_updates(updates, rules):
    middle_page_numbers = []
    
    for update in updates:
        if not is_correct_order(update, rules):
            ordered_update = correct_order(update, rules)
            middle_page_numbers.append(ordered_update[len(ordered_update) // 2])
    
    return middle_page_numbers

# Parse rules and updates from CSV files
rules_file_path = 'config_rules.csv'
updates_file_path = 'config_updates.csv'

rules = parse_rules_from_csv(rules_file_path)
updates = parse_updates_from_csv(updates_file_path)

middle_page_numbers = find_middle_page_numbers_of_incorrect_updates(updates, rules)
result = sum(middle_page_numbers)

print(f"The sum of the middle page numbers after correctly ordering the incorrect updates is {result}.")
