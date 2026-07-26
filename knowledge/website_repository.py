from utils.json_manager import load_json

DATABASE = "database/websites.json"


def get_all_websites():

    return load_json(DATABASE)


def find_website(name):

    websites = get_all_websites()

    name = name.lower()

    for website in websites:

        if name == website["name"].lower():

            return website

    return None