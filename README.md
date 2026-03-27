# Face Recognition Alarm

A real-time face detection application that uses your webcam to detect faces and plays an alarm sound when a face is detected. Built with OpenCV and Kivy.

## Tech Stack

- **Python** with OpenCV (cv2) for face detection
- **Kivy** for the GUI / live camera feed display
- **plyer** for desktop notifications
- **playsound** for alarm audio playback
- **Threading** for non-blocking alarm playback

## How It Works

1. Opens the default webcam and displays a live video feed in a Kivy window
2. Runs Haar cascade face detection on each frame
3. When a face is detected, plays an alarm sound (`sound.mp3`)
4. Cooldown of 5 seconds between alarms to avoid spam

## Setup

1. Install dependencies:
   ```bash
   pip install opencv-python kivy plyer playsound
   ```

2. Ensure `sound.mp3` is in the project root directory.

3. Run the application:
   ```bash
   python main.py
   ```

## Requirements

- Python 3.7+
- A working webcam
