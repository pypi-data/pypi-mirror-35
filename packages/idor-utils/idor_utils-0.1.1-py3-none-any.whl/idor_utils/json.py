# Fix module import in python 2.7 (json, same name of this file)
from __future__ import absolute_import

import json as p_json
import re

def load(filename):
    """Load data from a json file
    Parameters
    ----------
    filename : str
        Filename to load data from.
    Returns
    -------
    data : dict
    """
    with open(filename, 'r') as fp:
        data = p_json.load(fp)
    return data

def __json_dumps_pretty(j, indent=2, sort_keys=True):
    """Given a json structure, pretty print it by colliding numeric arrays
    into a line.
    If resultant structure differs from original -- throws exception
    """
    js = p_json.dumps(j, indent=2, sort_keys=True)
    js = js.replace(' \n', '\n')
    # trim away \n and spaces between entries of numbers
    js_ = re.sub(
        r'[\n ]+("?[-+.0-9e]+"?,?) *\n(?= *"?[-+.0-9e]+"?)', r' \1',
        js, flags=re.MULTILINE)
    # uniform no spaces before ]
    js_ = re.sub(r" *\]", "]", js_)
    # uniform spacing before numbers
    js_ = re.sub('  *("?[-+.0-9e]+"?)(?P<space> ?)[ \n]*',
                 r' \1\g<space>', js_)
    # no spaces after [
    js_ = re.sub(r'\[ ', '[', js_)
    # the load from the original dump and reload from tuned up
    # version should result in identical values since no value
    # must be changed, just formatting.
    j_just_reloaded = p_json.loads(js)
    j_tuned = p_json.loads(js_)

    assert j_just_reloaded == j_tuned, \
       "Values differed when they should have not. "\
       "Report to the heudiconv developers"

    return js_
    
def save(filename, data, indent=2):
    """Save data to a json file
    Parameters
    ----------
    filename : str
        Filename to save data in.
    data : dict
        Dictionary to save in json file.
    """
    s_data = __json_dumps_pretty( data, indent=indent, sort_keys=True)
    with open(filename, 'w') as fp:
        fp.write(s_data)