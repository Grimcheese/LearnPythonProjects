import json
import os

class MadLibs:
    path = "./templates"
    def __init__(self, word_descriptions, template):
        self.template = template
        self.word_descriptions = word_descriptions

    @classmethod
    def from_json(cls, name, path= None):
        if not path:
            path = cls.path
        fpath = os.path.join(path, name)
        with open(fpath, "r") as f:
          data = json.load(f)

        mad_lib = cls(**data)
        return mad_lib

# Get user input
def get_words_from_user(word_descriptions):

    user_words = []

    print("Please input the following words: ")
    for description in word_descriptions:
        user_input = input(description+ ": ")
        user_words.append(user_input)

    return user_words

# Build the story

def build_story(template, words):
    story = template.format(*words)
    
    return story

def select_template_name():
    print("Select a Mad Lib from the following list: ")
    templates = os.listdir(MadLibs.path)
    template = input(str(templates) + " ")
    
    return template

temp_name = select_template_name()
mad_lib = MadLibs.from_json(temp_name)

words = get_words_from_user(mad_lib.word_descriptions)
story = build_story(mad_lib.template, words)

print(story)