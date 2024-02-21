from PIL import Image
import tlogger
import os
import glob
import json

log = tlogger.Flogger().get_logger(__name__)


def load_danbooru_all_art_json(art_json_path):
    with open(art_json_path, "r") as json_file:
        danbooru_art_list = json.load(json_file)
        return danbooru_art_list


def get_png_path_list(folder_path):
    pattern = os.path.join(folder_path, "*.png")
    png_path_list = glob.glob(pattern)
    return png_path_list


def read_image_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            # 获取图像的元数据
            metadata = img.info
            return metadata
    except Exception as e:
        log.exception(f"没有元数据 {e}")
        return None


# 加载d站画师列表
danbooru_art_list_file = "./artists.json"
danbooru_art_list = load_danbooru_all_art_json(danbooru_art_list_file)
art_list = {}

# 图片文件夹
folder_path = "C:/Users/Downloads"
png_path_list = get_png_path_list(folder_path)

# 解析
for png_path in png_path_list:
    metadata = read_image_metadata(png_path)
    if metadata:
        if (
            len(metadata.keys()) == 6 and "Description" in metadata
        ):  # noval ai生成的图片格式
            _ = metadata["Description"]
            _ = (
                _.replace("[", "")
                .replace("]", "")
                .replace("{", "")
                .replace("}", "")
                .replace("artist", "")
                .replace(":", "")
                .replace("_", " ")
            )
            log.info(_)
            for tag in _.split(","):
                tag = tag.strip()
                if tag != "" and tag in danbooru_art_list:
                    if tag in art_list:
                        art_list[tag] += 1
                    else:
                        art_list[tag] = 1
log.info(art_list)
output_file_path = "./output.json"
with open(output_file_path, "w") as json_file:
    json.dump(art_list, json_file)

# 排序输出
sorted_keys = sorted(art_list, key=lambda x: art_list[x])
for key in sorted_keys:
    value = art_list[key]
    print(f"{key}: {value}")
