class OdFilter(object):
    def __init__(self, **kwargs):
        self.filters = kwargs

    @property
    def representation(self):
        return ""

    def __repr__(self):
        return self.representation
