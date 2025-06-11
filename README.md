# InvisiCloth_Real_Time_Invisibility_Cloak-

## Overview: 
Inspired by the magical cloak from the Harry Potter series, this project implements a real-time invisibility effect using computer vision. By detecting a specific color on a moving cloth and dynamically replacing it with the background, the application gives the illusion that the user has vanished from the frame. This project demonstrates key image processing and masking techniques using live video feeds.

## 🧰 Tech Stacks: 
Python – For core scripting and control logic

OpenCV – For video capture, color space transformation, and real-time image operations

NumPy – For efficient array manipulation during mask and frame processing


## 🧩 System Architecture: 
1. Background Capture → 2. Cloth Detection via HSV Mask → 3. Image Blending → 4. Real-Time Display

Background Capture: Captures a static background frame when the user is not visible, serving as the reference for the invisibility effect.

Cloth Detection: Uses HSV color space to generate a mask of the cloak, refined with morphological transformations (e.g., dilation, erosion).

Image Blending: Applies bitwise operations to replace the detected cloak region with the background, producing a convincing invisibility effect.

Live Rendering: Continuously processes and displays the transformed video frames with minimal latency.

