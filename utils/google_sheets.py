
import requests

WEB_APP_URL = "https://script.google.com/macros/s/AKfycbzEz6BVmAWhoR5Wws5h2FU76pH6ypE-aMe4bKopvRPHVuAWqI7Gfa5w4Je7i4YvJemk/exec"


def save_review(
    review_date,
    coordinator,
    task,
    frequency,
    priority,
    status,
    remarks
):

    payload = {

        "date": str(review_date),

        "coordinator": coordinator,

        "task": task,

        "frequency": frequency,

        "priority": priority,

        "status": status,

        "remarks": remarks

    }

    try:

        response = requests.post(

            WEB_APP_URL,

            json=payload,

            timeout=30

        )

        return response.json()

    except Exception as e:

        return {

            "success": False,

            "message": str(e)

        }
        def load_reviews():

    try:

        response = requests.get(
            WEB_APP_URL,
            timeout=30
        )

        return response.json()

    except Exception:

        return []
