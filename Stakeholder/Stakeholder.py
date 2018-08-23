# This Python file uses the following encoding: utf-8
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ledger.transaction import *
from chaincode.chainToJson import *

class Stakeholder:
    def __init__(self,  *args, **kwargs):
        return