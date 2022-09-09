import os
from operator import itemgetter
current_dir_path = os.path.abspath(os.path.dirname(__file__))

original_rule_list, temporary_list = [], []
output_lines = []
output_dict = dict()
comment_line_is_url = False
url_domains = ['https://cdn.jsdelivr.net','https://raw.githubusercontent.com']
target_filename = 'sg_sort.list'

rule_set_raw = open(os.path.join(current_dir_path, target_filename)).readlines()
for line in rule_set_raw:
    line = line.strip()
    original_rule_list.append(line)
    # URL
    # if ((line.startswith('# https://cdn.jsdelivr.net')) or (line.startswith('# https://raw.githubusercontent.com'))):
    if any(url in line for url in url_domains):
        output_lines.append(line)
        comment_line_is_url = True
    # Comments
    elif line.startswith('#->'):
        output_dict[line]=[]
        current_comment = line
    # Following Lines
    elif len(line):
        output_dict[current_comment].append(line)

sorted_output_dict = dict(sorted(output_dict.items()))
for comment, lines in sorted_output_dict.items():
    sorted_lines = sorted(lines)
    output_lines.append(comment)
    for line in sorted_lines:
        output_lines.append(line)
    output_lines.append('')

with open(os.path.join(str(current_dir_path), str('sorted_' + target_filename)), 'w') as file:
    for line in output_lines:
        file.write('%s\n' % line)
