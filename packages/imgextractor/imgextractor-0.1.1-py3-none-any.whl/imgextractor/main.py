# imgextract by Jiri Podivin
# v0.1.0

import tensorflow_hub as hub
import os
from PIL import Image
import glob
import uuid
import numpy as np
import tensorflow as tf
import argparse

def get_image(path, max_width=8000, max_height=6000):
   """Opens image and normalizes it in both size and data type.
   returns: numpy uint8 array
   """
   try:
      with Image.open(path) as file:
         if file.width > max_width or file.height > max_height: # Resizing
            scale = min(max_width/file.width, max_height/file.height)
            new_height = int(file.height*scale)
            new_width = int(file.width*scale)
            print(f"Resizing {path} from {file.width}x{file.height} to {new_width}x{new_height} pixels.")
            file = file.resize((new_width, new_height))
         file = np.asarray(file)

         return file
   except IOError as e:
      print(f"Image {path} is not accesible", e)
   return np.ndarray([], dtype='uint8')

def img_to_tensor(img):
   img = img/255 # uint8 to float
   img = np.reshape(img, (1, img.shape[0], img.shape[1], 3)) # model requires [1, width, height, 3] shape
   img = tf.convert_to_tensor(img, dtype=tf.float32) # and to tensor
   return img

def normalize_bbox(bounding_box, original_h, original_w):
   """Turns floats into integers for slicing.
   """
   bounding_box = bounding_box.numpy()
   bounding_box[0], bounding_box[2] = bounding_box[0] * original_h, bounding_box[2] * original_h
   bounding_box[1], bounding_box[3] = bounding_box[1] * original_w, bounding_box[3] * original_w
   return bounding_box.astype('int')

def extract_detections(bounding_box, img):
   """Retrieves slice of the picture. 
   """
   img = img[
      max(0, bounding_box[1]):bounding_box[3],
      max(0, bounding_box[0]):bounding_box[2],
      :]
   return img

def size_constraint(bounding_box, min_width, min_height):
   """Does detected object satisfy minimum constraints?
   """
   return bounding_box[0] >= min_width and bounding_box[0] >= min_height

def get_detections(path, model, classes, n_detections = 10, threshold=0.9, min_width=480, min_height=480):
   tf.get_logger().setLevel('ERROR') # This doesn't really help, although it should
   extracted_images = []

   img = get_image(path)
   tensor_img = img_to_tensor(img)
   detections = model.signatures['default'](tensor_img)
   print(f"Following unique objects found {set(detections['detection_class_entities'].numpy())}.")

   # Dictionary of lists to list of dictionaries
   detections = [
      {
         'bounding_box': detections['detection_boxes'][i],
         'detection_class_name': detections['detection_class_names'][i],
         'detection_class_label': detections['detection_class_labels'][i],
         'detection_score': detections['detection_scores'][i],
         'detection_class_entity': detections['detection_class_entities'][i]
      }
      for i in range(len(detections['detection_class_names']))]

   print(f"Filtering {classes} ...")

   # Apply filter
   for detection in detections:
      if detection['detection_class_entity'] in classes and detection['detection_score'] >= threshold:
         print(f"Found {detection['detection_class_entity'].numpy().decode()} with score {detection['detection_score']}...")
         bounding_box = normalize_bbox(detection['bounding_box'], img.shape[0], img.shape[1])
         if size_constraint(bounding_box, min_width, min_height):
            extracted_images.append(
               (detection['detection_class_entity'].numpy().decode(),
               extract_detections(bounding_box, img)))
         else:
            print(
               f"Skipping detected {detection['detection_class_entity'].numpy().decode()} "
               f"as its dimensions {bounding_box[0]}x{bounding_box[1]} are too small for given constraints.")
         # Apply cut off
         if len(extracted_images) >= n_detections:
            break
   print(f"Found total {len(extracted_images)} objects in {path}.")
   return extracted_images


def setup_dirs(output_path='extracted'):
   """Creates directory for extracted pictures.
   """
   try:
      os.mkdir(output_path)
   except FileExistsError: # If it exists already? Great!
      pass
   print('Dirs created!')

def main():
   # Replace with another model, if it has the same signature
   default_detector = 'https://tfhub.dev/google/faster_rcnn/openimages_v4/inception_resnet_v2/1'
   # Arg parser setup and argument value retrieval
   parser = argparse.ArgumentParser(
      prog="imgextract",
      description="Extract images with object detector using classes from OpenImages V4 dataset.",
      epilog=f"Using {default_detector} by default. Override is possible.",
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)

   parser.add_argument("input_path", type=str, help="Path to source images.")
   parser.add_argument("--output-path", action='store', type=str, default='./extracted/', help="Path where extracted images will be stored")
   parser.add_argument("--classes", action='extend', nargs='+', type=str, default=['Plant'], help="Space separated list of classes")
   parser.add_argument("--max-detections", action='store', type=int, default=10, help="Maximum number of reported detections")
   parser.add_argument("--threshold", action='store', default=0.2, type=float, help="Detection threshold <0.0, 1.0>")
   parser.add_argument("--minimum-width", action='store', default=100, type=int, help="Minimum width of detected object in px.")
   parser.add_argument("--minimum-height", action='store', default=100, type=int, help="Minimum height of detected object in px.")
   parser.add_argument("--detector", action='store', type=str, default=default_detector, help="Model to be used for image extraction. Should be URL to TFhub.")
   args = parser.parse_args()

   src_img_path = args.input_path
   output_path = args.output_path
   classes = args.classes
   max_detections = args.max_detections

   setup_dirs(output_path)

   try:
      model = hub.load(args.detector)
   except Exception as e:
      print(f"Model initialization failed with: {e}")
      exit(1)

   print('Model initialized')

   for img in [f for f in glob.glob(os.path.join(src_img_path,'*')) if os.path.isfile(f)]: # Get all files from the directory.
      detections = get_detections(
         img,
         model,
         n_detections=max_detections,
         classes=classes,
         threshold=min(max(0, args.threshold), 1.0),
         min_width=args.minimum_width,
         min_height=args.minimum_height)

      for i, extracted in enumerate(detections):
         try:
            extracted_img = Image.fromarray(extracted[1], mode='RGB')
         except ValueError as v_err:
            print(v_err)
            continue
         extracted_name = f"{os.path.basename(img)}_{extracted[0]}_{str(i)}_detection.jpg"
         extracted_img.save(os.path.join(output_path, extracted_name))
         print(f"Extracted: {extracted_name} saved ")

if __name__ == '__main__':
   main()
