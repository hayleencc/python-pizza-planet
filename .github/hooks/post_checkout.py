#!/usr/bin/env python3
import sys
import subprocess
import re

regex_piz_branch = "^(PIZ)-([0-9]+)-(\w+(?:-[a-zA-Z0-9]+)*)$"


def is_main_branch(branch_name):
    return branch_name == "main"


def is_valid_branch_name(branch_name):
    return bool(re.match(regex_piz_branch, branch_name))


def main():

    branch_name = str(
        subprocess.run(
            "git rev-parse --abbrev-ref HEAD", shell=True, check=True, stdout=subprocess.PIPE
        ).stdout
    )[2:-3]

    if is_main_branch(branch_name):
        print("You are not allowed to push to main. Please create a new branch and push your changes there.")
        return sys.exit(1)

    if is_valid_branch_name(branch_name):
        return sys.exit(0)
    else:
        print(f'''\n
        Error message:
            The following name is not allowed: {branch_name}
            Please rename your branch with using the following regex: 
            {regex_piz_branch} 
            or  PIZ-<number_ticket>-<title_ticket> 
            You won't be able to push or commit your changes until the issue is solved.
            ''')
    return sys.exit(1)


if __name__ == "__main__":
    main()
