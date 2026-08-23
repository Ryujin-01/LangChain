from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview", dimensions=128
)

docs = [
    "The capital of France is Paris.",
    "The capital of Germany is Berlin.",
    "The capital of Italy is Rome.",
    "The capital of Spain is Madrid.",
]

query = input("Ask: ")

doc_embeddings = embedding_model.embed_documents(docs)
query_embeddings = embedding_model.embed_query(query)

# Both the arguments must be 2D lists of vectors in cosine_similarity function
# By passing a single query into "[]" it will become a list of vectors.
# scores will be a 2D array where each element [0][i] represents the cosine similarity score between the query and the i-th document.
# The [0] is added at the last to get the first element of the 2D list.
scores = cosine_similarity([query_embeddings], doc_embeddings)[0]

# enumerate(scores): This takes your list and attaches an index to every item, pairing them up in tuples. Result: (0, 10), (1, 50), (2, 20)
# list(...): This simply forces those pairs into a concrete Python list so the sorted() function can read them easily. Result: [(0, 10), (1, 50), (2, 20)]
# sorted(..., key=lambda x:x[1]): sorted sorts the list in ascending order,
# key=lambda x:x[1] tells Python: "Look at each tuple (x), and sort them based on the second item inside the tuple (x[1], which is the score)."
# [-1]: Gives the last element of the list, i.e. the one with the highest score.
# Using two variables here, i.e. index and score, assigns the first element of the list to index and the second to score.
# e.g. If the list is something like [(0, 0.78), (3, 0.82), (2, 0.88), (1, 0.92)], then index would be "1" and score would be "0.92"
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(docs[index])
print("The similarity score is: ", score)
