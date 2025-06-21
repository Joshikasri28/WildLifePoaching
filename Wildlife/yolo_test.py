# Load YOLO model  
from ultralytics import YOLO  

model = YOLO('yolov8n.pt')  

# Run inference on the image  
results = model('C:/Users/welcome/OneDrive/Desktop/Lion.png')  

# Access the first result and show it  
results[0].show()
