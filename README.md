# Markov-Text-Generator
Creates a simple markov text generator


The markov text generator can be used with 2 functionalities. The text statistics and the text generator itself. The text generator uses the text statistics functionality. The text statistics produces some information about the text, such as most common words, unique words, etc. The text generator generates text from a given word, based on the "next word". The "next word" structure represents probabilities for word succession. Randomly navigating this system generates new text by following likely word choices. Absence of successors indicates the endpoint. This approach creates varied and playful compositions based on observed patterns in the original text.

### Run in the terminal:
//python text_stats.py <txt_file> <output_file>//
If the last argument is provided, the output is not printed but instead stored in the specified file.


//python generate_text.py <txt_file> <starting_word> <max_words>//
The second argument specifies the starting word, and the last argument determines the number of words to generate.
