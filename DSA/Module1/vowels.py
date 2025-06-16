class VowelFrequency:
    def __init__(self, text):
        self.text = text.lower()
        self.vowels = "aeiou"

    def count_vowels(self):
        frequency = {}
        for i in self.vowels:
            count = self.text.count(i)
            if count > 0:
                frequency[i] = count
        return frequency

text = input("Enter a string: ")
vobj = VowelFrequency(text)
print(vobj.count_vowels())
