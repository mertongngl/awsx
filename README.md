# `awsx` for switching awscli creds  `BETA`


**`awsx`** helps you switch between aws credentials:

![awsx demo GIF](img/awsx.gif)

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

    ![awsx demo GIF](img/awsx_print.gif)

- `--help`/`-h` : Showing help menu

    ![awsx demo GIF](img/awsx_help.gif)

- `--add`/`-a` : Copying your .aws/* files to .aws.configs/ directory with given name.

    ![awsx demo GIF](img/awsx_add.gif)

- `--add-prompt`/`-p` : Creating credentials files from prompt.

    ![awsx demo GIF](img/awsx_prompt.gif)

- `--remove`/`-r` : Removing your credentials from .aws.configs/ directory

    ![awsx demo GIF](img/awsx_remove.gif)


