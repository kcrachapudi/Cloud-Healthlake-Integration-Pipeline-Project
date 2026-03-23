import datetime

def log_message(msg, msg_type):

    with open("../logs/engine.log", "a") as f:
        f.write(
            f"{datetime.datetime.now()} TYPE={msg_type}\n{msg}\n\n"
        )