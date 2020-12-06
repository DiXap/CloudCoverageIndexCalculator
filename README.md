# Cloud Coverage Index Calculator
[![Generic badge](https://img.shields.io/badge/version-2.12.06-<COLOR>.svg)](https://shields.io/)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Generic badge](https://img.shields.io/badge/contributors-2-blue)](https://shields.io/)  
[![forthebadge made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  


## Table of contents
* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
* [Usage](#usage)  
    * [Night Mode](#night-mode)
    * [Tests](#tests)
* [Contributing](#contributing)
* [Contact](#contact)
* [Acknowledgements](#Acknowledgements)


# About the Project
A basic cli app which allows you to calculate the *Cloud Coverage Index* given a sky image.  
No need to worry for pre-processing the image!

# Getting Started
Since this app is all made with `Python` you're going to need some python-libraries and utilities listed below.

## Prerequisites
* First check that your current `Python` version is `Python 3.6` or above, by running the following command on your terminal:

    ```shell
    $ python --version
    ```
    > `Python 3.8+` is recommended 

    Note that in some linux distros you'll need to run it as: 
    ```shell
    $ python3 --version
    ```


* You migth as well check if you have PyPI as your Python package installer:  
  Since this process vary for every Linux distro, I'll link you to an article explanning how to set
  [PyPI](https://www.tecmint.com/install-pip-in-linux/) up.  

## Instalation
1. Clone the repo  
    ```shell
    $ git clone https://github.com/DiXap/CloudCoverageIndexCalculator.git
    ```

2. Move to project's `dir` and run the following
    ```shell
    $ pip install -r requirements.txt
    ```

3. The step above is going to automatically install packages needed for this project.  
If you want to install them manually, here's a list with the packages:
    * `opencv`
    * `click`
    * `numpy`

# Usage
Since this is a `cli` app, you're need to know the syntaxis:
```shell
$ python main.py [PATH_TO_IMAGE] [OPTIONS]
```
where:  
* `[PATH_TO_IMAGE]`, refers to the absolute path of the image you want to process
    > You can use relative paths only if the image or containing folder are inside project's `dir`
* `[OPTIONS]`, put as many flags as you wish in this section:  
    | Flags       | Description                                   |
    | ----------- |:---------------------------------------------:|
    |  `-s`       | Display processed image used to calculate CCI |
    | `--w`       | Save a copy of the processed image            |
    | `--d`       | Display original image                        |
    | `--n`       | Process a night-time image                    |

    At any given time you can pass the `--help` or `-h` to see all available flags:
    ```shell
    $ python main.py --help
    ```

For example, you can pass the following command:
```shell
$ python main.py /PATH/TO/IMAGE -s --w
```
and the program will show and write the image 
<img src="./dump/11838-seg.jpg" alt="drawing" width="500"/>  
> You can even try and pass all flags at the same time!

Regardless of your flag choices, the app will always display the CCI in your terrminal:
```
$ python python main.py /PATH/TO/IMAGE -s --d --w
    CCI for image exmaple.jpg is X.XX%
```

Images will always be dumped inside `./dump` folder, so please, don't delete it.  
You can modify this setting in `IPP.py`:
```python
def write(self, name: str, image='b&w', path='dump/'): # change path='' value
    ...
```

### Night Mode
As was mentioned before, you can get the CCI from a night-time photo, just do as it follows:  
```shell
$ python main.py /PATH/TO/IMAGE --n
```
> You can add more flags but DO NOT forget to put `--n`, otherwhise it won't work properly

## Tests

These test cases were coded to demostrate functions' error handling.  
Feel free to play around with them at `tests.py`.


# Contact
Diego J. Padilla  
[<img src="https://img.shields.io/badge/gmail-D14836?&style=for-the-badge&logo=gmail&logoColor=white"/>](https://mail.google.com/mail/?view=cm&source=mailto&to=dpadlara@gmail.com) <img src="https://img.shields.io/badge/discord-Dixap@5792-181717?style=for-the-badge&logo=discord" />

Alejandro Maldonado  
[<img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/>](https://github.com/RealMaldov)
[<img src="https://img.shields.io/badge/gmail-D14836?&style=for-the-badge&logo=gmail&logoColor=white"/>](https://mail.google.com/mail/?view=cm&source=mailto&to=amaldov@ciencias.unam.mx)


# Acknowledgements
* [DavidHdezU](https://github.com/DavidHdezU)
* [ForTheBadge](http://ForTheBadge.com) 
* [Badges 4 README.md Profile](https://github.com/alexandresanlim/Badges4-README.md-Profile)


---
![forthebadge biult-with-love](https://forthebadge.com/images/badges/built-with-love.svg) 
[![forthebadge powered-by-electricity](https://forthebadge.com/images/badges/powered-by-electricity.svg)](http://ForTheBadge.com)  

---
[Go up](#cloud-coverage-index-calculator)