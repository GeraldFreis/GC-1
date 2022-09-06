import pandas as pd
import matplotlib.pyplot as plt


class AnalysingReliability():
    def __init__(self):
        self.main_db = pd.read_csv("main_database_new.csv", low_memory=False)
        self.main_db["numVotes"] = self.main_db["numVotes"].fillna(0)

    def Top_10_based_on_Total_votes(self):
        new_df = self.main_db.sort_values(by=['numVotes'], inplace=False, ascending=False)
        new_data_frame = pd.DataFrame(columns=["Name", "totalVotes", "genres"])
        
        # for i in range(10): # copying top ten values across
        #     new_data_frame.at[i, "Name"] = new_df.at[i, "primaryTitle"]
        #     new_data_frame.at[i, "totalVotes"] = new_df.at[i, "numVotes"]
        #     new_data_frame.at[i, "genres"] = new_df.at[i, "genres"]


        
        # print(new_data_frame)
        new_df = new_df[new_df["titleType"] == "movie"]
        plt.barh(new_df["primaryTitle"].head(10).astype(str), new_df["numVotes"].head(10).astype(int))
        plt.title("Top 10 Movies according to total votes")
        plt.ylabel("Movie name")
        plt.xlabel("Total Votes")
        plt.show()

analysis = AnalysingReliability()
analysis.Top_10_based_on_Total_votes()

