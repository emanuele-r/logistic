import pandas as pd 
import numpy as np
from voronoi import graph_voronoi, generate_data, graph_delaunay

pf=pd.read_csv("sample_data.csv")
# oo=pd.read_csv("real.csv", low_memory=False).dropna()





sample_point=np.array([pf[["Longitude", "Latitude"]]])




graph_voronoi(generate_data(sample_point[0]), pf["Sale Amount"])


graph_delaunay(generate_data(sample_point[0]), pf["Sale Amount"])


