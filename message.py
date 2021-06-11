def show_message(texts):
    for text in texts:
        msg = f"Text your message is : {text} "
        print(msg)
def send_messages(texts):
    while texts:
        any_text = texts.pop()
        sent_messages.append(any_text)





text_messages = ['Yes this a text','Yes this is the text','No this is not a text']
sent_messages = []
show_message(text_messages)
send_messages(text_messages[:])
print(sent_messages)
print(text_messages)


