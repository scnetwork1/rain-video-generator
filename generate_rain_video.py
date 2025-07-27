import datetime
from pydub.generators import WhiteNoise
from moviepy.editor import *

def generate_rain_audio(duration_hours=10, output_file="rain_audio.mp3"):
    duration_ms = duration_hours * 60 * 60 * 1000
    audio = WhiteNoise().to_audio_segment(duration=duration_ms).apply_gain(-30)
    audio.export(output_file, format="mp3")
    return output_file

def generate_rain_video(audio_file, output_file="rain_video.mp4", resolution=(1280, 720)):
    background = ColorClip(size=resolution, color=(30, 30, 30), duration=36000)
    background = background.set_fps(24)
    txt = TextClip("Relaxing Rain Sounds", fontsize=70, color='white', bg_color='gray')
    txt = txt.set_duration(36000).set_position(("center", "bottom"))
    audio = AudioFileClip(audio_file)
    final = CompositeVideoClip([background, txt]).set_audio(audio)
    final.write_videofile(output_file, codec="libx264", audio_codec="aac", fps=24)

def main():
    audio_path = "rain_audio.mp3"
    video_path = f"rain_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.mp4"
    generate_rain_audio(output_file=audio_path)
    generate_rain_video(audio_file=audio_path, output_file=video_path)
    return video_path
