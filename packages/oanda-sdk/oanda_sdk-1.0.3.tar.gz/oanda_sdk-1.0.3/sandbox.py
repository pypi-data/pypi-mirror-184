import os
from dotenv import load_dotenv
from oanda_sdk-sdk.client import Client
from oanda_sdk-sdk.position import Position
from oanda_sdk-sdk.transaction import Transaction

load_dotenv()
ACCOUNT_ID = os.getenv("ACCOUNT_ID")
API_TOKEN = os.getenv("API_TOKEN")
client = Client()
client.set_account_id(ACCOUNT_ID)
client.set_api_token(API_TOKEN)

position = Position(client)
print(position.get_positions().status_code)
print(position.get_open_positions().status_code)
print(position.get_position_for("EUR_USD").status_code)
print(position.close_position_for("EUR_USD", "-50").status_code)

trans = Transaction(client)
print(trans.get_transaction("3502").status_code)
print(trans.get_transactions(from_id="3502", to_id="33514").status_code)
print(trans.get_transactions_since("3502").status_code)
