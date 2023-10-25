import os
import json

# read paths.json file to get the path to the data directory
with open('paths.json') as f:
    paths = json.load(f)
    data_dir = paths['datasets']
print("-"*50)

# print whether the data directory exists
if os.path.exists(data_dir):
    print(f'Data directory [{data_dir}] exists')
else:
    print(f'Data directory [{data_dir}] does not exist')
    raise Exception('Data directory does not exist')
print("-"*50)


# print the access permissions for the data directory
print('Data directory permissions:', oct(os.stat(data_dir).st_mode)[-3:])
# print read access, write access, and execute access
print('Read access:', os.access(data_dir, os.R_OK))
print('Write access:', os.access(data_dir, os.W_OK))
print('Execute access:', os.access(data_dir, os.X_OK))
print("-"*50)

# try to write a file to the data directory
try:
    with open(os.path.join(data_dir, 'test.txt'), 'w') as f:
        f.write('test')
    print('Successfully wrote to data directory')
except PermissionError:
    print('Permission denied: cannot write to data directory')

# try to delete the written file
try:
    os.remove(os.path.join(data_dir, 'test.txt'))
    print('Successfully deleted test.txt')
except FileNotFoundError:
    print('File not found: cannot delete test.txt')

print("-"*50)