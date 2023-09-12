import random
import numpy as np
import matplotlib.pyplot as plt

def generate_data():
    num_points=10
    _gen_data_x=np.array([random.randint(-100, 100) for _ in range(num_points)])
    _gen_data_y=np.array([random.randint(-100, 100) for _ in range(num_points)])
    return _gen_data_x, _gen_data_y


def gen_central_point():
    _gen_central_point_x=random.randint(-100, 100)
    _gen_central_point_y=random.randint(-100, 100)
    return _gen_central_point_x, _gen_central_point_y

def calculate_distance(_gen_data_x, _gen_data_y, _gen_central_point_x, gen_centrla_point_y):
    distances=np.sqrt((_gen_data_x- _gen_central_point_x)**2 + (_gen_data_y - gen_centrla_point_y)**2)
    return distances

_gen_data_x, _gen_data_y = generate_data()
_gen_central_point_x, _gen_central_point_y=gen_central_point()

distances=calculate_distance(_gen_data_x, _gen_data_y, _gen_central_point_x, _gen_central_point_y)

min_distance=np.argmin(distances)



plt.scatter(_gen_data_x, _gen_data_y)
plt.scatter(_gen_central_point_x, _gen_central_point_y, c="red", label="Central Point")



for i, (x, y, d) in enumerate(zip(_gen_data_x,_gen_data_y, distances)):
    linestyle = "--" if i != min_distance else "-"  
    color = "gray" if i != min_distance else "blue"  
    plt.plot([x, _gen_central_point_x], [y, _gen_central_point_y], linestyle=linestyle, color=color)




plt.title("Random generated data samples")
plt.legend()
plt.show()


