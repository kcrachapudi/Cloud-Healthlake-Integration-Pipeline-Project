def classify_hl7(hl7):

    msh = hl7.split("\n")[0].split("|")

    trigger = msh[8]

    if "ORU" in trigger:
        return "ORU"
    elif "ORM" in trigger:
        return "ORM"
    elif "SIU" in trigger:
        return "SIU"
    else:
        return "ADT"