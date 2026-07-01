import cv2
import mediapipe as mp
import pyautogui
import time


pyautogui.PAUSE = 0

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


hand_detector = mp.solutions.hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()


smoothening = 5
prev_x, prev_y = 0, 0
curr_x, curr_y = 0, 0


last_click_time = 0
click_cooldown = 1.0 


frame_reduction = 100 

while True:
    success, frame = cap.read()
    if not success:
        break
        
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    
    
    cv2.rectangle(frame, (frame_reduction, frame_reduction), 
                  (frame_width - frame_reduction, frame_height - frame_reduction),
                  (255, 0, 255), 2)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            
            
            index_tip = landmarks[8]
            thumb_tip = landmarks[4]
            
            
            x1 = int(index_tip.x * frame_width)
            y1 = int(index_tip.y * frame_height)
            
            x2 = int(thumb_tip.x * frame_width)
            y2 = int(thumb_tip.y * frame_height)
            
            
            cv2.circle(img=frame, center=(x1, y1), radius=10, color=(0, 255, 255), thickness=cv2.FILLED)
            cv2.circle(img=frame, center=(x2, y2), radius=10, color=(0, 255, 255), thickness=cv2.FILLED)
            
            
            screen_x = (x1 - frame_reduction) * (screen_width / (frame_width - 2 * frame_reduction))
            screen_y = (y1 - frame_reduction) * (screen_height / (frame_height - 2 * frame_reduction))
            
            
            screen_x = max(0, min(screen_x, screen_width))
            screen_y = max(0, min(screen_y, screen_height))
            
            curr_x = prev_x + (screen_x - prev_x) / smoothening
            curr_y = prev_y + (screen_y - prev_y) / smoothening
            
            
            distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
            
            
            current_time = time.time()
            if distance < 40: 
                if current_time - last_click_time > click_cooldown:
                    pyautogui.click()
                    last_click_time = current_time
                    
                    cv2.circle(img=frame, center=(x1, y1), radius=15, color=(0, 255, 0), thickness=cv2.FILLED) 
            else:
                
                try:
                    pyautogui.moveTo(curr_x, curr_y)
                except pyautogui.FailSafeException:
                    pass
                
            
            prev_x, prev_y = curr_x, curr_y

    cv2.imshow('Virtual Mouse', frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()