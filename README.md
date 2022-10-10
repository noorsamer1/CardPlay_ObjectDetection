# cardplay-
## view project 

cardplay recognition 
detect type of card and play 13 round of Tarneeb play using opencv &pytorch

## Work Team
shahed alruwaidan :

write code using opencv and pytorch
load yolo model using pytorch, detect results and connect to webcam using opencv to 
Import card in logic play (function description play)


Laith abuassoud & Noor alharahsheh  
write code for play logic and train yolo model to get more precision in detection 
 
 
. all team worked together  to write  logic code  & fixed error
## card play -phase 1
detection card type using yolov5

``` git clone https://github.com/ultralytics/yolov5 ``` 


``` cd yolov5```

```pip install -r requirements.txt ```

     
.replace  detect file in yolov5  with detect_new.py 


``` !python detect_new.py --weights best.pt --imgsz 416 --source 0 ```

_______________________________________________________________
## Tarneeb -phase 2 : 
1. download weight  & source code (cardetection.py detection with out change card in round , realtime.py can change card in round )
2. select source camera  
3. run command in cmd :
```python  sourcecode.py```
