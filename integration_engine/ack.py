def generate_ack(message):

    lines = message.split("\n")
    msh = lines[0].split("|")

    control_id = msh[9]

    ack = f"""MSH|^~\\&|ENGINE|Cloud|HIS|Hospital|202403201210||ACK|{control_id}|P|2.3
MSA|AA|{control_id}
"""

    return ack