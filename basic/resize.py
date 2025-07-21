import cv2 as cv

# Load video file from path
capture = cv.VideoCapture('#video')

# Function to change webcam resolution (useful for live camera)
def changeRes(width, height):
    capture.set(3, width)  # Property 3 is width
    capture.set(4, height) # Property 4 is height

# Function to rescale frames (works for images, videos, and webcam frames)
def rescale(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Read and display video frames in a loop
while True:
    isvalid, frame = capture.read()

    if not isvalid or frame is None:
        print("Error: Could not read frame or end of video.")
        break

    resized_frame = rescale(frame)

    cv.imshow('Original Video', frame)
    cv.imshow('Resized Video', resized_frame)

    # Exit when 'd' is pressed
    if cv.waitKey(29) & 0xFF == ord('d'):
        print("Video stopped by user.")
        break

# Release video capture and close all OpenCV windows
capture.release()
cv.destroyAllWindows()
