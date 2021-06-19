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

    def move(self, direction, dist):
        pass

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
        car = self.map[x][y]
        return car.

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







            




        

main()
