import sys
from pyparsing import *

OpenBracket = Regex("[({]").suppress()
CloseBracket = Regex("[)}]").suppress()

def Enclose(val):
  return OpenBracket + val + CloseBracket

def SetDefType(typekw):
  def f(a, b, c):
    c["defType"] = typekw
  return f

def NoDashes(a, b, c):
  return c[0].replace("-", "_")

def DefineTypeDef(typekw, typename, typedef):
  return typename.addParseAction(SetDefType(typekw)).setResultsName("definitionType") - \
    Optional(Enclose(typedef).setResultsName("definition"))



SizeConstraintBodyOpt = Word(nums).setResultsName("minSize") - \
  Optional(Suppress(Literal("..")) - Word(nums + "n").setResultsName("maxSize"))

SizeConstraint = Group(Keyword("SIZE").suppress() - Enclose(SizeConstraintBodyOpt)).setResultsName("sizeConstraint")

Constraints = Group(delimitedList(SizeConstraint)).setResultsName("constraints")

DefinitionBody = Forward()

TagPrefix = Enclose(Word(nums).setResultsName("tagID")) - Keyword("IMPLICIT").setResultsName("tagFormat")

OptionalSuffix = Optional(Keyword("OPTIONAL").setResultsName("isOptional"))
JunkPrefix = Optional("--F--").suppress()
AName = Word(alphanums + "-").setParseAction(NoDashes).setResultsName("name")

SingleElement = Group(JunkPrefix - AName - Optional(TagPrefix) - DefinitionBody.setResultsName("typedef") - OptionalSuffix)

NamedTypes = Dict(delimitedList(SingleElement)).setResultsName("namedTypes")

SetBody = DefineTypeDef("Set", Keyword("SET"), NamedTypes)
SequenceBody = DefineTypeDef("Sequence", Keyword("SEQUENCE"), NamedTypes)
ChoiceBody = DefineTypeDef("Choice", Keyword("CHOICE"), NamedTypes)

SetOfBody = (Keyword("SET") + Optional(SizeConstraint) + Keyword("OF")).setParseAction(SetDefType("SetOf")) + Group(DefinitionBody).setResultsName("typedef")
SequenceOfBody = (Keyword("SEQUENCE") + Optional(SizeConstraint) + Keyword("OF")).setParseAction(SetDefType("SequenceOf")) + Group(DefinitionBody).setResultsName("typedef")

CustomBody = DefineTypeDef("constructed", Word(alphanums + "-").setParseAction(NoDashes), Constraints)
NullBody = DefineTypeDef("Null", Keyword("NULL"), Constraints)

OctetStringBody = DefineTypeDef("OctetString", Regex("OCTET STRING"), Constraints)
IA5StringBody = DefineTypeDef("IA5String", Keyword("IA5STRING"), Constraints)

EnumElement = Group(Word(printables).setResultsName("name") - Enclose(Word(nums).setResultsName("value")))
NamedValues = Dict(delimitedList(EnumElement)).setResultsName("namedValues")
EnumBody = DefineTypeDef("Enum", Keyword("ENUMERATED"), NamedValues)

BitStringBody = DefineTypeDef("BitString", Keyword("BIT") + Keyword("STRING"), NamedValues)

DefinitionBody << (OctetStringBody | SetOfBody | SetBody | ChoiceBody | SequenceOfBody | SequenceBody | EnumBody | BitStringBody | IA5StringBody | NullBody | CustomBody)

Definition = AName - Literal("::=").suppress() - Optional(TagPrefix) - DefinitionBody

Definitions = Dict(ZeroOrMore(Group(Definition)))

pf = Definitions.parseFile(sys.argv[1])

TypeDeps = {}
TypeDefs = {}

def SizeConstraintHelper(size):
  s2 = s1 = size.get("minSize")
  s2 = size.get("maxSize", s2)
  try:
    return("constraint.ValueSizeConstraint(%s, %s)" % (int(s1), int(s2)))
  except ValueError:
    pass

ConstraintMap = {
  'sizeConstraint' : SizeConstraintHelper,
}

def ConstraintHelper(c):
  result = []
  for key, value in c.items():
    r = ConstraintMap[key](value)
    if r:
      result.append(r)
  return result

def GenerateConstraints(c, ancestor, element, level=1):
  result = ConstraintHelper(c)
  if result:
    return [ "subtypeSpec = %s" % " + ".join(["%s.subtypeSpec" % ancestor] + result) ]
  return []

def GenerateNamedValues(definitions, ancestor, element, level=1):
  result = [ "namedValues = namedval.NamedValues(" ]
  for kw in definitions:
    result.append("  ('%s', %s)," % (kw["name"], kw["value"]))
  result.append(")")
  return result

OptMap = {
  False: "",
  True: "Optional",
}

def GenerateNamedTypesList(definitions, element, level=1):
  result = []
  for val in definitions:
    name = val["name"]
    typename = None

    isOptional = bool(val.get("isOptional"))

    subtype = []
    constraints = val.get("constraints")
    if constraints:
      cg = ConstraintHelper(constraints)
      subtype.append("subtypeSpec=%s" % " + ".join(cg))
    tagId = val.get("tagID")
    if tagId:
      subtype.append("implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, %s)" % tagId)

    if subtype:
      subtype = ".subtype(%s)" % ", ".join(subtype)
    else:
      subtype = ""

    cbody = []
    if val["defType"] == "constructed":
      typename = val["typedef"]
      element["_d"].append(typename)
    elif val["defType"] == "Null":
      typename = "univ.Null"
    elif val["defType"] == "SequenceOf":
      typename = "univ.SequenceOf"
      print val.items()
      cbody = [ "  componentType=%s()" % val["typedef"]["definitionType"] ]
    elif val["defType"] == "Choice":
      typename = "univ.Choice"
      indef = val.get("definition")
      if indef:
        cbody = [ "  %s" % x for x in GenerateClassDefinition(indef, name, typename, element) ]
    construct = [ "namedtype.%sNamedType('%s', %s(" % (OptMap[isOptional], name, typename), ")%s)," % subtype ]
    if not cbody:
      result.append("%s%s%s" % ("  " * level, construct[0], construct[1]))
    else:
      result.append("  %s" % construct[0])
      result.extend(cbody)
      result.append("  %s" % construct[1])
  return result



def GenerateNamedTypes(definitions, ancestor, element, level=1):
  result = [ "componentType = namedtype.NamedTypes(" ]
  result.extend(GenerateNamedTypesList(definitions, element))
  result.append(")")
  return result


defmap = {
  'constraints' : GenerateConstraints,
  'namedValues' : GenerateNamedValues,
  'namedTypes' : GenerateNamedTypes,
}

def GenerateClassDefinition(definition, name, ancestor, element, level=1):
  result = []
  for defkey, defval in definition.items():
    if defval:
      fn = defmap.get(defkey)
      if fn:
        result.extend(fn(defval, ancestor, element, level))
  return ["  %s" % x for x in result]

def GenerateClass(element, ancestor):
  name = element["name"]

  top = "class %s(%s):" % (name, ancestor)
  definition = element.get("definition")
  body = []
  if definition:
    body = GenerateClassDefinition(definition, name, ancestor, element)
  else:
    typedef = element.get("typedef")
    if typedef:
      element["_d"].append(typedef["definitionType"])
      body.append("  componentType = %s()" % typedef["definitionType"])
      szc = element.get('sizeConstraint')
      if szc:
        body.extend(GenerateConstraints({ 'sizeConstraint' : szc }, ancestor, element))

  if not body:
    body.append("  pass")

  TypeDeps[name] = list(frozenset(element["_d"]))

  return "\n".join([top] + body)

StaticMap = {
  "Null" : "univ.Null",
  "Enum" : "univ.Enumerated",
  "OctetString" : "univ.OctetString",
  "IA5String" : "char.IA5String",
  "Set" : "univ.Set",
  "Sequence" : "univ.Sequence",
  "Choice" : "univ.Choice",
  "SetOf" : "univ.SetOf",
  "BitString" : "univ.BitString",
  "SequenceOf" : "univ.SequenceOf",
}

def StaticConstructor(x):
  x["_d"] = []
  if x["defType"] == "constructed":
    dt = x["definitionType"]
    x["_d"].append(dt)
  else:
    dt = StaticMap[x["defType"]]
  return GenerateClass(x, dt)


for element in pf:
  TypeDefs[element["name"]] = StaticConstructor(element)

while TypeDefs:
  ready = [ k for k, v in TypeDeps.items() if len(v) == 0 ]
  if not ready:
    x = list()
    for a in TypeDeps.values():
      x.extend(a)
    x = frozenset(x) - frozenset(TypeDeps.keys())

    print TypeDefs

    raise ValueError, sorted(x)

  for t in ready:
    for v in TypeDeps.values():
      try:
        v.remove(t)
      except ValueError:
        pass

    del TypeDeps[t]
    print TypeDefs[t]
    print
    print

    del TypeDefs[t]
  

