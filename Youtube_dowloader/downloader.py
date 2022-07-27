from pytube import YouTube
inputURL = input("Paste the youtube URL here: ")
yt = YouTube(inputURL) #add YouTube URL here as a string

downloadOptions = int(input("Choose an option: 1 for video download or 2 for audio only: "))

if downloadOptions == 1:
    print(yt.streams)
    streamChosen = int(input("type the tag of the desired stream: "))
    #yt.streams.filter(adaptive = True)
    stream = yt.streams.get_by_itag(streamChosen) #add tag of the desired stream
    #download(output_path: Optional[str] = None, filename: Optional[str] = None, filename_prefix: Optional[str] = None, skip_existing: bool = True, timeout: Optional[int] = None, max_retries: Optional[int] = 0) → str
    
elif downloadOptions == 2:
    print(yt.streams)
    streamChosen = int(input("type the tag of the desired stream"))
    #yt.streams.filter(audio_only = True)
    stream = yt.streams.get_by_itag(streamChosen) #add tag of the desired stream
    stream.download()