import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


def sentence():
    s = Sentence('"The time has come," the Walrus said,')
    print(s)

    for word in s:
        print(word)

    print(list(s))


def type_iterator():
    s = Sentence('"The time has come," the Walrus said,')

    from collections import abc
    print(issubclass(Sentence, abc.Iterable))  # False, because no __iter__, even though it's iterable in practice

    print(isinstance(s, abc.Iterable))

    class Foo:
        def __iter__(self):
            pass

    print(issubclass(Foo, abc.Iterable))  # True, because has __iter__

    print(isinstance(Foo(), abc.Iterable))


def iter_and_next():
    s3 = Sentence('Pig and Pepper')
    it = iter(s3)
    print(it)
    print(next(it))
    print(next(it))
    print(next(it))
    try:
        print(next(it))
    except StopIteration as e:
        print(list(it))  # no way to reset iterator
        print(list(iter(s3)))  # only way to reset


