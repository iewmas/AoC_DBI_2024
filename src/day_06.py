
import copy

class Map:

    OBSTACLE = '#'
    OBSTACLE_NEW = 'O'
    VISITED = 'X'

    GUARD_UP = '^'
    GUARD_RIGHT = '>'
    GUARD_DOWN = 'v'
    GUARD_LEFT = '<'
    GUARD_DIRS = [GUARD_UP, GUARD_RIGHT, GUARD_DOWN, GUARD_LEFT]

    LEFT_AREA = 0
    IN_AREA = 1
    LOOP_DETECTED = 2

    map = list() 
    guard_pos = {'x':-1, 'y':-1}
    guard_start_pos = {'x':-1, 'y':-1}


    def __init__(self, map):
        self.map = copy.deepcopy(map)
        self.guard_pos = self.find_guard_pos()
        self.guard_start_pos = self.guard_pos.copy() 


    def print_map(self):
        for m in self.map:
            print(''.join(m))


    def count_visited_area(self):
        result = 0

        for idx in range(len(self.map)):
            result = result + self.map[idx].count('X')

        return result


    def is_obstacle(self, x, y):
        if x >= len(self.map[0]) or y >= len(self.map) or x < 0 or y < 0: return False 

        return self.map[y][x] == self.OBSTACLE or self.map[y][x] == self.OBSTACLE_NEW 


    def turn_right(self, guard):
        if   guard == self.GUARD_UP: return self.GUARD_RIGHT
        elif guard == self.GUARD_RIGHT: return self.GUARD_DOWN
        elif guard == self.GUARD_DOWN: return self.GUARD_LEFT
        else: return self.GUARD_UP


    def is_leaving_area(self, x, y, guard):
        if   guard == self.GUARD_UP and y == 0: return True
        elif guard == self.GUARD_RIGHT and x == len(self.map[0])-1: return True
        elif guard == self.GUARD_DOWN and y == len(self.map)-1: return True
        elif guard == self.GUARD_LEFT and x == 0: return True

        return False


    def find_guard_pos(self, verbose = False):
        for x in range(len(self.map)):
            for y in range(len(self.map[0])):
                if self.map[y][x] in self.GUARD_DIRS:
                    if verbose: print('FOUND GUARD', x, y, self.map[y][x])
                    return {'x':x, 'y':y}
        return None


    def get_guard(self):
        x = self.guard_pos['x']
        y = self.guard_pos['y']
        guard = self.map[y][x]

        return guard
    

    def set_guard(self, x, y, g):
        self.guard_pos = {'x':x, 'y':y}
        self.map[y][x] = g 
    

    def do_one_move(self, verbose = False):
        if verbose: self.print_map() 
        
        # self.guard_pos = self.find_guard_pos(verbose)
        # if self.guard_pos == None: return self.LEFT_AREA

        x = self.guard_pos['x']
        y = self.guard_pos['y']
        guard = self.get_guard()

        FLAG_OBSTACLE = False

        if guard == self.GUARD_UP:
            if self.is_obstacle(x, y-1):
                if verbose: print('OBSTACLE - Turn right', x, y-1, guard)
                FLAG_OBSTACLE = True

        elif guard == self.GUARD_RIGHT:
            if self.is_obstacle(x+1, y):
                if verbose: print('OBSTACLE - Turn right', x+1, y, guard)
                FLAG_OBSTACLE = True
        
        elif guard == self.GUARD_DOWN:
            if self.is_obstacle(x, y+1):
                if verbose: print('OBSTACLE - Turn right', x, y+1, guard)
                FLAG_OBSTACLE = True
                
        elif guard == self.GUARD_LEFT:
            if self.is_obstacle(x-1, y):
                if verbose: print('OBSTACLE - Turn right', x-1, y, guard)
                FLAG_OBSTACLE = True

        if FLAG_OBSTACLE:
            self.map[y][x] = self.turn_right(guard)
            return self.IN_AREA
        
        self.map[y][x] = self.VISITED

        if self.is_leaving_area(x, y, guard): 
            return self.LEFT_AREA
        else: 
            if   guard == self.GUARD_UP:    self.set_guard(x, y-1, guard)  # self.map[y-1][x] = guard
            elif guard == self.GUARD_RIGHT: self.set_guard(x+1, y, guard)  # self.map[y][x+1] = guard
            elif guard == self.GUARD_DOWN:  self.set_guard(x, y+1, guard)  # self.map[y+1][x] = guard
            elif guard == self.GUARD_LEFT:  self.set_guard(x-1, y, guard)  # self.map[y][x-1] = guard

            #$self.guard_pos = self.find_guard_pos(verbose)

            return self.IN_AREA