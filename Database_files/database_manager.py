import pandas as pd


akas = pd.read_table("title.akas.tsv", sep="\t", low_memory=False)
basics = pd.read_table("title.basics.tsv", sep="\t", low_memory=False)
ratings = pd.read_table("title.ratings.tsv", sep="\t", low_memory=False)


hit_titles = list()

# adding values to the basics database
basics["averageRating"] = ratings["averageRating"]
basics["numVotes"] = ratings["numVotes"]
basics["region"] = None



# counter = 0
# for line in range(len(basics)):
#     for this_line in range(len(akas)):
#         if(akas["titleId"].iloc[this_line]in hit_titles or akas["titleId"].iloc[this_line] != basics["tconst"].iloc[line]):
#             pass
#         else:
#             # basics["region"].iloc[line] = akas["region"].iloc[this_line]
#             basics.at[line, "region"] = akas.at[this_line, "region"]
#             hit_titles.append(akas.at[this_line, "titleId"])

#     print(line)

basics.to_csv("Compiled_csv.csv")
print(basics.head(7))