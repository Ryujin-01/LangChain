# This is a Youtube chatbot app. It is an application of RAG.

from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_classic.retrievers import MultiQueryRetriever
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

load_dotenv()

# Setting up our LLM
llm_model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")


# Setting up the API
ytt_api = YouTubeTranscriptApi()


# Fetching the data.
video_id = "kpIy4pmP62Y"
try:
    # This contains all the metadata about the transcript, including the timestamps.
    transcript_list = ytt_api.fetch(video_id=video_id, languages=["en"])

except Exception as e:
    print("No transcript available :(\n")
    print(e)  # Prints the exception
    exit()  # Exits the code here.

# join() is used to combine multiple strings using a separator.
# Here we are fetching the text of the transcript and joining it into one single string.
transcript = " ".join(snippet.text for snippet in transcript_list)

# print(transcript)


# Splitting the transcript into smaller chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, separators=[" ", ""]
)

chunks = splitter.split_text(transcript)

# print(len(chunks), chunks)


# Setting up the vector store.
# We are making a document object here because the ".from_document" method expects a document object.
docs = [
    Document(
        page_content=chunk,
        metadata={"source": "YouTube", "video_id": video_id, "chunk_id": i},
    )
    for i, chunk in enumerate(chunks)
]

# We could have used the ".from_text" method to take the list of strings. This would have saved us time in making document object.
# But that way we could not give metadata to the documents. Hence we are using document object.
# NOTE: We are storing the vector store on RAM because we are just learning and testing our little RAG application.
# And hence there is no need to specify a directory or collection_name.
vector_store = Chroma.from_documents(
    documents=docs,
    embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001"),
)

# print(vector_store.get(include=["documents", "metadatas", "embeddings"]))


# Setting up the Multi Query Retriever to account for ambiguous questions asked by the user.
retriever = MultiQueryRetriever.from_llm(
    retriever=vector_store.as_retriever(
        search_type="mmr", search_kwargs={"fetch_k": 6, "k": 3, "lambda_mult": 0.5}
    ),
    llm=llm_model,
)


# Setting up a prompt for the final LLM call.
template = PromptTemplate.from_template("""
    You are a helpful assistant answering questions about a YouTube video.

    Answer the user's question using ONLY the information provided in the
    retrieved transcript context below.

    If the answer cannot be found in the context, say:
    "I couldn't find the answer in the video transcript."

    Do not make up information or use outside knowledge.

    Be concise but provide enough explanation to properly answer the question.

    Retrieved transcript context:
    {context}

    User question:
    {question}

    Answer:
""")


# Taking the user query
question = input("Ask: ")


# Setting up the chains.
parallel_chain = RunnableParallel(question=RunnablePassthrough(), context=retriever)

parser = StrOutputParser()
chain = parallel_chain | template | llm_model | parser


# Final result
result = chain.invoke(question)
print(result)
