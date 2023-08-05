class Map(object):
    def __init__(self):
        self.rows = 9
        self.cols = 9
        self.min_rows = 3
        self.min_cols = 3
        self.numList = []
    
    def check_legal(self):
        if len(self.numList) <> 9:
            raise Exception('')
        for nums in self.numList:
            if len(nums) <> 9:
                raise Exception('')
        return True