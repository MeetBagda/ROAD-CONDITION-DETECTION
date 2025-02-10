import os
import yaml
from data.dataset import Dataset
from models.yolo import YOLO

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def main():
    # Load configuration
    config = load_config('src/config/config.yaml')

    # Initialize dataset
    dataset = Dataset(config['dataset']['path'])
    
    # Initialize YOLO model
    model = YOLO(config['model'])

    # Start training
    model.train(dataset)

if __name__ == "__main__":
    main()