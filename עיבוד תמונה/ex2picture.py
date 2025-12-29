import sys
from PIL import Image

def stretch_histogram(img):
    # Get the darkest and brightest pixel values
    min_val, max_val = img.getextrema()

    # If the image is a solid color, no stretching is possible
    if max_val == min_val:
        return img
    
    # Define the stretching logic
    def calculate_stretch(v):
        # Stretch the values to the full 0-255 range
        new_value = (v - min_val) * 255 / (max_val - min_val)
        return int(new_value)

    # Apply the function to every pixel
    return img.point(calculate_stretch)

def main():
    # Check if a filename was provided
    if len(sys.argv) < 2:
        print("Usage: python ex1picture.py <filename>")
        return
    
    filepath = sys.argv[1]

    try:
        with Image.open(filepath) as img:
            # 1. Convert to Grayscale (Black & White)
            bw_img = img.convert('L')
            
            # 2. Calculate Histogram
            hist_before = bw_img.histogram()
            print("Histogram calculated successfully.")

            # 3. Get original range for verification
            min_v, max_v = bw_img.getextrema()
            print(f"Original range: {min_v} to {max_v}")

            # 4. Stretch Histogram
            stretched_img = stretch_histogram(bw_img)

            # 5. Display results
            print("Displaying Original B&W and Stretched image...")
            bw_img.show(title="Original B&W")
            stretched_img.show(title="Stretched Image")

            # 6. Save the result
            stretched_img.save("stretched_result.jpg")
            print("Success! Stretched image saved as 'stretched_result.jpg'")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()