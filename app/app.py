# Connect to API
import requests

base_url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"

def get_info_today(date):
    url = f"{base_url}?DATE={date}"
    response = requests.get(url)
    
    # If there is no error, response will be 200
    if response.status_code == 200:
        todays_data = response.json()
        return todays_data
    else:
        print(f"Failed to retrieve data, response code: {response.status_code}")

today = "20260228"
todays_info = get_info_today(today)

# Values used to navigate through the JSON dictionary
events_id = 0
competitions_id = 0
competitors_id = 0
# The 'attribute' we want to find, such as 
# displayName : the team's name
# logo : the teams logo etc.
attribute = "displayName"
base_JSON_request = f"{todays_info["events"][events_id]["competitions"][competitions_id]["competitors"][competitors_id]["team"][attribute]}"

if todays_info:
    print(base_JSON_request)