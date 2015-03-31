import sys

import pyasn1.codec.ber.decoder
import parserimp

class CDRFileParser(object):
  def __init__(self, filename):
    self.filename = filename
    self.blocks = 0
    self.entries = 0

  def parse(self):
    if not hasattr(self, 'file'):
      self.file = open(self.filename, 'rb')

    while True:
      block = self.file.read(4096)
      if not block:
        break

      self.blocks += 1

      for entry in self.ParseBlock(block):
        self.entries += 1
        yield entry

  def ParseBlock(self, block):
    while block and block[0] != '\x00':
      result, block = pyasn1.codec.ber.decoder.decode(block, asn1Spec=parserimp.defs.CallDataRecord())
      yield result

#def ParseSingleRecord(r):
#  print r.prettyPrint()
#  r = r.getComponentByName('u')
#  if r.getComponentByName('mSOriginating'):
#    c = short_pb2.CDR()
#    c.type = c.ORIG_CALL
#    
#    print r.getComponentByName('mSOriginating').prettyPrint()

p = CDRFileParser(sys.argv[1])

for r in p.parse():
  print r.prettyPrint()

#  if r.getComponentByName('uMTSGSMPLMNCallDataRecord'):
#    r.prettyPrint()
#  elif r.getComponentByName('compositeCallDataRecord'):
#    for x in r.getComponentByName('compositeCallDataRecord'):
#      ParseSingleRecord(x)
    
print "Blocks:", p.blocks, "Records:", p.entries

