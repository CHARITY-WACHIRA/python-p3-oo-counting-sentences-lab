#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace common abbreviations with a placeholder
        value = re.sub(r'\b(Mrs?|Mr|Dr|Jr|Sr|Rev|Prof|Gen|Lt|Adm|Hon|Capt|Sgt|Col|Maj|Pfc|Pvt|Cpl|Cpl)\. ', r'\1_PLACEHOLDER ', self.value)

        # Split the value by sentence terminators (.?!) while keeping the terminators
        sentences = re.split(r'([.?!])', value)

        # Filter out empty strings and placeholders
        sentences = [s.strip('_PLACEHOLDER') for s in sentences if s.strip('_PLACEHOLDER')]

        # Count the remaining sentences
        return len(sentences)