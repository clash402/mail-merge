class App:
    def __init__(self, data_manager):
        self.PATH_INVITED_NAMES = "input/names/invited_names.txt"
        self.PATH_STARTING_LETTER = "input/letters/starting_letter.txt"
        self.PATH_FINAL_LETTERS = "output/ready_to_send"

        self.data_manager = data_manager

        self.names = self.data_manager.get_names(self.PATH_INVITED_NAMES)
        self.letter = self.data_manager.get_letter_template(self.PATH_STARTING_LETTER)

        self.compose_letters(self.names, self.letter, self.PATH_FINAL_LETTERS)

    # PUBLIC METHODS
    def compose_letters(self, names, letter, path_to_save):
        for name in names:
            stripped_name = name.strip()
            new_letter = letter.replace("[name]", stripped_name)

            self.data_manager.save_letter(path_to_save, name, new_letter)
