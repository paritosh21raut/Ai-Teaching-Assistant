import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import textwrap

def show_slide(title, summary, image_path=None):
    width = 1280
    height = 720

    # Create white canvas
    slide = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(slide)

    # Load system font
    title_font = ImageFont.truetype("arial.ttf", 48)
    body_font = ImageFont.truetype("arial.ttf", 28)

    # Draw title
    draw.text((60, 40), title, font=title_font, fill="black")

    # Wrap summary
    wrapped_text = textwrap.wrap(summary, width=70)

    y_offset = 140
    for line in wrapped_text:
        if y_offset > 600:
            break
        draw.text((60, y_offset), line, font=body_font, fill=(40, 40, 40))
        y_offset += 40

    # Add image
    if image_path:
        try:
            img = Image.open(image_path)
            img = img.resize((400, 300))
            slide.paste(img, (820, 350))
        except:
            pass

    # Convert PIL image to OpenCV format
    slide_np = np.array(slide)
    slide_np = cv2.cvtColor(slide_np, cv2.COLOR_RGB2BGR)

    cv2.namedWindow("Teaching Assistant", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Teaching Assistant", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Teaching Assistant", slide_np)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
