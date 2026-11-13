import pyautogui
import time
import pyperclip
from google import genai
from google.genai import types
from pathlib import Path
from dotenv import load_dotenv

# click the browser button to open the browser
pyautogui.click(1268,1170)
# wait till the browser opens
time.sleep(1)
# move to start of the chat
pyautogui.moveTo(745,298)
# drag till end of the chat
pyautogui.dragTo(1850,1039,duration=1.0,button='left')
# copy the selected text to the clipboard
pyautogui.hotkey('ctrl','c')
# wait till the text gets copied to the clipboard
time.sleep(1)
# paste the text in the variable
text = pyperclip.paste()
# click at the starting position to deselect the selected text
pyautogui.click(745,298)




# text = '''
# [20:30, 12/6/2024] Naruto: jo sunke coding ho sake?
# [20:30, 12/6/2024] Rohan Das: https://www.youtube.com/watch?v=DzmG-4-OASQ
# [20:30, 12/6/2024] Rohan Das: ye
# [20:30, 12/6/2024] Naruto: https://www.youtube.com/watch?v=DzmG-4-OASQ
# [20:31, 12/6/2024] Naruto: This is hindi
# [20:31, 12/6/2024] Naruto: send me some english songs
# [20:31, 12/6/2024] Naruto: but wait
# [20:31, 12/6/2024] Naruto: this song is amazing
# [20:31, 12/6/2024] Naruto: so I will stick to it
# [20:31, 12/6/2024] Naruto: send me some english song also
# [20:31, 12/6/2024] Rohan Das: hold on
# [20:31, 12/6/2024] Naruto: I know what you are about to send
# [20:32, 12/6/2024] Naruto: 😄
# [20:32, 12/6/2024] Rohan Das: https://www.youtube.com/watch?v=ar-3chBG4NU
# ye hindi English mix hai but best hai
# [20:33, 12/6/2024] Naruto: okok
# [20:33, 12/6/2024] Rohan Das: Haan
# '''

env_path = Path(__file__).parent / ".env"
load_dotenv(env_path, override=True)   

API_KEY = load_dotenv('GEMINI_API_KEY')
MODEL = "gemini-3.6-flash" 

client = genai.Client(api_key=API_KEY)


completion = client.models.generate_content(
    model=MODEL,
    config=types.GenerateContentConfig(
        system_instruction="You are a person named naruto who speaks hindi as well as english. You are from India and you are also a coder. You analyze chat history and respond like yourself(naruto), Output should be next chat response like naruto",
    ),
    contents=text,
)

output = completion.text
print(output)

pyperclip.copy(output)

# pyautogui.click(1268,1170)
# time.sleep(1)

pyautogui.click(967,1085)
time.sleep(1)


pyautogui.hotkey('ctrl','v')
time.sleep(1)

pyautogui.press('Enter')

