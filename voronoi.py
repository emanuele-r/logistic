import numpy as np 
import random
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay, delaunay_plot_2d
import matplotlib.pyplot as plt 


# points=np.array([[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]])
# vor=Voronoi(points)
# tri=Delaunay(points)
# fig=voronoi_plot_2d(vor)
# _=delaunay_plot_2d(tri)
# plt.title("Voronoi Regions")
# plt.show()





# def generate_data(num_points):
#     num_points=num_points
#     gen_x = np.random.randint(num_points, size=(num_points, 2))
#     return gen_x

def generate_data(gen_x):
    return gen_x



def graph_voronoi(generate_data, text ):
    try :
        vor=Voronoi(generate_data)
        _=voronoi_plot_2d(vor)
        plt.title(f"Voronoi Regions, num of points :{len(generate_data)}")
        for i , (x, y ) in enumerate(generate_data):
                # plt.annotate(f'{generate_data[i]}', xy=(x, y), xytext=(x, y))
                plt.annotate(f'$ {text[i]}', xy=(x,y), xytext=(x,y))
        plt.show()
    except Exception as e :
        print(f'An Error Occured')

    return _ 



def graph_delaunay(generate_data, text):
    try:
        tri=Delaunay(generate_data)
        __=delaunay_plot_2d(tri)
        for i , (x, y ) in enumerate(generate_data):
                # plt.annotate(f'{generate_data[i]}', xy=(x, y), xytext=(x, y))
                plt.annotate(f'$ {text[i]}', xy=(x,y), xytext=(x,y))
        plt.title("Delaunay")
        plt.show()
    except Exception as e :
        print(f'An Error Occured')
    
    return __


def graph_simple(generate_data, text):
    for i, (x,y) in enumerate(generate_data):
        plt.scatter(x, y)
        plt.title(f'Simple Scatter Graph')
        plt.annotate(f' $ {text[i]}', xy=(x,y), xytext=(x,y))
        plt.legend(f'{text[i]}')
    plt.show()

