import datetime
import glob 

def log_message(msg, msg_type):
    logfile = glob.glob("../logs/engine.log")
    with open(logfile[0], "a") as f:
        f.write(
            f"{datetime.datetime.now()} TYPE={msg_type}\n{msg}\n\n"
        )