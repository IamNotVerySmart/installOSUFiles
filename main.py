import os
import shutil

download_path = "C:\\Users\\xalie\\Downloads"
beatmap_path = "C:\\Users\\xalie\\AppData\\Local\\osu!\\Songs"
skin_path = "C:\\Users\\xalie\\AppData\\Local\\osu!\\Skins"
beatmap = ".osz"
skin = ".osk"
number = 0

for file in os.listdir(download_path):
    if file.endswith(beatmap) or file.endswith(skin):
        number += 1
        start_path = os.path.join(download_path, file)

        if file.endswith(beatmap):
            beatmap_end_path = os.path.join(beatmap_path, file)
            shutil.move(start_path, beatmap_end_path)
            print(f"[{number}] found file: {file} was moved to {beatmap_path}.")
        else:
            skin_end_path = os.path.join(skin_path, file)
            shutil.move(start_path, skin_end_path)
            print(f"[{number}] found file: {file} was moved to {skin_path}")
    else:
        print(f"didn't found specified file.({beatmap}, {skin})")
