# -*- coding: utf-8 -*-
"""Various methods for getting conversations
"""

from ._shared import _get_conversations, _api_call

def get(id=None, name=None, name_normalized=None, **kwargs):
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
