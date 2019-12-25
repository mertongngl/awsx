# `awsx` for switching awscli creds


**`awsx`** helps you switch between aws credentials:

![awsx demo GIF](img/awsx.gif)

## Requirements

- You should have `awscli`

## Installation

### `Linux` & `macOS`

Command:

    sudo cp awsx /bin/awsx
    sudo chmod +x /bin/awsx

## Notes

- `--list`/`-l` : Listing your credentials

    ![awsx demo GIF](img/awsx_print.gif)

- `--help`/`-h` : Showing help menu

    ![awsx demo GIF](img/awsx_help.gif)

- `--add`/`-a` : Copying your .aws/* files to .aws.configs/ directory with given name.

    ![awsx demo GIF](img/awsx_add.gif)

- `--remove`/`-r` : Removing your credentials from .aws.configs/ directory

    ![awsx demo GIF](img/awsx_remove.gif)


