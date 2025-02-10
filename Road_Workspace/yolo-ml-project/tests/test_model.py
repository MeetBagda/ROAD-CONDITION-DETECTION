import unittest
from src.models.yolo import YOLO

class TestYOLOModel(unittest.TestCase):

    def setUp(self):
        self.model = YOLO()

    def test_model_initialization(self):
        self.assertIsNotNone(self.model)

    def test_model_training(self):
        # Assuming we have a method to train the model
        result = self.model.train()
        self.assertTrue(result)

    def test_model_inference(self):
        # Assuming we have a method for inference
        test_image = "path/to/test/image.jpg"
        predictions = self.model.infer(test_image)
        self.assertIsInstance(predictions, list)

if __name__ == '__main__':
    unittest.main()