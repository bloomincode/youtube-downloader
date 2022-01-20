from pytube import YouTube

def display_stats(yt):
    video = {
        "title": yt.title,
        "description": yt.description,
        "length": (yt.length / 60),
        "views": yt.views
    }
    for key, value in video.items():
        print(key, ":", value)
        print("--------------")

def download_video(video):
    print("Downloading..")
    try:
        video.download(output_path="./youtube-downloader/")
        print("Download finished")
    except TimeoutError:
        print("Download was taking too long!")
        pass

def main():
    print("Enter YT Link: ")
    link = input()
    yt = YouTube(link)
    display_stats(yt)
    video = yt.streams.get_highest_resolution()
    download_video(video)

if __name__ == "__main__":
    main()