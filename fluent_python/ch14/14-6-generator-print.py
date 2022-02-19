def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')
    return 'C'  # legal(not error), but do nothing


for c in gen_AB():  # the for loop will catch StopIteration
    print('-->', c)
