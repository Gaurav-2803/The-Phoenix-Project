# Inbuilt Imports
import socket
import subprocess

# Third Party Imports
import requests

# User Imports
from lib.script_files import NETWORK_EXCEPTION, REQUEST_EXCEPTION


class ScriptInvoke:
    # Fetching URL
    def __init__(self):
        self.ip_address = socket.gethostbyname(socket.gethostname())
        self.url = f"https://{self.ip_address}"

        # Testing IPs
        # Arslaan
        # self.url = "http://52.66.204.129:8000"
        # Gaurav
        # self.url = "http://3.7.252.171:80"

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
                    f"scripts\\request\\{self.bash_file}",
                ]
            )
        else:
            raise NotImplementedError(f"No script for {self.error_name}")

    # Intialize scripts to fix 'Network' errors
    def __check_network_error(self):
        self.error_name = self.__get_response(self.url)

        accepted_code = {200, 201, 202}
        if self.error_name in accepted_code:
            return "Running OK"

        elif self.error_name in NETWORK_EXCEPTION:
            self.bash_file = NETWORK_EXCEPTION.get(self.error_name)
            subprocess.run(
                [
                    "sh",
                    f"scripts\\network\\{self.bash_file}\\{self.bash_file}",
                ]
            )
        else:
            raise NotImplementedError(f"No script for {self.error_name}")


if __name__ == "__main__":
    script = ScriptInvoke()
    script.invoke_scripts()
