import os
import platform
import static_ffmpeg


def FFmpeg_Installation(Video):
    # ffmpeg installed on first call to add_paths(), threadsafe.
    static_ffmpeg.add_paths()  # blocks until files are downloaded
    # Now ffmpeg and ffprobe will use static_ffmpeg versions.
    os.system(f"ffmpeg -i {Video} ...") # Input a video for call


def Execute_FFmpeg_Installation():
    try:
        FFmpeg_Installation("None.mp4") # Video is not actually needed

    except:
        try:
            # It turned out to be an issue with the dns entries on windows
            if platform.system() == 'Windows':
                os.system("ipconfig /flushdns & ipconfig /release & ipconfig /renew")
            # Try again
            FFmpeg_Installation("None.mp4")
            print("FFmpeg installed")
        except:
            return False

    else:
        print("FFmpeg installed")

    finally:
        print("Done")

'''
Further Information:
 - Got errors on first call (https://github.com/zackees/static_ffmpeg/issues/10)
'''