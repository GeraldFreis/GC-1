import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from extraneous_functions import write_data_to_file

"""
Class to handle the analysis and data creation of the source
"""
class Data_Analysis():
    def __init__(self):
        self.df = pd.read_csv("Database_files/Compiled_csv.csv", sep=",", low_memory=False)
        self.df_of_average_rating = pd.read_csv("Database_files/year_vs_average_rating.csv", sep=",", low_memory=False)
        self.df_of_average_votes = pd.read_csv("Database_files/year_vs_num_votes.csv", sep=',', low_memory=False)

    def greatest_rating_vs_total_votes(self):
        self.df.sort_values(by=['averageRating'], ascending=False).plot.line(x="averageRating", y="numVotes")
    
    def greatest_rating_vs_release_year(self):
        self.df.sort_values(by=['startYear'], ascending=True)
        # problem: some of the data from early on does not actually have any votes

        #have to clean the data set so that we only have data with average ratings 
        # also have to create a dataframe of average ratings for each year
        self.df["averageRating"] = self.df["averageRating"].fillna(0)

        self.hit_list = list()
        null_indexs = list()
        for line in range(len(self.df)):
            # if(self.df.at[line, "averageRating"] == 0):
            #     null_indexs.append(line)

            if(self.df.at[line, "startYear"] not in self.hit_list):
                self.hit_list.append(self.df.at[line, "startYear"])

        self.df_of_average_rating = pd.DataFrame(columns=["startYear","averageRating"])
        counter = 0

        self.df["startYear"] = self.df["startYear"].replace(["1891"], "1981")
        self.df["startYear"] = self.df["startYear"].replace(["1890"], "1980")
        self.df["startYear"] = self.df["startYear"].replace(["1892"], "1982")

        # iterating over the list of years and finding their equivalent in the main df then averageing the average ratings
        for year in self.hit_list:
            index_list = list()
            this_average = 0.0
            amount = 0
            index_list = self.df.index[self.df["startYear"] == year].to_list()

            for index in index_list:

                if(self.df.at[index, "averageRating"] >= 1):    
                    this_average += self.df.at[index, "averageRating"]; 
                    amount += 1
            
            
            if(this_average != 0):
                this_average = this_average / amount
                self.df_of_average_rating.at[counter, "startYear"] = year
                self.df_of_average_rating.at[counter, "averageRating"] = this_average
                    
            counter += 1

        # self.df.plot.line(y="averageRating", x="startYear")
        print(self.df_of_average_rating)

        # df_of_average_rating.dropna(subset=["startYear"])
        self.df_of_average_rating.sort_values(by="startYear", ascending=True, inplace=True)
        # self.df_of_average_rating.plot.line(x="startYear", y="averageRating")
        write_data_to_file(self.df_of_average_rating, "year_vs_average_rating.csv")

    def num_of_votes_vs_year(self):
        self.df["numVotes"] = self.df["numVotes"].fillna(0) # filling all the NaN's in numVotes column
        self.df_of_average_votes = pd.DataFrame(columns=["startYear","numVotes"])
        self.df["startYear"] = self.df["startYear"].replace(["1891"], "1981")
        self.df["startYear"] = self.df["startYear"].replace(["1890"], "1980")
        self.df["startYear"] = self.df["startYear"].replace(["1892"], "1982")

        counter = 0

        for year in self.hit_list:
            index_list = list()
            this_average = 0
            amount = 0
            index_list = self.df.index[self.df["startYear"] == year].to_list()

            for index in index_list:
                if(self.df.at[index, "numVotes"] >= 1):
                    this_average += self.df.at[index, "numVotes"]
                    amount += 1
            
            if(this_average != 0):
                this_average = this_average / (amount)
                self.df_of_average_votes.at[counter, "startYear"] = year
                self.df_of_average_votes.at[counter, "numVotes"] = this_average
            
            counter += 1

        self.df_of_average_votes.sort_values(by="startYear", ascending=True, inplace=True)
        # self.df_of_average_votes.plot.line(x="startYear", y="numVotes")
        write_data_to_file(self.df_of_average_votes, "Database_files/year_vs_num_votes.csv")
    
    # this function will investigate why 1891 has an average number of votes of 7041
    def investigating_1891(self):
        self.df_of_1981 = self.df[self.df["startYear"] == "1981"]
        self.df_of_1981 = self.df_of_1981[self.df_of_1981["numVotes"] > 1000]
        # self.df_of_1981["numVotes"] = self.df_of_1981["numVotes"].fillna(0)
        self.df_of_1981.plot.bar(x="primaryTitle", y="numVotes")

        self.df_of_1981.sort_values(by="numVotes", ascending=False, inplace=True)
        print(self.df_of_1981.head(10))
    
    def plot_data(self):

        self.df_of_average_rating.sort_values(by="startYear", ascending=True, inplace=True); self.df_of_average_votes.sort_values(by="startYear", ascending=True, inplace=True)
        
        plot, frame = plt.subplots(2,1)

        frame[0].set_xticks(np.arange(1, 136, 20))

        frame[0].plot(self.df_of_average_rating["startYear"], self.df_of_average_rating["averageRating"])
        frame[0].set_title("Year released vs Average Rating")
        # frame[0].set_xticks([list(val for val in range(int(self.df_of_average_rating.at[2, "startYear"]), int(self.df_of_average_rating.at[len(self.df_of_average_rating)-1, "startYear"]), 10))])
        
        self.df_of_average_votes.sort_values(by="startYear", ascending=True, inplace=True); self.df_of_average_votes.sort_values(by="startYear", ascending=True, inplace=True)

        frame[1].plot(self.df_of_average_votes["startYear"], self.df_of_average_votes["numVotes"])
        frame[1].set_title("Year released vs Average number of votes")

        print(self.df_of_average_votes[self.df["startYear"]=="1891"])
    # to explain, 1981 in the provided DB had a significant amount of votes and a concurrent high rating, even though it is very unlikely (I believe it unlikely)
    def checking_1981(self):
        print(self.df_of_average_votes[self.df_of_average_votes["startYear"] == "1891"])


    def get_start_year(self):
        for line in range(len(self.df)):
            if(self.df.at[line, "averageRating"] == "NaN"):
                self.df.drop([line])

        print(self.df.sort_values(by=['startYear'], ascending=False).head(10))

    def fixing_all_early_data(self):
        # we need to take the compiled csv, and reorganize most 1890's -1900 films into 1980's etc. 
        update = self.df[self.df["startYear"] == "1891"]
        self.df.loc[update, "startYear"] = "1981"
    

    def get_df(self):
        return self.df
