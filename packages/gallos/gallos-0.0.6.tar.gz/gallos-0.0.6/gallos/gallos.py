"""
    library to talk with brollo
"""
from random import randint

def talk():
    """
        Returns a typical sentence from brollo

        Returns:
            A string with the actual sentence
    """
    sentences = [
        "yo",
        "com'e'",
        "tutto tappo?",
        "che sbatti",
        "ciao brollo",
        "letto librito?",
        "capra!",
        "qui nanna ora",
        "uff"]
    print(sentences[randint(0,len(sentences)-1)])

def synonym(noun):
    """
        Provides a synonym for a given noun

        Args:
            noun (str): The noun for the synonym

        Returns:
            A string with the synonym
    """
    print("anche {} si chiama".format(noun))
