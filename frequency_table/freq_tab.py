import math

# Program used to create frequency distribution table in statistics

# Input data
data = [30, 45, 43, 35, 34, 43, 44, 31, 46, 30]

# Sort
n = len(data)
for i in range(0, n-1):
    swapped = False
    for j in range(0, n-i-1):
        if data[j] > data[j+1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
            swapped = True
    if not swapped:
        break

# Range
min = data[0]
max = data[n-1]
r = max - min

# Class
c = 1 + math.log10(3.3) * n
c = int(c)

# Length
l = r / c
l = int(l) + 1

# Table
row = c + 1
j = 0
i = data[0]
while i <= max:
    #Limit
    end = i + l-1
    print(f"{i} - {end}")

    #Frequency
    inrange = True
    total = 0
    while inrange and j < n:
        if data[j] >= i and data[j] <= end:
            total += 1
            j += 1
        else:
            inrange = False

    # Relative Frequency
    rel = total / n * 100

    print(f"Frequency: {total}")
    print(f"Relative: {rel}%")

    i = end + 1

