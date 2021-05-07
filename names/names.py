import time

start_time = time.time()

with open('names_1.txt', 'r') as f:
    names_1 = {name_1: True for name_1 in f.read().split("\n")}

with open('names_2.txt', 'r') as f:
    names_2 = f.read().split("\n")  # List containing 10000 names

duplicates = [name_2 for name_2 in names_2 if names_1.get(name_2)]

end_time = time.time()

print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
