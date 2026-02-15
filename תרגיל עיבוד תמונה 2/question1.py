import cv2

import numpy as np
import matplotlib.pyplot as plt

def create_gradient_image(height, width):
    img = np.zeros((height, width), dtype=np.uint8)
    max_val = (width - 1) + (height - 1)
    for i in range (height):
        for j in range (width):
            intensity = j + (height - 1 - i)
            
            # 2. נרמול לטווח 0-255
            # אנחנו מחלקים במקסימום ומכפילים ב-255 כדי למנוע Overflow
            color = int((intensity / max_val) * 255)
            
            img[i, j] = color
    
    plt.imshow(img,cmap="gray", vmin=0,vmax=255 )
    plt.title(f"Custom Image {width}x{height}")
    plt.colorbar() # מוסיף סרגל שמראה איזה מספר מייצג איזה גוון
    plt.show()
    return img

def check():
    print(f"OpenCV version: {cv2.__version__}")

create_gradient_image(300, 500)
check()
def brightening_func(img, b, func):
    # המרת התמונה ל-float כדי למנוע בעיות בחישובים לפני הקיצוץ
    img_float = img.astype(np.int16) 
    
    if func == "p.add":
        # Numpy חיבור רגיל של 
        # מבצע "Modulo" (שארית) - אם הערך הוא 260, הוא יהפוך ל-4 (שחור)
        res = (img_float + b).astype(np.uint8)
    elif func == "c2":
        # OpenCV חיבור של 
        # מבצע "Saturation" - אם הערך עובר 255, הוא נשאר 255 (לבן)
        res = cv2.add(img, b)
    else:
        res = img
        
    return res

# הרצה והצגה (שאלה 3)
gradient_img = create_gradient_image(300, 500)
bright_p = brightening_func(gradient_img, 100, "p.add")
bright_c = brightening_func(gradient_img, 100, "c2")

plt.figure(figsize=(10,5))
plt.subplot(1,2,1); plt.imshow(bright_p, cmap='gray'); plt.title("Numpy Add (Wrap)")
plt.subplot(1,2,2); plt.imshow(bright_c, cmap='gray'); plt.title("OpenCV Add (Saturation)")
plt.show()

# שאלה 4 - יצירת תמונה עם קונטרסט נמוך
def create_low_contrast(bg, fg, size=(300, 300)):
    img = np.full(size, bg, dtype=np.uint8)
    cv2.circle(img, (150, 150), 50, fg, -1)
    return img

# שאלה 5 - פונקציית נרמול (מתיחת היסטוגרמה)
def normalize_image(img):
    # המרה ל-float לצורך דיוק בחישובים [cite: 49]
    img_f = img.astype(np.float32)
    f_min = np.min(img_f)
    f_max = np.max(img_f)
    
    # נוסחת הנרמול [cite: 45, 46]
    # dst = (pixel - min) * (255 / (max - min))
    if f_max > f_min:
        dst = (img_f - f_min) * (255.0 / (f_max - f_min))
    else:
        dst = img_f
        
    return np.clip(dst, 0, 255).astype(np.uint8) [cite: 51]

# הרצה
low_con = create_low_contrast(100, 105)
normalized = normalize_image(low_con)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1); plt.imshow(low_con, cmap='gray', vmin=0, vmax=255); plt.title("Low Contrast")
plt.subplot(1,2,2); plt.imshow(normalized, cmap='gray'); plt.title("After Normalization")
plt.show()

def calc_histogram(img):
    # יצירת מערך של 256 אפסים
    hist = np.zeros(256, dtype=int)
    
    # מעבר על כל הפיקסלים וספירת מופעים
    for pixel_val in img.ravel():
        hist[pixel_val] += 1
        
    return hist

# הצגה
hist_values = calc_histogram(gradient_img)
plt.bar(range(256), hist_values, color='gray')
plt.title("Histogram (Manual Calculation)")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()