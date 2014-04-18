__author__ = 'Nick'

class messageToSkype:


    def __init__(self):
        import Skype4Py

        skype = None
        self.msg = None
        self.topic = 'Lean Lists Party Group!'
        self.skype = Skype4Py.Skype()
        self.skype.Attach()

    def sendmessage2(self,msg):
        print 'hi'
        for chat in self.skype.Chats:
            if chat.Topic == self.topic:
               print 'test'
               #chat.SendMessage(msg)

# for c in chats:
#     for m in c.Messages:
#         print m.Body


# if not messageSent:
#     for chat in skype.BookmarkedChats:
#         if chat.Topic == topic:
#             chat.SendMessage("SomeMessageHere")
#             messageSent = True
