# This file is auto-generated from weight.idl(1.0.9-6-gd5557e3) with jenerator version 1.0.7-6-g1ae743a/develop
# *** DO NOT EDIT ***


import msgpackrpc
import jubatus.common
from .types import *
from jubatus.common.types import *

class Weight(jubatus.common.ClientBase):
  def __init__(self, host, port, name, timeout=10):
    super(Weight, self).__init__(host, port, name, timeout)

  def update(self, d):
    return self.jubatus_client.call("update", [d], TList(TUserDef(Feature)),
        [TDatum()])

  def calc_weight(self, d):
    return self.jubatus_client.call("calc_weight", [d], TList(TUserDef(
        Feature)), [TDatum()])

  def clear(self):
    return self.jubatus_client.call("clear", [], TBool(), [])
