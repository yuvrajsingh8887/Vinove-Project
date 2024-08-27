import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

class ScriptRunner:
    def __init__(self):
        self.process = None

    def start_script(self):
        """Start the external Python script."""
        try:
            # Run the main monitoring script using subprocess
            self.process = subprocess.Popen([sys.executable, 'main.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Display message that script started
            messagebox.showinfo("Info", "Agent running in background..")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while starting the script: {e}")

    def stop_script(self):
        """Stop the running external Python script."""
        if self.process and self.process.poll() is None:  # Check if the process is running
            try:
                self.process.terminate()  # Terminate the process
                self.process.wait()  # Wait for the process to terminate
                messagebox.showinfo("Info", "Agent stopped.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while stopping the script: {e}")
        else:
            messagebox.showinfo("Info", "No script is currently running.")
    
    def download_script(self):
        """Start the external Python script to download screenshots."""
        try:
            # Run the script to download screenshots
            self.process = subprocess.Popen([sys.executable, 'get-screenshots-from-s3.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Display message that download started
            messagebox.showinfo("Info", "Downloading initiated..")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while starting the script: {e}")

def create_gui():
    """Create and run the GUI application."""
    # Create the main window
    root = tk.Tk()
    root.title("Python GUI App")
    # Set the window size (width x height)
    root.geometry("400x200")

    script_runner = ScriptRunner()

    # Create Start button and attach the start_script function to it
    start_button = tk.Button(root, text="Start Monitoring Agent", command=script_runner.start_script)
    start_button.pack(pady=10)

    # Create Stop button and attach the stop_script function to it
    stop_button = tk.Button(root, text="Stop Monitoring Agent", command=script_runner.stop_script)
    stop_button.pack(pady=10)
    
    # Create Download button and attach the download_script function to it
    download_button = tk.Button(root, text="Download Screenshots", command=script_runner.download_script)
    download_button.pack(pady=10)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
