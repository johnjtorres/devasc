import json
import xml.etree.ElementTree as ET

import xmltodict

school = """\
<school>
    <children>
        <child>Timmy</child>
        <child>Susan</child>
        <child>Harry Potter</child>
    </children>
    <teachers>
        <teacher>Ms. Frizzle</teacher>
        <teacher>Prof. Lupen</teacher>
        <teacher>Mr. Crocker</teacher>
    </teachers>
</school>
"""

# Use the find or findall command to search the XMl document.
print("Finding every child")
root = ET.fromstring(school)
children = root.findall(".//child")
for child in children:
    print(child.text)

print("\n", "=" * 100, "\n", sep="")

# Use xmltodict to convert XML to a python dictionary.
print("Converting XML to JSON.")
parsed = xmltodict.parse(school)
print(json.dumps(parsed, indent=2, sort_keys=True))
