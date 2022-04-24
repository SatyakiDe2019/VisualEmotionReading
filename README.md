# VisualEmotionReading

## About this app

This computer-vision app will visually read the human emotions from any video or Web-CAM in real-time. This application developed using Open-CV & another brilliant model calls DeepFace. This project is for the intermediate Python developer & Data Science Newbi's.


## How to run this app

(The following instructions apply to Posix/bash. Windows users should check
[here](https://docs.python.org/3/library/venv.html).)

First, clone this repository and open a terminal inside the root folder.

Create and activate a new virtual environment (recommended) by running
the following:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Run the model Visual Reading-App:

```bash
python peopleEmotionRead.py
```

Make sure that you are properly connected with a functional WebCam (Preferably a separate external WebCam) & mount that at a pre-defined distance from the subjects.

## Screenshots

![demo.GIF](demo.GIF)

## Resources

- To learn more about Open-CV, check out our [documentation](https://opencv.org/opencv-free-course/).
- To learn more about DeepFace, check out our [documentation](https://pypi.org/project/deepface/).
- To view the complete demo with sound, check out our [YouTube Page](https://youtu.be/HpAtddSGUNE).
