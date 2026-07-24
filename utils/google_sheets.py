import requests
import pandas as pd

WEB_APP_URL = "https://script.google.com/macros/s/AKfycbwLX91WvDWwj0QmRMvdFHy42iPTqarUPv1pTz7h08TKYcxFUD2NNqa23NJHOcl0ujvz/exec"


def save_review(date, coordinator, task, frequency, priority, status, remarks):

    payload = {
        "date": date,
        "coordinator": coordinator,
        "task": task,
        "frequency": frequency,
        "priority": priority,
        "status": status,
        "remarks": remarks
    }

    try:
        r = requests.post(WEB_APP_URL, json=payload)
        return r.json()

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def load_reviews():

    try:

        r = requests.get(WEB_APP_URL)

        data = r.json()

        df = pd.DataFrame(data)

        if df.empty:
            return df

        # Convert all column names to lowercase
        df.columns = [str(c).strip().lower() for c in df.columns]

        return df

    except Exception as e:

        print(e)

        return pd.DataFrame()

def add_coordinator(name):

    payload = {
        "action": "add_coordinator",
        "name": name
    }

    r = requests.post(
        WEB_APP_URL,
        json=payload
    )

    return r.json()
def load_coordinators():

    try:

        r = requests.get(
            WEB_APP_URL + "?action=coordinators"
        )

        return r.json()

    except:

        return []
