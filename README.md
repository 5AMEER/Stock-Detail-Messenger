# Stock-Detail-Messenger
Automated program application which will notify users the details about the stock and the top five headlines related to the company every day via SMS on his registered mobile.

# Automated Stock and News Notification App

This application is designed to automate the process of sending daily stock details and top five headlines related to a company via SMS to the user's registered mobile number. The program utilizes the Twilio API for SMS services and fetches stock details using an API. The code is written in Python.

## Features

- Automated daily notifications for stock details and news headlines.
- Utilizes the Twilio API for sending SMS notifications.
- Fetches stock details using a stock API.
- Provides the top five news headlines related to the specified company.

## Prerequisites

Before using the application, you'll need to have the following:

- Python 3.x installed on your system.
- A Twilio account with the Twilio SID, Auth Token, and a Twilio phone number.
- Access to a stock API for fetching stock details.

## Setup and Usage

1. Clone this repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Open the `config.py` file and replace the placeholders with your Twilio account details and stock API information.
4. Run the `automated_notification.py` script.
5. The program will fetch stock details and news headlines, and then send an SMS with the information to the registered mobile number.

## Configurations

In the `config.py` file, you can set the following:

- `TWILIO_ACCOUNT_SID`: Your Twilio Account SID.
- `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token.
- `TWILIO_PHONE_NUMBER`: Your Twilio phone number.
- `USER_PHONE_NUMBER`: The user's registered mobile number.
- `STOCK_API_ENDPOINT`: The URL of the stock API.

## Example Output
