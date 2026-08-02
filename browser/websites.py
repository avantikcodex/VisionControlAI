import webbrowser

from utils.json_manager import load_json
from brain.fuzzy_match import fuzzy_search

DATABASE = "database/websites.json"


def search_website(command):

    websites = load_json(DATABASE)

    names = [site["name"] for site in websites]

    match = fuzzy_search(command, names)

    if match is None:
        return None

    for site in websites:

        if site["name"] == match:

            return site

    return None


def open_website(website):

    if website is None:

        print("Website not found.")

        return False

    print("Opening:", website["url"])

    webbrowser.open(website["url"])

    return True