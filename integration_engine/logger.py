import datetime
import glob 

def log_message(msg, msg_type):
    with open("../integration_logs/engine.log", "a") as f:
        f.write(
            f"{datetime.datetime.now()} TYPE={msg_type}\n{msg}\n\n"
        )