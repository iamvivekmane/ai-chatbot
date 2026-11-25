# ai-chatbot

A Python bot that watches a WhatsApp Web conversation and automatically replies using an LLM. It reads the chat on screen, checks who sent the last message, and only responds when the last message came from the other person.

> **Status:** Learning project. Expect rough edges.

## How it works

1. Opens WhatsApp Web in your browser.
2. Copies the current conversation from the screen using `pyautogui`.
3. Checks the last message:
   - If it is from the **other person**, the chat is sent to an LLM API, which generates a reply.
   - If it is from **you**, the bot does nothing and waits.
4. Types and sends the generated reply in the chat.
5. Repeats continuously, re-copying the chat each cycle.

## Tech stack

- Python 3.11.9
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for browser and keyboard/mouse automation
- An LLM API for reply generation (Gemini)

## Getting started

### Prerequisites

- Python 3.11.9
- A desktop browser with a WhatsApp Web session (log in by scanning the QR code)
- An API key for your LLM provider

### Installation

```bash
git clone https://github.com/iamvivekmane/ai-chatbot.git
cd ai-chatbot
pip install -r requirements.txt
```

### Configuration

Create the .env file with GEMINI_API_KEY=your_key_here
Add your API key where the app expects it. 

### Run

```bash
python main.py
```

Keep the WhatsApp Web chat open and visible on screen. Because the bot controls your mouse and keyboard through PyAutoGUI, avoid using your computer while it runs.

To stop it, move the mouse to a corner of the screen (PyAutoGUI's fail-safe) or press `Ctrl + C` in the terminal.

## Project structure

```
ai-chatbot/
├── main.py            # Main script
├── requirements.txt   # Dependencies
└── README.md
```

## Limitations

- Depends on screen position and timing, so changes to the browser layout, zoom level, or window size can break it.
- Needs the browser window in focus, and it takes over your mouse and keyboard while running.
- Copies the whole visible chat each cycle, which can be slow and may send more text to the LLM than needed.
- No message history beyond what is visible on screen.

## Ideas for improvement

- Use a more robust automation tool such as Playwright or Selenium instead of screen coordinates
- Add a configurable persona or tone for replies
- Limit replies to selected contacts and ignore group chats
- Add a configurable polling interval and rate limiting
- Add logging and error handling

## Disclaimer

This project is for **educational purposes only**. Automating WhatsApp Web may violate WhatsApp's Terms of Service and can lead to your account being restricted or banned. Use it only on a test account or with people who know they are talking to an automated assistant. Messages are sent to a third-party LLM API, so do not use it for private or sensitive conversations. The author is not responsible for any misuse.


## Author

Vivek Mane
