from pathlib import Path
from rich.console import Console
from rich.style import Style
import typer, json, os, sys
from pymongo import MongoClient
import dotenv
import certifi
from pydantic import ValidationError

# Get project's home directory,
BASEDIR = Path(__file__).parents[0]
# All data directory
DATADIR = BASEDIR / "data"
# Insert the BASEDIR to system path
sys.path.insert(0, os.fspath(BASEDIR))

# get imm system's env variables
path = os.path.abspath(os.path.join(os.path.expanduser("~"), ".immenv"))
config = dotenv.dotenv_values(path)
# load env variables if a .env file exists
dotenv.load_dotenv(path)

SERVER_URL = "https://imm.jackyzhang.pro/"

# Mongodb
account = os.getenv("MongoDBUser")
password = os.getenv("MongoDBPassword")
connection = f"mongodb+srv://{account}:{password}@noah.yi5fo.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(connection, tlsCAFile=certifi.where())
database = "test"
db = client[database]

# imm account
imm_account: str = config.get("imm_user")
imm_password: str = config.get("imm_password")



class Default:
    rcic = "jacky"
    rciccompany = "noah"
    temp_num = 1  # for word generation using template
    uploaddir = "."  # for webform, uploading all dir's file
    initial = False  # Only for BCPNP webform to check if it is initial reg or app
    previous = False  # Only for BCPNP webform to check if there is previous application
    user_permission = ["make", "check"]


app = typer.Typer()
console = Console(record=True)

error_style = Style(color="red")
success_style = Style(color="green")
warning_style = Style(color="yellow")


def print_success(e: str):
    console.print(e, style=success_style)


def print_exception(e: Exception):
    console.print(e, style="red")


def print_validation_errors(e: ValidationError):
    for err in e.errors():
        console.print("->".join(err["loc"]) + ": " + err["msg"], style="red")


def print_error(e):
    console.print(e, style=error_style)


def print_warning(msg: str):
    console.print(msg, style=warning_style)
