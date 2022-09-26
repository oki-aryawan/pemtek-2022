x = int(input('Input: '))

def faktorial(nilai):
    if nilai > 2:
        return x * faktorial(nilai - 1)
    return 2
print(f'Nilai {x}!: {faktorial(x)}')


