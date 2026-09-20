import numpy as np
# Create grayscale image
def create_image():
    image = np.array([
        [50, 100, 150, 200],
        [60, 110, 160, 210],
        [70, 120, 170, 220],
        [80, 130, 180, 230]
    ])

    return image


# Adjust brightness
def adjust_brightness(image, value):
    return np.clip(image + value, 0, 255)


# Horizontal flip
def horizontal_flip(image):
    return np.fliplr(image)


# Vertical flip
def vertical_flip(image):
    return np.flipud(image)


# Calculate average brightness
def average_brightness(image):
    return np.mean(image)


# Find pixels based on threshold
def threshold_analysis(image, threshold):
    above = image[image > threshold]
    below = image[image < threshold]

    return above, below


# Main program
image = create_image()

print("Original Image:")
print(image)

try:
    value = int(input("\nEnter brightness adjustment: "))

    result = adjust_brightness(image, value)

    print("\nBrightness Adjusted:")
    print(result)

except ValueError:
    print("Enter a valid number.")

print("\nHorizontal Flip:")
print(horizontal_flip(image))

print("\nVertical Flip:")
print(vertical_flip(image))

print("\nAverage Brightness:")
print(average_brightness(image))

try:
    threshold = int(input("\nEnter brightness threshold: "))

    above, below = threshold_analysis(image, threshold)

    print("Pixels Above Threshold:", above)
    print("Pixels Below Threshold:", below)

except ValueError:
    print("Enter a valid threshold")