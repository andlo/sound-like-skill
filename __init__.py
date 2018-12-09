from mycroft import MycroftSkill, intent_file_handler
import freesound

class SoundLike(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def Initialize():
        self.freesound = freesound.FreesoundClient()
        self.freesound.set_token("<your_api_key>","token")


    @intent_file_handler('like.sound.intent')
    def handle_like_sound(self, message):
        self.speak_dialog('like.sound')


def create_skill():
    return SoundLike()

