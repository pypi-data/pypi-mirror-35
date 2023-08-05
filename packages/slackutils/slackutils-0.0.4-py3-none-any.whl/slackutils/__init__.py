# -*- coding: utf-8 -*-
from ._shared import _get_conversations, _get_users, _api_call

def get_conversation(id=None, name=None, name_normalized=None, **kwargs):
    """Fetches a conversation (and just one) based on other parameters than the ID.
    The most useful is probably looking up a channel by its name.
    """
    ### If the ID is supplied, use that to look up the channel directly
    if id:
        return _api_call('conversations.info', channel=id, **kwargs)
    
    ### If any of the other parameters are specified, get the list of all channels and look for a match
    if name:
        match = name
        field_match = 'name'
    elif name_normalized:
        match = name_normalized
        field_match = 'name_normalized'

    conversations = _get_conversations(**kwargs)
    for conversation in conversations:
        if conversation.get(field_match) == match:
            return conversation
    
    ### If no conversation is returned by now, return an empty channel
    return {}


def get_user(id=None, email=None, **kwargs):
    """Looks up a user by his/her email. 
    TODO: Add more parameters? 
    """
    ### If the ID is specified, get that user directly
    if id:
        return _api_call('users.info', user=id, **kwargs).get('user')
    
    ### Else, loop trough all users and get the right one
    if email:
        match = email
        field_match = 'email'
    
    for user in _get_users(**kwargs):
        if user.get('profile', {}).get(field_match) == match:
            return user
    
    ### Return an empty user if not found
    return {}

