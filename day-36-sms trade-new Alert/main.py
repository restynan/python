# Assuming yesterday was  11th
# we pull closing stock for 10th $1000
# closing price the previous day $900
# increase is up-100

# fetch news to find the reason for te increase(lauched a new product
# send sms using twillo
import requests

from twilio.rest import Client

print("test")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "https://www.alphavantage.co/query"
STOCK_API_KEY = ""
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = ""
account_sid = ""
auth_token = ""

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=GVNEPMVNI4I8PZBV
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_API, stock_params)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']

# list compression
data_list = [value for (key, value) in stock_data.items()]
yesterday_closing_price = data_list[0]["4. close"]
previous_day_closing_price = data_list[1]["4. close"]
print(f"yesterday closing price: {yesterday_closing_price}")
print(f"previous day closing price: {previous_day_closing_price}")

# difference
difference = float(yesterday_closing_price) - float(previous_day_closing_price)
print(f"difference: {difference}")
up_down = "🔺"
if difference < 0:
    up_down = "🔻"


# percentage difference
diff_percent = round((abs(difference) / float(yesterday_closing_price)) * 100)
print(f"percentage difference: {diff_percent}")

# if percentage difference > 5  call get news
# get the first 3 news pieces for the COMPANY_NAME.
# https://newsapi.org/v2/everything?q=Tesla%20Inc&apiKey=35ea7dc6fd2840c4ba2208512e409440

if diff_percent > 2:
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(NEWS_ENDPOINT, news_params)
    response.raise_for_status()
    top_three_articles = response.json()["articles"][:3]
    #print(top_three_articles)

    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}% \nHeadline: {article ['title']}. \nBrief: {article['description']}" for article in top_three_articles]
    print(formatted_articles)

    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+13856854937',
            to='+16416661250'
        )
        print(message.status)
        print(message.sid)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
