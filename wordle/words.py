# TODO:: Store the game logic for wordle
#


class Wordle:

    MAX_ATTEMPTS = 6
    MAX_LETTERS = 5

    def __init__(self, secret: str):
        self.secret = secret
        self.attempts = []
        pass

    def attempt(self, word):
        self.attempts.append(word)

    # check if wordle is solved
    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    # check the attempts remaining

    @property
    def remaining_attempts(self):
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved
