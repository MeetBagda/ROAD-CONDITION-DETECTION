# convert_annotations.py
import json
import os
from tqdm import tqdm
import glob

def convert_annotation(json_file, output_dir, class_map):
    """Converts a JSON annotation to YOLO format."""
    with open(json_file, 'r') as f:
        data = json.load(f)

    img_width = data['size']['width']
    img_height = data['size']['height']
    image_name = os.path.splitext(os.path.basename(json_file))[0].replace(".jpg", "")

    txt_file = os.path.join(output_dir, f"{image_name}.txt")

    with open(txt_file, 'w') as outfile:
        for obj in data['objects']:  # Iterate through objects, not shapes
            label = obj['classTitle'] # Access the class title from object
            if label not in class_map:
                print(f"Warning: Label '{label}' not found in class map. Skipping.")
                continue
            class_id = class_map[label]
            points = obj['points']['exterior'] #access points

            # Get bounding box coordinates
            x1, y1 = points[0]
            x2, y2 = points[1]


            x_center = ((x1 + x2) / 2) / img_width
            y_center = ((y1 + y2) / 2) / img_height
            width = abs(x2 - x1) / img_width
            height = abs(y2 - y1) / img_height

            outfile.write(f"{class_id} {x_center} {y_center} {width} {height}\n")


if __name__ == "__main__":
    # Define your class mapping here.  IMPORTANT: The IDs MUST start from 0.
    class_map = {
        'alligator crack': 0,
        'block crack': 1,
        'longitudinal crack': 2,
        'other corruption': 3,
        'pothole': 4,
        'repair': 5,
        'transverse crack': 6,
    }

    dataset_dir = "dataset" # Update with the root directory
    train_ann_dir = os.path.join(dataset_dir, "train", "ann")
    test_ann_dir = os.path.join(dataset_dir, "test", "ann")

    output_train_dir = os.path.join(dataset_dir, "train", "labels")  # Create this directory
    output_test_dir = os.path.join(dataset_dir, "test", "labels")  # Create this directory

    os.makedirs(output_train_dir, exist_ok=True)
    os.makedirs(output_test_dir, exist_ok=True)

    print("Converting training annotations...")
    for json_file in tqdm(glob.glob(os.path.join(train_ann_dir, "*.json"))):
        convert_annotation(json_file, output_train_dir, class_map)

    print("Converting testing annotations...")
    for json_file in tqdm(glob.glob(os.path.join(test_ann_dir, "*.json"))):
        convert_annotation(json_file, output_test_dir, class_map)

    print("Conversion complete!")