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

def get_teams_today():
    for games in range(len(todays_info["events"])):
        # Home team
        base_JSON_request = f"{todays_info["events"][games]["competitions"][0]["competitors"][0]["team"]["displayName"]}"
        print(base_JSON_request)

        # Away team
        base_JSON_request = f"{todays_info["events"][games]["competitions"][0]["competitors"][1]["team"]["displayName"]}"
        print(base_JSON_request)

get_teams_today()