#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from Rules import Rules
from UpRule import UpRule
from DownRule import DownRule
from RedBlackRule import RedBlackRule
from SameColorRule import SameColorRule
from SameSuitRule import SameSuitRule

""" Constructors for the default rules. """

""" Up rules """

def RedBlackUpRules():
    return Rules([UpRule(), RedBlackRule()])

def SameColorUpRules():
    return Rules([UpRule(), SameColorRule()])

def SameSuitUpRules():
    return Rules([UpRule(), SameSuitRule()])

""" Down rules """

def RedBlackDownRules():
    return Rules([DownRule(), RedBlackRule()])

def SameColorDownRules():
    return Rules([DownRule(), SameColorRule()])

def SameSuitDownRules():
    return Rules([DownRule(), SameSuitRule()])
