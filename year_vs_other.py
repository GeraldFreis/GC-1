from analysis import Data_Analysis
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

analyser = Data_Analysis()
analyser.greatest_rating_vs_release_year()
analyser.num_of_votes_vs_year()
analyser.plot_data()
plt.xticks(np.arange(1, 136, 20))
plt.savefig("year_vs_average_rating_and_numvotes.png")

plt.show()