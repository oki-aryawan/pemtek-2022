x = int(input('Input: '))


def faktorial(nilai):
    if nilai > 1:
        return x * faktorial(nilai - 1)
    return 1


print(f'Nilai {x}!: {faktorial(x)}')
