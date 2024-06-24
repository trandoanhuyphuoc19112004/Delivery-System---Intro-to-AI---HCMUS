class Board:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.start_pos = self.find_start_pos()
        self.goal_pos = self.find_goal_pos()
    
    def find_start_pos(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == 'S':
                    return (i, j)
        return None

    def find_goal_pos(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == 'G':
                    return (i, j)
        return None
    
    def get_neighbors(self, pos):
        x, y = pos
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if self.is_valid_move(new_x, new_y):
                neighbors.append((new_x, new_y))
        return neighbors
    
    def is_valid_move(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.matrix[x][y] in [0, 'G']