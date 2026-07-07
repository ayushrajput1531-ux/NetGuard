import socket
import platform
import getpass


def get_hostname():
    return socket.gethostname()


def get_os():
    return platform.system()


def get_os_version():
    return platform.version()


def get_architecture():
    return platform.machine()


def get_username():
    return getpass.getuser()