# WELCOME TO KINEVA

![Bildschirmfoto 2024-10-11 um 11 25 30](https://github.com/user-attachments/assets/5d81e013-4741-4c31-b047-7d6e8a2498ad)

## Welcome to KINEVA
Welcome to the repository for **KINEVA**, a selection of pre-trained computer vision models designed for a wide range of object detection tasks. This model is ideal for various applications, including complex scenes with challenging lighting and noise conditions, such as low-light security footage.

## Comparison with Other Models
In this repository, we've compared KINEVA Model 1 with other well-known pre-trained models like YOLO 8 and YOLO 11. We want to demonstrate what you can do with different types of pre-trained models.

[![YouTube Video](https://github.com/user-attachments/assets/41baa766-790b-4fc1-b591-58328e61f78f)](https://www.youtube.com/watch?v=24NAldaw_PU)

## Model Overview

Below is an overview of the performance across various test images:

<p align="center">
  <img src="https://github.com/user-attachments/assets/7383af12-c57e-4ccc-904f-d4d81f81283c" height="300"/>
  <img src="https://github.com/user-attachments/assets/549fac74-c8b3-4aeb-9c4a-293c54be829e" height="300"/>
  <img src="https://github.com/user-attachments/assets/cc1be9d4-dc9a-4834-b0b2-c3ee6411045f" height="300"/>
</p>

| Model           | PARAMS | MAP  | STATE       | CATEGORIES               | TYPE   | VERSION |
|-----------------|--------|------|-------------|--------------------------|--------|---------|
| KINEVA Model 1  | 40M    | 75.3 | RELEASED    | HEAD PERSON NEGATIVES     | VISION | 0.2B    |
| KINEVA Model 2  | >80M   | -    | IN TRAINING | HEAD PERSON NEGATIVES BG  | VISION | -       |

## Production
This is our first model, use it at your own risk.

## Model Architecture
TBA (To Be Announced)

## Application
- Security
- Smart City
- Robotics
- Research

## Download KINEVA Model
The model 1 is released in the [models folder](#).

## License
**KINEVA Non-Commercial License (KNCL)**  
Version 1.0, October 2024  
(See [license](#).)

## About KINEVA Model 1
The public KINEVA Model 1 is trained on synthetic, public, and custom datasets. It contains the categories Person, Head, and Negatives. The additional background classes with a higher optimized model are not released yet.

## Future Plans
We plan to release more open-source models, including additional versions of KINEVA. We are also working on integrating KINEVA with **Ultralytics** and training it on synthetic datasets to further improve its accuracy in different scenarios.

Feel free to explore and test **KINEVA Model 1** in your own projects. You can also compare it with **YOLO 8** and **YOLO 11** for a better understanding of its capabilities.

Thank you for trying out KINEVA Model 1! We welcome any feedback or contributions. 😊

## Requirements
- **Python 3.9** or higher
- **PyTorch** 1.10 or higher
- Other dependencies (see `requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/kineva.git
   ```

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the KINEVA Model 1 from the [models folder](#).

4. You're ready to go! You can start using the model in your projects.

## Usage

To run inference with **KINEVA Model 1**, you can use the following example:

```python
import torch
from kineva import KinevaModel

# Load the model
model = KinevaModel('path_to_kineva_model')

# Load an image
image = 'path_to_image.jpg'

# Run inference
results = model.predict(image)

# Display the results
print(results)
```

For further examples and detailed explanations, refer to the `examples` folder.

## Contributing

We welcome contributions to the KINEVA project! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of the changes.
4. Ensure all tests pass before submitting your PR.

For major changes, please open an issue first to discuss what you would like to change.


## Contact

If you have any questions, suggestions, or issues, feel free to open an issue on GitHub or reach out to us at:
- **Page**: [@kineva_ai](https://rebotnix.com/kineva)
- **LinkedIn**: [@kineva_ai](https://www.linkedin.com/company/18547399)
