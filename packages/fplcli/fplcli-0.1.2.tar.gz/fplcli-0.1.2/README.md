[![Build Status](https://travis-ci.org/janerikcarlsen/fpl-cli.svg?branch=master)](https://travis-ci.org/janerikcarlsen/fpl-cli)
[![Python Versions](https://img.shields.io/pypi/pyversions/fplcli.svg)](https://pypi.org/project/fplcli)

# fpl-cli
FPL CLI is a command line tool for Fantasy Premier League, written in Python. 
The tools integrates with Fantasy Premier League API, and provides the following features directly to your terminal window: 
```
fpl                     (Get the help menu)
fpl configure           (Input your team_id as found in the URL of your points status on fantasy.premierleague.com)
fpl points              (Get the live points for your team, player and team scores are updated live)
fpl leagues             (Get the leagues you participate in)
fpl league <id>         (Get league information about a league by league_id)
fpl liveleague <id>     (Get live updated league information about a league by league_id)
fpl entry               (Get your team/user information)
fpl players             (Get information about all players that are available for selection)
```

# Installing 
FPL CLI has been tested with Python versions 2.7, 3.4, 3.5, 3.6 and 3.7.
In a terminal window where Python is installed (Verify Python version with `python --version`): 
```
pip install fplcli
```
then proceed to use FPL CLI starting with 
```
fpl configure
```


