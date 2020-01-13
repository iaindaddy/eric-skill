from mycroft import MycroftSkill, intent_file_handler


class Eric(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('eric.intent')
    def handle_eric(self, message):
        self.speak_dialog('eric')


def create_skill():
    return Eric()

