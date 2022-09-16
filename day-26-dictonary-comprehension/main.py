# dictionary comprehension
# new _dict = {new_key:new_value for (key,value) in dict.items() if test}
import random
'''
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_score = {name: random.randint(1, 100) for name in names}
print(student_score)

passed_students = {student: score for (student, score) in student_score.items() if score > 59}
print(passed_students)

# takes a word in a sentence and  calculates the number of letters in each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

word_number_of_letters = {word: len(word) for word in sentence.split()}
print(word_number_of_letters)

# takes temperature in degrees Celsius and converts it into degrees Fahrenheit
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# (temp_c *9/5)+32 =temp_f
weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)
'''
#Looping rows through data frames
import pandas
student_data = {"student": ["Angelle", "Resty", "Mary"],
                "scores": ["70", "87", "29"]}
student_data_frame = pandas.DataFrame(student_data)
print(student_data_frame.to_dict())
#print(student_data_frame)
#for (key, value) in student_data_frame.items():
#    print(value)
for (index, row) in student_data_frame.iterrows():
        print(row.student)