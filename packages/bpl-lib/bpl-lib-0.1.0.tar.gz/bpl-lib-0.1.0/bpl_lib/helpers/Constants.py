from enum import IntEnum
import os

from bpl_lib import ROOT

INTERVAL = 15

NETWORKS_DB = os.path.join(ROOT, "network\\networks.db")

class TRANSACTION_TYPE(IntEnum):
    TRANSFER = 0
    SECOND_SIGNATURE = 1
    DELEGATE = 2
    VOTE = 3
    MULTI_SIGNATURE = 4
    IPFS = 5


TRANSACTION_FEES = {
    0: 10000000,
    1: 500000000,
    2: 1000000000,
    3: 100000000,
    4: 500000000,
    5: 10000000
}
