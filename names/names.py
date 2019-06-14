import time

start_time = time.time()

f = open('names_1.txt', 'r')  # List containing 10000 names
names_1 = {}
for name_1 in f.read().split("\n"):
    names_1[name_1] = True
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for name_2 in names_2:
    if names_1.get(name_2):
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
