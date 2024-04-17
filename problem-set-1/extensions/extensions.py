def main():
    file = input("File: ").lower().strip()

    if file.endswith(".gif"):
        mediaType = "image/gif"
    elif file.endswith(".jpg") or file.endswith(".jpeg"):
        mediaType = "image/jpeg"
    elif file.endswith(".png"):
        mediaType = "image/png"
    elif file.endswith("pdf"):
        mediaType = "application/pdf"
    elif file.endswith(".txt"):
        mediaType = "text/plain"
    elif file.endswith(".zip"):
        mediaType = "application/zip"
    else:
        mediaType = "application/octet-stream"
    
    print(mediaType)

main()
    