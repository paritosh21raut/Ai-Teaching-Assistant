import cv2
import numpy as np
import textwrap

def show_slide(title, summary, image_path=None):
    width = 1280
    height = 720

    # White background
    slide = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Title
    cv2.putText(slide, title,
                (50, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (0, 0, 0),
                2)

    # Wrap summary text
    wrapped_text = textwrap.wrap(summary, width=60)

    y_offset = 150
    for line in wrapped_text[:10]:  # limit lines
        cv2.putText(slide, line,
                    (50, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (50, 50, 50),
                    1)
        y_offset += 35

    # Add image if exists
    if image_path:
        img = cv2.imread(image_path)
        if img is not None:
            img = cv2.resize(img, (400, 300))
            slide[350:650, 800:1200] = img

    cv2.namedWindow("Teaching Assistant", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Teaching Assistant", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Teaching Assistant", slide)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
