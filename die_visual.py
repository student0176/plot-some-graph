from die import Die
import pygal

roll_nums = 50000
die_num = 2
die1 = Die(6)
die2 = Die(10)


frequency = [0] * die1.num_sides + [0] * die2.num_sides
for roll_num in range(roll_nums):
    res = die1.roll() + die2.roll()
    frequency[res - 1] += 1 # 這裏是我的原創，比書上簡潔
# print(result)
# print(frequency)

hist = pygal.Bar()
hist.title = 'Result of rolling D6 and D12 1000 times'
hist.x_labels = [str(i+1) for i in range(die1.num_sides + die2.num_sides)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Resilt'

hist.add('D6',frequency)
hist.render_to_file('./image_die/die_visual_6+10.svg')