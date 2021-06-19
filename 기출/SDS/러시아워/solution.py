class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Car:
    # direction, front = Coord(), rear = Coord()
    def __init__(self, id, direction, front, rear = Coord(0, 0)):
        self.id = id
        self.direction = direction
        self.front = front
        self.rear = self.set_rear()

    def move(self, front, rear):
        self.front = front
        self.rear = rear

    def get_front(self):
        return self.front.x, self.front.y

    def get_rear(self):
        return self.rear.x, self.rear.y
    
    def set_rear(self):
        x, y = 0, 0
        if self.direction == 'N':
            x, y = self.front.x + 1, self.front.y
        if self.direction == 'S':
            x, y = self.front.x - 1, self.front.y
        if self.direction == 'W':
            x, y = self.front.x, self.front.y + 1
        if self.direction == 'E':
            x, y = self.front.x, self.front.y - 1
        return Coord(x, y)


class Map:
    def __init__(self, map):
        self.map = map
        self.rows = len(self.map)
        self.cols = len(self.map[0])

    def addCar(self, car):
        front_x, front_y = car.front.x, car.front.y
        rear_x, rear_y = car.rear.x, car.rear.y
        self.map[front_x][front_y] = car
        self.map[rear_x][rear_y] = car

    def moveCar(self, car):
        pass

    def getCar(self, x, y):
        return self.map[x][y]

    def printMap(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.map[i][j] != 0:
                    #print("{}, {}".format(i, j))
                    print(self.map[i][j].id)
                    
    
def main():
    n = int(input())
    for _ in range(n):
        carCount = int(input())
        #set map
        map = Map([[0 for _ in range(5)] for _ in range(5)])
        for i in range(carCount):
            x, y, dir = list(input().split(' '))
            car = Car(i, dir, Coord(int(x)-1, int(y)-1))
            map.addCar(car)
            # solve
            stack, path = [], [(2,0), (2,1), (2,2), (2,3), (2,4)]
            while path:
                x, y = path[-1]
                # check if path is blocked
                if map.map[x][y] != 0:
                    # calculate where to move the car
                    car = map.getCar(x, y)
                    dir, front_x, front_y , rear_x, rear_y = car.direction, car.get_front(), car.get_rear()
                    moved = False
                    if dir == 'N' or dir == 'S':
                        col = front_y
                        for i in range(5):
                            # rear 에서는 -dif 하면 됨
                            dif = front_x - i
                            # valid condition
                            if map.map[i][col] == 0 and map.map[rear_x - dif][col] == 0 and i != x and rear_x - dif != x:
                                car.move(Coord(i, col), Coord(rear_x - dif, col))
                                # previous position set to 0
                                map.map[front_x][front_y] = 0
                                map.map[rear_x][rear_y] = 0
                                # new position set
                                map.map[i][col] = car
                                map.map[rear_x - i][col] = car
                                moved = True
                    if dir == 'W' or dir == 'E':
                        row = front_x
                        for i in range(5):
                            # rear 에서는 -dif 하면 됨
                            dif = front_y - i
                            # valid condition
                            if map.map[row][i] == 0 and map.map[row][rear_y - dif] == 0 and i != y and rear_y - dif != y:
                                car.move(Coord(row, i), Coord(i, rear_y - dif))
                                # previous position set to 0
                                map.map[front_x][front_y] = 0
                                map.map[rear_x][rear_y] = 0
                                # new position set
                                map.map[row][i] = car
                                map.map[row][rear_y - dif] = car
                                moved = True
                






            




        

main()
