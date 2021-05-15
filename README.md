# AutoMeet
AutoMeet is a python script which joins and leaves Teams meetings automatically. Supports Microsoft 365 accounts [for now](https://github.com/chinsingh/AutoMeet/issues/4). 

## Installation

Installation for the script is not required. Although, there are some prerequisites.

#### Prerequisites
* You need to have [python](https://www.python.org/downloads/) on your system.
* Also, only [Google Chrome](https://www.google.com/intl/en_in/chrome/) browser is supported [for now](https://github.com/chinsingh/AutoMeet/issues/2).

Once you have both of these, go to the **Code** button on top-right area of this repo, download the zip and extract it. [![Code Button Image](https://docs.github.com/assets/images/help/repository/code-button.png =50%x50%)](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) You can also clone it if you are that kind of person.


After you have this repository on your system, follow the initial configuration steps listed below.

#### Intial Steps
1. Run the following command on your terminal or command prompt.
   ```bash
    pip install -r requirements.txt
   ```
   This will install the [required dependencies](https://github.com/chinsingh/AutoMeet/blob/master/requirements.txt) on your system.

2. Now, go to the [settings.json](https://github.com/chinsingh/AutoMeet/blob/master/settings.json) file in wherever you have kept the AutoMeet folder and enter your username, minimum number of participants allowed etc.

You are now ready to use AutoMeet.

*Tip: You can create copies of the folder with different settings in each of them (for example, different minimum number of participants for different meetings) and run them depending on whichever meeting you have coming up.*

## Usage

Run [automeet.py](https://github.com/chinsingh/AutoMeet/blob/master/automeet.py)
```bash
python automeet.py
```
:warning: You need to either **enter the full path** for automeet.py (wherever you've kept it) or **go to that directory** and execute the command.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

You can also [report a bug, request a feature](https://github.com/chinsingh/AutoMeet/issues/new/choose) or [email me](mailto:mr.chinmaysingh.gmail.com).


## License
[MIT](https://github.com/chinsingh/AutoMeet/blob/master/LICENSE.md)
