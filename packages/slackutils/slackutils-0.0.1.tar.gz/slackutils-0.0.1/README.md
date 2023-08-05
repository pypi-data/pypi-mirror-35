# Introduction

**NOTE**: This is an alpha version. Expect everything to change.

**slackutils** is a small library for simplifying some tasks with the [Slack Web API](https://api.slack.com/web). It is an extension of [slackclient](https://pypi.org/project/slackclient/), and mostly contains methods for looking up users or channels by other parameters than their ID.

# Installation

Recommended method is to install using pip:

`pip install --upgrade slackutils`


# Usage

## Authenication

You need a slack token to use this library.  **slackutils** looks for the token using one of two alternatives: 

1. All methods support a named parameter `SLACK_API_TOKEN` which is used to authenticate.
2. If no named parameter is found, slackutils will look for the environment variable `SLACK_API_TOKEN`. 

If neither of the above variables exist, an error will be raised.


## Examples

Simplify looking up users and channels by other parameters than their ID

```
import slackutils
marketing_channel = slackutils.channels.get(name='marketing')

from slackutils import users
dave = users.get(email='dave@example.com')

```
