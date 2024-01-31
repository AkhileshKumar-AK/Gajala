# pip install pyaudio pydub
import pyaudio
import wave
import subprocess
from pydub import AudioSegment
from pydub.playback import play

def record_audio(output_file, duration=5, sample_rate=44100, channels=2, chunk_size=1024):
    p = pyaudio.PyAudio()

    # Open stream
    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk_size)

    print("Recording...")

    frames = []

    for i in range(0, int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio to a WAV file
    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

def execute_helper_script():
    try:
        subprocess.run(['python', 'main.py',"C:/Users/HP/Desktop/py/gajala/files/audio.wav"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing helper script: {e}")
        sound = AudioSegment.from_mp3("default.wav")
        print("\n Gajala confused \n")
        play(sound)

if __name__ == "__main__":
    output_file = "C:/Users/HP/Desktop/py/gajala/files/audio.wav"
    record_audio(output_file, duration=5)
    print(f"Audio recorded and saved to {output_file}.")
    execute_helper_script()