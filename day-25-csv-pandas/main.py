import csv
import pandas

# pandas is python data analysis library
data = pandas.read_csv("weather_data.csv")
print(type(data))  # prints a data frame object
print(data)
'''
# covert data to a dictionary
weather_dict = data.to_dict()
print(weather_dict)

# data for  a column
print(type(data["temp"]))  # returns a series object equivalent to a list
print(data["temp"])

# convert temperature data to a list
temp_list = data["temp"].to_list()
print(temp_list)

# Average
average = data["temp"].mean()
print(f"average temperature : {average}")

# Maximum temp
max_temp = data["temp"].max()
print(f"maximum temperature : {max_temp}")
'''
# getting data in a row
monday_row = data[data.day == "Monday"]
print(monday_row)
print(f"Monday temperature : {int(monday_row.temp)}")

# row with the maximum temp in the week
max_temp = data.temp.max()
print(data[data.temp == max_temp])

# creating a data frame from scratch
students_scores = {"students": ["Amy", "James", "Angela"],
                   "scores": [76, 69, 23]}
students_dataframe = pandas.DataFrame(students_scores)
print(students_dataframe)
students_dataframe.to_csv("new_data.csv")


with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)  # return an object
    print(data)
    temperatures = []
    for row in data:
        print(row)
        if not row[1] == "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

