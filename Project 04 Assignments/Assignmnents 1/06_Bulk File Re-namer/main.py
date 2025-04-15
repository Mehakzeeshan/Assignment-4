import os

def main():
    i = 0
    path = "C:/Users/i Tech Computers/Pictures/Screenshots"

    for filename in os.listdir(path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Only rename image files
            my_source = os.path.join(path, filename)
            my_dest = os.path.join(path, f"img{i}.jpg")
            os.rename(my_source, my_dest)
            i += 1

if __name__ == "__main__":
    main()
# This code will rename all image files in the specified directory to img0.jpg, img1.jpg, etc.