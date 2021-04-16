from glob import glob
from ocr import search_cpf

test_files = glob('photos/*')
print('Founded files:')
print(test_files)

for test_file in test_files:
  search_cpf(test_file, is_testing=False)