import socket

import requests

import scripts


class ScriptInvoke:
    def __init__(self):
        # self.ip_address = socket.gethostbyname(socket.gethostname())
        # self.url = f"https://{self.ip_address}"
        self.url = "http://52.66.204.129:8000"
        # self.url = "http://3.7.252.171:80"

    @staticmethod
    def __get_response(__url):
        try:
            response = requests.get(__url).status_code
            return response
        except Exception as error:
            return type(error).__name__

    def invoke_scripts(self):
        response_type = (
            "Network Error"
            if isinstance(self.__get_response(self.url), int)
            else "Server Error"
        )
        if response_type == "Server Error":
            self.fix_server_error()
        else:
            self.fix_network_error()

    def fix_server_error(self):
        print("Fixing Server Errors")

    def fix_network_error(self):
        print("Fixing Network Errors")


if __name__ == "__main__":
    si = ScriptInvoke()
    si.invoke_scripts()

# # import subprocess as sp

# # def mainBot():
# #     running = True
# #     while running:
# #         try:
# #             sp.


# import requests

# try:
#     response = requests.get("http://52.66.204.129:8080").status_code
#     print("YES", response)

# except requests.exceptions.ConnectTimeout as x:
#     print("Error: ", x)

# # print(requests.exceptions.RequestException)


# import psutil


# def getRemoteSystemStatus():
#     """Checks the system status of a remote machine.

#     Args:
#       host: The hostname or IP address of the remote machine.

#     Returns:
#       A dictionary containing the CPU usage, memory usage, and disk usage of the remote machine.
#     """

#     # Create a connection to the remote machine.
#     with psutil.Process() as pro:
#         pro.connect("http://3.7.252.171:80")

#         # Get the CPU usage, memory usage, and disk usage of the remote machine.
#         cpu_usage = pro.cpu_percent()
#         memory_usage = pro.memory_percent()
#         disk_usage = pro.disk_usage("/").percent

#     return {
#         "cpu_usage": cpu_usage,
#         "memory_usage": memory_usage,
#         "disk_usage": disk_usage,
#     }


# if __name__ == "__main__":
#     host = "http://3.7.252.171:80"

#     system_status = getRemoteSystemStatus()

#     print("CPU usage:", system_status["cpu_usage"])
#     print("Memory usage:", system_status["memory_usage"])
#     print("Disk usage:", system_status["disk_usage"])
