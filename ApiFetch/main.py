
import requests
import cv2
import numpy as np

# Function to fetch the low-resolution image using the dummy API
def fetch_low_resolution_image():
    dummy_api_url = "https://cdn.pixabay.com/user/2013/11/05/02-10-23-764_250x250.jpg"  # Replace this with your dummy API endpoint
    response = requests.get(dummy_api_url)
    if response.status_code == 200:
        image_data = response.content
        low_resolution_image = cv2.imdecode(np.frombuffer(image_data, dtype=np.uint8), cv2.IMREAD_COLOR)
        return low_resolution_image
    else:
        print(f"Failed to fetch the image. Status code: {response.status_code}")
        return None

# Function to change resolution of the image
def change_resolution(image, new_width, new_height):
    return cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

# Fetch the low-resolution image from the dummy API
low_resolution_image = fetch_low_resolution_image()

# Check if the image was fetched successfully
if low_resolution_image is not None:
    # Display the original low-resolution image
    cv2.imshow("Low-Resolution Image", low_resolution_image)

    # Change resolution to desired high resolution (e.g., double the dimensions)
    new_width, new_height = low_resolution_image.shape[1] * 2, low_resolution_image.shape[0] * 2
    high_resolution_image = change_resolution(low_resolution_image, new_width, new_height)

    # Display the high-resolution image
    cv2.imshow("High-Resolution Image", high_resolution_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed to fetch the image from the dummy API.")
