import os
import shutil
import glob
from tqdm import tqdm
Raw_DIR= r'F:\studies\SEM-7\SGP\DDDS_DL\Data'
for dirpath, dirname, filenames in os.walk(Raw_DIR):
    for i in tqdm([f for f in filenames if f.endswith('.png')]):
        if i.split('_')[4]=='0':
            shutil.copy(src=dirpath+'/'+i, dst=r'F:\studies\SEM-7\SGP\DDDS_DL\Dataset\Closed')
        
        elif i.split('_')[4]=='1':
            shutil.copy(src=dirpath+'/'+i, dst=r'F:\studies\SEM-7\SGP\DDDS_DL\Dataset\Open')
