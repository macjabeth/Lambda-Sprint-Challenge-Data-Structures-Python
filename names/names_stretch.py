import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_1.sort()
names_2.sort()

duplicates = []
i, j = 0, 0
while i < 10000 and j < 10000:
    if names_1[i] == names_2[j]:
        duplicates.append(names_1[i])
        i, j = i+1, j+1
    elif names_1[i] < names_2[j]:
        i += 1
    else:
        j += 1

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
