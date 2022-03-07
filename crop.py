import cv2
import os


def crop_image(path, box, num):
    img = cv2.imread(path)

    dh, dw, _ = img.shape
    print(dh, dw)

    # box = "0 0.057682 0.579630 0.066406 0.233333"
    class_id, x_center, y_center, w, h = box.strip().split()
    x_center, y_center, w, h = float(x_center), float(y_center), float(w), float(h)
    x_center = round(x_center * dw)
    y_center = round(y_center * dh)
    w = round(w * dw)
    h = round(h * dh)
    x = round(x_center - w / 2)
    y = round(y_center - h / 2)

    imgCrop = img[y:y + h, x:x + w]
    cv2.imwrite("croped_imgs/" + path.split(".")[0] + "-" + str(num) + "." + path.split(".")[1], imgCrop)


files_path = os.listdir()
# print(files_path)
os.makedirs("croped_imgs")
for file in files_path:
    if len(file.split(".")) > 1:
        if file.split(".")[1] == "txt":
            f = open(file, "r")
            f = f.read().split("\n")[:-1]
            for i in range(len(f)):
                crop_image(file.split(".")[0]+".jpg", f[i], i + 1)

                print(file)
#
# f = open("video(2522)1.txt", "r")
# f = f.read().split("\n")
# print(f[:-1])
# for i in range(len(f)):
#     img_coordinates = f[i].split(" ")
#     print(img_coordinates)

# crop_image("video(2522)1.jpg", "0 0.057682 0.579630 0.066406 0.233333")
