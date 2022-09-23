# FileNotFound error

try:
    my_file = open("my_file.txt", mode="r")
    dict = {"key": "value"}
    value = dict["non_existent_key"]
except FileNotFoundError as error_message:
    print(error_message)
except KeyError as key:
    print(f"{key} not found in dictionary")
else:
    my_file.read()
finally:
    print("in finally")
'''
# TODO: Catch the exception and make sure the code runs without crashing.
fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as error_message:
        print(error_message)
    else:
        print(fruit + " pie")


make_pie(4)
#the dictionaries without likes  means should have zero likes
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        likes = post['Likes']
    except KeyError as error_message:
        print(f"key: {error_message} doesn't exist in {post}")
    else:
        total_likes += likes

print(total_likes)