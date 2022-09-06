import pandas as pd
import matplotlib.pyplot as plt
from extraneous_functions import write_data_to_file

class Type_vs_profitability():
    def __init__(self):
        self.main_df = pd.read_csv("main_database_new.csv", low_memory=False)
        self.main_df["numVotes"] = self.main_df["numVotes"].fillna(0)

    def creating_type_vs_profitability_csv(self):
        """Process:
        Create a dataframe of the average number of votes of each genre in each type of entertainment
        - To do this:
            - iterate over every line in the DF
            - if the type of entertainment is not in the existing DF (list lookup)
                - add the type to the DF (and list)
                - add the number of votes to the current number of votes
                - add 1 to the occurrence
            - else
                - add number of votes to current number of votes
                - add 1 to occurrence
            
            - at the end of the DF
                - divide total votes by occurrence and save this into the average votes column of the df
            - save df to csv file
        """
        type_list = list()

        new_df = pd.DataFrame(columns=["titleType", "total_votes", "occurrence", "average_votes"])
        new_df_index_counter = 0

        for line_index in range(len(self.main_df)):
            print(line_index)
            if(self.main_df.at[line_index, "titleType"] not in type_list):
                type_list.append(self.main_df.at[line_index, "titleType"])
                new_df.at[new_df_index_counter, "titleType"] = self.main_df.at[line_index, "titleType"]
                new_df.at[new_df_index_counter, "total_votes"] = 0
                new_df.at[new_df_index_counter, "occurrence"] = 0
                new_df.at[new_df_index_counter, "average_votes"] = 0
                new_df_index_counter += 1
            # adding num votes and occurrence to the current index
            index = new_df.index[new_df["titleType"] == self.main_df.at[line_index,"titleType"]] # assumption is that there are not two indexs in the new df that match the type
            new_df.at[index[0], "total_votes"] = new_df.at[index[0], "total_votes"] + self.main_df.at[line_index, "numVotes"]
            new_df.at[index[0], "occurrence"] = new_df.at[index[0], "occurrence"] + 1
        
        # calculating the averages of each movie type
        for line_index in range(len(new_df)):
            new_df.at[line_index, "average_votes"] = new_df.at[line_index, "total_votes"] / new_df.at[line_index, "occurrence"]
        
        write_data_to_file(new_df, "type_vs_profitability.csv")

    def plotting_type_vs_profitability_total_votes(self):
        new_df = pd.read_csv("type_vs_profitability.csv")

        plt.bar(new_df["titleType"], new_df["total_votes"], color=["green"])
        plt.title("Medium vs Total Votes")
        plt.xlabel("Medium")
        plt.ylabel("Total Votes")
        plt.legend(["Total Votes"], loc=0, frameon=True)

        plt.show()

    def plotting_type_vs_profitability_occurrence(self):
        new_df = pd.read_csv("type_vs_profitability.csv")

        plt.bar(new_df["titleType"], new_df["occurrence"], color=["orange"])
        plt.title("Medium vs Occurrence")
        plt.xlabel("Medium")
        plt.ylabel("Occurrence")
        plt.legend(["Occurrence"], loc=0, frameon=True)

        plt.show()
    
    def plotting_type_vs_profitability_average_votes(self):
        new_df = pd.read_csv("type_vs_profitability.csv")

        plt.bar(new_df["titleType"], new_df["average_votes"], color=["blue"])
        plt.title("Medium vs Average Votes")
        plt.xlabel("Medium")
        plt.ylabel("Average Votes")
        plt.legend(["Average Votes"], loc=0, frameon=True)

        plt.show()
        

class Genre_vs_Type():
    def __init__(self):
        self.main_df = pd.read_csv("main_database_new.csv", low_memory=False)
        self.main_df["numVotes"] = self.main_df["numVotes"].fillna(0)
    
    """
    For this analysis of genre vs type we are going to look at the average number of votes for each genre in each movie type
    """
    def creating_new_db(self):
        new_df = pd.DataFrame(columns=["genre", "short", "movie", "tvMovie", "tvSeries", "tvEpisode", "tvShort", "tvMiniSeries", "tvSpecial", "video", "videoGame"])
        type_list = ["short", "movie", "tvMovie", "tvSeries", "tvEpisode", "tvShort", "tvMiniSeries", "tvSpecial", "video", "videoGame"]
        
        new_df = pd.DataFrame(columns=["Country", "City", "temp1", "temp2", "deltaT", "dt_1", "dt_2"])
        main_db["temperature"] = main_db["temperature"].filna(0)

        country_list = list()
        counter = 0 
        for country in country_list:
            index_list = main_db.index[main_db["country"] == country].to_list()

            for index in index_list:
                if(main_db.at[index, "temperature"] != 0):
                    new_df.at[counter, "temp1"] = main_db.at[index, "temperature"]
                    new_df.at[counter, "city"] = main_db.at[index, "city"]
                    new_df.at[counter, "dt_1"] = main_db.at[index, "dt"]

                    break;
            


            counter += 1
            

            
        genre_list = ["Film-Noir","Documentary", "Drama", "Comedy", "Romance", "Talk-Show"]

        genre_occurrence = [0,0,0,0,0,0]

        for i in range(6):
            new_df.at[i, "short"] = 0; new_df.at[i, "movie"] = 0; new_df.at[i, "tvMovie"] = 0; new_df.at[i,"tvSeries"] = 0; new_df.at[i, "tvEpisode"] = 0;
            new_df.at[i, "tvShort"] = 0; new_df.at[i, "tvMiniSeries"] = 0; new_df.at[i, "tvSpecial"] = 0; new_df.at[i, "video"] = 0; new_df.at[i, "videoGame"] = 0
        
        new_df.at[0, "genre"] = "Film-Noir"; new_df.at[1, "genre"] = "Documentary"; new_df.at[2, "genre"] = "Drama";
        new_df.at[3, "genre"] = "Comedy"; new_df.at[4, "genre"] = "Romance"; new_df.at[5, "genre"] = "Talk-Show"

        for genre_index in range(len(genre_list)):
            print(genre_index)
            genre = new_df.at[genre_index, "genre"]
            index_list = self.main_df.index[self.main_df["genres"] == genre].to_list()
            genre_occurrence[genre_index] = len(index_list)

            for index in index_list:
                if(self.main_df.at[index, "titleType"] in type_list):

                    new_df.at[genre_index, self.main_df.at[index, "titleType"]] = new_df.at[genre_index, self.main_df.at[index, "titleType"]] + self.main_df.at[index, "numVotes"]
        
        for i in range(6):
            if(new_df.at[i, "short"] > 0):
                new_df.at[i, "short"] = new_df.at[i, "short"] / genre_occurrence[i]; 
            if(new_df.at[i, "movie"] > 0):
                new_df.at[i, "movie"] = new_df.at[i, "movie"] / genre_occurrence[i]; 
            if(new_df.at[i, "tvMovie"] > 0):
                new_df.at[i, "tvMovie"] = new_df.at[i, "tvMovie"] / genre_occurrence[i]; 
            if(new_df.at[i, "tvSeries"] > 0):
                new_df.at[i,"tvSeries"] =  new_df.at[i, "tvSeries"] / genre_occurrence[i]; 
            if(new_df.at[i, "tvEpisode"] > 0):
                new_df.at[i, "tvEpisode"] =  new_df.at[i, "tvEpisode"] / genre_occurrence[i];
            if(new_df.at[i, "tvShort"] > 0):
                new_df.at[i, "tvShort"] =  new_df.at[i, "tvShort"] / genre_occurrence[i]; 
            if(new_df.at[i, "tvMiniSeries"] > 0):
                new_df.at[i, "tvMiniSeries"] =  new_df.at[i, "tvMiniSeries"] / genre_occurrence[i]; 
            if(new_df.at[i, "tvSpecial"] > 0):
                new_df.at[i, "tvSpecial"] =  new_df.at[i, "tvSpecial"] / genre_occurrence[i]; 
            if(new_df.at[i, "video"] > 0):
                new_df.at[i, "video"] =  new_df.at[i, "video"] / genre_occurrence[i]; 
            if(new_df.at[i, "videoGame"] > 0):
                new_df.at[i, "videoGame"] =  new_df.at[i, "videoGame"] / genre_occurrence[i]

        write_data_to_file(new_df, "genre_average_votes_vs_type.csv")
    
    def plotting_genre_vs_type_average_votes(self):
        new_df = pd.read_csv("genre_average_votes_vs_type.csv")

        plt.plot(new_df["genre"], new_df["short"])
        plt.plot(new_df["genre"], new_df["movie"])
        plt.plot(new_df["genre"], new_df["tvMovie"])
        plt.plot(new_df["genre"], new_df["tvSeries"])
        plt.plot(new_df["genre"], new_df["tvEpisode"])
        plt.plot(new_df["genre"], new_df["tvMiniSeries"])
        plt.plot(new_df["genre"], new_df["tvSpecial"])
        plt.plot(new_df["genre"], new_df["video"])
        plt.plot(new_df["genre"], new_df["videoGame"])

        plt.legend(["Short", "Movie", "tvMovie", "tvSeries", "tvEpisode", "tvMiniSeries", "tvSpecial", "video", "videoGame"], loc=0, frameon=True)

        plt.show()
    
    def plotting_genre_vs_type_average_votes_top_5_line(self):
        new_df = pd.read_csv("genre_average_votes_vs_type.csv")

        plt.plot(new_df["genre"], new_df["short"])
        plt.plot(new_df["genre"], new_df["movie"])
        plt.plot(new_df["genre"], new_df["tvMovie"])
        plt.plot(new_df["genre"], new_df["tvSeries"])
        plt.plot(new_df["genre"], new_df["tvEpisode"])

        plt.legend(["Short", "Movie", "tvMovie", "tvSeries", "tvEpisode", "tvMiniSeries", "tvSpecial", "video", "videoGame"], loc=0, frameon=True)
        plt.title("Average votes of Each Medium vs Genre")
        plt.ylabel("Average Votes")
        plt.xlabel("Genre")
        plt.show()
    
    def plotting_genre_vs_type_average_votes_top_5_bar(self):
        new_df = pd.read_csv("genre_average_votes_vs_type.csv")

        plt.bar(new_df["genre"], new_df["short"])
        plt.bar(new_df["genre"], new_df["movie"])
        plt.bar(new_df["genre"], new_df["tvMovie"])
        plt.bar(new_df["genre"], new_df["tvSeries"])
        plt.bar(new_df["genre"], new_df["tvEpisode"])

        plt.legend(["Short", "Movie", "tvMovie", "tvSeries", "tvEpisode", "tvMiniSeries", "tvSpecial", "video", "videoGame"], loc=0, frameon=True)
        plt.title("Average votes of Each Genre vs Medium")
        plt.ylabel("Average Votes")
        plt.xlabel("Genre")
        plt.show()
    
    def plotting_genre_vs_type_average_votes_top_5_stacked(self):
        new_df = pd.read_csv("genre_average_votes_vs_type.csv")

        plt.stackplot(new_df["genre"], new_df["short"], new_df["movie"], new_df["tvMovie"],new_df["tvSeries"], new_df["tvEpisode"])


        plt.legend(["Short", "Movie", "tvMovie", "tvSeries", "tvEpisode", "tvMiniSeries", "tvSpecial", "video", "videoGame"], loc=0, frameon=True)
        plt.title("Average votes of Each Genre vs Medium")
        plt.ylabel("Average Votes")
        plt.xlabel("Genre")
        plt.show()
    
    
    




# analysis = Type_vs_profitability()()
# analysis.plotting_type_vs_profitability_total_votes()
# analysis.plotting_type_vs_profitability_occurrence()
# analysis.plotting_type_vs_profitability_average_votes()
analysis = Genre_vs_Type()
analysis.plotting_genre_vs_type_average_votes_top_5_line()
            