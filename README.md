# playingcard-detection-project

## brief about our project
 
**The project was divided into two phases:**
- The first phase was gathering the data set of playing cards that we had collected and preparing it for the object detection model (yolov5). We labeled our images using roboflow and detecting type of the card (Rank & Suit).
- The second phase was about writing code for Arabian Tarneeb live stream game and making the code contain the greatest number of features that we could create in the shortest amount of time.
This is the first version of the project, which is still in development.
- We used opencv & pytorch to satisfy our requirements.

# Contributors on the project
## This project was completed by a group of three people tasks were assigned to all team members as needed and we all worked togather as shown below.... 

Noor-Aldeen Alharahshes & Laith abuassoud & shahed alruwaidan :
1. We generated fresh data by photographing the cards (approximately 10,000 photographs), then using roboflow to augment the images and labeled them.
2. we trained our yolov5 version (yolov5m) 
3. Shahed created a code with opencv and Pytorch that loads our model to detect the card, and she linked the code to the webcam.
4. Laith and I we wrote the code for the Tarneeb game.
all team worked together  to write  logic code  & fixed error

## playing-card - Folder (phase 1)
detection card type using yolov5

``` git clone https://github.com/ultralytics/yolov5 ``` 

``` cd yolov5```

```pip install -r requirements.txt ```

- replace  detect file in yolov5  with detect_new.py 

``` !python detect_new.py --weights best.pt --imgsz 416 --source 0 ```

_______________________________________________________________
## Tarneeb -Folder (phase 2) : 
1. download weight & source code (cardetection.py detection with out change card in round , realtime.py can change card in round )
2. select camera source   
3. run command in Anaconda Prompt (anaconda) :
```python  sourcecode.py```
