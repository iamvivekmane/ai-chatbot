import pyautogui
import time
import pyperclip

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
# again click the browser button to minimize the browser
pyautogui.click(1268,1170)
print(text)

