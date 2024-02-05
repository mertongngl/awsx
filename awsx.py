#!/usr/bin/python3
import argparse
import os
import subprocess
import json
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

## this is for parsing args and parameters
parser = argparse.ArgumentParser()

home_dir = os.getenv('HOME')
## this dir is for credentials
base_dir = home_dir + "/.aws.configs"

credentials_template = """[default]
aws_access_key_id = {} 
aws_secret_access_key = {}
"""

config_template = """[default]
region = {}
"""

mfa_arn_template = "{}"

credentials_template_with_mfa = """[default]
aws_access_key_id = {} 
aws_secret_access_key = {}
aws_session_token = {}
"""

def create_basedir():
    stderr_mkdir = os.system(
        "mkdir -p {}".format(base_dir)
        )
    stderr_touch = os.system(
        "touch {}/.curr_creds".format(base_dir)
        )
    if(stderr_mkdir != 0 or stderr_touch != 0):
        return "Base directory could not create"
    return "Base directory created"

def change_creds(selected_creds):
    if not (os.path.exists("{}/{}".format(base_dir, selected_creds))):
        return "There is no '{}' credentials".format(selected_creds)
    stderr_1 = os.system(
        "cp {}/{}/config {}/.aws/".format(
            base_dir,
            selected_creds,
            home_dir
            )
        )
    stderr_2 = os.system(
        "cp {}/{}/credentials {}/.aws/".format(
            base_dir,
            selected_creds,
            home_dir
            )
        )
    if(stderr_1 != 0 or stderr_2 != 0):
        return "Cannot change credentials"
    set_current_item(selected_creds)
    return "Credentials changed to '{}'".format(selected_creds)

def get_creds():
    creds_list = list()
    curr_item = get_current_item()
    list_dirs = os.listdir(base_dir)
    list_dirs.remove(".curr_creds")
    for i in list_dirs:
        if i == curr_item:
            creds_list.append(bcolors.HEADER + bcolors.BOLD + bcolors.WARNING + "* {}".format(i) + bcolors.ENDC)
            continue
        creds_list.append("  {}".format(i))
    return "\n".join(creds_list)

def set_current_item(curr_item):
    with open("{}/.curr_creds".format(base_dir), 'w') as f:
        f.write(curr_item)

def get_current_item():
    with open("{}/.curr_creds".format(base_dir), 'r') as f:
        curr_item = f.readline().replace('\n','')
    return curr_item

def get_current_mfa_arn(creds_name):
    if not (os.path.exists("{}/{}/.mfa_arn".format(base_dir,creds_name))):
        return None
    with open("{}/{}/.mfa_arn".format(base_dir,creds_name), 'r') as f:
        curr_mfa_arn = f.readline().replace('\n','')
    return curr_mfa_arn

def remove_selected_item(selected_creds):
    if not (os.path.exists("{}/{}".format(base_dir, selected_creds))):
        return "There is no '{}' credentials".format(selected_creds)
    stderr = os.system(
        "rm -rf {}/{}/".format(
            base_dir,
            selected_creds
            )
        )
    if(stderr != 0):
        return "Cannot remove '{}' credentials".format(selected_creds)
    return "Removed '{}' credentials successfully".format(selected_creds)

def store_item(creds_name):
    stderr_1 = os.system(
        "mkdir -p {}/{}/".format(
            base_dir,
            creds_name
            )
        )
    stderr_2 = os.system(
        "cp -r {}/.aws/* {}/{}/".format(
            home_dir,
            base_dir,
            creds_name
            )
        )
    if(stderr_1 != 0 or stderr_2 !=0):
        return "Cannot store '{}' credentials".format(creds_name)
    return "Stored '{}' credentials succesfully".format(creds_name)

def prompt_store_item(creds_name):
    stderr_1 = 0
    acc_key = str(input("Please enter your access key:"))
    acc_secret = str(input("Please enter your secret key:"))
    region = str(input("Please enter your region:"))
    mfa_arn = str(input("Please enter your MFA arn [optional]:"))
    if(acc_key != "" and acc_secret != "" and region != ""):
        new_creds = credentials_template.format(
            acc_key,
            acc_secret
        )
        new_config = config_template.format(
            region
        )
        if not (os.path.exists("{}/{}/".format(base_dir,creds_name))):
            stderr_1 = os.system(
                "mkdir -p {}/{}/".format(
                    base_dir,
                    creds_name
                )
            )
        with open("{}/{}/credentials".format(base_dir,creds_name), 'w') as credential_file:
            credential_file.write(new_creds)
        
        with open("{}/{}/config".format(base_dir,creds_name), 'w') as config_file:
            config_file.write(new_config)

        if(mfa_arn != ""):
            new_mfa_arn = mfa_arn_template.format(
                mfa_arn
            )
            with open("{}/{}/.mfa_arn".format(base_dir,creds_name), 'w') as arn_file:
                arn_file.write(new_mfa_arn)

        if(stderr_1 != 0):
            return "Cannot store '{}' credentials".format(creds_name)
        return "Stored '{}' credentials succesfully".format(creds_name)
    return "Cannot get values from prompt"

def update_mfa(mfa_code):
    stderr_1 = 0
    creds_name = get_current_item()
    mfa_arn = get_current_mfa_arn(creds_name)
    if mfa_arn is None:
        return "There is no MFA ARN"
    change_creds(creds_name)
    try:
        stdout_1 = subprocess.check_output(
            "aws sts get-session-token --serial-number {} --token-code {}".format(
                mfa_arn,
                mfa_code
            ),
            shell=True
        )
        session = json.loads(stdout_1)["Credentials"]
        new_cred = credentials_template_with_mfa.format(
            session["AccessKeyId"],
            session["SecretAccessKey"],
            session["SessionToken"]
        )
        with open("{}/.aws/credentials".format(home_dir), 'w') as credential_file:
            credential_file.write(new_cred)
        return "{}{}{} session is updated with MFA code".format(
            bcolors.OKGREEN,
            creds_name,
            bcolors.ENDC
        )
    except subprocess.CalledProcessError as e:
        return "\n"
    
def rotate_credential(creds_name):
    stderr_1 = 0
    try:
        if not (os.path.exists("{}/{}/".format(base_dir,creds_name))):
            return "Cannot find '{}' credentials".format(creds_name)
        
        username = subprocess.check_output(
            "aws iam get-user --query 'User.UserName'",
            shell=True,
            text=True
        ).strip()

        new_key = subprocess.check_output(
            "aws iam create-access-key --user-name {}".format(username),
            shell=True,
            text=True
        )
        acc_key = json.loads(new_key)["AccessKey"]["AccessKeyId"]
        acc_secret = json.loads(new_key)["AccessKey"]["SecretAccessKey"]
        
        with open("{}/{}/credentials".format(base_dir, creds_name), 'r') as credential_file:
            credentials_data = credential_file.read()
            old_key_id = re.search(r'aws_access_key_id = (.+)', credentials_data).group(1)

        new_creds = credentials_template.format(
            acc_key,
            acc_secret
        )
        with open("{}/{}/credentials".format(base_dir,creds_name), 'w') as credential_file:
            credential_file.write(new_creds)

        subprocess.run(
            "aws iam delete-access-key --access-key-id {} --user-name {}".format(old_key_id, username),
            shell=True,
            check=True
        )
        return "Credentials rotated successfully"

    except subprocess.CalledProcessError as e:
        return "Error during credentials rotation: {}".format(e)

def get_args():
    parser.add_argument(
        "-a",
        "--add",
        required=False,
        help = "add your credentials to awsx"
    )
    parser.add_argument(
        "-r",
        "--remove",
        required=False,
        help = "remove your credentials from awsx"
    )
    parser.add_argument(
        "-l",
        "--list",
        required=False,
        action="store_true",
        help = "list your credentials from awsx"
    )
    parser.add_argument(
        "change",
        nargs="?",
        help = "Example: awsx foo , awsx bar"
    )
    parser.add_argument(
        "-p",
        "--add-prompt",
        required = False,
        help = "you can create creds from prompt"
    )
    parser.add_argument(
        "-mfa",
        "--update-mfa",
        required = False,
        help = "update your mfa session"
    )
    parser.add_argument(
        "-c",
        "--rotate-credential",
        required = False,
        help = "rotate your credentials (create new and remove previous) Example: awsx -c foo -mfa 123456"
    )
    return parser.parse_args()

def parse_options(arguments):
    if(arguments.list):
        return get_creds()
    elif(arguments.remove):
        return remove_selected_item(arguments.remove)
    elif(arguments.add):
        return store_item(arguments.add)
    elif(arguments.add_prompt):
        return prompt_store_item(arguments.add_prompt)
    elif(arguments.change):
        if(arguments.update_mfa):
            change_creds(arguments.change)
            return update_mfa(arguments.update_mfa)
        else:
            return change_creds(arguments.change)
    elif(arguments.rotate_credential):
        change_creds(arguments.rotate_credential)
        if(arguments.update_mfa):
            update_mfa(arguments.update_mfa)
        return rotate_credential(arguments.rotate_credential)
    elif(arguments.update_mfa):
        return update_mfa(arguments.update_mfa)
    else:
        return get_creds()
def main():
    if not (os.path.exists("{}/.aws".format(home_dir))):
        os.system("mkdir -p {}/.aws".format(home_dir))
    if not (os.path.exists(base_dir)):
        create_basedir()
    parsed_option = parse_options(get_args())
    if len(parsed_option) == 0:
        parser.print_help()
    else:
        print(parsed_option)

if __name__ == "__main__":
    main()