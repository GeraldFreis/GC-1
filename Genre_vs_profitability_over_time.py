import pandas as pd
import matplotlib.pyplot as plt
from extraneous_functions import write_data_to_file

class Genre_vs_profit_over_time():
    def __init__(self):
        self.main_df = pd.read_csv("main_database_new.csv", low_memory=False)

    def genre_vs_profit_over_time_occurrence(self):
        # looking at average number of votes of a genre over each year
        year_list = list([year for year in range(1895, 2023)])
        self.total_df = pd.DataFrame(columns=["year", "documentary", "film-noir","short", "comedy", "drama", "romance", "talkshow"])
        genre_list = list(("Film-Noir", "Documentary", "Short", "Drama", "Comedy", "Romance", "Talk-show"))
        counter = 0
        for year in year_list:
            self.total_df.at[counter, "year"] = str(year)
            self.total_df.at[counter, "documentary"] = 0; self.total_df.at[counter, "short"] = 0; self.total_df.at[counter, "comedy"] = 0
            self.total_df.at[counter, "drama"] = 0; self.total_df.at[counter, "romance"] = 0; self.total_df.at[counter, "talkshow"] = 0
            self.total_df.at[counter, "film-noir"] = 0;

            try:
                index_list = self.main_df.index[self.main_df["startYear"] == str(year)].to_list()

                for index in index_list:
                    genres = self.main_df.at[index, "genres"].split(",")

                    for genre in genres:
                        if(genre == "Documentary"): 
                            self.total_df.at[counter, "documentary"] = self.total_df.at[counter, "documentary"] + 1
                        if(genre == "Short"): 
                            self.total_df.at[counter, "short"] = self.total_df.at[counter, "short"] + 1
                        if(genre == "Comedy"): 
                            self.total_df.at[counter, "comedy"] = self.total_df.at[counter, "comedy"] + 1
                        if(genre == "Romance"): 
                            self.total_df.at[counter, "romance"] = self.total_df.at[counter, "romance"] + 1
                        if(genre == "Drama"): 
                            self.total_df.at[counter, "drama"] = self.total_df.at[counter, "drama"] + 1
                        if(genre == "Talk-Show"): 
                            self.total_df.at[counter, "talkshow"] = self.total_df.at[counter, "talkshow"] + 1
                        if(genre == "Film-Noir"):
                            self.total_df.at[counter, "film-noir"] = self.total_df.at[counter, "film-noir"] + 1
                            print(self.total_df.at[counter, "film-noir"])
            except:
                continue;
            
            print(self.total_df.at[counter, "film-noir"])
            counter += 1
            
        write_data_to_file(self.total_df, "genre_vs_occurence_over_time.csv")
    
    def plotting_genres_over_time(self):
        self.main_new = pd.read_csv("genre_vs_occurence_over_time.csv", low_memory=False)

        plt.title("Year vs Genres popularity in terms of occurrence")
        plt.xlabel("Year")
        plt.ylabel("Occurence in the Database")

        plt.plot(self.main_new["year"], self.main_new["film-noir"], label="Film-Noir")
        plt.plot(self.main_new["year"], self.main_new["documentary"], label="Documentary")
        plt.plot(self.main_new["year"], self.main_new["drama"], label="Drama")
        plt.plot(self.main_new["year"], self.main_new["comedy"], label="Comedy")
        plt.plot(self.main_new["year"], self.main_new["romance"], label="Romance")
        plt.plot(self.main_new["year"], self.main_new["talkshow"], label="Talk-Shows")

        plt.legend(["Film-Noir","Documentary", "Drama", "Comedy", "Romance", "Talk-Shows"], loc=0, frameon=True)

        plt.show()
    
    def genre_vs_profit_over_time_total_votes(self):
        year_list = list([year for year in range(1895, 2023)])
        self.total_df = pd.DataFrame(columns=["year", "documentary", "film-noir","short", "comedy", "drama", "romance", "talkshow"])
        genre_list = list(("Film-Noir", "Documentary", "Short", "Drama", "Comedy", "Romance", "Talk-show"))

        self.main_df["numVotes"] = self.main_df["numVotes"].fillna(0)
        counter = 0

        for year in year_list:
            print(year)
            try:
                index_list = self.main_df.index[self.main_df["startYear"] == str(year)].to_list()
                self.total_df.at[counter, "year"] = str(year)
                self.total_df.at[counter, "documentary"] = 0; self.total_df.at[counter, "short"] = 0; self.total_df.at[counter, "comedy"] = 0
                self.total_df.at[counter, "drama"] = 0; self.total_df.at[counter, "romance"] = 0; self.total_df.at[counter, "talkshow"] = 0
                self.total_df.at[counter, "film-noir"] = 0;


                for index in index_list:
                    genres = self.main_df.at[index, "genres"].split(",")

                    for genre in genres:
                        if(genre == "Documentary"): 
                            self.total_df.at[counter, "documentary"] = self.total_df.at[counter, "documentary"] + self.main_df.at[index, "numVotes"]
                            print(self.total_df.at[counter, "documentary"])
                        if(genre == "Short"): 
                            self.total_df.at[counter, "short"] = self.total_df.at[counter, "short"] + self.main_df.at[index, "numVotes"]
                        if(genre == "Comedy"): 
                            self.total_df.at[counter, "comedy"] = self.total_df.at[counter, "comedy"] + self.main_df.at[index, "numVotes"]
                        if(genre == "Romance"): 
                            self.total_df.at[counter, "romance"] = self.total_df.at[counter, "romance"] + self.main_df.at[index, "numVotes"]
                        if(genre == "Drama"): 
                            self.total_df.at[counter, "drama"] = self.total_df.at[counter, "drama"] + self.main_df.at[index, "numVotes"]
                        if(genre == "Talk-Show"): 
                            self.total_df.at[counter, "talkshow"] = self.total_df.at[counter, "talkshow"] + self.main_df.at[index, "numVotes"]
                        if(genre == "Film-Noir"):
                            self.total_df.at[counter, "film-noir"] = self.total_df.at[counter, "film-noir"] + self.main_df.at[index, "numVotes"]
                
                counter += 1
            except:
                continue;

        
        write_data_to_file(self.total_df, "genre_vs_total_votes_over_time.csv")

    def plotting_genres_over_time_vs_total_votes(self):
        self.main_new = pd.read_csv("genre_vs_total_votes_over_time.csv", low_memory=False)

        plt.title("Year vs Genres popularity in terms of total votes")
        plt.xlabel("Year")
        plt.ylabel("Total Votes")

        plt.plot(self.main_new["year"], self.main_new["film-noir"], label="Film-Noir")
        plt.plot(self.main_new["year"], self.main_new["documentary"], label="Documentary")
        plt.plot(self.main_new["year"], self.main_new["drama"], label="Drama")
        plt.plot(self.main_new["year"], self.main_new["comedy"], label="Comedy")
        plt.plot(self.main_new["year"], self.main_new["romance"], label="Romance")
        plt.plot(self.main_new["year"], self.main_new["talkshow"], label="Talk-Shows")

        plt.legend(["Film-Noir","Documentary", "Drama", "Comedy", "Romance", "Talk-Shows"], loc=0, frameon=True)

        plt.show()
    


    def genre_vs_profit_over_time_average_votes(self):
        year_list = list([year for year in range(1895, 2023)])
        self.total_df = pd.DataFrame(columns=["year", "documentary", "film-noir","short", "comedy", "drama", "romance", "talkshow"])
        genre_list = list(("Film-Noir", "Documentary", "Short", "Drama", "Comedy", "Romance", "Talk-show"))

        self.main_df["numVotes"] = self.main_df["numVotes"].fillna(0)
        counter = 0

        for year in year_list:
            print(year)
            genre_occurence = [0,0,0,0,0,0,0]

            # try:
            index_list = self.main_df.index[self.main_df["startYear"] == str(year)].to_list()
            self.total_df.at[counter, "year"] = str(year)
            self.total_df.at[counter, "documentary"] = 0; self.total_df.at[counter, "short"] = 0; self.total_df.at[counter, "comedy"] = 0
            self.total_df.at[counter, "drama"] = 0; self.total_df.at[counter, "romance"] = 0; self.total_df.at[counter, "talkshow"] = 0
            self.total_df.at[counter, "film-noir"] = 0;


            for index in index_list:
                genres = self.main_df.at[index, "genres"].split(",")

                for genre in genres:

                    if(genre == "Documentary"):
                        genre_occurence[0] += 1
                        self.total_df.at[counter, "documentary"] = self.total_df.at[counter, "documentary"] + self.main_df.at[index, "numVotes"] 
                    if(genre == "Short"): 
                        genre_occurence[1] += 1
                        self.total_df.at[counter, "short"] = self.total_df.at[counter, "short"] + self.main_df.at[index, "numVotes"]
                    if(genre == "Comedy"): 
                        genre_occurence[2] += 1
                        self.total_df.at[counter, "comedy"] = self.total_df.at[counter, "comedy"] + self.main_df.at[index, "numVotes"]
                    if(genre == "Romance"): 
                        genre_occurence[3] += 1
                        self.total_df.at[counter, "romance"] = self.total_df.at[counter, "romance"] + self.main_df.at[index, "numVotes"]
                    if(genre == "Drama"): 
                        genre_occurence[4] += 1
                        self.total_df.at[counter, "drama"] = self.total_df.at[counter, "drama"] + self.main_df.at[index, "numVotes"]
                    if(genre == "Talk-Show"):
                        genre_occurence[5] += 1
                        self.total_df.at[counter, "talkshow"] = self.total_df.at[counter, "talkshow"] + self.main_df.at[index, "numVotes"]
                    if(genre == "Film-Noir"):
                        genre_occurence[6] += 1
                        self.total_df.at[counter, "film-noir"] = self.total_df.at[counter, "film-noir"] + self.main_df.at[index, "numVotes"]
                            
            # print(self.total_df.at[counter, "documentary"])
            if(genre_occurence[0] > 0):
                self.total_df.at[counter, "documentary"] = self.total_df.at[counter, "documentary"] / genre_occurence[0]
            if(genre_occurence[1] > 0):
                self.total_df.at[counter, "short"] = self.total_df.at[counter, "short"] / genre_occurence[1]
            if(genre_occurence[2] > 0):
                self.total_df.at[counter, "comedy"] = self.total_df.at[counter, "comedy"] / genre_occurence[2]
            if(genre_occurence[3] > 0):
                self.total_df.at[counter, "romance"] = self.total_df.at[counter, "romance"] / genre_occurence[3]
            if(genre_occurence[4] > 0):
                self.total_df.at[counter, "drama"] = self.total_df.at[counter, "drama"] / genre_occurence[4]
            if(genre_occurence[5] > 0):
                self.total_df.at[counter, "talkshow"] = self.total_df.at[counter, "talkshow"] / genre_occurence[5]
            if(genre_occurence[6] > 0):
                self.total_df.at[counter, "film-noir"] = self.total_df.at[counter, "film-noir"] / genre_occurence[6]
            
            counter += 1

            # except:
            #     continue;

        
        write_data_to_file(self.total_df, "genre_vs_average_votes_over_time.csv")
    
    def plotting_genres_over_time_vs_average_votes(self):
        self.main_new = pd.read_csv("genre_vs_average_votes_over_time.csv", low_memory=False)

        plt.title("Year vs Genres popularity in terms of average votes")
        plt.xlabel("Year")
        plt.ylabel("Average Votes")

        plt.plot(self.main_new["year"], self.main_new["film-noir"], label="Film-Noir")
        plt.plot(self.main_new["year"], self.main_new["documentary"], label="Documentary")
        plt.plot(self.main_new["year"], self.main_new["drama"], label="Drama")
        plt.plot(self.main_new["year"], self.main_new["comedy"], label="Comedy")
        plt.plot(self.main_new["year"], self.main_new["romance"], label="Romance")
        plt.plot(self.main_new["year"], self.main_new["talkshow"], label="Talk-Shows")

        plt.legend(["Film-Noir","Documentary", "Drama", "Comedy", "Romance", "Talk-Shows"], loc=0, frameon=True)

        plt.show()


analysis = Genre_vs_profit_over_time();
# analysis.genre_vs_profit_over_time_occurrence()
# analysis.plotting_genres_over_time()
# analysis.genre_vs_profit_over_time_total_votes()
# analysis.plotting_genres_over_time_vs_total_votes()
# analysis.genre_vs_profit_over_time_average_votes()
analysis.plotting_genres_over_time_vs_average_votes()