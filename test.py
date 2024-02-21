import os
import glob

folder_path = "C:/Users/11963/Downloads/Telegram Desktop"


def get_png_files(folder_path):
    # 构造匹配 PNG 文件的通配符路径
    pattern = os.path.join(folder_path, "*.png")

    # 使用 glob 模块获取匹配的文件列表
    png_files = glob.glob(pattern)

    return png_files


# 文件夹路径

# 获取所有 PNG 图片地址
png_files = get_png_files(folder_path)

# 打印结果
print("PNG Files:")
for file in png_files:
    print(file)
