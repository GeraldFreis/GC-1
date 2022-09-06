import pandas as pd
import matplotlib.pyplot as plt


class Specific_genres:
    def romance_profitability_average_votes(self):
        self.df = pd.read_csv("genre_vs_average_votes_over_time.csv", low_memory=False)

        plt.plot(self.df["year"], self.df["romance"])
        plt.title("Romance: Average Votes vs Year")
        plt.xlabel("Year")
        plt.ylabel("Average Votes")  
        plt.legend(["Romance"], loc=0, frameon=True)

        plt.show() 
    
    def romance_profitability_total_votes(self):
        self.df = pd.read_csv("genre_vs_total_votes_over_time.csv", low_memory=False)

        plt.plot(self.df["year"], self.df["romance"])
        plt.title("Romance: Total Votes vs Year")
        plt.xlabel("Year")
        plt.ylabel("Total Votes")  
        plt.legend(["Romance"], loc=0, frameon=True)

        plt.show() 
    
    def romance_profitability_occurrence(self):
        self.df = pd.read_csv("genre_vs_occurence_over_time.csv", low_memory=False)

        plt.plot(self.df["year"], self.df["romance"])
        plt.title("Romance: Occurrence vs Year")
        plt.xlabel("Year")
        plt.ylabel("Occurrence")  
        plt.legend(["Romance"], loc=0, frameon=True)

        plt.show()
        
    def documentary_profitability_average_votes(self):
        self.df = pd.read_csv("genre_vs_average_votes_over_time.csv", low_memory=False)

        plt.plot(self.df["year"], self.df["documentary"])
        plt.title("Documentary: Average Votes vs Year")
        plt.xlabel("Year")
        plt.ylabel("Average Votes")  
        plt.legend(["Documentary"], loc=0, frameon=True)

        plt.show() 
    
    def documentary_profitability_total_votes(self):
        self.df = pd.read_csv("genre_vs_total_votes_over_time.csv", low_memory=False)

        plt.plot(self.df["year"], self.df["documentary"])
        plt.title("Documentary: Total Votes vs Year")
        plt.xlabel("Year")
        plt.ylabel("Total Votes")  
        plt.legend(["Documentary"], loc=0, frameon=True)

        plt.show() 
    
    def documentary_profitability_occurrence(self):
        self.df = pd.read_csv("genre_vs_occurence_over_time.csv", low_memory=False)

        plt.plot(self.df["year"], self.df["documentary"])
        plt.title("Documentary: Occurrence vs Year")
        plt.xlabel("Year")
        plt.ylabel("Occurrence")  
        plt.legend(["Documentary"], loc=0, frameon=True)

        plt.show()
    
    def drama_profitability_average_votes(self):
        self.df = pd.read_csv("genre_vs_average_votes_over_time.csv", low_memory=False)

        plt.plot(self.df["year"], self.df["drama"])
        plt.title("Drama: Average Votes vs Year")
        plt.xlabel("Year")
        plt.ylabel("Average Votes")  
        plt.legend(["Drama"], loc=0, frameon=True)

        plt.show()

    
    def drama_profitability_total_votes(self):
        self.df = pd.read_csv("genre_vs_total_votes_over_time.csv", low_memory=False)

        plt.plot(self.df["year"], self.df["drama"])
        plt.title("Drama: Total Votes vs Year")
        plt.xlabel("Year")
        plt.ylabel("Total Votes")  
        plt.legend(["Drama"], loc=0, frameon=True)

        plt.show()

    def drama_profitability_occurrence(self):
        self.df = pd.read_csv("genre_vs_occurence_over_time.csv", low_memory=False)

        plt.plot(self.df["year"], self.df["drama"])
        plt.title("Drama: Occurrence vs Year")
        plt.xlabel("Year")
        plt.ylabel("Occurrence")  
        plt.legend(["Drama"], loc=0, frameon=True)

        plt.show()
    
    def comedy_profitability_average_votes(self):
        self.df = pd.read_csv("genre_vs_average_votes_over_time.csv", low_memory=False)

        plt.plot(self.df["year"], self.df["comedy"])
        plt.title("Comedy: Average Votes vs Year")
        plt.xlabel("Year")
        plt.ylabel("Average Votes")  
        plt.legend(["Comedy"], loc=0, frameon=True)

        plt.show()
    
    def comedy_profitability_total_votes(self):
        self.df = pd.read_csv("genre_vs_total_votes_over_time.csv", low_memory=False)

        plt.plot(self.df["year"], self.df["comedy"])
        plt.title("Comedy: Total Votes vs Year")
        plt.xlabel("Year")
        plt.ylabel("Total Votes")  
        plt.legend(["Comedy"], loc=0, frameon=True)

        plt.show()
    
    def comedy_profitability_occurrence(self):
        self.df = pd.read_csv("genre_vs_occurence_over_time.csv", low_memory=False)

        plt.plot(self.df["year"], self.df["comedy"])
        plt.title("Comedy: Occurrence vs Year")
        plt.xlabel("Year")
        plt.ylabel("Occurrence")  
        plt.legend(["Comedy"], loc=0, frameon=True)

        plt.show()


analysis = Specific_genres()
analysis.comedy_profitability_occurrence()