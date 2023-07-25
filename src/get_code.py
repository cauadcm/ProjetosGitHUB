import random
class Getcode:
    def get_code(self):
        self.code = str(random.randint(10000, 99999))
        return self.code