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


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="lipsum wrapper for https://www.lipsum.com",
                                     epilog="Script writen by Theo Toth, see https://gitlab.com/xedre/Python-Lipsum-API or "
                                            "https://pypi.org/project/lipsumAPI for details"
                                     )

    modes = parser.add_argument_group(title="mode")
    modes = modes.add_mutually_exclusive_group(required=True)
    modes.add_argument("-P", "--paragraphs", help="set mode to paragraphs", action="store_const", const=0, dest="mode")
    modes.add_argument("-W", "--words", help="set mode to words", action="store_const", const=1, dest="mode")
    modes.add_argument("-B", "--bytes", help="set mode to bytes", action="store_const", const=2, dest="mode")
    modes.add_argument("-L", "--lists", help="set mode to lists", action="store_const", const=3, dest="mode")

    parser.add_argument("-S", "--starting_text", help="start text with 'Lorem ipsum dolor sit amet'",
                        action="store_true", dest="start")

    parser.add_argument("amount", help="amount of text to generate", type=int)

    args = parser.parse_args()

    print(lipsum(args.mode, args.amount, args.start))
