import urllib.request
import xml.etree.ElementTree as ElementTree


name = "lipsum"


class LipsumGen:
    def __init__(self, user_agent=None):
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' if user_agent is None else user_agent
        self.headers = {'User-Agent': self.user_agent}
        self.query = ""
        self.lipsum = ""
        self.generated = ""
        self.amount = 0
        self.start = False

    def _get_lipsum(self):
        request = urllib.request.Request("https://www.lipsum.com/feed/xml", self.query.encode('ascii'), headers=self.headers)

        with urllib.request.urlopen(request) as response:
            tree = ElementTree.fromstring(response.read().decode("utf-8"))
        return tree

    def get_lipsum(self):
        xml = self._get_lipsum()
        self.lipsum = xml[0].text
        self.generated = xml[1].text
        return self.lipsum

    def _words(self):
        self.query = "amount=" + str(self.amount) + "&what=words&start=" + str(self.start)
        self.get_lipsum()

    def _paras(self):
        self.query = "amount=" + str(self.amount) + "&what=paras&start=" + str(self.start)
        self.get_lipsum()

    def _bytes(self):
        self.query = "amount=" + str(self.amount) + "&what=bytes&start=" + str(self.start)
        self.get_lipsum()

    def _lists(self):
        self.query = "amount=" + str(self.amount) + "&what=lists&start=" + str(self.start)
        self.get_lipsum()

    def words(self, amount=None, start=None):
        if amount < 1:
            raise ValueError("amount lower than 0")
        elif amount < 3:
            print("amount lower than 2 may generate too much")
        self.amount = self.amount if amount is None else amount
        self.start = self.start if start is None else start
        self._words()
        return self.lipsum

    def paras(self, amount=None, start=None):
        if amount < 1:
            raise ValueError("amount lower than 0")
        self.amount = self.amount if amount is None else amount
        self.start = self.start if start is None else start
        self._paras()
        return self.lipsum

    def bytes(self, amount=None, start=None):
        if amount < 1:
            raise ValueError("amount lower than 0")
        elif amount < 28:
            print("amount lower than 27 may generate too much")
        self.amount = self.amount if amount is None else amount
        self.start = self.start if start is None else start
        self._bytes()
        return self.lipsum

    def lists(self, amount=None, start=None):
        if amount < 1:
            raise ValueError("amount lower than 0")
        self.amount = self.amount if amount is None else amount
        self.start = self.start if start is None else start
        self._lists()
        return self.lipsum


Lipsum = LipsumGen()


def words(amount, start=False):
    return Lipsum.words(amount, start)


def paras(amount, start=False):
    return Lipsum.paras(amount, start)


def byte(amount, start=False):  # named byte over bytes due to builtin func bytes
    return Lipsum.bytes(amount, start)


def lists(amount, start=False):
    return Lipsum.lists(amount, start)


def lipsum(mode, amount, start=False):
    mode = mode.lower()
    if type(mode) == str:
        modes = {"paras": paras, "words": words, "byte":byte, "lists": list}
        if mode == "bytes":
            return byte(amount, start)
        elif mode in modes:
            return modes[mode](amount, start)
        else:
            raise ValueError("mode invalid should be 'paras', 'words', 'bytes' or 'lists'")
    elif type(mode) == int:
        modes = (paras, words, byte, lists)
        if -1 < mode < 4:
            return modes[mode](amount, start)
        else:
            raise ValueError("mode should be between 0-3")
    else:
        raise TypeError("mode should be type str or int")
