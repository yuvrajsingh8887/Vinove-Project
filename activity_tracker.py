import time
from pynput import mouse, keyboard
from PIL import ImageGrab
import threading
import os
import json

class ActivityTracker:
    def __init__(self, screenshot_interval=5, screenshot_dir='screenshots', duration=300):
        self.screenshot_interval = screenshot_interval
        self.screenshot_dir = screenshot_dir
        self.duration = duration
        os.makedirs(screenshot_dir, exist_ok=True)
        self.active = True
        self.last_activity = time.time()
        self.metadata_file = 'screenshots/metadata.json'
        self.screenshot_metadata = self.load_metadata()

    def load_metadata(self):
        if os.path.exists(self.metadata_file):
            with open(self.metadata_file, 'r') as file:
                return json.load(file)
        return {}

    def save_metadata(self):
        with open(self.metadata_file, 'w') as file:
            json.dump(self.screenshot_metadata, file)

    def on_mouse_activity(self, x, y):
        self.last_activity = time.time()
        #print(f"Mouse moved to ({x}, {y})")

    def on_keyboard_activity(self, key):
        self.last_activity = time.time()

    def capture_screenshot(self):
        start_time = time.time()
        while self.active and (time.time() - start_time < self.duration):
            current_time = time.time()
            if current_time - self.last_activity < self.screenshot_interval:
                timestamp = int(current_time)
                filename = f"screenshot_{timestamp}.png"
                screenshot = ImageGrab.grab()
                screenshot.save(f"{self.screenshot_dir}/{filename}")
                self.screenshot_metadata[filename] = {'timestamp': timestamp}
                self.save_metadata()
            time.sleep(self.screenshot_interval)

    def start_tracking(self):
        mouse_listener = mouse.Listener(on_move=self.on_mouse_activity)
        keyboard_listener = keyboard.Listener(on_press=self.on_keyboard_activity)
        mouse_listener.start()
        keyboard_listener.start()

        screenshot_thread = threading.Thread(target=self.capture_screenshot)
        screenshot_thread.start()

    def stop_tracking(self):
        self.active = False
