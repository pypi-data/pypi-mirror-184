class Hello:
    
    def __init__(self, message):
        self.message = message
        self.len_message = 0

    def calculate_len_message(self):
        return len(self.message)