#a
lst = [int(i) for i in input().split()]
for i in range(1, len(lst)):
    if lst[i] > lst[i-1]:
        print(lst[i])

#b
lst = list(set([int(i) for i in input().split()]))
print(lst)

