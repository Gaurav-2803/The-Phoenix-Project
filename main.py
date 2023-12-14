# Inbuilt Imports
import os
import socket
import subprocess
import time
from datetime import datetime as d

# Third Party Imports
import requests

# User Imports
from lib.script_files import NETWORK_EXCEPTION, REQUEST_EXCEPTION, SYSTEM_EXCEPTION


class ScriptInvoke:
    # Fetching URL
    def __init__(self):
        self.ip_address = socket.gethostbyname(socket.gethostname())
        self.url = f"https://{self.ip_address}"

    # Fetching Type of Error
    @staticmethod
    def __get_response(__url: str) -> int or str:
        try:
            response = requests.get(__url).status_code
            return response
        except Exception as error:
            return type(error).__name__

    # Intialize Scripts in case of error
    def invoke_scripts(self):
        response_type = (
            "Network Error"
            if isinstance(self.__get_response(self.url), int)
            else "Request Error"
        )
        if response_type == "Request Error":
            self.__check_request_error()
        else:
            self.__check_network_error()

    # Intialize scripts to fix 'Request' errors
    def __check_request_error(self):
        self.error_name = self.__get_response(self.url)

        if self.error_name in REQUEST_EXCEPTION:
            self.bash_file = REQUEST_EXCEPTION.get(self.error_name)
            subprocess.run(
                [
                    "sh",
                    f"lib\\scripts\\request\\{self.bash_file}",
                ]
            )
        else:
            raise NotImplementedError(f"No script for {self.error_name}")

    # Intialize scripts to fix 'Network' errors
    def __check_network_error(self):
        self.error_name = self.__get_response(self.url)

        accepted_code = {200, 201, 202}
        if self.error_name in accepted_code:
            while True:
                if self.__check_system_error():
                    print("System Error")
                else:
                    print("Running OK")
                time.sleep(10)

        elif self.error_name in NETWORK_EXCEPTION:
            self.bash_file = NETWORK_EXCEPTION.get(self.error_name)
            subprocess.run(
                [
                    "sh",
                    f"lib\\scripts\\network\\{self.bash_file}\\{self.bash_file}",
                ]
            )
        else:
            raise NotImplementedError(f"No script for {self.error_name}")

    @staticmethod
    def __check_system_error():
        os.chdir("../../../var/log")
        log_file = open("syslog", "r")
        logs = log_file.readlines()
        filterd_logs = []

        for log in logs[::-1]:
            line = log.split(" ")[:6]

            # Check Time
            now = d.utcnow()
            start_time = d.strptime(" ".join(line[:3]), "%b %d %H:%M:%S")
            end_time = now.strftime("%b %d %H:%M:%S")
            end_time = d.strptime(end_time, "%b %d %H:%M:%S")
            time_diff = abs((end_time - start_time).total_seconds())

            log_title, error = line[4:6]

            if time_diff <= 30:
                if "systemd" in log_title and error in SYSTEM_EXCEPTION:
                    filterd_logs.append(log)
            else:
                break

        return not filterd_logs


if __name__ == "__main__":
    script = ScriptInvoke()
    script.invoke_scripts()
