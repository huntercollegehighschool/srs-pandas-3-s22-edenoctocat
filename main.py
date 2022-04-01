# 1. Import pandas
import pandas as pd

# 2. Read the "metacritic2.csv" file, and save the data in a dataframe variable. Print the data
reviews = pd.read_csv('metacritic2.csv', index_col = 0)
print(reviews)

# 3. Create a new dataframe with only Mario Games. Save that in a new dataframe variable and print that data (this will involve Boolean indexing)
mariogames = reviews[reviews.index.str.contains("Mario")]
print(mariogames)

# 4. Sort the Mario data by release year in descending order. (a .sort_values() function exists)
mariosorted = mariogames.sort_values(by = ["Release Year"], ascending = False)
print(mariosorted)

# 5. Last time we used a loop to find individual data on different platforms, years, etc. There is a .groupby() function that exists as well. Let's start by grouping by Release Year. Run the following code:
# <var> = <dataframe>.groupby("Release Year").count()
# What does it seems like count presents?
groupreleaseyear = reviews.groupby("Release Year").count()
print(groupreleaseyear)

# 6. Use groupby again, but this time on Platform. Afterwards, run .count(), .mean(), and .median(). Which platform looks like it has the best games?
groupplatform = reviews.groupby("Platform")
print(groupplatform.count())
print(groupplatform.mean())
print(groupplatform.median())

# 7. Create a new dataframe from the HunterAMC.csv file.
amc = pd.read_csv("HunterAMC.csv", index_col = 0, sep = "\t")
print(amc)

# 8. In that csv, contest 0 is the AMC 10, and contest 2 is the AMC 12. Create two separate dataframes containing data from the two different contests.
amc10 = amc[amc['contest'] == 0]
print(amc10)
amc12 = amc[amc['contest'] == 2]
print(amc12)

# 9. Find the average scores for each contest.
print(amc10['TotalScore'].mean())
print(amc12['TotalScore'].mean())

# 10. For each column, count how often each answer choice was selected.
columns = []
for i in range(1, 25):
  columns += ["ID" + str(i)]

likelyanswers = {}
for column in columns:
  thiscolumn = amc10.groupby(column).count()["Age"]
  print(thiscolumn)
  dictcolumn = dict(thiscolumn)
  dictcolumn.pop('.', None)
  maxvalue = max(dictcolumn, key=dictcolumn.get)
  likelyanswers[column] = maxvalue

print(likelyanswers)