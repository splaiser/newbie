def show_message(texts):
    for text in texts:
        msg = f"Text your message is : {text} "
        print(msg)
text_messages = ['Yes this a text','Yes this is the text','No this is not a text']
show_message(text_messages)