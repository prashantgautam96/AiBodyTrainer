# Pose Estimation AI Trainer

## Introduction
This project is a Pose Estimation AI Trainer that uses computer vision to track and analyze body movements. It's designed to help users improve their physical exercises by providing real-time feedback on their form and performance.

## Features
- Video capture from file
- Real-time pose detection
- Angle calculation for specific body parts
- Percentage calculation for exercise completion
- Visual feedback through progress bar
- Counting repetitions of exercises
- Displaying frames per second (FPS) for performance monitoring

## Technologies Used
- Python
- OpenCV
- NumPy
- Custom `poseModule` for pose detection

## Setup and Installation
1. Ensure you have Python installed on your system.
2. Install the required libraries using `pip install opencv-python numpy`.
3. Clone the repository to your local machine.
4. Place your video files in the `poseVideos` directory.

## Usage
Run the script with `python AiTrainer.py` to start the pose estimation. Make sure you're in the correct directory and have a video file named `2.mp4` in the `poseVideos` folder.

## How It Works
The script captures video frames and processes them to detect human poses. It calculates the angle between joints and uses this information to estimate the completion percentage of an exercise. It also provides a visual progress bar and counts the repetitions.

## Contributing
Contributions to the project are welcome! Please fork the repository and submit a pull request with your features or fixes.


## Acknowledgements
Special thanks to the OpenCV and NumPy communities for their invaluable resources and support.
