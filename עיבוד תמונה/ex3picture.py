import sys
from PIL import Image

def stretch_channel(channel):
    """Stretches the histogram of a single channel."""
    min_val, max_val = channel.getextrema()
    
    # If the channel is solid, return it as is
    if max_val == min_val:
        return channel
    
    # Stretching formula for a single channel
    def calc(v):
        return int((v - min_val) * 255 / (max_val - min_val))
    
    return channel.point(calc)

def main():
    if len(sys.argv) < 2:
        print("Usage: python ex01.03.py <filename>")
        return
    
    filepath = sys.argv[1]

    try:
        with Image.open(filepath) as img:
            # Ensure the image is in RGB mode
            img = img.convert('RGB')
            
            # 1. Split into R, G, B channels
            r, g, b = img.split()
            print("Channels separated successfully.")

            # 2. Calculate Histogram for each (Implicitly done during stretching)
            # You can also get histograms using r.histogram(), etc.
            
            # 3. Stretch each channel separately
            r_stretched = stretch_channel(r)
            g_stretched = stretch_channel(g)
            b_stretched = stretch_channel(b)
            print("Each channel stretched independently.")

            # 4. Merge them back together
            result_img = Image.merge('RGB', (r_stretched, g_stretched, b_stretched))
            
            # Display and Save
            print("Displaying original vs processed image...")
            img.show(title="Original Image")
            result_img.show(title="Color Stretched Result")
            
            result_img.save("color_stretched_result.jpg")
            print("Success! Saved as 'color_stretched_result.jpg'")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()