N = int(input())
allValid = True
errorCodes = []
for i in range(N):
    record = input().split(' ')
    if record[1] == 'false':
        allValid = False
        errorCodes.append(record[2])

if allValid:
    print('Yes')
else:
    print('No')
    print(' '.join(errorCodes))
