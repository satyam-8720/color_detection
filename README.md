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

## 🎛️ Customization

To detect a different color, change the `bgr_color` list. Example:

```python
bgr_color = [255, 0, 0]  # Blue
```

## 🧹 Exit Instructions

Press the `d` key while the webcam window is active to stop the detection and exit.


## 📄 License

None

---

Made with ❤️ using Python and OpenCV.
## AUTHOR....
 SATYAM

