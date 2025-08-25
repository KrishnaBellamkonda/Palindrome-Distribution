# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import Letters


# %%
# Get the required dictionary csv
Letters.generate_words_csv()

# %%
# dictionary = pd.DataFrame(["bob", "candle", "yes"], columns=["Word"])

# %%
# Palindrome check
def palindrome_check(words: pd.DataFrame):
    words["reverse"] = words["word"].str[::-1]
    words["isPalindrome"] = words["word"] == words["reverse"]
    palindromes = words[words["isPalindrome"]]["word"].tolist()
    return words["isPalindrome"].sum(), palindromes

# %%
# Set up
min_letters = 2
max_letters = 25
number_of_letters = np.arange(1, max_letters+1)
values = []
palindrome_words = []

for n_letters in number_of_letters:
    df = Letters.get_words_by_length(n_letters)
    n_palindromes, palindromes = palindrome_check(df)
    values.append(n_palindromes)
    palindrome_words.append(palindromes)

# %%
palindrome_words[2]

# %%
# Extract the required df

# %%
# Figure size
plt.figure(figsize=(6,4))

# Bar plot with soft color + edge
bars = plt.bar(number_of_letters, values, color="steelblue", edgecolor="black", alpha=0.8)

# Titles and labels
plt.title("Palindrome Frequency Distribution", fontsize=14, weight="bold")
plt.xlabel("Number of Letters in Word", fontsize=12)
plt.ylabel("Number of Palindromes", fontsize=12)

# Grid for readability
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Add values on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.2,
             str(height), ha="center", va="bottom", fontsize=10)

# Ticks styling
plt.xticks(number_of_letters, fontsize=11)
plt.yticks(fontsize=11)

# Clean layout
plt.tight_layout()
plt.show()

# %%



