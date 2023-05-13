# Inttelligent Video Surveillance System using YOLO and OpenCV

This is a project to perform object detection, fall detection, car crash detection and social distancing detection.

# Software Required
- Python(v3.9): Language in which code is written
- CMake(v3.25.2): For compiling openCV
- Visual Studio Code: For building openCV and darknet code
- Nvidia GPU Driver: For faster GPU performance
- CUDA(v12.0): For parallel computing using GPU
- CuDNN(8.8.0): A GPU-accelerated library of primitives for deep neural networks
- OpenCV(v4.7.0): For working on images/videos in python
- Darknet: Neural network framework for YOLO

You can follow the two part YouTube videos of [Augmented Startups](https://www.youtube.com/watch?v=5pYh1rFnNZs&ab_channel=AugmentedStartups)

# Deployment
We have deployed our project using Flask framework. Our website is hosted onto a local server and we can use that website to perform detections
on videos using Youtube video as input.

## Runing the script
```
python app.py
```

# Website

## Home Page

![Intelligent Video Survillance System - Google Chrome 13-05-2023 16_02_25](https://github.com/anubhavshail/Video_analyzer/assets/75006992/9d804ec4-5de1-4bdf-a9ef-671a03284c31)


## Fall Detection Page

![Intelligent Video Survillance System - Google Chrome 13-05-2023 16_03_48](https://github.com/anubhavshail/Video_analyzer/assets/75006992/8b902dcc-8019-4dfd-8e68-afe869c021b9)
![Intelligent Video Survillance System - Google Chrome 13-05-2023 16_04_33](https://github.com/anubhavshail/Video_analyzer/assets/75006992/ef993998-5f9b-4ea7-b987-63bc54f76b2c)


## Car Crash Detection Page

![Intelligent Video Survillance System - Google Chrome 13-05-2023 16_04_49](https://github.com/anubhavshail/Video_analyzer/assets/75006992/d286b8b5-1cd4-427d-951b-6dd5f847c1f2)
![Intelligent Video Survillance System - Google Chrome 13-05-2023 16_06_25](https://github.com/anubhavshail/Video_analyzer/assets/75006992/dd4d08b6-12e9-4141-9c65-551583380141)


## Social Distancing Detection Page

![Intelligent Video Survillance System - Google Chrome 13-05-2023 16_07_01](https://github.com/anubhavshail/Video_analyzer/assets/75006992/412ae985-3275-409a-a214-cf39f94dc80a)
![social - Notepad 13-05-2023 16_10_15](https://github.com/anubhavshail/Video_analyzer/assets/75006992/a90eaf84-1fdf-4dc4-bf8b-9dc53fa62be5)


## Object Detection Page

![Intelligent Video Survillance System - Google Chrome 13-05-2023 16_10_48](https://github.com/anubhavshail/Video_analyzer/assets/75006992/ba7cfedc-399e-4e35-b8c3-850619efe319)
![Intelligent Video Survillance System - Google Chrome 13-05-2023 16_11_12](https://github.com/anubhavshail/Video_analyzer/assets/75006992/b0abde0a-595b-427b-9fc0-1a4e9f569b34)

# File Structure
```
.
└── YOLOv4
    └── darknet-master
        └── build              # compiled files
            └── darknet
                └── x64
                    ├── env
                    ├── static
                    │   ├── css
                    │   │   ├── styles.css
                    │   │   ├── styles1.css
                    │   │   └── styles2.css
                    │   └── images
                    ├── templates              # template files
                    │   ├── CarCrashDetection.html
                    │   ├── FallDetection.html
                    │   ├── index.html
                    │   ├── ObjectDetection.html
                    │   ├── SocialDistancingDetection.html
                    │   └── video.html
                    ├── a.py
                    ├── app.py             # main file for YOLO website
                    ├── object.py
                    └── requirements       # required packages for app.py
 ```
