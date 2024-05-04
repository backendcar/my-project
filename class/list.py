class ListModifier:
    def __init__(self, l):
        self.l = l

    def integers(self):
        int_ = []
        for i in self.l:
            if isinstance(i, int):
                int_.append(i)
        return int_