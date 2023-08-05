from colorama import Fore, Back

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

class Cell(object):
    def __init__(self, value):
        self.value = value
        self.i = 0
        self.j = 0
        self.visible = True
        self.cover = 0

    def set_coords(self, i, j):
        self.i = i
        self.j = j
    
    def set_visible(self, visible):
        self.visible = visible
    
    def get_value(self):
        if not self.need_fill():
            return str(self.value)
        else:
            if self.has_fill():
                return Fore.RED + str(self.cover) + Fore.RESET
            else:
                return Fore.RED + '*' + Fore.RESET

    def need_fill(self):
        return self.visible == False
    
    def has_fill(self):
        return self.need_fill() and self.cover <> 0

    def get_value_2(self):
        if not self.need_fill():
            return self.value
        
        # if self.has_fill():
        #     return self.cover
        return 0

    def get_value_3(self):
        if not self.need_fill():
            return self.value
        else:
            return self.cover

class Board(object):
    
    def __init__(self, cells, need):
        self.cells = cells
        self.need = need

        for i, e in enumerate(self.cells):
            self.cells[i].set_coords(i / 9 + 1, i % 9 + 1)

    def set_cell(self, i, j, cover):
        self.cells[(i - 1) * 9 + j - 1].cover = cover

    def get_cell(self, i, j):
        return self.cells[(i - 1) * 9 + j - 1]

    def over(self):
        # 需要填写信息已完毕
        has_full = len([cell.cover for cell in self.cells if cell.cover <> 0]) == self.need

        # print 'has_full', has_full

        def _true_over(instance):
            print '_true_over'
            end = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
            # 逐行
            rows = list(chunks(instance.cells, 9))

            for i, row in enumerate(rows):
                row = set(sorted([cell.get_value_3() for cell in row]))
                if end <> row:
                    return False
            
            # 逐列
            for i in range(9):
                col = set([cell.get_value_3() for cell in instance.cells if cell.j == i + 1])
                if end <> col:
                    return False
            
            return True

        return has_full and _true_over(self)

    def check(self, i, j, cover):
        """
            检查输入当前行、列及3*3单元的合法性
        """
        # 当前行
        row_cells = [cell.get_value_2() for cell in self.cells[(i - 1) * 9: i * 9] if cell.get_value_2() <> 0]

        if cover in row_cells:
            return False
        
        # 当前列
        col_cells = [self.cells[j - 1 + k * 9].get_value_2() for k in range(9) if self.cells[j - 1 + k * 9].get_value_2() <> 0]
        # print col_cells

        if cover in col_cells:
            return False

        # 当前3*3单元
        section_cells = [0 for k in range(9)]
        
        k = 0
        for s in range(3):
            for t in range(3):
                ind = ((i - 1) / 3 ) * 27 + s * 9 + ((j - 1) / 3) * 3 + t
                section_cells[k] = self.cells[ind]
                k = k + 1

        section_cells = [cell.get_value_2() for cell in section_cells if cell.get_value_2() <> 0]
        # print section_cells

        if cover in section_cells:
            return False

        return True
        

    def debug_print(self):
        for i in range(9):
            for j in range(9):
                e = self.cells[i * 9 + j]
                print e.get_value(), e.i, e.j, 'visible' if e.visible else 'invisible'
            print '\n'