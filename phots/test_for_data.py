import cv2
import os
import git
from datetime import datetime

# GitHub repository details
REPO_PATH = '/home/manohar/Desktop/Volume/h/DepthSense-Volume-Calculation'  # Path to your local clone of the GitHub repo
REPO_URL = 'git@github.com:Maneeshbhaskarpulidindi/APP_for_data.github.io.git'
NUM_IMAGES = 10  # Number of images to capture

# Capture multiple images using OpenCV
def capture_images(num_images):
    captured_files = []
    cap = cv2.VideoCapture(0)  # Use the default camera
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return None
    
    for i in range(num_images):
        ret, frame = cap.read()
        if ret:
            filename = f'captured_image_{i + 1}.jpg'
            cv2.imwrite(filename, frame)
            captured_files.append(filename)
            print(f"Image {filename} saved.")
            # Optional: Delay between captures
            # time.sleep(1)
        else:
            print(f"Error: Could not capture image {i + 1}.")
    
    cap.release()
    return captured_files

# Push changes to GitHub
def push_to_github(file_paths):
    # Clone the repository if not already cloned
    if not os.path.exists(REPO_PATH):
        print(f"Cloning repository from {REPO_URL}...")
        git.Repo.clone_from(REPO_URL, REPO_PATH)
    
    # Open the repository
    repo = git.Repo(REPO_PATH)
    
    for file_path in file_paths:
        # Copy files to the repo directory
        os.rename(file_path, os.path.join(REPO_PATH, file_path))
    
    # Commit and push all files
    repo.git.add('*')  # Add all files in the repo directory
    commit_message = f'Add {len(file_paths)} new images on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push()
    print("Changes pushed to GitHub.")

if __name__ == '__main__':
    image_files = capture_images(NUM_IMAGES)
    if image_files:
        push_to_github(image_files)

