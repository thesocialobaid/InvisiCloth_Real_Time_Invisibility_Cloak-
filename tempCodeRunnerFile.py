def create_background(cap, num_frames=30): 
    print("Capturing background. Please move out of the frame.")
    backgrounds = []
    for i in range(num_frames):
        ret, frame = cap.read()
        if ret: 
            backgrounds.append(frame)
        else: 
            print(f"Warning: Could not read frame {i+1}/{num_frames}")
            time.sleep(0.1)
    if backgrounds: 
        return np.median(backgrounds, axis=0).astype(np.uint8)
    else: 
        raise ValueError("Could not capture any frame for background")

def create_mask(frame, lower_color, upper_color): 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=2) 
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3),np.uint8), iterations=1) 
    return mask 

def apply_cloack_affect(frame, mask, background): 
    mask_inv = cv2.bitwise_not(mask)
    fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    bg = cv2.bitwise_and(background, background, mask=mask)
    return cv2.add(fg, bg)