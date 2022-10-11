import requests
import datetime as dt

# https://docs.pixe.la/

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "nabeel943khan"
USER_TOKEN = ""
GRAPH_ID = "graph1"

user_params = {
    "token": USER_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(PIXELA_ENDPOINT, json=user_params)
# print(response.text)
# Authentication is in the header
graph_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'

graph_params = {
    "id": GRAPH_ID,
    "name": "playing video games",
    "unit": "hour",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": USER_TOKEN
}
# graph_response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
# formating datetime
# https://www.w3schools.com/python/python_datetime.asp
today = dt.datetime.today()
today_formatted = today.strftime("%Y%m%d")
print(today.strftime("%Y%m%d"))
yesterday = dt.datetime(year=2022, month=10, day=5)
print(yesterday)
pixel_data = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "7"
}

# pixel_response = requests.post(pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(pixel_response.text)
# https://pixe.la/v1/users/nabeel943khan/graphs/graph1.html

# updata

update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"

update_pixel_data = {
    "quantity": "15"
}
pixel_update_response = requests.put(update_pixel_endpoint, json=update_pixel_data, headers=headers)
print(pixel_update_response.text)
# delete
delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today_formatted}"
delete_pixel_response = requests.delete(url=delete_endpoint, headers=headers)
print(delete_pixel_response.text)
