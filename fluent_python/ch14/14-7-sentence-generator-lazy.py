import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        # no words

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):  # No need for a separate iterator class
        for match in RE_WORD.finditer(self.text):  # returns a generator
            yield match.group()


def run():
    s = Sentence('"The time has come," the Walrus said,')
    print(s)

    for word in s:
        print(word)

    print(list(s))

    # Type check
    from collections import abc
    print(issubclass(Sentence, abc.Iterable))  # True, because has __iter__

    print(isinstance(s, abc.Iterable))

    print(type(s))

    iter_s = iter(s)
    print(type(iter_s))  # class generator

    for word in iter_s:
        print(word)

    # already index reached at the end
    new_iter_s = iter(iter_s)
    for word in new_iter_s:
        print(word)


run()
