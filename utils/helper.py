from datetime import datetime


def today():

    return datetime.today().strftime("%d-%m-%Y")


def current_time():

    return datetime.now().strftime("%I:%M %p")


def greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "Good Morning"

    elif hour < 17:
        return "Good Afternoon"

    return "Good Evening"
