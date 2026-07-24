import requests
import pandas as pd

WEB_APP_URL = "YOUR_APPS_SCRIPT_WEBAPP_URL"


def save_review(date,
                coordinator,
                task,
                frequency,
                priority,
                status,
                remarks):

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

        r = requests.post(

            WEB_APP_URL,

            json=payload,

            timeout=30

        )

        return r.json()

    except Exception as e:

        return {

            "success": False,

            "message": str(e)

        }


def load_reviews():

    try:

        r = requests.get(

            WEB_APP_URL,

            timeout=30

        )

        data = r.json()

        if isinstance(data, list):

            return pd.DataFrame(data)

        return pd.DataFrame()

    except:

        return pd.DataFrame()
