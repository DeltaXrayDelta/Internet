import os
current_dir_path = os.path.abspath(os.path.dirname(__file__))

original_rule_dict, temporary_dict = [], []
is_comment = False
target_filename = 'sg_sort.list'

rule_set_raw = open(os.path.join(current_dir_path, target_filename)).readlines()
for line in rule_set_raw:
    line = line.strip()
    original_rule_dict.append(line)
    # Comments
    if (line.startswith("#")):
        is_comment = True

original_rule_dict.sort()
print(original_rule_dict)

with open(os.path.join(str(current_dir_path), str('sorted_' + target_filename)), 'w') as file:
    for line in original_rule_dict:
        file.write('%s\n' % line)