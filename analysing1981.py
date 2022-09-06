from analysis import Data_Analysis
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



analyser = Data_Analysis()
analyser.investigating_1891()
plt.xticks(np.arange(1, 136, 20))
plt.show()