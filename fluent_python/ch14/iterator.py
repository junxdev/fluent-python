def run():
    s = 'ABC'
    for char in s:
        print(char)

    it = iter(s)
    while True:
        try:
            print(next(it))
        except StopIteration:
            # del it
            break

    _it = iter(it)  # no items
    while True:
        try:
            print(next(_it))
        except StopIteration:
            del it
            break
