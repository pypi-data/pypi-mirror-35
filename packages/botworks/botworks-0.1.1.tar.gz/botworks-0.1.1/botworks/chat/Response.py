import random


class IResponse:
    def respond(self, client, payload): pass


class Response(IResponse):
    def __init__(self, text=None, emoji=None, ghostly=None, threaded=None, method=None):
        self.text = self.__to_list(text)
        self.emojis = self.__to_list(emoji)
        self.ghostly = self.__to_list(ghostly)
        self.threaded_response = self.__to_list(threaded)
        self.method = method

    def respond(self, client, payload):
        if self.method:
            self.method(client=client, payload=payload)
        if self.text:
            for t in self.text:
                client.post_message(channel=payload.channel, message=t)
        if self.emojis:
            for e in self.emojis:
                client.react(payload, e)
        if self.ghostly:
            for e in self.ghostly:
                client.ephemeral(payload, e)
        if self.threaded_response:
            for m in self.threaded_response:
                client.thread_reply(payload, m)

    @staticmethod
    def __to_list(o):
        if type(o) is list:
            return o
        return [o]


class Responses(IResponse):
    def __init__(self, responses):
        self.responses = responses

    def respond(self, client, payload):
        if type(self.responses) is list:
            random.choice(self.responses).respond(client, payload)
        else:
            self.responses.respond(client, payload)


