import pprint
import pickle

contacts = []
data = {}

with open('for_sale.vcf', mode='r') as vcf_:


    for line in vcf_:



        black_list = ['BEGIN', 'VERSION', 'CHARSET']
        end_tag = ['END']
        name_tag = ["N"]
        first_name_tag = ['FN']
        numbers_tag = ['TEL', 'CELL']
        org_tag = ['ORG', "Org", 'org']

        if [ele for ele in black_list if(ele in line)]:
            continue

        #NAMES
        if [ele for ele in name_tag if(ele in line)] and not [ele for ele in first_name_tag if(ele in line)]:
            namer = line.split(':')
            lenghtOfnamer = len(namer)
            if lenghtOfnamer==2:
                if namer[-1].strip()!='VCARD':
                    data['name'] = namer[-1].strip()
            else:
                joinNamers = ''.join(namer[1:])
                if joinNamers.strip()!='VCARD':
                    data['name'] = joinNamers.strip()

        # NUMBERS
        if [ele for ele in numbers_tag if (ele in line)]:
            namer = line.split(':')
            lenghtOfnamer = len(namer)
            if lenghtOfnamer == 2:
                data['Tel'] = namer[-1].strip()
            else:
                joinNamers = namer[1:]

                for i in range(len(joinNamers)):
                    joinNamers[i]=joinNamers[i].strip()
                data['Tel'] = joinNamers


        #FIRST NAMES
        if [ele for ele in first_name_tag if(ele in line)]:
            namer = line.split(':')
            lenghtOfnamer = len(namer)
            if lenghtOfnamer==2:
                data['first name'] = namer[-1].strip()
                if len(namer[-1])>9:
                    if namer[-1].isnumeric():
                        data['Cell'] = int(namer[-1].strip())
            else:
                joinNamers = ''.join(namer[1:])
                data['first name'] = joinNamers.strip()

                if len(joinNamers)>9:
                    if joinNamers.isnumeric():
                        data['Cell'] = int(joinNamers.strip())


        #ORGANIZATIONS
        if [ele for ele in org_tag if(ele in line)]:
            namer = line.split(':')
            lenghtOfnamer = len(namer)
            if lenghtOfnamer==2:
                data['org'] = namer[-1].strip()
            else:
                joinNamers = ''.join(namer[1:])
                data['org'] = joinNamers.strip()


        #END
        if [ele for ele in end_tag if(ele in line)]:
            contacts.append(data)
            data = {}


with open('pickFile', mode='wb') as pickFile:
    pickle.dump(contacts, pickFile)
    pickFile.close()

pprint.pprint(contacts[0])
pprint.pprint(len(contacts))
