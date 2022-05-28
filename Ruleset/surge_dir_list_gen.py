import glob, os
current_dir_path = os.path.abspath(os.path.dirname(__file__))

output = []
target_filename = 'sg_list.txt'

sg_list = glob.glob(current_dir_path+'/*.list')
for sg in sg_list:
    sg = sg.replace(current_dir_path, '')
    output.append(sg)

file_ext = ['list','sgmodule','js']
for ext in file_ext:
    sg_list_sub = glob.glob(current_dir_path+'/*/*.'+ext)
    for sg in sg_list_sub:
        sg = sg.replace(current_dir_path, '')
        output.append(sg)

with open((current_dir_path+'/'+target_filename), 'w') as file:
    for line in output:
        file.write('%s\n' % line)

print(current_dir_path)