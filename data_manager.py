class DataManager:

    # PUBLIC METHODS
    def get_names(self, path):
        with open(path) as names:
            return names.readlines()

    def get_letter_template(self, path):
        with open(path) as letter:
            return letter.read()

    def save_letter(self, path, name, letter):
        formatted_name = name.strip().lower()
        with open(f"{path}/letter_for_{formatted_name}.txt", mode="w") as completed_letter:
            completed_letter.write(letter)
