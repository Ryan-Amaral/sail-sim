from sail.boat import Boat
import matplotlib.pyplot as plt


waypoints = [(5,5), (20,20), (50,10), (70,60), (100,100)]

boat = Boat(waypoints=waypoints)

xs = [boat.x]
ys = [boat.y]

while not boat.finished:
    boat.update_position_dummy()
    xs.append(boat.x)
    ys.append(boat.y)

plt.plot(xs, ys)
plt.show()