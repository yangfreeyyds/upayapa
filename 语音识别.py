from pydub import AudioSegment
import speech_recognition as sr

# 将MP3文件转换为WAV格式
def convert_mp3_to_wav(mp3_file, wav_file):
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format="wav")

# 进行语音识别
def transcribe_audio(wav_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)  # 使用record()函数直接读取音频文件
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "无法识别音频"
        except sr.RequestError as e:
            return f"请求错误: {e}"

# 主函数
def dddd(mp3_file):
    wav_file = "temp.wav"
    convert_mp3_to_wav(mp3_file, wav_file)
    text = transcribe_audio(wav_file)
    print("转录的文本：", text)


