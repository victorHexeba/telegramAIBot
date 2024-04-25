from google_images_download import google_images_download

def download_image(query, index=1):
    response = google_images_download.googleimagesdownload()
    
    # Configure arguments for the image download
    arguments = {
        "keywords": query,
        "limit": 3,  # Limiting to 3 images to ensure we have enough results
        "print_urls": False,
        "no_directory": True,
        "output_directory": "downloads",  # Directory where images will be downloaded
        "chromedriver": "path/to/chromedriver.exe"  # Specify the path to your chromedriver
    }

    # Download images
    paths = response.download(arguments)
    
    # Return the path to the requested image
    if paths:
        if index <= len(paths[0][query]):
            return paths[0][query][index - 1]
        else:
            print("Requested index is out of range.")
    else:
        print("No images found for the given query.")

# Example usage:
query = "cats"  # Your search query
index = 2  # Index of the image you want to download (2nd image)
image_path = download_image(query, index)
print("Downloaded image path:", image_path)
