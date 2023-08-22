import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

COMPANY_NAME = "TESLA"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

VIRTUAL_TWILIO_NUMBER = '+175xxxx6321'
VERIFIED_NUMBER = '+919xxxxx3952'

STOCK_API_KEY = "8ZCRBAQxxxxx5LS"
NEWS_API_KEY = "c543b33dfb0345fxxxxxx4060c4f1"
TWILIO_SID = "AC6fa85d4108f93fa0xxxxxxxa6d78"
TWILIO_AUTH_TOKEN = "4c0624a0cc019d0xxxxxxxx69fb1"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
# print(data)

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)


if abs(diff_percent) > -2:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]


    three_articles = articles[:3]
    # print(three_articles)


    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    # print(formatted_articles)

  
    #Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)


    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
