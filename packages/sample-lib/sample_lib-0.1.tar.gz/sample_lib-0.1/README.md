## Setup

* Add setup.py
    * Make sure you have a remote origin for the repo since a url is needed in this file
    * Now you are able to install your library and use it anywhere in your local PC using
        * `pip install .`
        * `pip install -e .`
            * This command is preferred since changes to the source files will be immediately available to other users of the package on our system
            * Take care that now it is recommended to add "*.egg-info" to your .gitignore file
* Publishing on PyPi
    * Add a license file
    * `python setup.py register`
        * Login using your username and password. My username is "youssef_sherif"