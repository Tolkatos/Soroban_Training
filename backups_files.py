import json

class Files:
    def __init__(self):
        self.game_log = 'game_log.txt'

    def save_data(self, add_data):
        data = open(self.game_log, "a+")
        data.write(add_data)
        data.write("\n")
        data.close()

    def load_data(self):
        data = open(self.game_log, "r")
        last_line = data.readlines()[-1]
        data.close()
        return last_line
