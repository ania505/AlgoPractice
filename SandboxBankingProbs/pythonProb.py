# Problems #1 from Sandbox Banking Python Code Challenge

def search(first_name=None, last_name=None, address=None, tax_id=None):

    import csv
    with open('SandboxBankingProbs/people.csv', 'r') as csvfile:
        ppl_reader = csv.reader(csvfile, delimiter=',')

        header = True
        info = []
        for row in ppl_reader:
            if header:
                # skipping 1st row
                header = False
                continue
            # print(row)
            per_person = {}
            per_person['first_name'] = row[0]
            # print(per_person)
            per_person['last_name'] = row[1]
            # print(per_person)
            per_person['address'] = row[2]
            # print(per_person)
            per_person['tax_id'] = row[3]
            # print(per_person)
            info.append(per_person)
            # WHY IS TAX_ID BEING ADDED IN 1ST???
            # print(per_person)
        # print(info)

    result = []
    # need to check if the inputs are empty >>> return entire ppl list
    if first_name==None and last_name==None and address==None and tax_id==None:
        return info
    # make case insensitive >>> lower everything OR TITLE CASE
    # check which inputs are not existent 
    matching = False
    for person in info:
        if first_name != None:
            # print(first_name, person['first_name'])
            if person['first_name'] == first_name.title():
                matching = True
            else:
                matching = False
        if last_name != None:
            if person['last_name'] == last_name.title():
                matching = True
            else:
                matching = False
        if address != None:
            if person['address'] == address.title():
                matching = True
            else:
                matching = False
        if tax_id != None:
            if person['tax_id'] == tax_id:
                matching = True
            else:
                matching = False
            # tried to replace the conditionals with a python ternary but didnt work
        if matching:
            # print(person['first_name'], 'added!')
            result.append(person)
    return result

print(search())                                       # passes
print(search(first_name='BORIS'))                     # passes
print(search(first_name='FRANK'))                     # passes
print(search(last_name='lInCoLn'))                    # passes
print(search(tax_id='0000000000'))                    # passes
print(search(first_name='Manny', last_name='Macho'))  # passes


