import os
import json

# textures 文件夹路径
textures_dir = os.path.join(os.getcwd(), "textures")

# 模板 JSON 数据（除 textures 字段外固定）
template = {
    "version": "1.0.0",
    "model": "../model.moc",
    "textures": [],
    "layout": {"center_x": 0.0, "center_y": -0.05, "width": 2.0},
    "hit_areas_custom": {
        "head_x": [-0.35, 0.6],
        "head_y": [0.19, -0.2],
        "body_x": [-0.3, -0.25],
        "body_y": [0.3, -0.9],
    },
    "motions": {
        "idle": [
            {"file": "../motions/Breath1.mtn"},
            {"file": "../motions/Breath2.mtn"},
            {"file": "../motions/Breath3.mtn"},
            {"file": "../motions/Breath5.mtn"},
            {"file": "../motions/Breath7.mtn"},
            {"file": "../motions/Breath8.mtn"},
            {"file": "../motions/Breath9.mtn"},
        ],
        "sleepy": [{"file": "../motions/Sleeping.mtn"}],
        "flick_head": [
            {"file": "../motions/Touch Dere1.mtn"},
            {"file": "../motions/Touch Dere2.mtn"},
            {"file": "../motions/Touch Dere3.mtn"},
            {"file": "../motions/Touch Dere4.mtn"},
            {"file": "../motions/Touch Dere5.mtn"},
            {"file": "../motions/Touch Dere6.mtn"},
        ],
        "tap_body": [
            {"file": "../motions/Sukebei1.mtn"},
            {"file": "../motions/Sukebei2.mtn"},
            {"file": "../motions/Sukebei3.mtn"},
            {"file": "../motions/Touch1.mtn"},
            {"file": "../motions/Touch2.mtn"},
            {"file": "../motions/Touch3.mtn"},
            {"file": "../motions/Touch4.mtn"},
            {"file": "../motions/Touch5.mtn"},
            {"file": "../motions/Touch6.mtn"},
        ],
    },
}

# 保存生成的 JSON 文件名
json_files = []

# 遍历 textures 文件夹中所有 png 图片
for file_name in os.listdir(textures_dir):
    if file_name.lower().endswith(".png"):
        texture_path = os.path.join("textures", file_name)
        json_data = template.copy()
        json_data["textures"] = [f"../{texture_path}"]

        # 去掉文件扩展名用于命名 JSON 文件
        base_name = os.path.splitext(file_name)[0]
        json_file_name = f"jsons/{base_name}.json"
        json_files.append(f"Potion-Maker/Tia/{json_file_name}")

        with open(json_file_name, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)

        print(f"生成: {json_file_name}")

# 输出所有生成的 JSON 文件名数组
print("\n所有生成的 JSON 文件名：")
print(json.dumps(json_files, indent=4, ensure_ascii=False))
