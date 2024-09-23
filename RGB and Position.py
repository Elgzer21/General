import pyautogui
import time

def show_rgb_color():
    print("Move the cursor to see the RGB color of the pixel under it. Press Ctrl+C to exit.")
    
    try:
        while True:
            x, y = pyautogui.position()  # Get the current mouse cursor position
            rgb_color = pyautogui.pixel(x, y)  # Get the color at the cursor position
            print(f"Cursor Position: ({x}, {y}) | RGB Color: {rgb_color}")  # Print the position and color
            time.sleep(0.5)  # Update every 0.5 seconds
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    show_rgb_color()
