import numpy as np
import re


class ABCIDATA():
    ALLOCATE_SIZE = 10000

    def __init__(self):
        self.__cache_flush = True
        self.__data = {}
        self.__reverse = False
        self.__desc = {"title": "",
                       "xlab": "",
                       "ylab": "",
                       "else": []}
        self.__last_desc = "title"
        self.__store_to_new = False
        self.__last_data_name = ""
        self.__last_data_index = 0
        self.__legends = {}
        self.__pattern = re.compile(r"(X+|V+|F)")

    def __cache_allocate(self, n=ALLOCATE_SIZE):
        self.__cache = np.zeros((n, 2))
        self.__cache_pos = 0

    def __cache_crop(self):
        self.__cache.resize((self.__cache_pos, 2))

    def store_to_new(self, val):
        self.__store_to_new = val

    def insert(self, x, y):
        if self.__cache_flush:
            self.__cache_allocate()
            self.__cache_flush = False
        if len(self.__cache) == self.__cache_pos:
            self.__cache.resize((self.__cache_pos * 10, 2))
        self.__cache[self.__cache_pos] = [x, y]
        self.__cache_pos += 1

    def cache_dump(self):
        self.__cache_crop()
        return self.__cache

    def cache_store(self, name, new):
        self.__cache_crop()
        self.__last_data_name = name
        if name in self.__data:
            if self.__store_to_new or new:
                self.__data[name].append(self.__cache)
                self.store_to_new(False)
                self.__last_data_index = len(self.__data[name]) - 1
            else:
                self.__data[name][0] = np.concatenate((self.__data[name][0],
                                                       self.__cache))
                self.__last_data_index = 0
        else:
            self.__data[name] = [self.__cache]
            self.__last_data_index = 0
        self.__cache_flush = True

    def last_is_legend(self, text):
        self.__legends[self.__last_data_name] = text
        self.__data[self.__last_data_name].pop(self.__last_data_index)

    def legends_dump(self):
        return self.__legends

    def data_dump(self):
        return self.__data

    def title_add(self, text):
        self.__desc["title"] = text
        self.__last_desc = "title"

    def title_dump(self):
        return self.__desc["title"].strip()

    def xlab_add(self, text):
        self.__desc["xlab"] = text
        self.__last_desc = "xlab"

    def xlab_dump(self):
        return self.__desc["xlab"].strip()

    def ylab_add(self, text):
        self.__desc["ylab"] = text
        self.__last_desc = "ylab"

    def ylab_dump(self):
        return self.__desc["ylab"].strip()

    def apply_case(self, overlay):
        if self.__last_desc == "else":
            strings = self.__desc[self.__last_desc]
            string = strings[len(strings) - 1]
        else:
            string = self.__desc[self.__last_desc]
        match = [m for m in re.finditer(self.__pattern, overlay)]
        match.reverse()
        for m in match:
            if "X" in m.group(0):
                string = string[:m.start()] + \
                         "$^{" + string[m.start():m.end()] + \
                         "}$" + string[m.end():]
            if "V" in m.group(0):
                string = string[:m.start()] + \
                         "$_{" + string[m.start():m.end()] + \
                         "}$" + string[m.end():]
            if "F" in m.group(0):
                if string[m.start()] == "W":
                    string = string[:m.start()] + \
                        r"$\Omega$" + string[m.end():]
        if self.__last_desc == "else":
            self.__desc[self.__last_desc][len(strings) - 1] = string
        else:
            self.__desc[self.__last_desc] = string

    def append_last(self, text):
        if self.__last_desc == "else":
            self.__desc["else"][len(self.__desc["else"])-1] = \
                self.__desc["else"][len(self.__desc["else"])-1] + text
        else:
            self.__desc[self.__last_desc] = \
                self.__desc[self.__last_desc] + text

    def description_add(self, text):
        self.__desc["else"].append(text)
        self.__last_desc = "else"

    def description_dump(self):
        return self.__desc["else"]

    def reverse(self, val=None):
        if val is not None:
            self.__reverse = val
        return self.__reverse


def top_parse(f):
    buf = []
    cur = None
    # dig = re.compile(r"(\d+\.\d+|\d+\.?|\.?\d+|NaN)")
    try:
        with open(f) as text:
            newpart = True
            for line in text:
                linel = line.strip().split()
                if cur is not None and len(linel) == 2:
                    try:
                        cur.insert(float(linel[0]), float(linel[1]))
                        continue
                    except ValueError:
                        pass  # fallthrough
                if cur is not None and linel[0] == "SET":
                    if len(linel) > 3 and linel[1] == "ORDER":
                        if linel[2] == "X":
                            cur.reverse(True)
                    continue
                if cur is not None and linel[0] == "TITLE":
                    cur.store_to_new(True)
                    li = line.strip().split("'")
                    li = [i for i in li if len(i) > 0]
                    msg = ""
                    if len(li) > 1:
                        msg = msg.join(li[1:])
                    if len(linel) > 3 and newpart:
                        cur.title_add(msg)
                    elif "BOTTOM" in linel:
                        cur.xlab_add(msg)
                    elif "LEFT" in linel:
                        cur.ylab_add(msg)
                    elif "DATA" in linel and "SIZE" in linel:
                        cur.last_is_legend(msg)
                    else:
                        cur.description_add(msg)
                    newpart = False
                    continue
                if cur is not None and linel[0] == "MORE":
                    li = line.strip().split("'")
                    li = [i for i in li if len(i) > 0]
                    msg = ""
                    if len(li) > 1:
                        msg = msg.join(li[1:]).strip()
                    cur.append_last(msg)
                    continue
                if cur is not None and linel[0] == "CASE":
                    li = line.strip().split("'")
                    li = [i for i in li if len(i) > 0]
                    msg = ""
                    if len(li) > 1:
                        msg = msg.join(li[1:])
                    cur.apply_case(msg)
                    continue
                if cur is not None and linel[0] == "JOIN":
                    new = True
                    if len(linel) > 1 and linel[1].isdigit():
                        new = True
                    if "DOTS" in linel:
                        cur.cache_store("dotted", new)
                    elif "DASH" in linel:
                        cur.cache_store("dashed", new)
                    elif "DOTDASH" in linel:
                        cur.cache_store("dashdot", new)
                    else:
                        cur.cache_store("solid", new)
                    continue
                if linel[0] == "NEW":
                    if cur is not None:
                        buf.append(cur)
                    cur = ABCIDATA()
                    newpart = True
                    continue
                if linel[0] == "PLOT":
                    continue
            if cur is not None:
                buf.append(cur)
    except PermissionError:
        pass

    return(buf)
