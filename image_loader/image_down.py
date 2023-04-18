from simple_image_download import simple_image_download as simp
response = simp.Downloader
keyword = ["lion"]
for i in keyword:
    response().download(i , 10)