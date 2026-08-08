import os
import shutil
import subprocess


class AppController:

    def __init__(self):

        self.apps = {

            "chrome": [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            ],

            "google chrome": [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            ],

            "edge": [
                r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
                r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            ],

            "microsoft edge": [
                r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
                r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            ],

            "notepad": [
                "notepad.exe",
            ],

            "calculator": [
                "calc.exe",
            ],

            "paint": [
                "mspaint.exe",
            ],

            "explorer": [
                "explorer.exe",
            ],

            "file explorer": [
                "explorer.exe",
            ],

            "cmd": [
                "cmd.exe",
            ],

            "command prompt": [
                "cmd.exe",
            ],

            "powershell": [
                "powershell.exe",
            ],
        }

        self.commands = {
            "vscode": "code.cmd",
            "visual studio code": "code.cmd",
        }

    def _find_application(self, app):

        app = str(app).lower().strip()

        # Direct configured application
        for path in self.apps.get(app, []):

            path = os.path.expandvars(path)

            if os.path.isfile(path):

                return path

            # Windows commands such as notepad.exe
            if shutil.which(path):

                return path

        # Command-line applications
        command = self.commands.get(app)

        if command:

            found = shutil.which(command)

            if found:

                return found

        # PATH fallback
        found = shutil.which(app)

        if found:

            return found

        return None

    def open(self, app):

        # Handle VEXA entity dictionary
        if isinstance(app, dict):

            name = app.get("name", "")
            shortcut = app.get("shortcut", "")

            # First try the application name
            app = name

            # If name isn't recognized, use shortcut
            if shortcut and not self._find_application(app):

                if os.path.isfile(shortcut):

                    app = shortcut

        if not app:

            print(
                "[Automation] No application specified"
            )

            return False

        app = str(app).strip()

        path = self._find_application(app)

        # Shortcut fallback
        if not path and os.path.isfile(app):

            path = app

        if not path:

            print(
                f"[Automation] Application not found : {app}"
            )

            return False

        try:

            # .lnk shortcut
            if str(path).lower().endswith(".lnk"):

                os.startfile(path)

            else:

                subprocess.Popen(
                    [path],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
                )

            print(
                f"[Automation] Opened : {app}"
            )

            return True

        except Exception as error:

            print(
                f"[Automation] Failed to open {app} : {error}"
            )

            return False