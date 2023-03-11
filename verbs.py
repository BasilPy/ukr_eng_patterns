from oauth2client.service_account import ServiceAccountCredentials
import gspread
from datetime import datetime
import string
# TODO TUTRIAL https://www.youtube.com/watch?v=ddf5Z0aQPzY
date_and_time = datetime.today()
scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('./dry_patterns.json', scope)
# dry_patterns.json -> replace with your json credential key
client = gspread.authorize(creds)

python_test = client.open("eng_patterns").worksheet("Sheet2")

pronouns = ["_", "I", "My mother", "You", "She", "He", "You", "We", "It", "They"]

verb = "hug"
ending = "s"
position = [1, 1]
character = string.ascii_uppercase[position[1]]  # represent column as a character

for i in range(1, len(pronouns)):
    if pronouns[i] == "She" or pronouns[i] == "He" \
            or pronouns[i] == "It" or pronouns[i] == "My mother":
        python_test.update_cell(i + position[0]-1, position[1]+1, str(f'{pronouns[i]} {verb}{ending}'))
    else:
        python_test.update_cell(i + position[0]-1, position[1]+1, str(f'{pronouns[i]} {verb}'))

for i in range(1, len(pronouns)):
    python_test.update_cell(i + position[0]-1, position[1],
                            str(f'=GOOGLETRANSLATE({character}{i+position[0]-1}, "en", "uk")'))
