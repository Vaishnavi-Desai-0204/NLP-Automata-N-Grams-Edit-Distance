CS 491/691 Project 1: Natural Language Processing
This GitHub repository contains the code for Project 1 of the CS 491/691 course on Natural Language Processing. The project focuses on implementing various algorithms and models for automata, minimum edit distance, and N-grams. The repository includes the necessary files and functions to run the project and evaluate the implementations.

Project Structure
The repository has the following structure:

automata.py: This file contains the implementation of automata.

create_automata(option): Takes an option (1, 2, or 3) and returns an automaton that recognizes a specific language. The automata returned should be deterministic finite automata (DFA) and can be stored in any suitable format, such as a list, dictionary, or graph.
generate_language(automata): Takes an automaton as input and generates a word/utterance in the recognized language. This involves making random choices, so the random package should be used. The input automaton is assumed to be a DFA with no epsilon transitions.
recognize_language(automata, utterance): Takes an automaton and an utterance (string) as input and determines whether the utterance is accepted or rejected by the automaton. The function returns 1 for accept and 0 for reject.
edit_distance.py: This file contains the implementation of minimum edit distance calculations.

calc_min_edit_dist(source, target): Uses dynamic programming to calculate the edit distance between a source word and a target word. The output is the edit distance, considering insertion costs 1, deletion costs 1, and substitution costs 2.
align(source, target): Uses dynamic programming to align a source word and a target word. The function returns three lists of characters: the first represents the source word with insertions indicated by "", the second represents the target word with deletions indicated by "", and the third is a list indicating the operation performed for each character.
ngrams.py: This file contains the implementation of N-gram models.

train_ngram(train_data, n): Trains an n-gram model using the provided training data, which is a list of sentences or utterances. The function supports n-gram models with n ranging from 1 to 3. The n-gram probabilities are stored in a suitable format, such as a list or dictionary, based on your preference.
generate_language(ngram_model, max_words): Takes an n-gram model as input and generates a sentence or utterance from the model. The function randomly samples from the probability distribution to generate words, with the maximum number of words limited by max_words.
calculate_probability(utterance, ngram_model): Takes an utterance (string) and an n-gram model and calculates the probability of the utterance given the n-gram model.
test_script.py: This script is used to evaluate the implementations of the models. It includes a load_data function for the N-Gram portion of the project. Make sure the code runs without errors when executing test_script.py.

README.txt: This file should contain additional information about the project, including details about the implementation choices, any preprocessing steps performed, and any assumptions made.
