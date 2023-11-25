# video_intro.py

import cv2
import pygame

def play_video_intro(video_file, bgm_file):
    # Initialize Pygame
    pygame.init()

    # Load background music
    pygame.mixer.music.load(bgm_file)
    pygame.mixer.music.play(-1)  # -1 means loop indefinitely

    # Open a video file
    cap = cv2.VideoCapture(video_file)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    # Get the frames per second (fps) of the video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Create a window to display the video
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)

    # Adjust this value to synchronize video and audio
    frame_delay = 5  # Experiment with different values

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Display the frame
        cv2.imshow('Video', frame)

        # Adjust the frame delay to synchronize video and audio
        pygame.time.delay(int(1000 / fps) - frame_delay)

        # Exit on any key press
        if cv2.waitKey(1) & 0xFF != 255:
            break

    # Release the video capture object
    cap.release()
    cv2.destroyAllWindows()

    # Stop and quit Pygame
    pygame.mixer.music.stop()
    pygame.quit()
