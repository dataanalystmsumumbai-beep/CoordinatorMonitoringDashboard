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

        df.columns = (
            df.columns
            .astype(str)
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        return df

    except Exception as e:

        print(e)

        return pd.DataFrame()
