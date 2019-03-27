import re

def code_to_boro(code):
    # Convert 1 to MN and etc
    # Intake a string 
    # If not found, return empty string
    if code == '1':
        return 'MN'
    elif code == '2':
        return 'BX'
    elif code == '3':
        return 'BK'
    elif code == '4':
        return 'QN'
    elif code == '5':
        return 'SI'
    else: 
        return ''

def month_to_number(hnum):
    hnum = re.sub(r'jan-', '01', hnum.lower())
    hnum = re.sub(r'feb-', '02', hnum.lower())
    hnum = re.sub(r'mar-', '03', hnum.lower())
    hnum = re.sub(r'apr-', '04', hnum.lower())
    hnum = re.sub(r'may-', '05', hnum.lower())
    hnum = re.sub(r'jun-', '06', hnum.lower())
    hnum = re.sub(r'jul-', '07', hnum.lower())
    hnum = re.sub(r'aug-', '08', hnum.lower())
    hnum = re.sub(r'sep-', '09', hnum.lower())
    hnum = re.sub(r'oct-', '10', hnum.lower())
    hnum = re.sub(r'nov-', '11', hnum.lower())
    hnum = re.sub(r'dec-', '12', hnum.lower())
    hnum = re.sub(r'-jan', '01', hnum.lower())
    hnum = re.sub(r'-feb', '02', hnum.lower())
    hnum = re.sub(r'-mar', '03', hnum.lower())
    hnum = re.sub(r'-apr', '04', hnum.lower())
    hnum = re.sub(r'-may', '05', hnum.lower())
    hnum = re.sub(r'-jun', '06', hnum.lower())
    hnum = re.sub(r'-jul', '07', hnum.lower())
    hnum = re.sub(r'-aug', '08', hnum.lower())
    hnum = re.sub(r'-sep', '09', hnum.lower())
    hnum = re.sub(r'-oct', '10', hnum.lower())
    hnum = re.sub(r'-nov', '11', hnum.lower())
    hnum = re.sub(r'-dec', '12', hnum.lower())
    return hnum

def convert_colnames(df):
    new_names = {}
    for i in df.columns:
        new_names[i] = i.lower().strip().replace(' ', '_')
    return df.rename(columns=new_names)

def parse_success(record):
    return record['output']

def parse_failure(record):
    record['output'].pop('alternative_names')
    record['output']['new_street_name'] = ''
    record['output']['new_house_number'] = ''
    record['output']['new_zip_code'] = ''
    record['output']['correction_status'] = ''
    return record['output']

def dump_success(lst):
    success = list(map(parse_success, 
                    filter(lambda x: x['status'] == 'success', lst)))
    print(f'success counts : {len(success)}')
    return success
 
def dump_failure(lst):
    failure = list(map(parse_failure, 
                    filter(lambda x: x['status'] == 'failure', lst)))
    print(f'failure counts : {len(failure)}')
    return failure