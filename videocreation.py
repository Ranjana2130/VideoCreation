import cv2
import os

path = "C:/Users/akash.patwa/OneDrive/Desktop/BlockVerse/Images"
output_video_path = "C:/Users/akash.patwa/OneDrive/Desktop/BlockVerse/Sunset.mp4"
video_secs = 1

images = []

# Collect all image paths with the valid extensions
for file in os.listdir(path):
    # Separate the name and extension
    name, extension = os.path.splitext(file)
    if extension.lower() in ['.jpg', '.jpeg']:
        file_name = os.path.join(path, file)
        images.append(file_name)

# Ensure there are images to process
if images:
    # Read the first image to get dimensions
    frame = cv2.imread(images[0])
    if frame is None:
        raise ValueError("Could not read the first image. Check the image paths.")
    height, width, layers = frame.shape
    print("Frame dimensions:", height, width, layers)

    # Create the video writer object
    video = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), 1.0, (width, height))

    # Add each image to the video
    for img in images:
        image_frame = cv2.imread(img)
        if image_frame is not None:
            for _ in range(video_secs):
                video.write(image_frame)
        else:
            print(f"Warning: Image {img} could not be read.")

    # Release resources
    cv2.destroyAllWindows()
    video.release()
    print("Video creation complete.")
else:
    print("No images found in the specified directory.")
