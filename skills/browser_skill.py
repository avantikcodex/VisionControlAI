from browser.websites import search_website
from browser.browser_engine import open_url


class BrowserSkill:

    name = "BROWSER"

    def execute(self, command):

        website = search_website(command)

        if website is None:

            return False

        open_url(website["url"])

        return True