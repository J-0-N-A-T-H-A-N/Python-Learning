import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

stock_change = 3

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

STOCK_API_KEY = "9MYYQ6C95EPPA7H5"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

stock_data = requests.get(url=STOCK_ENDPOINT, params=stock_params).json()
time_series = stock_data["Time Series (Daily)"]
yesterday = list(time_series.items())[0]
day_before = list(time_series.items())[1]
print(yesterday)
yesterday_close = float(yesterday[1]["4. close"])
day_before_close = float(day_before[1]["4. close"])
print(f"Closing price on {yesterday[0]}: {yesterday_close}")
print(f"Closing price on {day_before[0]}: {day_before_close}")

difference = (yesterday_close - day_before_close) / day_before_close * 100
print(f"{difference:.2f}%")
if difference < 0:
    diff = f"🔻{difference:.1f}%"
else:
    diff = f"🔺{difference:.1f}"

if abs(difference) >= stock_change:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    NEWS_API_KEY = "df4fd04237e2407987360550b975c60d"
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    news_params = {
        "qInTitle": COMPANY_NAME,
        "from": dt.datetime.now().strftime("%Y-%m-%d"),
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": NEWS_API_KEY,
    }

    news_data = requests.get(url=NEWS_ENDPOINT, params=news_params).json()
    top_3 = list(news_data["articles"])[0:3]    # Top 3 stories in English
    headlines = []
    for article in top_3:
        headlines.append(f'{STOCK}: {diff}\nHeadline: {article["title"]}\nBrief: {article["title"]}\n')

    ## STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    account_sid = "ACf703f5ef03084ce4cb0dc0c58bcf1c6e"
    auth_token = "96da4afea68106cbdb26f608f049af9b"

    for item in headlines:
        # client = Client(account_sid, auth_token)
        # message = client.messages \
        #     .create(
        #     body=item,
        #     from_="+18646614174",
        #     to="+353863890220"
        # )
        # print(message.status)
        print(item)

    #Optional: Format the SMS message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """
