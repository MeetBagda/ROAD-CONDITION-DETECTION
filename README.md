# Road Condition Identifier

## Table of Contents

*   [Project Overview](#project-overview)
*   [Key Features](#key-features)
*   [Example Predictions](#example-predictions)
*   [Getting Started](#getting-started)
    *   [Prerequisites](#prerequisites)
*   [Future Work](#future-work)
*   [Contributing](#contributing)

## Project Overview

The Road-Condition-Identifier is an object detection system designed to automatically identify various types of road damage from images. It leverages the power of AI and computer vision to detect and classify road conditions such as potholes, cracks (alligator, block, longitudinal, transverse), other corruption, and repairs. This information can be used to:

*   **Improve road maintenance:** By providing timely and accurate data about road conditions, infrastructure management agencies can prioritize repairs and allocate resources more effectively.
*   **Enhance driver safety:** Real-time road condition information can be integrated into navigation systems or driver-assistance systems to warn drivers of potential hazards.
*   **Automate road surveys:** Eliminate the need for manual road inspections, saving time and resources.
*   **Create detailed road condition maps:** Visualize road damage over geographic areas for better infrastructure planning and analysis.

This project aims to provide an accurate, efficient, and scalable solution for road condition monitoring, using a readily available and powerful deep learning framework. This current iteration focuses on training a robust model using a diverse image dataset. Mobile development and model hyperparameter tuning are ongoing.

## Key Features

*   **Object Detection:** Identifies and localizes road damage within images using bounding boxes.
*   **Multi-Class Classification:** Distinguishes between several types of road damage, including:
    *   Alligator crack
    *   Block crack
    *   Longitudinal crack
    *   Transverse crack
    *   Pothole
    *   Other corruption
    *   Repair
*   **YOLOv8 Based:** Built on the state-of-the-art YOLOv8 object detection model, known for its speed and accuracy.
*   **PyTorch Implementation:** Leverages the flexibility and power of the PyTorch deep learning framework.
*   **Customizable:** Easy to adapt to different datasets and road conditions.
*   **Successful Detections:** The model demonstrates robust object detection capabilities across various road conditions and environments. See the example predictions below!

## Example Predictions

The following images showcase the model's ability to accurately identify and classify road damage in various scenarios:

![Prediction 1](https://github.com/user-attachments/assets/50e70a86-3583-4d31-a1aa-3402c56592d3)
*The model accurately detects transverse cracks and other road defects.*

![Prediction 2](https://github.com/user-attachments/assets/7029928f-bd89-40ef-930b-daba4e76272d)

*Detection of alligator cracking in challenging lighting conditions.*

![Prediction 3](https://github.com/user-attachments/assets/353155ad-5215-431d-b392-a6a9bc941f40)

*Robust pothole detection, even with partial visibility.*

![Prediction 4](https://github.com/user-attachments/assets/c8ee9e5c-e1c3-4c01-a8a3-52f0257f5717)

*Detection of longitudinal crack.*

![Prediction 5](https://github.com/user-attachments/assets/c36bae4f-593f-4c85-8c8b-a4db75d9e78c)

*Another Detection of longitudinal crack.*

![Prediction 6](https://github.com/user-attachments/assets/2a8195e5-3d88-4cd0-b049-2fdd6cf81d34)

*Example of repair mark detection.*

_Note: These images are for illustrative purposes and may not represent the model's performance on all datasets. The model is continually being improved._

## Getting Started

  ### Prerequisites

*   Python 3.7+
*   [PyTorch](https://pytorch.org/)
*   CUDA (if you want to use a GPU for faster training and inference)
*   Required Python packages (install using `pip install -r requirements.txt`)

## Future Work

*   **Mobile Development:** Developing a mobile app for real-time road condition detection using smartphone cameras. This would allow for crowdsourced data collection and provide drivers with immediate feedback on road hazards.
*   **Hyperparameter Tuning:** Optimizing the model's hyperparameters to further improve its accuracy and performance using techniques such as grid search or Bayesian optimization.
*   **Expand Class Support:** Adding support for new road damage classes, such as "rutting" or "raveling," to provide a more comprehensive road condition assessment.
*   **Real-time integration with navigation apps**: Integrate the model output to navigation apps to provide driver with real-time road condition information.
*   **Improve dataset**: Improving dataset diversity to support variety of road conditions and background.
*   **Add depth estimation**: Use methods to estimate the depth of the detected road damages for further assessments.

## Contributing

We welcome contributions to the Road-Condition-Identifier project! If you have ideas for new features, improvements, or bug fixes, please submit a pull request.

