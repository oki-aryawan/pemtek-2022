lis = [1,2,3,4]
set = {1,2,3,4}

print('[Sebelum]')
print(f' lis\t: {lis}')
print(f' set\t: {set}')

lis.remove(2)
lis.remove(4)

set.remove(2)
set.remove(4)

print('[Sesudah]')
print(f' lis\t: {lis}')
print(f' set\t: {set}')