<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">AWSX</h3>

  <p align="center">
    A powerful command-line tool for quickly and easily switching between AWS credentials.
    <br />
  </p>
</div>


## About The Project

`awsx-cli` is a command-line tool that helps you switch quickly and easily between Amazon Web Services (AWS) credentials. This tool is designed to streamline your tasks when you need to use multiple AWS credentials. You can use it to manage your AWS credentials, switch between them, and update Multi-Factor Authentication (MFA) sessions.

Key Features:

Manage and store your AWS credentials
Switch between different AWS credentials
Update Multi-Factor Authentication (MFA) sessions
Easy and fast to use




<!-- GETTING STARTED -->
## Getting Started

### Step 1: Installation

You can install awsx-cli using pip. If you don't have pip installed, you can follow the instructions here to install it.

   ```sh
   pip install awsx-cli
   ```

### Step 2: Basic Usage

Once awsx-cli is installed, you can start using it to manage your AWS credentials. Here are some basic commands to get you started:

* To list your stored credentials:

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

* To switch to a different set of credentials:

    ```zsh
    ❯ awsx aws02
    Credentials changed to 'aws02'
    ```

* To add new credentials:

    ```zsh
    ❯ awsx -a aws04
    Stored 'aws04' credentials succesfully
    ```
    or with the MFA ARN: 
    ```zsh
    ❯ awsx -a aws04 -m arn:aws:iam::123456789012:mfa/some-mfa-device
    Stored 'aws04' credentials succesfully
    ```

* To both switch to a different set of credentials and update the MFA session:

    ```zsh
    ❯ awsx aws02 -mfa your-mfa-code
    aws02 session is updated with MFA code
    ```

* To update an MFA session:

    ```zsh
    ❯ awsx -mfa your-mfa-code
    aws05 session is updated with MFA code
    ```
* To remove credentials:
 
     ```zsh
    ❯ awsx -r aws03
    Removed 'aws03' credentials successfully
    ```
* To rotate credentials:
 
     ```zsh
    ❯ awsx -c foo -mfa 123456
    Credentials rotated successfully
    ```
* To get help:

     ```zsh
    ❯ awsx --help
    usage: awsx [-h] [-a ADD] [-r REMOVE] [-l] [-p ADD_PROMPT] [-mfa UPDATE_MFA] [-c ROTATE_CREDENTIAL] [-m MFA_ARN] [change]

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
      -c ROTATE_CREDENTIAL, --rotate-credential ROTATE_CREDENTIAL
                            rotate your credentials (create new and remove previous) Example: awsx -c foo -mfa 123456
      -m MFA_ARN, --mfa-arn MFA_ARN
                            add your MFA ARN along with the credentials to awsx
    ```


## Now you're ready to start using awsx-cli to manage your AWS credentials efficiently!


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the APACHE-2.0 License. See `LICENSE.txt` for more information.


[contributors-shield]: https://img.shields.io/github/contributors/mertongngl/awsx?style=for-the-badge
[contributors-url]: https://github.com/mertongngl/awsx/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mertongngl/awsx?style=for-the-badge
[forks-url]: https://github.com/mertongngl/awsx/network/members
[stars-shield]: https://img.shields.io/github/stars/mertongngl/awsx?style=for-the-badge
[stars-url]: https://github.com/mertongngl/awsx/stargazers
[issues-shield]: https://img.shields.io/github/issues/mertongngl/awsx?style=for-the-badge
[issues-url]: https://github.com/mertongngl/awsx/issues
[license-shield]: https://img.shields.io/github/license/mertongngl/awsx?style=for-the-badge
[license-url]: https://github.com/mertongngl/awsx/blob/master/LICENSE.txt