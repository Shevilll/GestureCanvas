# GestureCanvas

**GestureCanvas** is an intuitive digital drawing application that uses hand gestures to control various drawing tools. Designed for a range of applications including education, creative tasks, and professional presentations, GestureCanvas offers a seamless and interactive experience for users by leveraging real-time hand tracking and gesture recognition.

## Features

-   **Gesture-Based Controls:**

    -   **Index Finger:** Draw or erase on the canvas.
    -   **Index and Middle Fingers:** Select different tools such as brushes and erasers.

-   **Customizable Tools:**

    -   **Brushes:** Three different colors with adjustable sizes.
    -   **Eraser:** Allows erasing parts of the drawing with adjustable thickness.

-   **Real-Time Visual Feedback:** Immediate visual response to gestures, ensuring an intuitive and responsive drawing experience.

## How It Works

GestureCanvas uses your device's webcam to capture hand movements. It detects the position of your index and middle fingers to perform various actions on the canvas. The application includes the following components:

-   **Hand Tracking Module:** Detects and tracks hand landmarks using MediaPipe.
-   **Gesture Detection:** Differentiates between drawing and selection gestures.
-   **Canvas Rendering:** Draws or erases on the canvas based on detected gestures.

## Application Areas

GestureCanvas is versatile and can be used in:

-   **Education:** Teachers and students can use it as a digital whiteboard.
-   **Creative Tasks:** Artists can create digital art using gestures.
-   **Professional Presentations:** Presenters can use it to annotate slides or explain concepts interactively.

## Installation

To use GestureCanvas, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Shevilll/GestureCanvas.git
    ```
2. **Run the Application:**
    ```bash
    python GestureCanvas.py
    ```

## Usage

1. **Start the application** and ensure your webcam is active.
2. **Choose a tool** by raising both your index and middle fingers and selecting from the options at the top.
3. **Draw or erase** by lowering your middle finger and using your index finger to perform actions on the canvas.
4. **Adjust tool settings** by selecting different brush sizes and colors.

## Data Flow Diagram

The Data Flow Diagram (DFD) for GestureCanvas provides a clear overview of how data flows through the system:

1. **Capture Image:** Continuously captures images from the camera.
2. **Detect Hand and Finger Gestures:** Processes the captured images to identify hand gestures.
3. **Process Gestures:** Determines the action (draw, erase, select) based on the detected gestures.
4. **Render Drawing:** Updates the canvas in real-time according to the user's gestures.

## Merits

-   **User-Friendly Interface:** Simple and intuitive controls that are easy to learn.
-   **Real-Time Response:** Immediate visual feedback for a smooth drawing experience.
-   **Versatile Application:** Suitable for various use cases, from education to professional presentations.
-   **No Specialized Hardware Needed:** Works with any standard webcam.

## Demerits

-   **Lighting Dependence:** Performance may vary based on lighting conditions and camera quality.
-   **Gesture Recognition Accuracy:** May not always accurately detect gestures, leading to unintended actions.
-   **Limited Toolset:** Focuses on basic drawing tools; lacks advanced features found in professional drawing applications.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to improve the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

-   **MediaPipe**: For providing the hand tracking solution.
-   **OpenCV**: For image processing and rendering.
