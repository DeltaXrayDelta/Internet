import os
current_dir_path = os.path.abspath(os.path.dirname(__file__))

adguard_output = []
target_filename = 'Reject_Carrier_ID.list'

rule_set_raw = open(os.path.join(current_dir_path, target_filename)).readlines()
for line in rule_set_raw:
    line = line.strip()
    # Comments
    if (line.startswith("#")):
            adguard_output.append(line.strip())
    # Generate DOMAIN-SET, combine '.' and URL
    elif (line.startswith('DOMAIN,')) or (line.startswith('DOMAIN-SUFFIX,')):
            adguard_output.append(('\n||' + line.split(',',1)[1]).strip() + '^')
    # New Line
    elif (line in ['\n', '\r\n']):
        adguard_output.append(('\r\n'))


with open(os.path.join(str(current_dir_path + '/AdGuard'), str('adguard_' + target_filename)), 'w') as file:
    for line in adguard_output:
        file.write('%s\n' % line)