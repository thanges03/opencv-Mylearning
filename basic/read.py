import cv2 as cv

# Load video from path
capture = cv.VideoCapture('video')

# Read and display video frame-by-frame
while True:
    isvalid, frame = capture.read()
    
  # If video ended or frame couldn't be read
    if not isvalid or frame is None:
        print("Error: Could not read frame")
        break  # Exit if the video can't be read

    # Display the frame
    cv.imshow('Video', frame)
    # Break if 'd' key is pressed
    if cv.waitKey(29) & 0xFF == ord('d'):
        break
# Release resources
capture.release()
cv.destroyAllWindows()
