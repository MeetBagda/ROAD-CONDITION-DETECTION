class Dataset:
    def __init__(self, image_dir, annotation_file):
        self.image_dir = image_dir
        self.annotation_file = annotation_file
        self.images = []
        self.annotations = []

    def load_images(self):
        # Code to load images from self.image_dir
        pass

    def load_annotations(self):
        # Code to load annotations from self.annotation_file
        pass

    def get_data(self):
        # Code to return loaded images and annotations
        return self.images, self.annotations