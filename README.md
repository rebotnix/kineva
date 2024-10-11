# WELCOME TO KINEVA

![Bildschirmfoto 2024-10-11 um 11 25 30](https://github.com/user-attachments/assets/5d81e013-4741-4c31-b047-7d6e8a2498ad)

Welcome to the repository for KINEVA, a selection of pre-trained computer vision models designed for a wide range of object detection tasks. This model is ideal for various applications, including complex scenes with challenging lighting and noise conditions, such as low-light security footage.

Comparison with Other Models
In this repository, we've also compared KINEVA Model 1 with other well-known pre-trained models like YOLO 8 and YOLO 11. 

[![YouTube Video](https://github.com/user-attachments/assets/41baa766-790b-4fc1-b591-58328e61f78f)](https://www.youtube.com/watch?v=24NAldaw_PU)

#Below is an overview of the performance across various test images:
<p align="center">
  <img src="https://github.com/user-attachments/assets/7383af12-c57e-4ccc-904f-d4d81f81283c" height="200"/>
  <img src="https://github.com/user-attachments/assets/549fac74-c8b3-4aeb-9c4a-293c54be829e" height="200"/>
  <img src="https://github.com/user-attachments/assets/cc1be9d4-dc9a-4834-b0b2-c3ee6411045f" height="200"/>
</p>


| Model           | PARAMS | MAP  | STATE       | CATEGORIES               | TYPE   | VERSION |
|-----------------|--------|------|-------------|--------------------------|--------|---------|
| KINEVA Model 1  | 40M    | 75.3 | RELEASED    | HEAD PERSON NEGATIVES     | VISION | 0.2B    |
| KINEVA Model 2  | >80M   | -    | IN TRAINING | HEAD PERSON NEGATIVES BG  | VISION | -       |

# Production
This is our first model, use it with your own risk. 

# Model architecture
TBA

# Application:
Security, Smart City, Robotics, Research

# Download KINEVA model
The model 1 is released in the models folder.

# License:
KINEVA Non-Commercial License (KNCL)
Version 1.0, October 2024
(See license).

# About KINEVA Model 1:
The Public KINEVA model one is trained on synthetic, public and custom dataset. It contains the categories Person, Head, Negatives. The additional background classes with higher optimized model is not released yet. 


# Future Plans
We plan to release more open-source models, including additional versions of KINEVA. We are also working on integrating KINEVA with Ultralytics and training it on synthetic datasets to further improve its accuracy in different scenarios.

Feel free to explore and test KINEVA Model 1 in your own projects. You can also compare it with YOLO 8 and YOLO 11 for a better understanding of its capabilities.

Thank you for trying out KINEVA Model 1! We welcome any feedback or contributions. 😊

#GitHub Repository Features:
 Pre-trained KINEVA Model 1
 
## Requirements
python3.9 or higher
