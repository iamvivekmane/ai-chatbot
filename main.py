import pyautogui
import time
import pyperclip
from google import genai
from google.genai import types
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / ".env"
load_dotenv(env_path, override=True)   
API_KEY = load_dotenv('GEMINI_API_KEY')
MODEL = "gemini-3.5-flash" 
client = genai.Client(api_key=API_KEY)

# click the browser button to open the browser
pyautogui.click(1268,1170)
# wait till the browser opens
time.sleep(1)

def receivedLast(text):
    messages = text.split('/2026]')[-1]
    if 'Mummy' in messages:
        return True
    else:
        return False

while True:
    # move to start of the chat
    pyautogui.moveTo(745,298)
    # drag till end of the chat
    pyautogui.dragTo(1850,1039,duration=1.0,button='left')
    # copy the selected text to the clipboard
    pyautogui.hotkey('ctrl','c')
    # wait till the text gets copied to the clipboard
    time.sleep(1)
    # paste the text in the variable
    chatHistory = pyperclip.paste()
    # click at the starting position to deselect the selected text
    pyautogui.click(745,298)

    # generate reply only if the last message was sent by sender at other end
    if (receivedLast(chatHistory)):
        # click on the input of the chat 
        pyautogui.click(967,1085)
        # wait till it clicks
        time.sleep(1)

        completion = client.models.generate_content(
        model=MODEL,
        config=types.GenerateContentConfig(
        system_instruction="You are a person named naruto who speaks hindi as well as english. You are from India and you are also a coder. You analyze chat history and respond like yourself(naruto), Output should be next chat response like naruto",
        ),
        contents=chatHistory,
        )
        output = completion.text
        
        # copy the output of the api to the clipboard
        pyperclip.copy(output)
        # paste the output in the input of chat
        pyautogui.hotkey('ctrl','v')
        # wait till it pastes the output 
        time.sleep(1)
        # send the message
        pyautogui.press('Enter')


