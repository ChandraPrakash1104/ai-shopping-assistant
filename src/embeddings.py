import pandas as pd
import numpy as np
import json
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

def load_product_data(file_path):
    df = pd.read_csv(file_path)

    df["text"] = (
        df["title"].fillna("") + " | " +
        df["description"].fillna("") + " | " + 
        df["brand"].fillna("")
    )
    return df

def build_embeddings(csv_path, vectors_out, meta_out):
    df = load_product_data(csv_path)

    model = SentenceTransformer(MODEL_NAME)

    texts = df["text"].tolist()
    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True
    )
    np.save(vectors_out, embeddings)

    meta = df[["id", "title", "description", "price", "brand", "image_url"]]
    meta.to_json(meta_out, orient="records", indent=2)
    print("Saved embeddings and metadata")
    print("Embedding shape:", embeddings.shape)

if __name__ == "__main__":
    build_embeddings(
        "data/products_sample.csv",
        "data/product_vectors.npy",
        "data/product_meta.json"
    )