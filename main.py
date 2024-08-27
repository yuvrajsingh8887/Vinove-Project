import threading
import time
from activity_tracker import ActivityTracker
from uploader import Uploader
from config_manager import ConfigManager
from error_handler import ErrorHandler
from web_server import start_server  # Ensure this line matches your web_server.py module

def main():
    config_manager = ConfigManager()
    error_handler = ErrorHandler()

    try:
        # Print all configuration settings to debug
        print("Configuration Settings:")
        for section in config_manager.config.sections():
            print(f"[{section}]")
            for option in config_manager.config.options(section):
                print(f"{option} = {config_manager.get_setting(section, option)}")

        # Read configuration settings
        screenshot_interval = int(config_manager.get_setting('DEFAULT', 'screenshot_interval'))
        upload_interval = int(config_manager.get_setting('DEFAULT', 'upload_interval'))
        duration = int(config_manager.get_setting('DEFAULT', 'duration'))
        s3_bucket = config_manager.get_setting('DEFAULT', 's3_bucket')
        s3_access_key = config_manager.get_setting('DEFAULT', 's3_access_key')
        s3_secret_key = config_manager.get_setting('DEFAULT', 's3_secret_key')

        tracker = ActivityTracker(screenshot_interval=screenshot_interval, duration=duration)
        uploader = Uploader(s3_bucket, s3_access_key, s3_secret_key)

        # Start the web server in a separate thread
        web_thread = threading.Thread(target=start_server)
        web_thread.start()

        tracker.start_tracking()
        end_time = time.time() + duration
        while time.time() < end_time:
            time.sleep(upload_interval)
            uploader.upload_files()
    except Exception as e:
        error_handler.log_error(f"Error in main loop: {str(e)}")
    finally:
        tracker.stop_tracking()

if __name__ == "__main__":
    main()
