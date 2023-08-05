# Commit hook (github) <img src="rope.png" alt="Logo" height="35" align="top" />

#### Reproduce Commit webhook from github.

[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

## Motivation

Github webhook are super awesome! But are not available to everyone since only the owner of the repo can create webhook. Sometimes it's very frustrating because you would like to do action in response to an other action concerning a repo that you don't own.
That's why I created this little package.  
It checks if a new commit has been pushed, then hit a webhook.

## Install

> Python 3.6 or higher is required

`pip install ...`

## Usage

The ideal is to create a crontab of your choice that execute this script.  
For example, a crontab that check everyday if a new commit has been pushed to a repo, then react in consequence.

#### Cli usage

`lcommit [usernameGithub] [repoName] [urlToHit] [locationConfig]`

## License

MIT Paul Rosset
