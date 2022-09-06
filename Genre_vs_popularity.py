import pandas as pd
import matplotlib.pyplot as plt
from extraneous_functions import write_data_to_file


class G_vs_profitability():
    def __init__(self):
        self.df = pd.read_csv("Database_files/Compiled_csv.csv", low_memory=False)
        self.df['numVotes'] = self.df['numVotes'].fillna(0)
        self.df['genres'] = self.df['genres'].fillna("Noval")
        self.df_of_average_votes_vs_genre = pd.read_csv("investigation_of_genre_vs_popularity.csv", low_memory=False)
    
    def initial_investigation(self):

        # iterating over the existing database and checking if short or documentary is in that list
        counter = 0
        for linenum in range(len(self.df)):
            # if("documentary" or "short" in self.df.at[linenum, "genres"]):
            print(self.df.at[linenum, "genres"].split(","))
            if("Short" in self.df.at[linenum, "genres"].split(",")):
                print(linenum)

            counter += 1

            if(counter > 10):
                return
    
    def creating_cleaned_df(self):
        self.df["numVotes"] = self.df["numVotes"].fillna(0)
        # self.df["numVotes"] = self.df["numVotes"].fillna(0)

        self.df_of_average_votes_vs_genre = pd.DataFrame(columns=["genres", "numVotes", 'occurrence', "averageVotes"])
        index_counter  = 0

        self.df_of_average_votes_vs_genre.at[0, "genres"] = "Documentary"; self.df_of_average_votes_vs_genre.at[2, "genres"] = "Comedy"
        self.df_of_average_votes_vs_genre.at[1, "genres"] = "Short"; self.df_of_average_votes_vs_genre.at[3, "genres"] = "Horror"
        self.df_of_average_votes_vs_genre.at[4, "genres"] = "Drama"; self.df_of_average_votes_vs_genre.at[5, "genres"] = "Action";
        self.df_of_average_votes_vs_genre.at[6, "genres"] = "Fantasy"; self.df_of_average_votes_vs_genre.at[7, "genres"] = "Animation";
        self.df_of_average_votes_vs_genre.at[8, "genres"] = "Western"; self.df_of_average_votes_vs_genre.at[9, "genres"] = "Family";
        self.df_of_average_votes_vs_genre.at[10, "genres"] = "Adventure"; self.df_of_average_votes_vs_genre.at[11, "genres"] = "Musical";
        self.df_of_average_votes_vs_genre.at[12, "genres"] = "Crime"; self.df_of_average_votes_vs_genre.at[13, "genres"] = "Mystery";
        self.df_of_average_votes_vs_genre.at[14, "genres"] = "Music"; self.df_of_average_votes_vs_genre.at[15, "genres"] = "History";
        self.df_of_average_votes_vs_genre.at[16, "genres"] = "War"; self.df_of_average_votes_vs_genre.at[17, "genres"] = "Thriller";
        self.df_of_average_votes_vs_genre.at[18, "genres"] = "Sci-Fi"; self.df_of_average_votes_vs_genre.at[19, "genres"] = "Biography";
        self.df_of_average_votes_vs_genre.at[20, "genres"] = "Romance"; self.df_of_average_votes_vs_genre.at[21, "genres"] = "Sport";
        self.df_of_average_votes_vs_genre.at[22, "genres"] = "Film-Noir"; self.df_of_average_votes_vs_genre.at[23, "genres"] = "News";
        self.df_of_average_votes_vs_genre.at[24, "genres"] = "Reality-TV"; self.df_of_average_votes_vs_genre.at[25, "genres"] = "Adult";
        self.df_of_average_votes_vs_genre.at[26, "genres"] = "Talk-Show"; self.df_of_average_votes_vs_genre.at[27, "genres"] = "Game-Show";

        self.df_of_average_votes_vs_genre.at[0, "numVotes"] = 0;self.df_of_average_votes_vs_genre.at[1, "numVotes"] = 0;
        self.df_of_average_votes_vs_genre.at[2, "numVotes"] = 0; self.df_of_average_votes_vs_genre.at[3, "numVotes"] = 0;
        self.df_of_average_votes_vs_genre.at[4, "numVotes"] = 0; self.df_of_average_votes_vs_genre.at[5, "numVotes"] = 0;
        self.df_of_average_votes_vs_genre.at[6, "numVotes"] = 0; self.df_of_average_votes_vs_genre.at[7, "numVotes"] = 0;
        self.df_of_average_votes_vs_genre.at[8, "numVotes"] = 0; self.df_of_average_votes_vs_genre.at[9, "numVotes"] = 0;
        self.df_of_average_votes_vs_genre.at[10, "numVotes"] = 0; self.df_of_average_votes_vs_genre.at[11, "numVotes"] = 0;
        self.df_of_average_votes_vs_genre.at[12, "numVotes"] = 0; self.df_of_average_votes_vs_genre.at[13, "numVotes"] = 0;
        self.df_of_average_votes_vs_genre.at[14, "numVotes"] = 0; 
        self.df_of_average_votes_vs_genre.at[15, "numVotes"] = 0;self.df_of_average_votes_vs_genre.at[16, "numVotes"] = 0;
        self.df_of_average_votes_vs_genre.at[17, "numVotes"] = 0; self.df_of_average_votes_vs_genre.at[18, "numVotes"] = 0;
        self.df_of_average_votes_vs_genre.at[19, "numVotes"] = 0; self.df_of_average_votes_vs_genre.at[20, "numVotes"] = 0;
        self.df_of_average_votes_vs_genre.at[21, "numVotes"] = 0; self.df_of_average_votes_vs_genre.at[22, "numVotes"] = 0;
        self.df_of_average_votes_vs_genre.at[23, "numVotes"] = 0; self.df_of_average_votes_vs_genre.at[24, "numVotes"] = 0;
        self.df_of_average_votes_vs_genre.at[25, "numVotes"] = 0; self.df_of_average_votes_vs_genre.at[26, "numVotes"] = 0;
        self.df_of_average_votes_vs_genre.at[27, "numVotes"] = 0;



        self.df_of_average_votes_vs_genre.at[0, "occurrence"] = 0;self.df_of_average_votes_vs_genre.at[1, "occurrence"] = 0;
        self.df_of_average_votes_vs_genre.at[2, "occurrence"] = 0; self.df_of_average_votes_vs_genre.at[3, "occurrence"] = 0;
        self.df_of_average_votes_vs_genre.at[4, "occurrence"] = 0; self.df_of_average_votes_vs_genre.at[5, "occurrence"] = 0;
        self.df_of_average_votes_vs_genre.at[6, "occurrence"] = 0; self.df_of_average_votes_vs_genre.at[7, "occurrence"] = 0;
        self.df_of_average_votes_vs_genre.at[8, "occurrence"] = 0; self.df_of_average_votes_vs_genre.at[9, "occurrence"] = 0;
        self.df_of_average_votes_vs_genre.at[10, "occurrence"] = 0; self.df_of_average_votes_vs_genre.at[11, "occurrence"] = 0;
        self.df_of_average_votes_vs_genre.at[12, "occurrence"] = 0; self.df_of_average_votes_vs_genre.at[13, "occurrence"] = 0;
        self.df_of_average_votes_vs_genre.at[14, "occurrence"] = 0; self.df_of_average_votes_vs_genre.at[15, "occurrence"] = 0;
        self.df_of_average_votes_vs_genre.at[16, "occurrence"] = 0; self.df_of_average_votes_vs_genre.at[17, "occurrence"] = 0;
        self.df_of_average_votes_vs_genre.at[18, "occurrence"] = 0; self.df_of_average_votes_vs_genre.at[19, "occurrence"] = 0;
        self.df_of_average_votes_vs_genre.at[20, "occurrence"] = 0;self.df_of_average_votes_vs_genre.at[21, "occurrence"] = 0;
        self.df_of_average_votes_vs_genre.at[22, "occurrence"] = 0; self.df_of_average_votes_vs_genre.at[23, "occurrence"] = 0;
        self.df_of_average_votes_vs_genre.at[24, "occurrence"] = 0; self.df_of_average_votes_vs_genre.at[25, "occurrence"] = 0;
        self.df_of_average_votes_vs_genre.at[26, "occurrence"] = 0; self.df_of_average_votes_vs_genre.at[27, "occurrence"] = 0;

        # for linenum in range(0, len(self.df)):
        for linenum in range(0, len(self.df)):
            print(linenum)

            try:
                for genre in self.df.at[linenum, "genres"].split(','):
                    index_list = self.df_of_average_votes_vs_genre.index[self.df_of_average_votes_vs_genre['genres']==genre].to_list()
                    
                    if(len(index_list) > 0):
                        self.df_of_average_votes_vs_genre.at[index_list[0], 'numVotes'] += self.df.at[linenum, 'numVotes']
                        self.df_of_average_votes_vs_genre.at[index_list[0], 'occurrence'] += 1
            except Exception:
                    continue;

        for line in range(len(self.df_of_average_votes_vs_genre)):
            self.df_of_average_votes_vs_genre.at[line, "averageVotes"] = self.df_of_average_votes_vs_genre.at[line, "numVotes"] / self.df_of_average_votes_vs_genre.at[line, "occurrence"]
        
        
        print(self.df_of_average_votes_vs_genre.head(10))

        write_data_to_file(self.df_of_average_votes_vs_genre, "investigation_of_genre_vs_popularity.csv")

    def plotting_genre_vs_popularity(self):
        # plot, frame = plt.subplots(2,2)
        # plt.bar(self.df_of_average_votes_vs_genre['genres'], self.df_of_average_votes_vs_genre["numVotes"])
        # plt.bar(self.df_of_average_votes_vs_genre['genres'], self.df_of_average_votes_vs_genre["averageVotes"])
        # plt.bar(self.df_of_average_votes_vs_genre['genres'], self.df_of_average_votes_vs_genre["occurrence"])
        # self.df_of_average_votes_vs_genre['numVotes'] = self.df_of_average_votes_vs_genre['numVotes'] / 100
        # self.df_of_average_votes_vs_genre['averageVotes'] = self.df_of_average_votes_vs_genre['averageVotes'] *  1000
        # plt.plot(self.df_of_average_votes_vs_genre['genres'], self.df_of_average_votes_vs_genre['numVotes'], color='r')
        # plt.plot(self.df_of_average_votes_vs_genre['genres'], self.df_of_average_votes_vs_genre['averageVotes'], color='g')
        # plt.plot(self.df_of_average_votes_vs_genre['genres'], self.df_of_average_votes_vs_genre['occurrence'])

        plt.xticks(rotation=90)

    
    def year_vs_genre_popularity(self):
        # idea is to iterate through each year and iterate over every movie for that year
        # then iterate over the genres and map which genre is most popular by taking the numVotes associated with it
        # look like, for year in year_list, index_list = df.index[df['StartYear']==year].to_list(), for val in indexlist

        # creating the year list:
        best_of_each_year = dict()

        for year in range(1895, 2022):
            # print(year)

            index_list = self.df.index[self.df['startYear'] == str(year)].to_list()
            genre_list = dict()

            for index in index_list:
                # getting the most popular genres from the year

                # 1. check if the genre exists already
                # if so:
                #   2. get the current number of total votes
                #   3. add the number of total votes onto the value set
                # if not:
                    # 2. update the genre_dictionary to include the current genre and numVotes

                for genre in self.df.at[index, 'genres'].split(','):
                    if(genre != "\\N"):
                        # print(genre)
                        if(self.df.at[index, 'genres'] in genre_list):

                            numval = genre_list[genre]
                            numval += self.df.at[index, 'numVotes']

                            genre_list[genre] = numval
                        
                        else:
                            genre_list[genre] = self.df.at[index, 'numVotes']

            
            sorted(genre_list)
            # newdf = pd.DataFrame.from_dict(genre_list, columns=["genre", "numVotes"])
            maxval = max(genre_list, key=genre_list.get)
            best_of_each_year[year] = maxval
        
        print(best_of_each_year)

        # newdf = pd.DataFrame(data=best_of_each_year, columns=["year", "genre"])

        # plt.bar(newdf["year"], newdf["genre"])

        # creating a new dictionary with the genre and its percentage of total years
        piedict = dict()
        total = 0

        for year in best_of_each_year:
            total += 1

            if(best_of_each_year[year] in piedict):
                piedict[best_of_each_year[year]] += 1

            else:
                piedict[best_of_each_year[year]] = 1

        
        for genre in piedict:
            piedict[genre] = (piedict[genre] / total) * 100
        

        newdf = pd.DataFrame(list(piedict.items()),columns=["genre", "percentage"])
        

        print(piedict)
        plt.pie(newdf["percentage"], labels=newdf["genre"], )
        write_data_to_file(newdf, "genrevsyearvspopularityintotal.csv")
    
    def separated_genres_of_each_time_period_1916_1936(self):
        best_of_each_year = dict()

        for year in range(1916, 1936):
            # print(year)

            index_list = self.df.index[self.df['startYear'] == str(year)].to_list()
            genre_list = dict()

            for index in index_list:
                # getting the most popular genres from the year

                # 1. check if the genre exists already
                # if so:
                #   2. get the current number of total votes
                #   3. add the number of total votes onto the value set
                # if not:
                    # 2. update the genre_dictionary to include the current genre and numVotes

                for genre in self.df.at[index, 'genres'].split(','):
                    if(genre != "\\N"):
                        # print(genre)
                        if(self.df.at[index, 'genres'] in genre_list):

                            numval = genre_list[genre]
                            numval += self.df.at[index, 'numVotes']

                            genre_list[genre] = numval
                        
                        else:
                            genre_list[genre] = self.df.at[index, 'numVotes']

            
            sorted(genre_list)
            # newdf = pd.DataFrame.from_dict(genre_list, columns=["genre", "numVotes"])
            maxval = max(genre_list, key=genre_list.get)
            best_of_each_year[year] = maxval
        
        print(best_of_each_year)

        # newdf = pd.DataFrame(data=best_of_each_year, columns=["year", "genre"])

        # plt.bar(newdf["year"], newdf["genre"])

        # creating a new dictionary with the genre and its percentage of total years
        piedict = dict()
        total = 0

        for year in best_of_each_year:
            total += 1

            if(best_of_each_year[year] in piedict):
                piedict[best_of_each_year[year]] += 1

            else:
                piedict[best_of_each_year[year]] = 1

        
        for genre in piedict:
            piedict[genre] = (piedict[genre] / total) * 100
        

        newdf = pd.DataFrame(list(piedict.items()),columns=["genre", "percentage"])
        

        print(piedict)
        plt.pie(newdf["percentage"], labels=newdf["genre"], autopct='%1.1f%%')
        plt.title("1916 to 1936, most profitable Genres")
        write_data_to_file(newdf, "1916-to-1936_genre_vs_time.csv")

    def separated_genres_of_each_time_period(self):
        best_of_each_year = dict()

        for year in range(1895, 1915):
            # print(year)

            index_list = self.df.index[self.df['startYear'] == str(year)].to_list()
            genre_list = dict()

            for index in index_list:
                # getting the most popular genres from the year

                # 1. check if the genre exists already
                # if so:
                #   2. get the current number of total votes
                #   3. add the number of total votes onto the value set
                # if not:
                    # 2. update the genre_dictionary to include the current genre and numVotes

                for genre in self.df.at[index, 'genres'].split(','):
                    if(genre != "\\N"):
                        # print(genre)
                        if(self.df.at[index, 'genres'] in genre_list):

                            numval = genre_list[genre]
                            numval += self.df.at[index, 'numVotes']

                            genre_list[genre] = numval
                        
                        else:
                            genre_list[genre] = self.df.at[index, 'numVotes']

            
            sorted(genre_list)
            # newdf = pd.DataFrame.from_dict(genre_list, columns=["genre", "numVotes"])
            maxval = max(genre_list, key=genre_list.get)
            best_of_each_year[year] = maxval
        
        print(best_of_each_year)

        # newdf = pd.DataFrame(data=best_of_each_year, columns=["year", "genre"])

        # plt.bar(newdf["year"], newdf["genre"])

        # creating a new dictionary with the genre and its percentage of total years
        piedict = dict()
        total = 0

        for year in best_of_each_year:
            total += 1

            if(best_of_each_year[year] in piedict):
                piedict[best_of_each_year[year]] += 1

            else:
                piedict[best_of_each_year[year]] = 1

        
        for genre in piedict:
            piedict[genre] = (piedict[genre] / total) * 100
        

        newdf = pd.DataFrame(list(piedict.items()),columns=["genre", "percentage"])
        

        print(piedict)
        plt.pie(newdf["percentage"], labels=newdf["genre"], autopct='%1.1f%%')
        plt.title("1895 to 1915, most profitable Genres")
        write_data_to_file(newdf, "1895-to-1915_genre_vs_time.csv")

    def separated_genres_of_each_time_period_1937_to_1957(self):
        best_of_each_year = dict()

        for year in range(1937, 1957):
            # print(year)

            index_list = self.df.index[self.df['startYear'] == str(year)].to_list()
            genre_list = dict()

            for index in index_list:
                # getting the most popular genres from the year

                # 1. check if the genre exists already
                # if so:
                #   2. get the current number of total votes
                #   3. add the number of total votes onto the value set
                # if not:
                    # 2. update the genre_dictionary to include the current genre and numVotes

                for genre in self.df.at[index, 'genres'].split(','):
                    if(genre != "\\N"):
                        # print(genre)
                        if(self.df.at[index, 'genres'] in genre_list):

                            numval = genre_list[genre]
                            numval += self.df.at[index, 'numVotes']

                            genre_list[genre] = numval
                        
                        else:
                            genre_list[genre] = self.df.at[index, 'numVotes']

            
            sorted(genre_list)
            # newdf = pd.DataFrame.from_dict(genre_list, columns=["genre", "numVotes"])
            maxval = max(genre_list, key=genre_list.get)
            best_of_each_year[year] = maxval
        
        print(best_of_each_year)

        # newdf = pd.DataFrame(data=best_of_each_year, columns=["year", "genre"])

        # plt.bar(newdf["year"], newdf["genre"])

        # creating a new dictionary with the genre and its percentage of total years
        piedict = dict()
        total = 0

        for year in best_of_each_year:
            total += 1

            if(best_of_each_year[year] in piedict):
                piedict[best_of_each_year[year]] += 1

            else:
                piedict[best_of_each_year[year]] = 1

        
        for genre in piedict:
            piedict[genre] = (piedict[genre] / total) * 100
        

        newdf = pd.DataFrame(list(piedict.items()),columns=["genre", "percentage"])
        

        print(piedict)
        plt.pie(newdf["percentage"], labels=newdf["genre"], autopct='%1.1f%%')
        plt.title("1937 to 1957 most profitable Genres")
        write_data_to_file(newdf, "1937-to-1957_genre_vs_time.csv")

    def separated_genres_of_each_time_period_1958_to_1978(self):
        best_of_each_year = dict()

        for year in range(1958, 1978):
            # print(year)

            index_list = self.df.index[self.df['startYear'] == str(year)].to_list()
            genre_list = dict()

            for index in index_list:
                # getting the most popular genres from the year

                # 1. check if the genre exists already
                # if so:
                #   2. get the current number of total votes
                #   3. add the number of total votes onto the value set
                # if not:
                    # 2. update the genre_dictionary to include the current genre and numVotes

                for genre in self.df.at[index, 'genres'].split(','):
                    if(genre != "\\N"):
                        # print(genre)
                        if(self.df.at[index, 'genres'] in genre_list):

                            numval = genre_list[genre]
                            numval += self.df.at[index, 'numVotes']

                            genre_list[genre] = numval
                        
                        else:
                            genre_list[genre] = self.df.at[index, 'numVotes']

            
            sorted(genre_list)
            # newdf = pd.DataFrame.from_dict(genre_list, columns=["genre", "numVotes"])
            maxval = max(genre_list, key=genre_list.get)
            best_of_each_year[year] = maxval
        
        print(best_of_each_year)

        # newdf = pd.DataFrame(data=best_of_each_year, columns=["year", "genre"])

        # plt.bar(newdf["year"], newdf["genre"])

        # creating a new dictionary with the genre and its percentage of total years
        piedict = dict()
        total = 0

        for year in best_of_each_year:
            total += 1

            if(best_of_each_year[year] in piedict):
                piedict[best_of_each_year[year]] += 1

            else:
                piedict[best_of_each_year[year]] = 1

        
        for genre in piedict:
            piedict[genre] = (piedict[genre] / total) * 100
        

        newdf = pd.DataFrame(list(piedict.items()),columns=["genre", "percentage"])
        

        print(piedict)
        plt.pie(newdf["percentage"], labels=newdf["genre"], autopct='%1.1f%%')
        plt.title("1958 to 1978 most profitable Genres")
        write_data_to_file(newdf, "1958-to-1978_genre_vs_time.csv")

    def separated_genres_of_each_time_period_1979_to_1999(self):
        best_of_each_year = dict()

        for year in range(1979, 1999):
            # print(year)

            index_list = self.df.index[self.df['startYear'] == str(year)].to_list()
            genre_list = dict()

            for index in index_list:
                # getting the most popular genres from the year

                # 1. check if the genre exists already
                # if so:
                #   2. get the current number of total votes
                #   3. add the number of total votes onto the value set
                # if not:
                    # 2. update the genre_dictionary to include the current genre and numVotes

                for genre in self.df.at[index, 'genres'].split(','):
                    if(genre != "\\N"):
                        # print(genre)
                        if(self.df.at[index, 'genres'] in genre_list):

                            numval = genre_list[genre]
                            numval += self.df.at[index, 'numVotes']

                            genre_list[genre] = numval
                        
                        else:
                            genre_list[genre] = self.df.at[index, 'numVotes']

            
            sorted(genre_list)
            # newdf = pd.DataFrame.from_dict(genre_list, columns=["genre", "numVotes"])
            maxval = max(genre_list, key=genre_list.get)
            best_of_each_year[year] = maxval
        
        print(best_of_each_year)

        # newdf = pd.DataFrame(data=best_of_each_year, columns=["year", "genre"])

        # plt.bar(newdf["year"], newdf["genre"])

        # creating a new dictionary with the genre and its percentage of total years
        piedict = dict()
        total = 0

        for year in best_of_each_year:
            total += 1

            if(best_of_each_year[year] in piedict):
                piedict[best_of_each_year[year]] += 1

            else:
                piedict[best_of_each_year[year]] = 1

        
        for genre in piedict:
            piedict[genre] = (piedict[genre] / total) * 100
        

        newdf = pd.DataFrame(list(piedict.items()),columns=["genre", "percentage"])
        

        print(piedict)
        plt.pie(newdf["percentage"], labels=newdf["genre"], autopct='%1.1f%%')
        plt.title("1979 to 1999 most profitable Genres")
        write_data_to_file(newdf, "1979-to-1999_genre_vs_time.csv")
    
    def separated_genres_of_each_time_period_2000_to_2022(self):
        best_of_each_year = dict()

        for year in range(2000, 2022):
            # print(year)

            index_list = self.df.index[self.df['startYear'] == str(year)].to_list()
            genre_list = dict()

            for index in index_list:
                # getting the most popular genres from the year

                # 1. check if the genre exists already
                # if so:
                #   2. get the current number of total votes
                #   3. add the number of total votes onto the value set
                # if not:
                    # 2. update the genre_dictionary to include the current genre and numVotes

                for genre in self.df.at[index, 'genres'].split(','):
                    if(genre != "\\N"):
                        # print(genre)
                        if(self.df.at[index, 'genres'] in genre_list):

                            numval = genre_list[genre]
                            numval += self.df.at[index, 'numVotes']

                            genre_list[genre] = numval
                        
                        else:
                            genre_list[genre] = self.df.at[index, 'numVotes']

            
            sorted(genre_list)
            # newdf = pd.DataFrame.from_dict(genre_list, columns=["genre", "numVotes"])
            maxval = max(genre_list, key=genre_list.get)
            best_of_each_year[year] = maxval
        
        print(best_of_each_year)

        # newdf = pd.DataFrame(data=best_of_each_year, columns=["year", "genre"])

        # plt.bar(newdf["year"], newdf["genre"])

        # creating a new dictionary with the genre and its percentage of total years
        piedict = dict()
        total = 0

        for year in best_of_each_year:
            total += 1

            if(best_of_each_year[year] in piedict):
                piedict[best_of_each_year[year]] += 1

            else:
                piedict[best_of_each_year[year]] = 1

        
        for genre in piedict:
            piedict[genre] = (piedict[genre] / total) * 100
        

        newdf = pd.DataFrame(list(piedict.items()),columns=["genre", "percentage"])
        

        print(piedict)
        plt.pie(newdf["percentage"], labels=newdf["genre"], autopct='%1.1f%%')
        plt.title("2000 to 2022 most profitable Genres")
        write_data_to_file(newdf, "2000-to-2022_genre_vs_time.csv")

    def separated_genres_of_each_time_period_1980_to_1990(self):
        best_of_each_year = dict()

        for year in range(1980, 1991):
            # print(year)

            index_list = self.df.index[self.df['startYear'] == str(year)].to_list()
            genre_list = dict()

            for index in index_list:
                # getting the most popular genres from the year

                # 1. check if the genre exists already
                # if so:
                #   2. get the current number of total votes
                #   3. add the number of total votes onto the value set
                # if not:
                    # 2. update the genre_dictionary to include the current genre and numVotes

                for genre in self.df.at[index, 'genres'].split(','):
                    if(genre != "\\N"):
                        # print(genre)
                        if(self.df.at[index, 'genres'] in genre_list):

                            numval = genre_list[genre]
                            numval += self.df.at[index, 'numVotes']

                            genre_list[genre] = numval
                        
                        else:
                            genre_list[genre] = self.df.at[index, 'numVotes']

            
            sorted(genre_list)
            # newdf = pd.DataFrame.from_dict(genre_list, columns=["genre", "numVotes"])
            maxval = max(genre_list, key=genre_list.get)
            best_of_each_year[year] = maxval
        
        print(best_of_each_year)

        # newdf = pd.DataFrame(data=best_of_each_year, columns=["year", "genre"])

        # plt.bar(newdf["year"], newdf["genre"])

        # creating a new dictionary with the genre and its percentage of total years
        piedict = dict()
        total = 0

        for year in best_of_each_year:
            total += 1

            if(best_of_each_year[year] in piedict):
                piedict[best_of_each_year[year]] += 1

            else:
                piedict[best_of_each_year[year]] = 1

        
        for genre in piedict:
            piedict[genre] = (piedict[genre] / total) * 100
        

        newdf = pd.DataFrame(list(piedict.items()),columns=["genre", "percentage"])
        

        print(piedict)
        plt.pie(newdf["percentage"], labels=newdf["genre"], autopct='%1.1f%%')
        plt.title("1980 to 1990 most profitable Genres")
        write_data_to_file(newdf, "1980-to-1990_genre_vs_time.csv")

    def separated_genres_of_each_time_period_1990_to_2000(self):
        best_of_each_year = dict()

        for year in range(1990, 2001):
            # print(year)

            index_list = self.df.index[self.df['startYear'] == str(year)].to_list()
            genre_list = dict()

            for index in index_list:
                # getting the most popular genres from the year

                # 1. check if the genre exists already
                # if so:
                #   2. get the current number of total votes
                #   3. add the number of total votes onto the value set
                # if not:
                    # 2. update the genre_dictionary to include the current genre and numVotes

                for genre in self.df.at[index, 'genres'].split(','):
                    if(genre != "\\N"):
                        # print(genre)
                        if(self.df.at[index, 'genres'] in genre_list):

                            numval = genre_list[genre]
                            numval += self.df.at[index, 'numVotes']

                            genre_list[genre] = numval
                        
                        else:
                            genre_list[genre] = self.df.at[index, 'numVotes']

            
            sorted(genre_list)
            # newdf = pd.DataFrame.from_dict(genre_list, columns=["genre", "numVotes"])
            maxval = max(genre_list, key=genre_list.get)
            best_of_each_year[year] = maxval
        
        print(best_of_each_year)

        # newdf = pd.DataFrame(data=best_of_each_year, columns=["year", "genre"])

        # plt.bar(newdf["year"], newdf["genre"])

        # creating a new dictionary with the genre and its percentage of total years
        piedict = dict()
        total = 0

        for year in best_of_each_year:
            total += 1

            if(best_of_each_year[year] in piedict):
                piedict[best_of_each_year[year]] += 1

            else:
                piedict[best_of_each_year[year]] = 1

        
        for genre in piedict:
            piedict[genre] = (piedict[genre] / total) * 100
        

        newdf = pd.DataFrame(list(piedict.items()),columns=["genre", "percentage"])
        

        print(piedict)
        plt.pie(newdf["percentage"], labels=newdf["genre"], autopct='%1.1f%%')
        plt.title("1990 to 2000 most profitable Genres")
        write_data_to_file(newdf, "1990-to-2000_genre_vs_time.csv")

    def plotting_total_genre_popularity(self):
        self.df_genre_vs_popularity = pd.read_csv("genrevsyearvspopularityintotal.csv")

        plt.pie(self.df_genre_vs_popularity["percentage"], labels=self.df_genre_vs_popularity["genre"],  autopct='%1.1f%%')



            

genre_vs_prof = G_vs_profitability()
# genre_vs_prof.initial_investigation()
# genre_vs_prof.creating_cleaned_df()
# genre_vs_prof.plotting_genre_vs_popularity()
# genre_vs_prof.year_vs_genre_popularity()
genre_vs_prof.separated_genres_of_each_time_period_1980_to_1990()
# genre_vs_prof.plotting_total_genre_popularity()
plt.show()