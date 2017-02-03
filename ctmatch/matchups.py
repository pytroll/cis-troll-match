class Obs(object):
    def __init__(self):
        pass

class SatObs(Obs):
    def __init__(self):
        self.output_filenames = None
        self.filename_pattern = None

    def find_matches(self, timestamp):
        filenames_list = generate_match_list()
        self.output_filenames = filenames_list
