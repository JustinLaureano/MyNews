import re

TAG_RE = re.compile(r'<[^>]+>')

text = """'Abu Hopkins’ stint as a fearless foreign '
'correspondent faltered when she was detained at '
'passport control. Then came the Special K … <br '
'/>Plus! Mel G rises again with Passion of Christ 2'"""

textTrail = TAG_RE.sub('', text)
print(textTrail)