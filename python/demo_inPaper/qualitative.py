"""把对齐前后的结果拼接在一起，放到论文里
"""

import os

from python.utils.pics_utils import merge_images2Row

data_root = 'E:/projects/Canonicalization-Objaverse/result/alignedCourse/secondBatch'
save_dir = 'E:/projects/Canonicalization-Objaverse/result/demo_inPaper'

# 获得文件夹下全部文件夹的名称
dirs = os.listdir(data_root)

indexs = [0,1,2,3]

for dir in dirs:
    data_dir = os.path.join(data_root, dir)

    # org pics 拼接
    org_pics_pathes = [os.path.join(data_dir, f'org_newObj_ins_{i}.png') for i in indexs]
    save_path = os.path.join(save_dir, f'{dir}_org.png')
    merge_images2Row(org_pics_pathes, output_pic_path=save_path)

    align_pics_pathes = [os.path.join(data_dir, f'aligned_newObj_ins_{i}.png') for i in indexs]
    save_path = os.path.join(save_dir, f'{dir}_align.png')
    merge_images2Row(align_pics_pathes, output_pic_path=save_path)
    print(f'{dir} done!')