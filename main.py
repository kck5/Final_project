import streamlit as st
import cv2
import mediapipe as mp

# Initialize mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Define functions
def process_frame(frame):
    # Hand detection
    results = hands.process(frame)
    hand_landmarks = results.multi_hand_landmarks

    # Check for detected hand
    if hand_landmarks:
        # Extract landmark points
        landmark_list = hand_landmarks[0].landmark
        # Calculate object dimensions (replace with specific logic)
        dimensions = calculate_dimensions(landmark_list)
        # Display dimensions
        st.write(f"Object dimensions: {dimensions}")

        # Optionally draw hand landmarks
        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    return frame

# Main app
def main():
    # Initialize video capture
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame
        success, frame = cap.read()

        # Process frame and get dimensions
        frame = process_frame(frame)

        # Display video
        st.image(frame)

        # Close on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
