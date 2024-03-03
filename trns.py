from googletrans import Translator

# Create a translator object
translator = Translator()

# Define a function to translate text
def translate(text, src, dest):
    """Translates text from one language to another.

    Args:
        text: The text to translate.
        src: The source language code.
        dest: The destination language code.

    Returns:
        The translated text.
    """

    translation = translator.translate(text, src=src, dest=dest)
    return translation.text

# Get the text to translate from the user
text = input("Enter the text to translate: ")

# Get the source and destination language codes from the user
src = input("Enter the source language code: ")
dest = input("Enter the destination language code: ")

# Translate the text
translated_text = translate(text, src, dest)

# Print the translated text
print("The translated text is:", translated_text)