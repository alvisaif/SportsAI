import pyttsx3


class TextToSpeech:
    engine: pyttsx3.Engine


    def  __init__(self, voice, rate: int, volume: float):
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('vioce', voice)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def list_available_voices(self):
        voices: list = [self.engine.getProperty('voices')]

        for i, voice in enumerate(voices[0]):
            print(f'{i + 1} {voice.name} {voice.age}: {voice.languages[0]} ({voice.gender}) [{voice.id}]')


    def text_to_speech(self, text: str, save: bool = True, file_name='C:Users/Awan/Downloads/code/output.mp3'):
        self.engine.say(text)
        print('I am speaking...')

        if save:
            self.engine.save_to_file(text, file_name)
            self.engine.runAndWait()

if __name__== '__main__':
    tts = TextToSpeech(None, 200, 1.0)
     #tts.list_available_voices()
    tts.text_to_speech('Hello threre! I am MALIK SAIF AWAN i am a student and i am a busines men i live javend singh wala and i developed many softwares!')