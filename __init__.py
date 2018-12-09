from mycroft import MycroftSkill, intent_file_handler


class SoundLike(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('like.sound.intent')
    def handle_like_sound(self, message):
        self.speak_dialog('like.sound')


def create_skill():
    return SoundLike()

