import defs, parsers

def rplPrettyOut(self, value):
  return repr(self.decval(value))

for name in dir(parsers):
  if (not name.startswith("_")) and hasattr(defs, name):
    target = getattr(defs, name)
    target.prettyOut = rplPrettyOut
    target.decval = getattr(parsers, name)
