*****
Gitlo
*****
A Command Line Interface made in Python. It's a simple tool that helps you to access Github API.
I used Python library ``Click`` to make this application.

Quick Start
########
Install Package::

    pip install gitlo

Examples
########

Get user info
**************
Use the ``gitlo user <username>`` command to get information of user.::

    $ gitlo user siddharthshringi
    Name: Siddharth Shringi, Repos: 16, Bio: Python Developer | ML Enthusiast

Get repository list of user
******************
Use the ``gitlo user <username>`` command to get information of user.::

    $ gitlo repos siddharthshringi
    blacksamsung.github.io
    create-your-own-adventure
    data
    diary_of_programming_puzzles
    django-rest-framework
    Gitlo
    hello-world
    hello_world
    markdown-here
    my-first-blog
    my-first-contact-app
    recipes
    reflections
    siddharthshringi.github.io
    Song-App
    ThinkStats2

Get language percentage of each repository
******************
Use the ``gitlo languages <username> <reponame>`` command to get language information in repository.::

    $ gitlo languages siddharthshringi Song-App
    Python: 59.84%
    HTML: 32.96%
    CSS: 7.2%

License
******************
MIT licensed. See the bundled `LICENSE <https://github.com/SiddharthShringi/Gitlo/blob/master/LICENSE>`_ file for more details.