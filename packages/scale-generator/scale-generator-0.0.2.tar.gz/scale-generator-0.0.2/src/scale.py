class Scale(object):
    def __init__(self, base=None, notes=None, intervals=None):
        self.__base: list = self.__try_set("base", base)
        self.__notes: list = self.__try_set("notes", notes)
        self.__intervals: list = self.__try_set("intervals", intervals)

        self.__sections: int = 0
        self.__section: float = 0.0
        self.__frequencies: list = [None] * 21
        self.generate()

    @property
    def base(self):
        return self.__base

    @property
    def notes(self):
        return self.__notes

    @property
    def intervals(self):
        return self.__intervals

    @property
    def sections(self):
        return self.__sections

    @property
    def section(self):
        return self.__section

    @property
    def frequencies(self):
        return self.__frequencies

    def __try_set(self, key, item):
        result = []
        if key == "base":
            assert isinstance(item, tuple) and len(item) == 2 and isinstance(item[0], str) and \
                   isinstance(item[1], float), "The base note should be a tuple(str, float)"

            result = [*item]

        elif key == "notes":
            assert isinstance(item, (list, set, tuple)) and len(item) == 7, \
                "The notes should be a list, set or tuple with 7 names of type<str>"
            assert len(set(item)) == len(item), "There can't be duplicate note names"
            assert self.__base[0] in item, "The note names list should have the base note in it"
            min_length = 2
            for value in item:
                assert isinstance(value, str), f"The note names should be of type<str>. Found: '{type(value)}: {value}'"
                min_length = min(min_length, len(value))

            funcs = [str.lower, str.title, str.upper] if min_length == 2 \
                else [lambda x: f"_{x}", lambda x: x, lambda x: f"{x}_"]
            for lst in [list(map(func_, item)) for func_ in funcs]:
                result.extend(lst)

        elif key == "intervals":
            assert isinstance(item, (list, set, tuple)) and len(item) == 7, \
                "The intervals should be a list, set or tuple with 7 items of type<int>"
            for value in item:
                assert isinstance(value, int), f"The interval should be of type<int>. Found: '{type(value)}: {value}'"
                assert value > 0, f"The interval should be at least one section long. Found: '{value}'"

            result = list(zip([*item[6:], *item[:6]], item)) * 3

        return result

    def __inject(self, obj, note, value):
        idx = self.__notes.index(note.strip("_").title())
        assert 6 < idx < 14, f"The note '{note}' was not found"

        if obj == "interval":
            assert value > 0, f"The interval should be at least one section long. Found: '{value}'"

            self.__intervals[idx - 7] = (self.__intervals[idx - 7][0], value)
            self.__intervals[idx - 6] = (value, self.__intervals[idx - 6][1])

            self.__intervals[idx] = (self.__intervals[idx][0], value)
            self.__intervals[idx + 1] = (value, self.__intervals[idx + 1][1])

            self.__intervals[idx + 7] = (self.__intervals[idx + 7][0], value)
            self.__intervals[(idx + 8) % 21] = (value, self.__intervals[(idx + 8) % 21][1])

        elif obj == "frequency":
            self.__frequencies[idx] = value

        self.generate()

    def inject_interval(self, note: str, value: int):
        self.__inject("interval", note, value)

    def inject_frequency(self, note: str, frequency: float):
        self.__inject("frequency", note, frequency)

    def generate(self):
        self.__sections = sum(note[0] for note in self.__intervals[:7])
        self.__section = 2.0 ** (1.0 / self.__sections)
        base_idx = self.__notes.index(self.__base[0])

        self.__frequencies = list(range(21))
        self.__frequencies[base_idx] = self.__base[1]
        for idx in range(base_idx - 1, -1, -1):
            self.__frequencies[idx] = round(
                self.__frequencies[idx + 1] / (self.__section ** self.__intervals[idx][1]),
                1
            )
        for idx in range(base_idx + 1, 21):
            self.__frequencies[idx] = round(
                self.__frequencies[idx - 1] * (self.__section ** self.__intervals[idx][0]),
                1
            )
        self.__frequencies[base_idx - 7] = self.__base[1] / 2
        self.__frequencies[base_idx + 7] = self.__base[1] * 2
