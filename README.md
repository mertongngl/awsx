# `awsx` for switching awscli creds  `BETA`


**`awsx`** helps you switch between aws credentials:


## Requirements

- You should have `awscli`

## Installation

### `Linux`

#### `Info: ` If you are using python3 on your PC, please use the `awsx-py3` script file.

Python3.x:

    sudo cp awsx-py3 /bin/awsx
    sudo chmod +x /bin/awsx    

Python2.x:

    sudo cp awsx /bin/awsx
    sudo chmod +x /bin/awsx

### `macOS`

Python3.x:

    sudo cp awsx-py3 /usr/local/bin/awsx
    sudo chmod +x /usr/local/bin/awsx

Python2.x:

    sudo cp awsx /usr/local/bin/awsx
    sudo chmod +x /usr/local/bin/awsx

## Notes

- `--list`/`-l` : Listing your credentials

    ```zsh
    ❯ awsx
      aws01
      aws04
    * aws02
    ```
    or
    ```zsh
    ❯ awsx -l
      aws01
      aws03
    * aws02
    ```


- `--help`/`-h` : Showing help menu

    ```zsh
    ❯ awsx --help
    usage: awsx [-h] [-a ADD] [-r REMOVE] [-l] [-p ADD_PROMPT] [-mfa UPDATE_MFA]
                [change]

    positional arguments:
    change                Example: awsx foo , awsx bar

    optional arguments:
    -h, --help            show this help message and exit
    -a ADD, --add ADD     add your credentials to awsx
    -r REMOVE, --remove REMOVE
                            remove your credentials from awsx
    -l, --list            list your credentials from awsx
    -p ADD_PROMPT, --add-prompt ADD_PROMPT
                            you can create creds from prompt
    -mfa UPDATE_MFA, --update-mfa UPDATE_MFA
                            update your mfa session

    ```

- `--add`/`-a` : Copying your .aws/* files to .aws.configs/ directory with given name.

    ```zsh
    ❯ awsx -a aws04
    Stored 'aws04' credentials succesfully
    ```

- `--add-prompt`/`-p` : Creating credentials files from prompt.

    ```zsh
    ❯ awsx -p aws01
    Please enter your access key:<YOUR_ACCESS_KEY_ID>
    Please enter your secret key:<YOUR_SECRET_KEY>
    Please enter your region:<YOUR_REGION>
    Please enter your MFA arn [optional]:<YOUR_VIRTUAL_MFA_DEVICE_ARN>
    Stored 'aws01' credentials succesfully

    ```

- `change`: Change current credentials

    ```zsh
    ❯ awsx aws02
    Credentials changed to 'aws02'
    ```

- `-mfa` : Get credentials from a new session with MFA

    ```zsh
    ❯ awsx -mfa 019542
    aws05 session is updated with MFA code
    ```

- `--remove`/`-r` : Removing your credentials from .aws.configs/ directory

    ```zsh
    ❯ awsx -r aws03
    Removed 'aws03' credentials successfully
    ```


