import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
count_gray = (data["Primary Fur Color"] == "gray").count()

count_cinnamon = (data["Primary Fur Color"] == "Cinnamon").count()
count_black = (data["Primary Fur Color"] == "Black").count()
Squirrel_dict = {"Fur Color": ["Gray", "Cinnamon", "Black"],
                 "Count": [count_gray, count_cinnamon, count_black]}
squirrel_dataframe = pandas.DataFrame(Squirrel_dict)

squirrel_dataframe.to_csv("squirrel_count.csv")
