user_file=input("file name:").lower().strip()
if user_file.endswith(".gif"):
    print("image/gif")
elif user_file.endswith(".jpeg") or user_file.endswhith(".jpg"):
    print("image/jpeg")
elif user_file.endswith(".txt"):
    print("text/plain")
elif user_file.endswith(".zip"):
    print("appliction/zip")
elif user_file.endswith(".pdf"):
    print("appliction/pdf")
elif user_file.endswith(".png"):
    print("image/png")
else:
    print("appliction/octet-stream")
    