def build_message(**info):
    message = "Here is the information provided:\n"
    for key, value in info.items():
        message += f"{key.capitalize()}: {value}\n"
    return message
print(build_message(name="Urooj Baloch", age=19, city="Karachi",occupation="Student"))
