# DepthSense-Volume-Calculation
 Leveraging YOLO and Intel RealSense camera to compute precise volumes swiftly. Ideal for robotics, logistics, and industrial applications, ensuring efficient spatial analysis and object measurement

# Project Setup and Execution Guide

This guide provides step-by-step instructions to set up a Conda environment, install the necessary dependencies, and run the `measure.py` script.

## Prerequisites

- [Anaconda/Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed on your system.

## Setup Instructions

### 1. Create a Conda Environment

First, create a Conda environment with Python 3.11:

```bash
conda create -n myenv python=3.11
```
if the pyrealsense is not working then try lower versions of the pyrealsense
```bash
pip install pyrealsense
pip install opencv-python numpy
pip install matplotlib scipy pandas torch torchvision torchaudio
```
```bash
run the file 
python3 file_name 
```
### Volume Calculation Methodology

The script `object_detection_volume.py` captures frames from a RealSense camera, detects objects in the color image, and calculates the volume of each detected object based on depth data:

1. **Object Detection**: Using the `ObjectDetection` class, objects are detected in the `color_image`. Bounding boxes (`bboxes`) with their class IDs (`class_ids`) and confidence scores (`scores`) are obtained.

2. **Bounding Box Processing**: For each detected object:
   - The bounding box coordinates (`x, y, x2, y2`) are used to define the region of interest in both the color and depth images.
   - The area of the bounding box in square centimeters (`area`) is calculated from its pixel dimensions.

3. **Depth Data Extraction**: 
   - The depth values within the bounding box (`bbox_depth`) are extracted from the `depth_image`.
   - The maximum (`max_depth`) and minimum (`min_depth`) depth values within the bounding box are computed in centimeters.

4. **Volume Calculation**: 
   - The volume of the object is estimated using the formula:
     ```
     volume = area * |max_depth - min_depth|
     ```
     where `|max_depth - min_depth|` represents the absolute difference between the maximum and minimum depths.

5. **Visualization**: 
   - The color image is annotated with bounding boxes, class names, and calculated volume, displayed in real-time.



