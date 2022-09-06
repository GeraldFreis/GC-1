import pandas as pd
import matplotlib.pyplot as plt
from extraneous_functions import write_data_to_file


class G_vs_profitability():
    def __init__(self):
        self.df = pd.read_csv("Database_files/Compiled_csv.csv", low_memory=False)
        self.df['numVotes'] = self.df['numVotes'].fillna(0)
        self.df['genres'] = self.df['genres'].fillna("Noval")
        self.df_of_average_votes_vs_genre = pd.read_csv("Database_files/investigation_of_genre_vs_popularity.csv", low_memory=False)
    
    def plotting_genre_vs_popularity(self):
        # plot, frame = plt.subplots(2,2)
        plt.title("Occurrence vs Genre")
        plt.xlabel("Genres"); plt.ylabel("Occurrence in Database")
        # plt.bar(self.df_of_average_votes_vs_genre['genres'], self.df_of_average_votes_vs_genre["numVotes"])
        # plt.bar(self.df_of_average_votes_vs_genre['genres'], self.df_of_average_votes_vs_genre["averageVotes"])
        plt.bar(self.df_of_average_votes_vs_genre['genres'], self.df_of_average_votes_vs_genre["occurrence"])
        # self.df_of_average_votes_vs_genre['numVotes'] = self.df_of_average_votes_vs_genre['numVotes'] / 100
        # self.df_of_average_votes_vs_genre['averageVotes'] = self.df_of_average_votes_vs_genre['averageVotes'] *  1000
        # plt.plot(self.df_of_average_votes_vs_genre['genres'], self.df_of_average_votes_vs_genre['numVotes'], color='r')
        # plt.plot(self.df_of_average_votes_vs_genre['genres'], self.df_of_average_votes_vs_genre['averageVotes'], color='g')
        # plt.plot(self.df_of_average_votes_vs_genre['genres'], self.df_of_average_votes_vs_genre['occurrence'])
        
        plt.xticks(rotation=90)
    
    def film_noir_movies(self):
        self.film_noir_df = pd.DataFrame(columns=["Name", "year", "numVotes"])
        running_counter = 0

        for index in range(len(self.df)):
            for genre in self.df.at[index, "genres"].split(","):

                if(genre == "Film-Noir"):
                    self.film_noir_df.at[running_counter, "Name"] = self.df.at[index, "primaryTitle"]
                    self.film_noir_df.at[running_counter, "year"] = self.df.at[index, "startYear"]
                    self.film_noir_df.at[running_counter, "numVotes"] = self.df.at[index, "numVotes"]
                    running_counter += 1
        
        self.film_noir_df.sort_values(by="numVotes", inplace=True, ascending=False)
        print(self.film_noir_df.head(20))

rawgraphs = G_vs_profitability()
# rawgraphs.plotting_genre_vs_popularity()
rawgraphs.film_noir_movies()
plt.show()
