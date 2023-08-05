# Multiple image stack with cv2 (calculates height/width)

```python
# Tested with:
# Python 3.9.13
# Windows 10

pip install cv2-multistack

from cv2_multistack import hstack_multiple_pics, vstack_multiple_pics


# Allowed image formats: url/path/buffer/base64/PIL/np
listofpics = [
"""https://raw.githubusercontent.com/hansalemaos/screenshots/main/cv2_putTrueTypeText_000008.png""",
"""https://raw.githubusercontent.com/hansalemaos/screenshots/main/cv2_putTrueTypeText_000009.png""",
"""https://raw.githubusercontent.com/hansalemaos/screenshots/main/cv2_putTrueTypeText_000010.png""",
"""https://raw.githubusercontent.com/hansalemaos/screenshots/main/cv2_putTrueTypeText_000011.png""",
"""https://raw.githubusercontent.com/hansalemaos/screenshots/main/cv2_putTrueTypeText_000012.png""",
"""https://raw.githubusercontent.com/hansalemaos/screenshots/main/cv2_putTrueTypeText_000013.png""",
"""https://raw.githubusercontent.com/hansalemaos/screenshots/main/cv2_putTrueTypeText_000014.png""",
"""https://raw.githubusercontent.com/hansalemaos/screenshots/main/cv2_putTrueTypeText_000015.png""",

]

bibi1=hstack_multiple_pics(listofpics, height=100, channels=3)
bibi2=vstack_multiple_pics(listofpics, width=100, channels=3)

```



<img title="" src="https://github.com/hansalemaos/screenshots/raw/main/multistack1.png" alt="">



<img title="" src="https://github.com/hansalemaos/screenshots/raw/main/multistack2.png" alt="">


