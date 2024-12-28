from gtts import gTTS

lag = "en"
text = "hello, How can I help You ?"

speech = gTTS(text=text,lang = lag,slow=False,tld="com.au")


# speech.save("text.mp3")