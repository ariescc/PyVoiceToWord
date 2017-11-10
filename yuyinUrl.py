import wave
from pyaudio import PyAudio,paInt16
from aip import AipSpeech

APP_ID = '10348056'
API_KEY = 'pXCd82qbjL8Gi3qZ1wMeEXUP'
SECRET_KEY = 'P0o70lPEtGE6BrfwZ7cSlm3GGpcEsOe9'

aipSpeech = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

framerate = 8000
NUM_SAMPLES = 2000
channels = 1
sampwidth = 2
TIME = 2

def save_wave_file(filename,data):
    wf = wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()

def record_wave():
    pa = PyAudio()
    stream = pa.open(format = paInt16,channels = 1,
                     rate = framerate, input = True,
                     frames_per_buffer = NUM_SAMPLES)
    my_buff = []
    count = 0
    while count < TIME*10:
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buff.append(string_audio_data)
        count+=1
        print('.')
    save_wave_file('01.wav',my_buff)
    stream.close()

chunk = 2014

def play():
    wf = wave.open(r"01.wav",'rb')
    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=
    wf.getnchannels(),rate=wf.getframerate(),output=True)
    while True:
        data = wf.readframes(chunk)
        if data == "": break
        stream.write(data)
    stream.close()
    p.terminate()

def get_file_content(filepath):
    with open(filepath,'rb') as fp:
        return fp.read()

def regorinize_voice():
    return aipSpeech.asr(get_file_content('2.wav'),'pcm',16000, {
        'lan': 'zh',
    })

if __name__ == '__main__':
    record_wave()
    print('over!!!')
    play()
    print(regorinize_voice())