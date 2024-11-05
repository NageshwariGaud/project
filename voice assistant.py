import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import smtplib
import requests
import json

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# API Key for OpenWeatherMap (replace with your own)
WEATHER_API_KEY = '42091986b59c93adb2180581cb5c0c7f'

# Email credentials
EMAIL_ADDRESS = 'nageshwarigaudgaonkar27@gmail.com'
EMAIL_PASSWORD = '#Nageshwari27'

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to voice input
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print(f"Command received: {command}")
            return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you repeat, please?")
        return ""
    except sr.RequestError:
        speak("Network error. Please check your connection.")
        return ""

# Function to get the current weather
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        speak(f"The current temperature in {city} is {temperature}°C with {description}.")
    else:
        speak("Sorry, I couldn't fetch the weather information.")

# Function to send an email
def send_email(to_address, subject, message):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            email_message = f"Subject: {subject}\n\n{message}"
            smtp.sendmail(EMAIL_ADDRESS, to_address, email_message)
        speak("Email sent successfully.")
    except Exception as e:
        speak("Sorry, I couldn't send the email.")
        print(e)

# Function to save reminders locally
reminders = []

def add_reminder(reminder_text):
    reminders.append(reminder_text)
    speak("Reminder added.")

def list_reminders():
    if reminders:
        speak("Here are your reminders:")
        for reminder in reminders:
            speak(reminder)
    else:
        speak("You have no reminders.")

# Main function to process commands
def process_command(command):
    if "hello" in command or "hi" in command:
        speak("Hello! How can I assist you today?")
    
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    
    elif "weather" in command:
        speak("Please tell me the city name.")
        city = listen()
        get_weather(city)
    
    elif "send email" in command:
        speak("Who should I send the email to?")
        to_address = listen().replace(" ", "") + "@gmail.com"
        speak("What is the subject of the email?")
        subject = listen()
        speak("What would you like the message to say?")
        message = listen()
        send_email(to_address, subject, message)
    
    elif "add reminder" in command:
        speak("What would you like to be reminded about?")
        reminder_text = listen()
        add_reminder(reminder_text)
    
    elif "list reminders" in command:
        list_reminders()
    
    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("Please tell me what you want to search for.")
    
    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that command.")

# Main loop to run the voice assistant
if __name__ == "__main__":
    speak("Voice Assistant activated. How can I help you?")
    while True:
        command = listen()
        if command:
            process_command(command)
