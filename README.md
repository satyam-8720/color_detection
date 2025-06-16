# 🎨 Color Detection Using OpenCV

This project detects a specific color (Yellow by default) from webcam input using OpenCV in Python. It converts the color to HSV space and finds contours matching the color range.

## 🚀 Features

- Detects objects of a specified BGR color in real-time
- Automatically calculates the HSV range around the target color
- Highlights detected regions with a green bounding box
- Ignores small noisy regions

## 📷 Example Use Case

Detect objects like a yellow ball, post-it, or toy using the webcam.

## 🛠 Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

## 📦 Installation

```bash
pip install opencv-python numpy
```

## 💡 How It Works

- Convert input BGR color to HSV
- Calculate a range around the HSV value
- Use `cv.inRange()` to create a mask
- Find and draw contours on detected objects

## 🧪 Sample Code

```python
import cv2 as cv
import numpy as np

def getlimit(color):
    bgr = np.uint8([[color]])
    hsvc = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)
    lower_limit = np.array([max(hsvc[0][0][0] - 10, 0), 100, 100], dtype='uint8')
    upper_limit = np.array([min(hsvc[0][0][0] + 10, 179), 255, 255], dtype='uint8')
    return lower_limit, upper_limit

bgr_color = [0, 255, 255]  # Yellow
lower_limit, upper_limit = getlimit(bgr_color)

vid = cv.VideoCapture(0)

while True:
    isTrue, frame = vid.read()
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv_frame, lower_limit, upper_limit)
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 500:
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.imshow("detected", frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

vid.release()
cv.destroyAllWindows()
```

## 🎛️ Customization

To detect a different color, change the `bgr_color` list. Example:

```python
bgr_color = [255, 0, 0]  # Blue
```

## 🧹 Exit Instructions

Press the `d` key while the webcam window is active to stop the detection and exit.

## 📄 License

MIT License

---

Made with ❤️ using Python and OpenCV.