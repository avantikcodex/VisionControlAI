import webbrowser


class BrowserController:

    def open(self, website):

        if isinstance(website, dict):
            website = website.get("url", "")

        if not website:
            print("[Automation] No website specified")
            return False

        website = str(website).strip()

        if not website:
            print("[Automation] No website specified")
            return False

        if not website.startswith(("http://", "https://")):
            website = "https://" + website

        try:

            opened = webbrowser.open_new_tab(website)

            if opened:

                print(
                    f"[Automation] Opened Website : {website}"
                )

                return True

            print(
                f"[Automation] Browser could not open : {website}"
            )

            return False

        except Exception as error:

            print(
                f"[Automation] Failed to open website : {error}"
            )

            return False