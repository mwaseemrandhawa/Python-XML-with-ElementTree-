import xml.etree.ElementTree as ET
import os
import csv
path = 'F:\xmlproject'
with open('names.csv', 'a') as csvfile:
    fieldnames = ['name', 'description', 'indication', 'synonyms', 'dosages']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for filename in os.listdir(path):
        if not filename.endswith('.xml'): continue
        fullname = os.path.join(path, filename)
        tree = ET.parse(fullname)
		synon = 
		doasag = 
        lst = tree.findall('drug', attrib={type})
        for i in lst:
            i_n = i.findall('name')
			i_d = i.findall(description)
			i_in = i.findall('indication')
			i_sy = i.findall.SubElement('synonyms', 'synonym')
			i_do = i.findall.SubElement('dosages', 'dosage')
            writer.writerow({'name': i_n, 'description': i_d, 'indication': i_in, 'synonym': i_sy, 'doasages': i_do}})