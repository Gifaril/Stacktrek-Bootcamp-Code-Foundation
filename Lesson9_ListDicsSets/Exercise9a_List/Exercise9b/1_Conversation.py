class Conversations:
    def __init__(self):
      self.messages = {}
      

    def add_message(self, message):
      mess = message.text
      num = message.sender_contact_number
      
      if (num in self.messages):
        self.messages[num].append(mess)
        return
      self.messages[num] = [mess]
         

    def display_conversations(self):
          # insert code
          pass

    def search(self, contact_number):
          # insert code
          pass


class Message:
    def __init__(self, sender_contact_number, text):
          self.text = text
          self.sender_contact_number =sender_contact_number
          
conversations = Conversations()
message1 = Message("09273966531", "hello")
message2 = Message("09273966531", "God Bless!")
message3 = Message("09090988888", "sorry")

conversations.add_message(message1)
conversations.add_message(message2)
conversations.add_message(message3)
print(conversations.messages)