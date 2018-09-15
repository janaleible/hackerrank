class Phonebook():
    def __init__(self):
        self.directory = {}

    def __getitem__(self, name: str) -> str:
        if not name in self.directory:
            return 'Not found'

        return name + '=' + self.directory[name]

    def add(self, name: str, phone_number: str):
        self.directory[name] = phone_number


phonebook = Phonebook()

number_of_entries = int(input())
for i in range(number_of_entries):
    (name, number) = input().split(' ')
    phonebook.add(name, number)

while True:
    try:
        print(phonebook[input()])
    except EOFError:
        break