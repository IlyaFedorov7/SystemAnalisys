import PySimpleGUI as sg
import speech_recognition as sr

sg.theme('DarkPurple1')  # Add a touch of color
# All the stuff inside your window.
v = ''
layout = [[sg.Text('Выбери систему ИИ и файл для распознавания (в формате WAV)')],
          [sg.Button('Выбрать Google'),
           sg.Button('Выбрать IBM'),
           sg.Button('Выбрать Houndify'),
           sg.Button('Выбрать Azure'),
          sg.Button('Выход')], [sg.Output(size=(70, 25),key = '_output_')]
          ]
# Create the Window
window = sg.Window('AI speech-to-text', layout)
#window = sg.Window('Input auto-clear', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Выход':  # if user closes window or clicks cancel
        break
    # print(valueaudio)
    from tkinter import Tk  # from tkinter import Tk for Python 3.x
    from tkinter.filedialog import askopenfilename

    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    if event == 'Выбрать Google':
        try:
            window.FindElement('_output_').Update('')
            rcgnzr = sr.Recognizer()
            harvard = sr.AudioFile(filename)
            with harvard as source:
                rcgnzr.adjust_for_ambient_noise(source)
                audio = rcgnzr.record(source)
            v = rcgnzr.recognize_google(audio)
            print("Google: ", v)
        except :
            print("Oops!  This service does not work right now :(")


    if event == 'Выбрать IBM':
        try:
            window.FindElement('_output_').Update('')
            window.refresh()
            import json
            from os.path import join, dirname
            from ibm_watson import SpeechToTextV1
            from ibm_watson.websocket import RecognizeCallback, AudioSource
            import threading
            from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

            authenticator = IAMAuthenticator('**********************************')
            service = SpeechToTextV1(authenticator=authenticator)
            service.set_service_url(
                'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/e87b34f3-e2cd-46ac-b673-e0e7752a622b')
            models = service.list_models().get_result()
            model = service.get_model('en-US_BroadbandModel').get_result()
            w = []
            with open(filename, 'rb') as audio_file:
                w.append(json.dumps(
                    service.recognize(
                        audio=audio_file,
                        content_type='audio/wav',
                        timestamps=True,
                        word_confidence=True).get_result(),
                    indent=2))
            i = w[0].find('"transcript": "') + len('"transcript": "')
            text = ''
            while (w[0][i] != '"'):
                text += w[0][i]
                i += 1
            print("IBM: ", text)
        except :
            print("Oops!  IBM service does not work right now :(")

    if event == 'Выбрать Houndify':
        try:
            window.FindElement('_output_').Update('')
            r = sr.Recognizer()
            with sr.AudioFile(filename) as source:
                audio = r.record(source)
            HOUNDIFY_CLIENT_ID = "******************"
            HOUNDIFY_CLIENT_KEY = "************************************************************************"  # Houndify client keys are Base64-encoded strings
            text = r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY)
            print("Houndify: ", text)
        except :
            print("Oops!  Houndify service does not work right now :(")

    if event == 'Выбрать Azure':
        try:
            window.FindElement('_output_').Update('')
            import requests
            import azure.cognitiveservices.speech as speechsdk

            speech_config = speechsdk.SpeechConfig(subscription='************************', region='eastus')
            audio_config = speechsdk.audio.AudioConfig(filename=filename)
            speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language="en-US",
                                                           audio_config=audio_config)
            result = speech_recognizer.recognize_once()
            if result.reason == speechsdk.ResultReason.RecognizedSpeech:
                print("Azure: ", result.text)
        except:
            print("Oops!  Azure service does not work right now :(")

window.close()