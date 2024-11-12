# 画出ist 有对齐数据作为监督的方法 在不同数据量训练的情况下，和我们方法结果的对比
import pandas as pd
import matplotlib.pyplot as plt

# Creating a dataframe for the data

# # compared with ist-net 
# data = {
#     "Threshold": [1, 20, 40, 80, 120, 160, 200, 257],
#     "IST_IC": [None, 1.7588, 0.6824, 0.5225, 0.4344, 0.4379, 0.1195, 0.01577],
#     "IST_CC": [None, 1.2574, 0.8694, 0.7572, 0.6074, 0.6101, 0.3036, 0.02977],
#     "IST_GEC": [None, 2.1428, 1.1458, 0.8322, 0.7233, 0.6876, 0.2972, 0.03502],
#     "ours_IC": [0.051, None, None, None, None, None, None, None],
#     "ours_CC": [0.061, None, None, None, None, None, None, None],
#     "ours_GEC": [0.058, None, None, None, None, None, None, None]
# }

# # compared with condor plane
# data = {
#     "Threshold": [1, 10, 20, 40, 80, 120, 160, 200, 240, 280],
#     "compared_IC": [None, 1.159, 0.831, 0.597, 0.691, 0.403, 0.845, 0.294, 0.473, 0.358],
#     "compared_CC": [None, 1.335, 0.907, 0.746, 0.812, 0.622, 0.665, 0.409, 0.402, 0.334],
#     "compared_GEC": [None, 1.633, 1.074, 0.901, 0.883, 0.647, 0.830, 0.436, 0.452, 0.366],
#     "ours_IC": [0.051, None, None, None, None, None, None, None, None, None],
#     "ours_CC": [0.061, None, None, None, None, None, None, None, None, None],
#     "ours_GEC": [0.058, None, None, None, None, None, None, None, None, None]
# }
# compared_name = "Condor"
# save_path = 'results/0610-teaser/Condor_plane.png'
# title = 'The comparison on the aeroplane'

# # compared with condor laptop
# data = {
#     "Threshold": [1, 10, 20, 40, 80, 120, 160, 200],
#     "compared_IC": [None, 0.896, 0.590, 0.383, 0.397, 0.126, 0.255, 0.137],
#     "compared_CC": [None, 0.817, 0.675, 0.476, 0.459, 0.208, 0.320, 0.228],
#     "compared_GEC": [None, 0.990, 0.855, 0.512, 0.550, 0.233, 0.367, 0.263],
#     "ours_IC": [0.187, None, None, None, None, None, None, None],
#     "ours_CC": [0.209, None, None, None, None, None, None, None],
#     "ours_GEC": [0.222, None, None, None, None, None, None, None]
# }
# compared_name = "Condor"
# save_path = 'results/0610-teaser/Condor_loptop.png'
# title = 'The comparison on the laptop' 


# compared with condor laptop
data = {
    "Threshold": [1, 10, 20, 40, 80, 120, 160, 200],
    "compared_IC": [None, 0.896, 0.590, 0.383, 0.397, 0.126, 0.255, 0.137],
    "compared_GEC": [None, 0.990, 0.855, 0.512, 0.550, 0.233, 0.367, 0.263],
    "ours_IC": [0.187, None, None, None, None, None, None, None],
    "ours_GEC": [0.222, None, None, None, None, None, None, None]
}
compared_name = "Condor"
save_path = 'E:\\projects\\Canonicalization-Objaverse\\result\\aba_experiment\\Condor_loptop.png'
title = 'Comparison in the Laptop Category'


# # compared with condor plane
# data = {
#     "Threshold": [1, 10, 20, 40, 80, 120, 160, 200, 240, 280],
#     "compared_IC": [None, 1.159, 0.831, 0.597, 0.691, 0.403, 0.845, 0.294, 0.473, 0.358],
#     "compared_GEC": [None, 1.633, 1.074, 0.901, 0.883, 0.647, 0.830, 0.436, 0.452, 0.366],
#     "ours_IC": [0.051, None, None, None, None, None, None, None, None, None],
#     "ours_GEC": [0.058, None, None, None, None, None, None, None, None, None]
# }
# compared_name = "Condor"
# save_path = 'E:\\projects\\Canonicalization-Objaverse\\result\\aba_experiment\\Condor_plane.png'
# title = 'Comparison in the Aeroplane Category'

df = pd.DataFrame(data)

# Plotting the data
plt.figure(figsize=(10, 7.5))
# 设置字体为 Times New Roman 并设置字体大小为 25
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 30

# IST lines
plt.plot(df["Threshold"], df["compared_IC"], marker='o', linestyle='-', color='blue', label=compared_name+'_IC')
plt.plot(df["Threshold"], df["compared_GEC"], marker='o', linestyle='-', color='red', label=compared_name+'_GEC')

# Ours markers using scatter for clarity
plt.scatter([1], df["ours_IC"].dropna(), marker='*', s=300, color='blue', label='ours_IC')
plt.scatter([1], df["ours_GEC"].dropna(), marker='*', s=300, color='red', label='ours_GEC')

plt.xlabel('Number of Priors', fontsize=30)
plt.ylabel('Value', fontsize=30)
plt.title(title)
plt.legend()
plt.grid(True)

# 保存为图片文件
plt.savefig(save_path)
print('save to:', save_path)

# 不显示图表
plt.close()
