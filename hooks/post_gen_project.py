import os
import sys


def check_cookie_renders():

    if "{{cookiecutter.open_source_license}}" == "No license file":
        os.unlink("LICENSE")


check_cookie_renders()
