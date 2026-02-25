import sys
try:
    from PIL import Image
    
    img = Image.open("newvers.jpeg")
    target_size = (1280, 800)
    
    img_ratio = img.width / img.height
    target_ratio = target_size[0] / target_size[1]
    
    if img_ratio > target_ratio:
        new_height = target_size[1]
        new_width = int(new_height * img_ratio)
        img = img.resize((new_width, new_height), getattr(Image, 'Resampling', Image).LANCZOS)
        left = (new_width - target_size[0]) / 2
        top = 0
        right = (new_width + target_size[0]) / 2
        bottom = target_size[1]
        img = img.crop((left, top, right, bottom))
    else:
        new_width = target_size[0]
        new_height = int(new_width / img_ratio)
        img = img.resize((new_width, new_height), getattr(Image, 'Resampling', Image).LANCZOS)
        left = 0
        top = (new_height - target_size[1]) / 2
        right = target_size[0]
        bottom = (new_height + target_size[1]) / 2
        img = img.crop((left, top, right, bottom))
    
    img = img.convert("RGB")
    img.save("newvers.png", format="PNG")
    print("Success")
except Exception as e:
    print(f"Error: {e}")
