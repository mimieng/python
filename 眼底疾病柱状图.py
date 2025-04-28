import matplotlib
# 设置后端为Agg，这是一个非交互式后端，可以避免显示问题
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# 设置中文字体
try:
    # 尝试使用微软雅黑字体
    font = FontProperties(fname=r"C:\Windows\Fonts\msyh.ttc", size=10)
except:
    # 如果找不到微软雅黑，使用系统默认字体
    font = FontProperties(size=10)

# 眼底疾病类别
categories = [
    '正常', 
    '糖尿病视网膜病变', 
    '青光眼', 
    '白内障', 
    '年龄相关性黄斑变性', 
    '高血压视网膜病变', 
    '病理性近视', 
    '其他眼病'
]

# 在这里填写各疾病的数据（示例数据，请替换为您的实际数据）
values = [
    1140,  # 正常
    1128,   # 糖尿病视网膜病变
    215,   # 青光眼
    212,   # 白内障
    164,   # 年龄相关性黄斑变性
    103,   # 高血压视网膜病变
    174,   # 病理性近视
    979    # 其他眼病
]

# 创建图形和坐标轴
plt.figure(figsize=(12, 6))

# 生成柱状图
bars = plt.bar(categories, values, color='skyblue', edgecolor='navy')

# 在柱子上方显示数值
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{height}',
             ha='center', va='bottom', fontproperties=font)

# 设置图表标题和轴标签
plt.title('眼底疾病数据统计', fontproperties=font, fontsize=16)
plt.xlabel('疾病类别', fontproperties=font, fontsize=12)
plt.ylabel('样本数量', fontproperties=font, fontsize=12)

# 旋转x轴标签，使其更易读
plt.xticks(rotation=45, ha='right', fontproperties=font)

# 添加网格线，使图表更易读
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 调整布局，确保所有元素都能显示
plt.tight_layout()

# 保存图表
plt.savefig(r'd:\python-learning\数据分析\眼底疾病统计图.png', dpi=300)

# 不使用plt.show()，而是提示用户查看保存的图像
# plt.show()  # 注释掉这一行

print("图表已保存到: d:\\python-learning\\数据分析\\眼底疾病统计图.png")
print("请直接打开该图片文件查看结果。")