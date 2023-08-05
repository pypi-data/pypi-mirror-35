# -*- coding: utf-8 -*-
"""Shared functions for slackutils, only to be used internally.
"""

import os
import slackclient

def _api_call(method, **kwargs):
    """Function for creating the slack client and doing the actual API call"""
    if 'SLACK_API_TOKEN' in kwargs:
        token = kwargs.get('SLACK_API_TOKEN')
    else:
        token = os.environ.get('SLACK_API_TOKEN')

    sc = slackclient.SlackClient(token)
    return sc.api_calls

def _get_conversations(**kwargs):
    """Returns all conversations the user has access to."""
    return _api_call('conversations.list', types='public_channel,private_channel,mpim,im', kwargs).get('channels')

def _get_users(**kwargs):
    """Returns all users in the slack team"""
    return _api_call('users.list', kwargs).get('members')