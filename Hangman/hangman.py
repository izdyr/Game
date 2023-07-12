import random

hangman_words = ['computer', 'science', 'history', 'geography', 'language', 'mathematics', 'psychology', 'philosophy', 'literature', 'art', 'music', 'architecture', 'engineering', 'medicine', 'biology', 'chemistry', 'physics', 'astronomy', 'geology', 'meteorology', 'zoology', 'botany', 'ecology', 'anthropology', 'sociology', 'economics', 'politics', 'law', 'religion', 'mythology', 'folklore', 'fairytales', 'legends', 'fables', 'nursery rhymes', 'sports', 'games', 'movies', 'television', 'celebrities', 'fashion', 'food', 'drinks', 'holidays', 'transportation', 'communication', 'technology', 'space exploration', 'oceans', 'mountains', 'deserts', 'forests', 'rivers', 'lakes', 'islands', 'countries', 'cities', 'landmarks', 'animals', 'insects', 'reptiles', 'birds', 'fish', 'plants', 'fruits', 'vegetables', 'desserts', 'spices', 'herbs', 'musical instruments', 'vehicles', 'household items', 'tools', 'professions', 'emotions', 'personality traits', 'body parts', 'clothing', 'accessories', 'furniture', 'colors', 'shapes', 'numbers', 'letters', 'seasons', 'weather', 'natural disasters', 'diseases', 'phobias', 'holidays', 'religions', 'world leaders', 'historical figures', 'famous authors', 'famous artists', 'famous musicians', 'famous actors', 'famous athletes', 'famous scientists', 'famous inventors', 'famous explorers', 'famous war heroes', 'famous philosophers', 'famous politicians', 'famous activists', 'famous businesspeople', 'famous comedians', 'famous chefs', 'famous talk show hosts', 'famous journalists', 'famous doctors', 'famous lawyers', 'famous astronauts', 'famous adventurers', 'famous gamers', 'famous youtubers', 'famous influencers', 'famous models', 'famous singers', 'famous bands', 'famous songs', 'famous albums', 'famous movies', 'famous directors', 'famous actors', 'famous characters', 'famous quotes', 'famous speeches', 'famous books', 'famous authors', 'famous plays', 'famous playwrights', 'famous poems', 'famous poets', 'famous art movements', 'famous art pieces', 'famous museums', 'famous sculptures', 'famous painters', 'famous photographers', 'famous fashion designers', 'famous models', 'famous fashion shows', 'famous cuisines', 'famous restaurants', 'famous chefs', 'famous recipes', 'famous cocktails', 'famous wines', 'famous beers', 'famous spirits', 'famous soft drinks', 'famous coffee', 'famous tea', 'famous candies', 'famous chocolates', 'famous desserts', 'famous ice creams', 'famous snacks', 'famous fast food chains', 'famous supermarkets', 'famous department stores', 'famous clothing brands', 'famous shoe brands', 'famous jewelry brands', 'famous watch brands', 'famous cosmetics brands', 'famous perfume brands', 'famous electronic brands', 'famous car brands', 'famous airline companies', 'famous hotel chains', 'famous tourist attractions', 'famous theme parks', 'famous natural wonders', 'famous landmarks', 'famous festivals', 'famous carnivals', 'famous parades', 'famous competitions', 'famous games', 'famous sports events', 'famous awards', 'famous musicians', 'famous actors', 'famous directors', 'famous producers', 'famous screenwriters', 'famous film editors', 'famous cinematographers', 'famous sound designers', 'famous animators', 'famous voice actors', 'famous comedians', 'famous talk show hosts', 'famous journalists', 'famousnews anchors', 'famous weather forecasters', 'famous scientists', 'famous inventors', 'famous engineers', 'famous mathematicians', 'famous physicists']

word_to_guess = random.choice(hangman_words)
correct_letters = []
incorrect_letters = []
max_guesses = 6
while max_guesses > 0:
    display_word = ""
    for letter in word_to_guess:
        if letter in correct_letters:
            display_word += letter
        else:
            display_word += "_"
    print(display_word)
    
    if len(incorrect_letters) > 0:
        print("Incorrect guesses: ")
        for letter in incorrect_letters:
            print(letter)
    
    guess = input("Guess a letter: ")
    # Check if the guess is correct
    if guess in word_to_guess:
        correct_letters.append(guess)
        print("Correct!")
    else:
        incorrect_letters.append(guess)
        max_guesses -= 1
        print("Incorrect!")
    
    # Check if the player has won
    if set(word_to_guess) == set(correct_letters):
        print("Congratulations, you won!")
        break
    
# Check if the player has lost
if max_guesses == 0:
    print("Sorry, you lost. The word was", word_to_guess)
