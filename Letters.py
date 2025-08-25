import nltk
import pandas as pd
import os
from nltk.corpus import wordnet, stopwords


# Define output directory and files
output_dir = r"./"
# os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "words.csv")


def generate_words_csv():
    """Generate words.csv from WordNet if it doesn't already exist."""
    if not os.path.exists(output_file):
        print("⚙️ Generating words.csv from WordNet...")

        # Download required corpora
        nltk.download("stopwords")
        nltk.download("wordnet")
        nltk.download("omw-1.4")
        set(stopwords.words('english'))
        
        # Get unique, lowercase words from WordNet
        word_list = sorted(set(w.lower() for w in wordnet.words()))

        # Build list with meanings, skip numeric-only entries
        data = []
        for w in word_list:
            if not w.isnumeric():  # skip pure numbers
                synsets = wordnet.synsets(w)
                if synsets:  # only keep words with meanings
                    meaning = synsets[0].definition()
                    data.append({"word": w, "meaning": meaning})

        # Save DataFrame
        df = pd.DataFrame(data)
        df.to_csv(output_file, index=False, encoding="utf-8")
        print(f"✅ Saved {len(df)} real words with meanings to {output_file}")
    else:
        print(f"📂 Found existing {output_file}, skipping generation.")


def get_words_by_length(length: int) -> pd.DataFrame:
    """Return a DataFrame of words that match a given character length."""
    # Load words.csv
    df = pd.read_csv(output_file)

    # Filter by length and remove numeric-only (extra safety)
    filtered_df = df[df["word"].str.len() == length]
    filtered_df = filtered_df[~filtered_df["word"].str.isnumeric()]

    return filtered_df[["word"]]


# ---- Main execution ----
# generate_words_csv()
