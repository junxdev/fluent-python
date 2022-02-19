def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')
    return 'C'  # legal(not error), but do nothing


res1 = [x * 3 for x in gen_AB()]  # list comprehension
print(type(res1))
for i in res1:
    print('-->', i)

res2 = (x * 3 for x in gen_AB())  # generator expression
print(type(res2))
for i in res2:
    print('-->', i)
