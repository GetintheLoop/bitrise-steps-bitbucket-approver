import random

class ApproverMessages:

    def __init__(self):
        self.successMessages = ["It's alive! It's alive!",
                                "You had me at hello.",
                                "To infinity and beyond!",
                                "Yippie-ki-yay, motherf-er!",
                                "May the Force be with you.",
                                "Look at that! Look how she moves! That's just like Jell-O on springs."]
        self.failureMessages = ["Help me, Obi-Wan Kenobi. You're my only hope.",
                                "Fasten your seatbelts. It's going to be a bumpy night.",
                                "You've got to ask yourself one question: 'Do I feel lucky?' Well, do ya punk?",
                                "Houston, we have a problem.",
                                "You can't handle the truth!",
                                "Of all the gin joints in all the towns in all the world, she walks into mine...",
                                "You're gonna need a bigger boat."]

    def getRandomInt(self, maxValue):
        return random.randint(0, maxValue)

    def getRandomFailureMessage(self):
        maxValue = len(self.failureMessages) - 1
        return ":thumbsdown: " + self.failureMessages[self.getRandomInt(maxValue)]

    def getRandomSuccessMessage(self):
        maxValue = len(self.successMessages) - 1
        return ":thumbsup: " + self.successMessages[self.getRandomInt(maxValue)]
