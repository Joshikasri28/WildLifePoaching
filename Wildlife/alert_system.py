from gtts import gTTS
import os
import pygame

def generate_voice_alert(threat_type, language='en'):
    messages = {
        'en': f'Alert! {threat_type} detected in the forest. Take immediate action!',
        'ta': f'காட்டில் கண்டறியப்பட்டது. உடனடியாக நடவடிக்கை எடுங்கள்! {threat_type}'
    }
    
    message = messages.get(language, messages['en'])
    tts = gTTS(text=message, lang=language)
    audio_file = f'alert_{language}.mp3'
    tts.save(audio_file)
    return audio_file

def play_audio(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

if __name__ == "__main__":
    threat = "Gunshot"
    audio_en = generate_voice_alert(threat, 'en')
    audio_ta = generate_voice_alert(threat, 'ta')
    print("Playing English Alert...")
    play_audio(audio_en)
    print("Playing Tamil Alert...")
    play_audio(audio_ta)
