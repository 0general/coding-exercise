from pytube import YouTube
import os

# link = input("insert Link Here : ")
link = "https://youtu.be/UXZViC4z1Jo"

url = YouTube(link)
print(url.title)
videos = url.streams.all()
video = list(enumerate(videos))

down_dir = "D:\coding-exercise\DownloaderTest"

for i in video:
    print(i)


'''
# for e in url.streams.filter(file_extension='mp4').all():
#     print(str(e))

# print("Downloading...........")

url.streams.filter(progressive=True, file_extension='mp4').order_by(
    'resolution').desc().first().download('D:\coding-exercise')
# 필터링된 것 중 resolution(해상도) 기준으로 정렬, 내림차순으로 정렬(해상도 가장 큰 것이 위로), 거기에서 첫번째 것 download
# DASH 관련 Stream 제거하는 progressive 옵션으로는 720p가 한계

# print("---------------------------------------------")
# for e in url.streams.filter(adaptive=True, file_extension='mp4').all():
#     print(str(e))


url.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by(
    'resolution').desc().first().download('D:\coding-exercise\DownloaderTest\video.mp4')
url.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).first(
).download('D:\coding-exercise\DownloaderTest\audio.mp4')
# print("Downloaded ! ")

'''
