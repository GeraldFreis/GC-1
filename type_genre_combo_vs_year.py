import pandas as pd
import matplotlib.pyplot as plt
from extraneous_functions import write_data_to_file

class GT_vs_year():
    def __init__(self):
        self.main_df = pd.read_csv("main_database_new.csv", low_memory=False)
        self.main_df["numVotes"] = self.main_df["numVotes"].fillna(0)
    
    def creating_db_total(self):
        # looking at the top 3 most profitable combos
        # Drama movies, Comedy tvEpisodes, Documentary movies
        combo_vs_year_df = pd.DataFrame(columns=["year", "Drama-Movies", "Comedy-tvEpisodes", "Documentary-Movies"]) # rows represent year, and average votes of each combo
        counter = 0

        for year in range(1895, 2022):
            print(year)
            index_list = self.main_df.index[self.main_df["startYear"] == str(year)].to_list()
            occurrence_list = [0,0,0] # indexes: 0 = DM, 1 = CTE, 2 = DM

            # initialising all row values
            combo_vs_year_df.at[counter, "year"] = year; combo_vs_year_df.at[counter, "Drama-Movies"] = 0; combo_vs_year_df.at[counter, "Comedy-tvEpisodes"] = 0
            combo_vs_year_df.at[counter, "Documentary-Movies"] = 0

            for index in index_list:
                genres = self.main_df.at[index, "genres"].split(",")

                for genre in genres:
                    if(genre == "Drama" and self.main_df.at[index, "titleType"] == "movie"):
                        occurrence_list[0] += 1
                        combo_vs_year_df.at[counter, "Drama-Movies"] = combo_vs_year_df.at[counter, "Drama-Movies"] + self.main_df.at[index, "numVotes"]
                    
                    elif(genre == "Comedy" and self.main_df.at[index, "titleType"] == "tvEpisode"):
                        print("Here")
                        occurrence_list[1] += 1
                        combo_vs_year_df.at[counter, "Comedy-tvEpisodes"] = combo_vs_year_df.at[counter, "Comedy-tvEpisodes"] + self.main_df.at[index, "numVotes"]
                    
                    elif(genre == "Documentary" and self.main_df.at[index, "titleType"] == "movie"):
                        occurrence_list[2] += 1
                        combo_vs_year_df.at[counter, "Documentary-Movies"] = combo_vs_year_df.at[counter, "Documentary-Movies"] + self.main_df.at[index, "numVotes"]
            
            if(occurrence_list[0] != 0):
                combo_vs_year_df.at[counter, "Drama-Movies"] = combo_vs_year_df.at[counter, "Drama-Movies"] / occurrence_list[0]
            if(occurrence_list[1] != 0):
                combo_vs_year_df.at[counter, "Comedy-tvEpisodes"] = combo_vs_year_df.at[counter, "Comedy-tvEpisodes"] / occurrence_list[1]
            if(occurrence_list[2] != 0):
                combo_vs_year_df.at[counter, "Documentary-Movies"] = combo_vs_year_df.at[counter, "Documentary-Movies"] / occurrence_list[2]
           
            counter += 1
        
        write_data_to_file(combo_vs_year_df, "most_profitable_combo.csv")

    def plotting_combos_total(self):
        df = pd.read_csv("most_profitable_combo.csv", low_memory=False)

        plt.plot(df["year"], df["Drama-Movies"], label="Drama Movies")
        plt.plot(df["year"], df["Comedy-tvEpisodes"], label="Comedy tvEpisodes")
        plt.plot(df["year"], df["Documentary-Movies"], label="Documentary Movies")
        plt.title("Most profitable combination of Genre and Medium vs Time")

        plt.xlabel("Year")
        plt.ylabel("Average Votes")

        plt.legend()
        plt.show()
    
    def creating_db_recent(self):
        # looking at the top 3 most profitable combos
        # Drama movies, Comedy tvEpisodes, Documentary movies
        combo_vs_year_df = pd.DataFrame(columns=["year", "Drama-Movies", "Comedy-tvEpisodes", "Documentary-Movies"]) # rows represent year, and average votes of each combo
        counter = 0

        for year in range(2000, 2022):
            print(year)
            index_list = self.main_df.index[self.main_df["startYear"] == str(year)].to_list()
            occurrence_list = [0,0,0] # indexes: 0 = DM, 1 = CTE, 2 = DM

            # initialising all row values
            combo_vs_year_df.at[counter, "year"] = year; combo_vs_year_df.at[counter, "Drama-Movies"] = 0; combo_vs_year_df.at[counter, "Comedy-tvEpisodes"] = 0
            combo_vs_year_df.at[counter, "Documentary-Movies"] = 0

            for index in index_list:
                genres = self.main_df.at[index, "genres"].split(",")

                for genre in genres:
                    if(genre == "Drama" and self.main_df.at[index, "titleType"] == "movie"):
                        occurrence_list[0] += 1
                        combo_vs_year_df.at[counter, "Drama-Movies"] = combo_vs_year_df.at[counter, "Drama-Movies"] + self.main_df.at[index, "numVotes"]
                    
                    elif(genre == "Comedy" and self.main_df.at[index, "titleType"] == "tvEpisode"):
                        print("Here")
                        occurrence_list[1] += 1
                        combo_vs_year_df.at[counter, "Comedy-tvEpisodes"] = combo_vs_year_df.at[counter, "Comedy-tvEpisodes"] + self.main_df.at[index, "numVotes"]
                    
                    elif(genre == "Documentary" and self.main_df.at[index, "titleType"] == "movie"):
                        occurrence_list[2] += 1
                        combo_vs_year_df.at[counter, "Documentary-Movies"] = combo_vs_year_df.at[counter, "Documentary-Movies"] + self.main_df.at[index, "numVotes"]
            
            if(occurrence_list[0] != 0):
                combo_vs_year_df.at[counter, "Drama-Movies"] = combo_vs_year_df.at[counter, "Drama-Movies"] / occurrence_list[0]
            if(occurrence_list[1] != 0):
                combo_vs_year_df.at[counter, "Comedy-tvEpisodes"] = combo_vs_year_df.at[counter, "Comedy-tvEpisodes"] / occurrence_list[1]
            if(occurrence_list[2] != 0):
                combo_vs_year_df.at[counter, "Documentary-Movies"] = combo_vs_year_df.at[counter, "Documentary-Movies"] / occurrence_list[2]
           
            counter += 1
        
        write_data_to_file(combo_vs_year_df, "most_profitable_combo_recent.csv")
    
    def plotting_combos_recent(self):
        df = pd.read_csv("most_profitable_combo_recent.csv", low_memory=False)

        plt.plot(df["year"], df["Drama-Movies"], label="Drama Movies")
        plt.plot(df["year"], df["Comedy-tvEpisodes"], label="Comedy tvEpisodes")
        plt.plot(df["year"], df["Documentary-Movies"], label="Documentary Movies")
        plt.title("Most profitable combination of Genre and Medium vs Past 2 Decades")

        plt.xlabel("Year")
        plt.ylabel("Average Votes")

        plt.legend()
        plt.show()
    
    def creating_db_recent_10(self):
        # looking at the top 3 most profitable combos
        # Drama movies, Comedy tvEpisodes, Documentary movies
        combo_vs_year_df = pd.DataFrame(columns=["year", "Drama-Movies", "Comedy-tvEpisodes", "Documentary-Movies"]) # rows represent year, and average votes of each combo
        counter = 0

        for year in range(2010, 2022):
            print(year)
            index_list = self.main_df.index[self.main_df["startYear"] == str(year)].to_list()
            occurrence_list = [0,0,0] # indexes: 0 = DM, 1 = CTE, 2 = DM

            # initialising all row values
            combo_vs_year_df.at[counter, "year"] = year; combo_vs_year_df.at[counter, "Drama-Movies"] = 0; combo_vs_year_df.at[counter, "Comedy-tvEpisodes"] = 0
            combo_vs_year_df.at[counter, "Documentary-Movies"] = 0

            for index in index_list:
                genres = self.main_df.at[index, "genres"].split(",")

                for genre in genres:
                    if(genre == "Drama" and self.main_df.at[index, "titleType"] == "movie"):
                        occurrence_list[0] += 1
                        combo_vs_year_df.at[counter, "Drama-Movies"] = combo_vs_year_df.at[counter, "Drama-Movies"] + self.main_df.at[index, "numVotes"]
                    
                    elif(genre == "Comedy" and self.main_df.at[index, "titleType"] == "tvEpisode"):
                        print("Here")
                        occurrence_list[1] += 1
                        combo_vs_year_df.at[counter, "Comedy-tvEpisodes"] = combo_vs_year_df.at[counter, "Comedy-tvEpisodes"] + self.main_df.at[index, "numVotes"]
                    
                    elif(genre == "Documentary" and self.main_df.at[index, "titleType"] == "movie"):
                        occurrence_list[2] += 1
                        combo_vs_year_df.at[counter, "Documentary-Movies"] = combo_vs_year_df.at[counter, "Documentary-Movies"] + self.main_df.at[index, "numVotes"]
            
            if(occurrence_list[0] != 0):
                combo_vs_year_df.at[counter, "Drama-Movies"] = combo_vs_year_df.at[counter, "Drama-Movies"] / occurrence_list[0]
            if(occurrence_list[1] != 0):
                combo_vs_year_df.at[counter, "Comedy-tvEpisodes"] = combo_vs_year_df.at[counter, "Comedy-tvEpisodes"] / occurrence_list[1]
            if(occurrence_list[2] != 0):
                combo_vs_year_df.at[counter, "Documentary-Movies"] = combo_vs_year_df.at[counter, "Documentary-Movies"] / occurrence_list[2]
           
            counter += 1
        
        write_data_to_file(combo_vs_year_df, "most_profitable_combo_recent_10.csv")
    
    def plotting_combos_recent_10(self):
        df = pd.read_csv("most_profitable_combo_recent_10.csv", low_memory=False)

        plt.plot(df["year"], df["Drama-Movies"], label="Drama Movies")
        plt.plot(df["year"], df["Comedy-tvEpisodes"], label="Comedy tvEpisodes")
        plt.plot(df["year"], df["Documentary-Movies"], label="Documentary Movies")
        plt.title("Most profitable combination of Genre and Medium vs Past Decade")

        plt.xlabel("Year")
        plt.ylabel("Average Votes")

        plt.legend()
        plt.show()

analysis = GT_vs_year()
# analysis.creating_db()
# analysis.creating_db_recent_10()
analysis.plotting_combos_recent_10()