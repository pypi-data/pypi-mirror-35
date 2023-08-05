# -*- coding: utf-8 -*-
"""Various methods for getting users
"""

from _shared import _get_users, _api_call

def get(id=None, email=None, **kwargs):
    """Looks up a user by his/her email. 
    TODO: Add more parameters? 
    """
    ### If the ID is specified, get that user directly
    if id:
        return _api_call('users.info', user=id).get('user')
    
    ### Else, loop trough all users and get the right one
    if email:
        match = email
        field_match = 'email'
    
    for user in get_users(kwargs):
        if user.get('profile', {}).get(field_match) == match:
            return user
    
    ### Return an empty user if not found
    return {}
