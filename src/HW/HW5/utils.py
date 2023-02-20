import copy as cp
import io
import json
import math
import random
import re
from typing import List, Union


def rint(lo: float=0, hi: float=1):
    return math.floor(0.5 + rand(lo, hi))


class Random:
    def __init__(self):
        self.seed = 937162211

    def set_seed(self, value: int):
        self.seed = value

    def rand(self, lo=0, hi=1):
        """
        Generates a pseudo-random number using seed.

        :param lo: Lower limit of generated number
        :param hi: Higher limit of generated number
        :return: Pseudo-random number
        """

        self.seed = (16807 * self.seed) % 2147483647
        return lo + (hi - lo) * self.seed / 2147483647


_inst = Random()
rand = _inst.rand
set_seed = _inst.set_seed


def rnd(n: float, n_places: int = 2) -> float:
    """
    Rounds number n to n places.

    :param n: Number
    :param n_places: Number of decimal places to round
    :return: Rounded number
    """
    mult = math.pow(10, n_places)
    return math.floor(n * mult + 0.5) / mult


def coerce(v):
    """
    Attempts to convert v to an int, float, bool, or keep as string

    :param v: String to convert
    :return: v converted to its type
    """
    types = [int, float]

    for t in types:
        try:
            return t(v)
        except ValueError:
            pass

    bool_vals = ["true", "false"]
    if v.lower() in bool_vals:
        return v.lower() == "true"

    return v


def csv(sFilename, fun):
    """
    call `fun` on rows (after coercing cell text)

    :param sFilename: String of the file to read
    :param fun: function to call per each row
    """
    f = io.open(sFilename)
    while True:
        s = f.readline().rstrip()
        if s:
            t = []
            for s1 in re.findall("([^,]+)", s):
                t.append(coerce(s1))
            fun(t)
        else:
            return f.close()


def cosine(a, b, c):
    """
    find x, y from a line connecting 'a' to 'b'
    """
    # might be an issue if c is 0
    if c == 0:
        return 0
    x1 = (a ** 2 + c ** 2 - b ** 2) / (2 * c)
    x2 = max(0, min(1, x1))
    #  -- in the incremental case, x1 might be outside 0,1
    y = (a ** 2 - x2 ** 2) ** .5

    if type(y) == complex:
        y = y.real
    return x2, y


def show(node, what: str = "mid", cols: List[Union['Sym', 'Num']] = None, nplaces: int = 2, lvl: int = 0) -> None:
    """
    Prints the tree.

    :param node: Node of tree
    :param what: Statistics to print
    :param cols: Columns to print stats for
    :param nplaces: Number of decimals to round the values to
    :param lvl: Level in the tree
    """
    if node:
        print(
            f"{'|.. ' * lvl}"
            f"{node['data'].rows[-1].cells[-1] if 'left' not in node else rnd(100 * node['c'])}"
        )

        show(node.get('left', None), what, cols, nplaces, lvl + 1)
        show(node.get('right', None), what, cols, nplaces, lvl + 1)


def many(t, n, seed=937162211):
    """
    returns some items from `t`
    """
    random.seed(seed)
    return random.choices(t, k=n)


def any(t, seed=937162211):
    """
    returns one items at random
    """
    random.seed(seed)
    return random.choices(t)[0]


def transpose(t):
    u = []
    for i in range(0, len(t[0])):
        u.append([])
        for j in range(0, len(t)):
            u[i].append(t[j][i])
    return u


def helper(k):
    return "Num" + str(k)


def copy(t):
    return cp.deepcopy(t)


def do_file(file):
    # if local X = y is present, find both the thing to replace and what to replace it with
    data = None
    with open(file, "r") as fp:
        data = fp.read()
    vars = re.match("local (.*) = (.*)\n", data)
    if vars:
        variable, value = vars.groups()
        data = data.replace(variable, value)
        data = re.sub("local .* = .*\n", "", data)
    # remove the return statement
    data = data.replace("return ", "")
    # remove newlines
    data = data.replace("\n", "")
    # replace domain= , cols= , rows=
    # change X=y to "X":y
    terms = ["domain", "cols", "rows"]
    for term in terms:
        data = re.sub("{}\s*=".format(term), '"{}":'.format(term), data)
    # replace { } with [ ]
    first, last = data.index("{"), data.rindex("}")
    data = data[first + 1:last].replace("{", "[").replace("}", "]")
    data = "{" + data + "}"

    # replace ' with "
    data = data.replace("'", '"')
    json_obj = json.loads(data)
    return json_obj


def oo(t):
    td = t.__dict__
    td['a'] = t.__class__.__name__
    td['id'] = id(t)
    print(dict(sorted(td.items())))


def last(t):
    return t[-1]

def adds(col, t):
    for _, x in enumerate(t or {}):
        col.add(x)
    return col