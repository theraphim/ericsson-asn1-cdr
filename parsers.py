
import datetime, struct

def Date(self, value):
  year = 0
  if len(value) == 4:
     year = ord(value[0]) * 100
     value = value[1:]
  else:
     year = 2000
  year += ord(value[0])
  month = ord(value[1])
  day = ord(value[2])

  return datetime.date(year, month, day)

def Time(self, value):
  hour = ord(value[0])
  minute = ord(value[1])
  second = ord(value[2])
  msec = 0
  if len(value) == 4:
    msec = ord(value[3]) * 100000
  return datetime.time(hour, minute, second, msec)

class _TBCDDecoder(object):
  D = {
    10: "+",
    11: "#",
    12: "a",
    13: "b",
    14: "c",
    15: ""
  }

  @classmethod
  def getchar(self, c):
    try:
      return self.D[c]
    except:
      return str(c)

  @classmethod
  def get2(self, c):
    return self.getchar(ord(c) & 15) + self.getchar(ord(c) >> 4)

  @classmethod
  def decode(self, value):
    return "".join(map(self.get2, value))

class _Attributed(dict):
  def __repr__(self):
    return "%s(%s)" % (self.__class__.__name__, ", ".join([ "%s=%s" % (k, repr(v)) for k, v in self.items() ]))
   

class _AddressString(object):
  def __init__(self, value):
    c = ord(value[0])
    self.ton = c >> 4
    self.npi = c & 15
    self.number = _TBCDDecoder.decode(value[1:])

  def __repr__(self):
    return "%s(%s, %s, '%s')" % (self.__class__.__name__, self.npi, self.ton, self.number)

class AddressString(_AddressString):
  pass

def TBCDStringD(size=None):
  if size:
    def f(self, value):
      return _TBCDDecoder.decode(value[:size])
    return f
  def f(self, value):
    return _TBCDDecoder.decode(value)
  return f

TBCDString = TBCDStringD()

IMEI = TBCDStringD(7)

class TAC(_Attributed):
  def __init__(self, value):
    self["TSC"], self["TOS"], self["TOI"] = map(ord, value[0:3])
    if len(value) == 4:
      self["TOP"] = ord(value[3])

class _IntMap(object):
  def __init__(self, value):
    self.value = _uint(self, value)

  def __repr__(self):
    return "%s(%s, '%s')" % (self.__class__.__name__, self.value, self.D[self.value])

class EosInfo(_IntMap):
  D = {
    0 : 'Free subscriber.',
    1 : 'Free subscriber. No time supervision.',
    2 : 'Free subscriber. No charging.',
    3 : 'Free subscriber. No time supervision. No charging.',
    4 : 'Free subscriber. Last party release.',
    5 : 'Free subscriber. No time supervision. Last party release.',
    6 : 'Free subscriber. No charging. Last party release.',
    7 : 'Free subscriber. No time supervision. No charging. Last party release.',
    16 : 'Set up speech condition.',
    17 : 'Set up speech condition. No time supervision.',
    18 : 'Set up speech condition. No charging.',
    33 : 'Access barred',
    34 : 'Transferred subscriber.',
    35 : 'Busy subscriber.',
    36 : 'Busy subscriber with callback protection.',
    37 : 'Unallocated number.',
    38 : 'Address incomplete.',
    39 : 'Call transfer protection, that is "follow me" not allowed to this subscriber.',
    40 : 'Subscriber line out of order.',
    41 : 'Intercepted subscriber.',
    42 : 'Supervised by an operator. Trunk offering marked.',
    43 : 'Rerouting to service centre.',
    44 : 'Line lock out.',
    45 : 'Send acceptance tone.',
    46 : 'No answer/incompatible destination (used for ISDN).',
    47 : 'Send refusal tone. Only used at subscriber services.',
    51 : 'Digital path not provided.',
    52 : 'Congestion without differentiation.',
    53 : 'Time release.',
    54 : 'Technical fault.',
    55 : 'Congestion in group selection network.',
    56 : 'Lack of devices.',
    57 : 'Congestion in subscriber selection network.',
    58 : 'Congestion in international network.',
    59 : 'Congestion in national network.',
    60 : 'Conditional congestion (Region option).',
    61 : 'Route congestion.',
    62 : 'Unpermitted traffic case.',
    63 : 'No acknowledgement from mobile subscriber.',
  }

class OriginatingLineInformation(_IntMap):
  D = {
    0 : 'Identified Line - no special treatment',
    2 : 'Automatic Number Identification (ANI) failure',
    61 : 'Traffic originating from cellular carrier over Type 1 connection to Inter-exchange Carrier (IXC) or International Exchange Carrier (INC). Charge Number is the switch identity.',
    62 : 'Traffic originating from cellular carrier over Type 2 connection to IXC or INC. Charge Number is the subscriber number (callingPartyNumber or last redirectingNumber).',
    63 : 'Traffic originating from cellular carrier over Type 2 connection to IXC or INC, roaming forwarding call. Charge Number is the subscriber number of called mobile subscriber.',
  }

class NetworkCallReference(object):
  def __init__(self, value):
    self.SequenceNumber = _uint(self, value[0:3])
    self.SwitchIdentity = _uint(self, value[3:])

  def __repr__(self):
    return "%s(SequenceNumber=%s, SwitchIdentity=%s)" % (self.__class__.__name__, self.SequenceNumber, self.SwitchIdentity)

class LocationInformation(_Attributed):
  def __init__(self, value):
    self["MCC"] = (ord(value[0]) & 15) * 100 + (ord(value[0]) >> 4) * 10 + ord(value[1]) & 15
    self["MNC"] = (ord(value[2]) & 15) * 10 + ord(value[2]) >> 4
    if ord(value[1]) >> 4 != 15:
      self["MNC"] = self["MNC"] * 10 + ord(value[1]) >> 4
    self["LAC"] = _uint(self, value[3:5])
    self["CI"] = _uint(self, value[5:7])

class InternalCauseAndLoc(_Attributed):
  def __init__(self, value):
    self["LOCATION"] = ord(value[0])
    self["CAUSE"] = ord(value[1])

def _uint(self, value):
  l = len(value)
  if l <= 4:
    return struct.unpack("!I", ("\x00" * (4-l)) + value)[0]
  elif l <= 8:
    return struct.unpack("!Q", ("\x00" * (8-l)) + value)[0]

CallIDNumber = \
RecordSequenceNumber = \
TypeOfCallingSubscriber = \
ChargingOrigin = \
TariffClass = \
RedirectionCounter = \
FaultCode = \
SubscriptionType = \
SwitchIdentity = \
ChargingCase = \
TeleServiceCode = \
ServiceKey = \
GSMCallReferenceNumber = \
  _uint
