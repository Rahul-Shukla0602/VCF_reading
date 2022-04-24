import re
import pprint

with open('for_sale.vcf', mode='r') as vcf_:
    contacts = []

    for line in vcf_:
        # name = re.findall('FN:(.*)', line)
        # tel = re.findall('tel:(.*)', line)
        # nm = ''.join(name)
        # tel = ''.join(tel)
        # cell = re.findall('FN:')
        # if len(nm) == 0 and len(tel) == 0:
        #     continue
        # data = {'name': nm, 'phone': tel}
        # contacts.append(data)
        #
        #
        test_list = ['BEGIN', 'END', 'VERSION', 'CHARSET']
        if [ele for ele in test_list if(ele in line)]:
            continue



        print(line)

    pprint.pprint(contacts)
