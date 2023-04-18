from simple_image_download import simple_image_download as simp
response = simp.Downloader
keyword = ["lion"] #here you replace the instance with your required instance
for i in keyword:
    response().download(i , 10) # here 10 denotes the number of images to be loaded
