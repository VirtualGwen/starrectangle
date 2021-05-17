num_rows = int(input())
num_cols = int(input())

for i in range(num_rows):
    print('*', end=' ')
    for j in range(num_cols-1):
        print('*', end=' ')
    print()
