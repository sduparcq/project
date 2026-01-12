
class Context:
    def __init__(self, ref_dict):
        self.ref_dict = ref_dict
        self.universe = list(ref_dict.keys())

    def set_universe(self, universe):
        self.universe = universe

    def get_ref(self):
        pass

    def _build_df(self):
        pass

