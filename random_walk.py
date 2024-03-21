from random import choice


class Randomwalk():
    def __init__(self,num=50000):
        self.num_point = num

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        self.x_values = [0]
        self.y_values = [0]
        while len(self.x_values) < self.num_point:
            x_direction = choice([1,-1])
            y_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4,])
            y_distance = choice([0,1,2,3,4,])

            x_step = x_direction * x_distance
            y_step = y_direction * y_distance
            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)