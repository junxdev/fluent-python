import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        """
        every time you call __iter__, returns new Iterator(support multiple traversals)
        :return: Iterator
        """
        return SentenceIterator(self.words)


class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


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
    print(type(iter_s))

    for word in iter_s:
        print(word)

    # already index reached at the end
    new_iter_s = iter(iter_s)
    for word in new_iter_s:
        print(word)

run()
