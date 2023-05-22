def train_ngram(train_data, n):
    # Initialize the n-gram model dictionary
    ngram_model = {}

    # Iterate over each sentence in the training data
    for sentence in train_data:
        # Split the sentence into individual words
        words = sentence.split()

        # Iterate over each n-gram in the sentence
        for i in range(len(words) - n + 1):
            ngram = ' '.join(words[i:i+n-1])

            # If the n-gram is not already in the dictionary, add it
            if ngram not in ngram_model:
                ngram_model[ngram] = {}

            # Increment the count for the following word
            next_word = words[i+n-1]
            if next_word not in ngram_model[ngram]:
                ngram_model[ngram][next_word] = 0
            ngram_model[ngram][next_word] += 1

    # Normalize the counts to obtain probabilities
    for ngram in ngram_model:
        total_count = sum(ngram_model[ngram].values())
        for next_word in ngram_model[ngram]:
            ngram_model[ngram][next_word] /= total_count
    
    return ngram_model

import random

def generate_language(ngram_model, max_words):
    ngram = random.choice(list(ngram_model.keys()))
    sentence = ngram.split()

    while len(sentence) < max_words:
        if ngram not in ngram_model:
            break

        next_words = list(ngram_model[ngram].keys())
        probabilities = list(ngram_model[ngram].values())
        next_word = random.choices(next_words, probabilities)[0]

        sentence.append(next_word)
        ngram = ' '.join(sentence[-(len(ngram.split())-1):])

    return ' '.join(sentence)

def calculate_probability(sentence, ngram_model): #doesnt work 100% but i cant figure out why especuially for the unigram
    n = len(list(ngram_model.keys())[0].split()) + 1
    
    # Split the sentence into individual words
    words = sentence.split()

    # Initialize the probability to 1.0
    probability = 1.0

    # Iterate over each n-gram in the sentence
    for i in range(len(words) - (n-1)):
        ngram = ' '.join(words[i:i+n-1])
            
            # Check if the n-gram is in the model
        if ngram in ngram_model:
            next_word = words[i+n-1]

            probability *= ngram_model[ngram][next_word]
                
        else:
            # If the n-gram is not in the model, assign a probability of zero
            probability = 0.0
            break
    

    return probability
