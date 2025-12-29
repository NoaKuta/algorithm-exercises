import sys  # ספרייה לטיפול בארגומנטים משורת הפקודה
from PIL import Image  # ייבוא כלי עבודה עם תמונות מתוך Pillow

def main():
    # 1. בדיקה שהמשתמש הקליד שם של קובץ בשורת הפקודה
    # sys.argv[0] הוא תמיד שם הסקריפט, לכן אנחנו מחפשים את sys.argv[1]
    if len(sys.argv) < 2:
        print("Please provide an image filename.")
        return

    # 2. שמירת שם הקובץ שקיבלנו מהמשתמש לתוך משתנה
    filename = sys.argv[1]

    try:
        # 3. פתיחת התמונה מהתיקייה
        with Image.open(filename) as img:
            
            # 4. המרה ל-RGB (חשוב כדי לוודא שיש בדיוק 3 ערוצים)
            img = img.convert("RGB")
            
            # 5. פיצול התמונה ל-3 ערוצים: אדום, ירוק וכחול
            r, g, b = img.split()

            # 6. הצגת כל ערוץ בחלון נפרד על המסך
            print(f"Showing channels for {filename}...")
            r.show(title="Red Channel")
            g.show(title="Green Channel")
            b.show(title="Blue Channel")

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found in this folder.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# שורה סטנדרטית בפייתון שאומרת: "אם הריצו אותי ישירות, תפעיל את פונקציית main"
if __name__ == "__main__":
    main()