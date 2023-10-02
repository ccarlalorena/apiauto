import os

from dotenv import load_dotenv

# Load the stored environment variables
load_dotenv()

#Get the values
TOKEN_TODO = os.getenv("TOKEN")
print(f"TOKEN = {TOKEN_TODO}")

HEADERS = {
    "Authorization": f"Bearer {TOKEN_TODO}"
}
ABS_PATH = os.path.abspath(__file__ + "../../../")

