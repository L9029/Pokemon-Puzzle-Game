import os
import random

def Get_Images_Paths(root_dir):
    image_names = os.listdir(root_dir)
    
    assert len(image_names) > 0
    
    return os.path.join(root_dir, random.choice(image_names))