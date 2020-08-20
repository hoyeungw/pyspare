from dataclasses import dataclass


@dataclass
class Message:
    __slots__ = 'origin', 'target', 'body'

    def __init__(self, origin, target, body):
        self.origin = origin
        self.target = target
        self.body = body
