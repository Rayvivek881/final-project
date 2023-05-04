import cv2
import glob
import numpy as np
import controller as cnt
# from inspect import getargs
class VehicleDetector:

    def __init__(self):
        # Load Network
        net = cv2.dnn.readNet("dnn_model/yolov4.weights", "dnn_model/yolov4.cfg")
        self.model = cv2.dnn_DetectionModel(net)
        self.model.setInputParams(size=(832, 832), scale=1 / 255)
        # Allow classes containing Vehicles only
        self.classes_allowed = [1, 2, 3, 5, 6, 7, 8]

    # def gen():
    #  IMAGE_FILES = []
    #  filename = []
    #  dir_path = r'C:\Users\Mayuree Deori\Downloads\source code\source code\images'
    #  x = os.listdir(dir_path)
     
    #  for x in range(1,10,4):
    #     img_path = os.path.join(dir_path, x)
    #     img_path = images.load_image_file(img_path)  # reading image and append to list
    #     IMAGE_FILES.append(img_path)
    #     filename.append(x.split(".", 1)[0])

    def detect_vehicles(self, img):
        # Detect Objects
        vehicles_boxes = []
        class_ids, scores, boxes = self.model.detect(img, nmsThreshold=0.4)
        for class_id, score, box in zip(class_ids, scores, boxes):
            if score < 0.5:
                # Skip detection with low confidence
                continue

            if class_id in self.classes_allowed:
                vehicles_boxes.append(box)

        return vehicles_boxes

# Load Veichle Detector
vd = VehicleDetector()

# Load images from a folder
images_folder = glob.glob("images/*.jpg")
vehicles_folder_count = []

# this will return count for every image


    
def answer(path, ind) :
    
    img = cv2.imread(path)
    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)
    
    for box in vehicle_boxes:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)
    cnt.led(vehicle_count, ind)
    cv2.imshow("Cars", img)
    cv2.waitKey(1)
    return vehicle_count
    
  
# Loop through all the images
for i in range(len(images_folder)):
    vehicles_folder_count.append(answer(images_folder[i], i))

print("count Array of images", vehicles_folder_count)


