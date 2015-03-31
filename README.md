# Applied cryptozoology: CDR parser for Ericsson switches.

CDRs are in ASN.1 form. ASN.1 definition was in some doc I forgot where.
Hand-coding all ASN.1 stuff is ridiculous. So.

`syntax.py` is using pyparsing to parse syntax.txt (which is a syntax). Then
you make it into defs.py by adding imports line on top.

Next, use decode.py on binary CDR file from the switch.
The rest is DIY.
