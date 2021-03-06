import json

class Config:
    def __init__(self, fname):
        with open(fname, 'rt') as fp:
            config_data = json.load(fp)
        self.weights = config_data['weights']['arithmetic']
    
    # TODO: Calculate this
    @property
    def sp_initial(self):
        return 0xFFFF