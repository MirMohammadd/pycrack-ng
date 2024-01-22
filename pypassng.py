import itertools

def generate_combinations(character_sets, length):
    return itertools.product(character_sets, repeat=length)

def generate_words(fixed_string, character_sets, min_length, max_length):
    for length in range(min_length // 2, (max_length + 1) // 2 + 1):
        combinations_before = generate_combinations(character_sets, length)
        combinations_after = generate_combinations(character_sets, length)

        for combination_before in combinations_before:
            for combination_after in combinations_after:
                word = "".join(combination_before) + fixed_string + "".join(combination_after)
                yield word

def save_to_file(words, output_file):
    with open(output_file, "w") as file:
        for word in words:
            file.write(word + "\n")

fixed_string = "Amir"
character_sets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?/[]{}"
min_length = 6
max_length = 20
output_file = "wordlist.txt"

words_generator = generate_words(fixed_string, character_sets, min_length, max_length)
save_to_file(words_generator, output_file)

print(f"Wordlist generated and saved to {output_file}")
