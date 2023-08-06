import os
import uuid
import shutil
import subprocess
from typing import Optional

from .models import QualityOptions
from .utils import find_ffmpeg


class TempFile:
    def __init__(self, source: Optional[bytes] = None, extension: str = "tmp"):
        self.path = f"{str(uuid.uuid4())}-tmp.{extension}"
        if source is not None:
            with open(self.path, "wb+") as f:
                f.write(source)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __str__(self):
        return self.path

    def close(self):
        os.remove(self.path)


def _run(args: str) -> subprocess.CompletedProcess:
    command = f'"{find_ffmpeg()}" -y -hide_banner {args}'
    result = subprocess.run(command, shell=True, capture_output=True, check=True)
    return result


def merge(audio: bytes, video: bytes, dest: str) -> subprocess.CompletedProcess:
    """Merge the video and audio stream downloaded

    :param audio: bytes of audio stream
    :param video: bytes of video stream
    :param dest: destination of output file
    :return: `CompletedProcess`
    """
    with TempFile(extension="mp4") as output, TempFile(audio) as audio_file, TempFile(video) as video_file:
        result = _run(f"-i {audio_file} -i {video_file} -c copy -strict experimental {output}")
        shutil.copy(output.path, dest)
    return result


def extract_audio(audio: bytes, dest: str, quality: QualityOptions) -> subprocess.CompletedProcess:
    """Extract the audio from MP4 container stream

    :param audio: bytes of audio stream
    :param dest: destination of output file
    :param quality: Quality Options, contain dolby_audio: bool, flac_audio: bool
    :return: `CompletedProcess`
    """
    extension = "aac"
    if quality.dolby_audio:
        extension = "ac3"
    if quality.flac_audio:
        extension = "flac"
    with TempFile(extension=extension) as output, TempFile(audio) as audio_file:
        result = _run(f"-i {audio_file} -vn -c copy {output}")
        shutil.copy(output.path, dest)
    return result
