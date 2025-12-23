import numpy as np
import faiss
import json
from sklearn.preprocessing import normalize
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

def load_data():
  vectors = np.load("data/product_vectors.npy")
  with open("data/product_meta.json", "r") as f:
    meta = json.load(f)
  return vectors, meta

def build_index(vectors):
  vectors = normalize(vectors, axis=1)
  dim = vectors.shape[1]
  index = faiss.IndexFlatIP(dim)

  index.add(vectors.astype("float32"))
  return index

def search(query, index, meta, top_k=5):
  model = SentenceTransformer(MODEL_NAME)
  query_vector = model.encode([query], convert_to_numpy=True)
  query_vector = normalize(query_vector, axis=1)

  scores, indices = index.search(query_vector.astype("float32"), top_k)

  results = []
  
  for idx, score in zip(indices[0], scores[0]):
    product = meta[idx]
    product["score"] = float(score)
    results.append(product)
  
  return results


if __name__ == "__main__":
    vectors, meta = load_data()
    index = build_index(vectors)

    # query = "black running shoes with good cushioning"
    query = "cheap casual sneakers"


    results = search(query, index, meta)

    for r in results:
      print(r["title"], "score:", round(r["score"], 3))

