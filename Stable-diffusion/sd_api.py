import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin
import time
from datetime import datetime

url = "http://127.0.0.1:7860"

# prompt var
## photo quality
quality1 = "best quality, masterpiece, ultra high res, (photorealistic:1.4), RAW photo, 8k, high resolution"
quality2 = "extremely cute girl, extremely detailed face, extremely detailed skin, extremely detailed legs"
quality3 = "extremely cute 1 girl, extremely detailed cute face, extremely detailed skin, extremly detailed legs, extremely detailed hip, extremely detailed back, extremely detailed eyes"
quality4 = "extremely detailed eyes"
quality5 = "extremely cute 1 girl, extremely detailed cute face, extremely detailed eyes, extremely detailed skin, extremely detailed small nose"

## number of person and sexual
person1 = "1 girl"

## age
age1 = "18 years old"

## face infomation
face1 = "detailed brown eyes, small face"
face2 = "((put on pink mask, covered mouth, mask, mouth mask))"

## expression infomation
express1 = "seductive smile"

## chest infomation
# chest = "huge breasts, breasts cleavage,"
chest1 = "huge breasts, cleavage"
chest2 = "midium breasts"
chest3 = "cleavage"
chest4 = "big breasts, cleavage"

## camera angle
angle1 = "looking at viewer"
angle2 = "bird's eye view"
angle3 = "from bellow"
angle4 = "looking down"
angle5 = "lower body"
angle6 = "close-up hip"
angle7 = "from back"
angle8 = "looking away"
angle9 = "looking to the side"
angle10 = "portrait"
angle11 = "cowboy shot"

## hair length infomation
hair1 = "short bob hair, (beautiful brawn hair:1.3)"
hairlength1 = "very short hair"
hairlength2 = "short hair"
hairlength3 = "medium hair"
hairlength4 = "long hair"
hairlength5 = "very long hair"
hairlength6 = "absurdly long hair"
hairlength7 = "short bob hair"

## hair style infomaiton
hairstyle1 = "messy hair"
hairstyle2 = "straight hair"
hairstyle3 = "wavy hair"
hairstyle4 = "flipped hair"
hairstyle5 = "asymmetrical hair"
hairstyle6 = "ponytail"
hairstyle7 = "high ponytail"
hairstyle8 = "low ponytail"
hairstyle9 = "twintails"
hairstyle10 = "low twintails"
hairstyle11 = "short twintails"
hairstyle12 = "braid"
hairstyle13 = "curly hair"
hairstyle14 = "drill hair"
hairstyle15 = "twin drills"
hairstyle16 = "hair bun"

## bangs infomation
bangs1 = "blunt bangs"
bangs2 = "asymmetrical bangs"
bangs3 = "hair over eyes"
bangs4 = "hair over one eye"
bangs5 = "parted bangs"
bangs6 = "swept bangs"
bangs7 = "hair between eyes"

## hip infomation
hip1 = "butt up, wide hip, ass, backshot"

## body style infomation
style1 = "model"

## place infomation
#place = "fashion magazine, magazine title, cover page, English, full body"
place1 = "bar counter, girls bar, drinking, drinnking beer, sake, rounge"
place2 = "lying on bed"
place3 = "background in business office"
place4 = "outside"
place5 = "pool side"

## makeup or not
makeup = ""

## panty infomation
panty1 = "thong"
panty2 = "thong under pantyhose"
panty3 = "micro skirt"
panty4 = "bikini"

## pose infomation
pose1 = "skirt lift, showing panties, thong"
pose2 = "butt sticking out, close up hip, thong"
pose3 = "armpits"
pose4 = "cross legs"

## clothes
cloth1 = "tank top, shoulder"
cloth2 = "bikini, sexy bikini"
cloth3 = "Santa Claus, shoulder"
cloth4 = "sailer uniform, sailer school uniform"
cloth5 = "school swim suit, school swim"
cloth6 = "sexy bra, lace bra, black bra"
cloth7 = "nice elegant dress"

## situation
situation1 = "wet, sweat, sheet of spray, wet clothes"

## lighting
light1 = "sun set, sunset lighting"

## additinal infomation
addition = "earing, necklace, cute cheek, seductive smile"
addition2 = "from back, ass, butt up, full body, wide hip, thong"
addition3 = "from back, ass, butt up, full body, gigantic hip, thong"
test1 = "accentuate the chest"
test2 = "half undress"
test3 = "skirt lift"
test4 = "showing panties"
test5 = "panties aside"
test6 = "topless"
test7 = "bottomless"
test8 = "undressing"
test9 = "see through dress"
test10 = "nipple stand"
test11 = "skindantation"
test12 = "pussy line, cameltoe"
test13 = "pow pose"
test14 = "put on mask"
test15 = "swept bangs, panties under pantyhose, ass, backshot"
test16 = "thong, ass, backshot"

override_settings = {}
#override_settings["sd_model_checkpoint"] = "BRAV5finalfp16.safetensors"
#override_settings["sd_model_checkpoint"] = "chilloutmix_NiPrunedFp32Fix"
#override_settings["sd_model_checkpoint"] = "beautifulRealistic_brav5"
override_settings["sd_model_checkpoint"] = "beautifulRealistic_v60"
#override_settings["sd_vae"] = "vae-ft-mse-840000-ema-pruned"
#override_settings["sd_vae"] = "v2-1_768-ema-pruned"

# loop and seed settings
loop = 20
seed = -1
#enable_hr = False
enable_hr = True

#prompt = f"{quality}, {quality2}, {age}, {cloth}, {face}, {hair}, {place}, {chest}, {angle}, {makeup}, {addition}, {addition2}"
# prompt = f"{quality1}, {person1}, {quality3}, {angle1}, {age1}, {chest2}, {addition2}, {hair1}, {pose2}, {place4}, {style1}"
# prompt = f"{quality1}, {person1}, {quality3}, {angle3}, {age1}, {chest2}, {addition2}, {hair1}, {pose2}, {place4}, {style1}"
# prompt = f"{quality1}, {test16}, {place4}"
# prompt = f"{quality1}, {person1}, {hair1}, {hip1}, {panty1}, {place4}"
prompt = f"{quality1}, {quality5}, {angle11}, {person1}, {style1}, {age1}, {face1}, {hairlength7}, {chest1}, {cloth6}, ({pose4}:1.1), {place5}, {light1}"

negative_prompt = "illustration,3d,sepia,painting,cartoons,sketch,(worst quality:2),((monochrome)),((grayscale:1.2)),(backlight:1.2),analog,analog photo,(bad hands, bad fingers, bad arms, bad legs, bad knees, bad navel:1.5),Shank Hair,(nipples:1.2), (muscle:1.1),(extra fingers, extra arms, extra legs, extra digit, fewer digits:1.5),(text:1.3), signature, missing limb, missing fingers, nipples, 2 persons"

def counter_file_check(counter=0):
    # スクリプトの実行回数の記録
    try:
        with open("C:/Users/mokos/Stable_Diffusion/sd.webui/webui/outputs/api_output/script_counter.txt", "r") as file:
            counter = int(file.read().strip()) + 1
    except FileNotFoundError:
        counter = 0

    # スクリプトの実行回数を追記する
    with open("C:/Users/mokos/Stable_Diffusion/sd.webui/webui/outputs/api_output/script_counter.txt", "w") as file:
        file.write(str(counter))

    return(counter)

def loop_crate_image(seed):
    for c in range(loop):

        payload = {
            # "sd_model_checkpoint": "BRAV5finalfp16.safetensors",
            # "sd_model_checkpoint": "chilloutmix_NiPrunedFp32Fix",
            # "enable_hr": True,
            "enable_hr": enable_hr,
            "denoising_strength": 0.3,
            "hr_scale": 2.05,
            "hr_upscaler": "LDSR",
            "prompt": prompt,
            "steps": 40,
            "seed": seed,
            "width": 540,
            "height": 960,
            "negative_prompt": negative_prompt,
            "sampler_index": "DPM++ SDE Karras",
            "override_settings": override_settings
        }

        response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

        r = response.json()

        for i in r['images']:
            image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

            png_payload = {
                "image": "data:image/png;base64," + i
            }
            response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

            pnginfo = PngImagePlugin.PngInfo()
            pnginfo.add_text("parameters", response2.json().get("info"))
            image.save(f'C:/Users/mokos/Stable_Diffusion/sd.webui/webui/outputs/api_output/{counter}-{c + 1}-seed[{seed}].png', pnginfo=pnginfo)

            # seed値に1を加えてループを終了(seed = -1 の場合はスルー)
            if seed == -1:
                seed = -1
            else:
                seed = seed + 1 

        print(f"image created : {c + 1}")
        print(f"Prompt : {prompt}")
        print(f"Negative : {negative_prompt}")

start_time = time.time() # スクリプトの開始時間
nows = datetime.now()

print(f"Start time: {nows.strftime('%Y-%m-%d %H:%M:%S')}")
counter = counter_file_check()
loop_crate_image(seed)

nowe = datetime.now()
print(f"End time: {nowe.strftime('%Y-%m-%d %H:%M:%S')}")

end_time = time.time() # 終了時間の記録
execution_time = end_time - start_time # 実行時間計算

# print(f"start_time : {start_time} s")
# print(f"end_time : {end_time} s")
print(f"Execution time : {execution_time} s")

m, s = divmod(execution_time, 60)
h, m = divmod(m, 60)
d, h = divmod(h, 24)

print(f"Execution time: {d} days, {h} hours, {m} minutes, {s} seconds")





























# import webuiapi

# api = webuiapi.WebUIApi(host='127.0.0.1', port=7860, sampler='DPM++ SDE Karras', steps=40)

# result1 = api.txt2img(prompt="cute squirrel",
#                       negative_prompt="ugly, out of frame",
#                       seed=-1,
#                       styles=["anime"],
#                       cfg_scale=7,
#                       sampler_index='DDIM',
#                       steps=30,
#                       enable_hr=True,
#                       hr_scale=2,
#                       hr_upscaler=webuiapi.HiResUpscaler.LDSR,
#                       hr_second_pass_steps=20,
#                       denoising_strength=0.4
#                       )
# result2 = api.txt2img(prompt="cute squirrel",
#                       negative_prompt="ugly, out of frame",
#                       seed=-1,
#                       styles=["anime"],
#                       cfg_scale=7,
#                       sampler_index='DDIM',
#                       steps=30,
#                       enable_hr=True,
#                       hr_scale=2,
#                       hr_upscaler=webuiapi.HiResUpscaler.LDSR,
#                       hr_second_pass_steps=20,
#                       denoising_strength=0.4
#                       )

# print(result1.images)
# result1.image
# print(result1.info)
# print(result1.parameters)
# result1.image.save('output1.png')
# result2.image.save('output2.png')

## payload
# {
#   "enable_hr": false,
#   "denoising_strength": 0,
#   "firstphase_width": 0,
#   "firstphase_height": 0,
#   "hr_scale": 2,
#   "hr_upscaler": "string",
#   "hr_second_pass_steps": 0,
#   "hr_resize_x": 0,
#   "hr_resize_y": 0,
#   "hr_sampler_name": "string",
#   "hr_prompt": "",
#   "hr_negative_prompt": "",
#   "prompt": "",
#   "styles": [
#     "string"
#   ],
#   "seed": -1,
#   "subseed": -1,
#   "subseed_strength": 0,
#   "seed_resize_from_h": -1,
#   "seed_resize_from_w": -1,
#   "sampler_name": "string",
#   "batch_size": 1,
#   "n_iter": 1,
#   "steps": 50,
#   "cfg_scale": 7,
#   "width": 512,
#   "height": 512,
#   "restore_faces": false,
#   "tiling": false,
#   "do_not_save_samples": false,
#   "do_not_save_grid": false,
#   "negative_prompt": "string",
#   "eta": 0,
#   "s_min_uncond": 0,
#   "s_churn": 0,
#   "s_tmax": 0,
#   "s_tmin": 0,
#   "s_noise": 1,
#   "override_settings": {},
#   "override_settings_restore_afterwards": true,
#   "script_args": [],
#   "sampler_index": "Euler",
#   "script_name": "string",
#   "send_images": true,
#   "save_images": false,
#   "alwayson_scripts": {}
# }


# prompt = f"(RAW photo, masterpiece, 8k, best quality),\
        #   huge breasts, breasts cleavage,\
        #   looking at viewer, 18 years old,\
        #   extremely cute girl, (faint smile:1.1),\
        #   short bob, brown hair, (hands behind head:1.2), model,\
        #   extremely detailed baby face, extremely detailed, skin, extremely detailed legs,\
        #   armpits, {cloth},\
        #   outside,"

# prompt = f"(RAW photo, masterpiece, 8k, best quality),\
#           huge breasts, breasts cleavage,\
#           looking at viewer, 18 years old,\
#           extremely cute girl, (faint smile:1.1),\
#           short bob, brown hair, model,\
#           extremely detailed baby face, extremely detailed skin, extremely detailed legs,\
#           dance, {cloth}, \
#           outside,"
