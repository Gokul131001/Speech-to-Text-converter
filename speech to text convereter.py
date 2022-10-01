import speech_recognition
def record_voice():
microphone = speech_recognition.Recognizer()
with speech_recognition.Microphone() as live_phone:
microphone.adjust_for_ambient_noise(live_phone)
print(&quot;I&#39;m trying to hear you: &quot;)
audio = microphone.listen(live_phone)
try:
phrase = microphone.recognize_google(audio, language=&#39;en&#39;)
return phrase

except speech_recognition.UnkownValueError:
return &quot;I didn&#39;t understand what you said&quot;
if __name__ == &#39;__main__&#39;:
phrase = record_voice()
with open(&#39;you_said_this.txt&#39;,&#39;w&#39;) as file:
file.write(phrase)
print(&#39;the last sentence you spoke was saved in you_said_this.txt&#39;)