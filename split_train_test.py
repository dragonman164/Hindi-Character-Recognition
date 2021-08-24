import os
import random 
from shutil import copyfile

train_percentage = 75
test_percentage = 25

# os.mkdir('train')
# os.mkdir('test')
# os.mkdir('train/Positive')
# os.mkdir('train/Negative')
# os.mkdir('test/Positive')
# os.mkdir('test/Negative')

pos_class_files = os.listdir('training/Positive')
negative_class_files = os.listdir('training/Negative')
pc = len(pos_class_files)
nc = len(negative_class_files)
pc_train = int((train_percentage/100)*pc)
pc_test = pc - pc_train
nc_train = int((train_percentage/100)*nc)
nc_test = nc - nc_train

random.shuffle(pos_class_files)
random.shuffle(negative_class_files)

for i in range(pc_train):
    copyfile(f'./training/Positive/{pos_class_files[i]}',f'./train/Positive/{pos_class_files[i]}')

for i in range(pc_train,pc):
    copyfile(f'./training/Positive/{pos_class_files[i]}',f'./test/Positive/{pos_class_files[i]}')




for i in range(nc_train):
    copyfile(f'./training/Negative/{negative_class_files[i]}',f'./train/Negative/{negative_class_files[i]}')

for i in range(nc_train,nc):
    copyfile(f'./training/Negative/{negative_class_files[i]}',f'./test/Negative/{negative_class_files[i]}')



