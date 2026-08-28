---
Date: 12-August-2026
Time: 07:32 AM
Status:
  - Completed
---
---
# **Notes** :-

# 1) Virtual Environment

In Python programming, a virtual environment is an isolated, self-contained folder that holds its own specific version of Python,
and its own private set of installed packages. It is designed to solve one major problem: dependency conflicts.

Imagine you are building two different software projects on the exact same computer:

- Project A is an older app you built two years ago. It relies on Package X (Version 1.0).
- Project B is a brand new app you are starting today. It requires Package X (Version 3.0).

If you just run pip install normally, Python puts everything into one giant, global folder (called site-packages).

Because you cannot have two different versions of the exact same package in one folder, installing Version 3.0 for your new app will overwrite Version 1.0.

Suddenly, your older Project A completely breaks because it doesn't understand the new code.

## The Solution: Virtual Environments

A virtual environment prevents this chaos by giving every project its own "sandbox." Think of your computer as a large house:

- **Global Installation:** This is the main shared kitchen. If you start trying to bake a cake and cook a spicy curry on the exact same counter at the exact same time using the same bowls, you get a mess.
- **Virtual Environment:** This is like building a temporary, soundproof mini-kitchen inside the house just for baking the cake. It has its own bowls, its own ingredients, and its own rules.

When you are done, you can just tear the mini-kitchen down.

### a) `python -m venv venv`

It tells Python to make a new virtual environment folder and name it venv. The second one the name of the folder.

- **-m:** The -m flag stands for module. When you use it, you are telling Python: "Search through all of my installed libraries for a module with this exact name, and run it as a script."

### b) `venv\Scripts\activate`

You have to "turn the venv on" so your computer knows to use this isolated sandbox.

---
# 2) `pip install -r requirements.txt`

### a) `pip install`

The standard command to download and install a Python package.

### b) `-r`

This flag stands for requirements. It tells pip: "Do not go looking for a package named 'requirements.txt' on the internet. Instead, read this local text file and install the things listed inside it."

### c) `requirements.txt`

This is the name of the text file you want pip to read.

---
# 3) Embeddings

An embedding is a translation layer that turns complex human information (like words, images, or audio) into a list of numbers so a computer can understand its meaning.

---
# 4) Lexical Search

If you search a database for the phrase "how to fix a leaky pipe", the computer literally scans every document looking for the words "fix", "leaky", and "pipe".

### The Flaw:

If a perfectly helpful document is titled "Repairing Drip Issues in Plumbing", a keyword search will completely miss it because it doesn't contain your exact words.

---
# 5) Semantic Search

Semantic search completely ignores the spelling of the words and focuses entirely on the mathematical coordinates (embeddings).

Here is exactly how it solves the plumbing problem step-by-step:

### a) Mapping the Database:

Before you even search, the system runs every single document it has through an embedding model.

It turns every document into a list of coordinates and plots them on that massive, multi-dimensional map.

Because they have similar meanings, the document "Repairing Drip Issues in Plumbing" is placed very close to terms like "fix", "leak", and "pipe" on the map.

### b) Mapping the query:

When you type "how to fix a leaky pipe", the search engine doesn't look for text. It instantly converts your search sentence into its own set of coordinates.

### c) Finding the "Nearest Neighbors":

The system then does a rapid mathematical calculation (usually called Cosine Similarity). It drops your query's coordinates onto the map and draws a circle around it.

It grabs whatever documents are physically sitting closest to your query in that mathematical space.

---
# 6) Prompt

A prompt is the set of instructions or the starting text you give to an AI to tell it what you want it to do.

An AI is heavily dependent on prompt, hence even if the prompt is slightly changed, the result may vary by a large margin.

### a) Static Prompt:

A static prompt is a fixed string of text. It never changes. Every single time your code runs, the exact same words are sent to the LLM.

e.g.

```python
prompt = input("Ask: ") 
result = model.invoke(prompt)
```

This is not a good way to pass prompts to the LLM as the user might make some mistakes while writing the prompt and this may cause the LLM to hallucinate.

You want a generalised experience for all the users, hence why dynamic prompts are used.

### b) Dynamic Prompt:

A dynamic prompt acts like a blueprint. Instead of hardcoding the exact request, you write a "fill-in-the-blank" template.

Before the prompt is actually sent to the LLM, your Python code injects live data, user inputs, or database information into those blanks.

e.g.

```python
user_ingredient = input("What ingredient do you have? ")
user_diet = input("Any dietary restrictions? ")

# The prompt dynamically changes based on what the user typed
prompt = f"Act as a chef. Give me a {user_diet} recipe using {user_ingredient}."

result = model.invoke(prompt)
```

### c) PromptTemplate vs ChatPromptTemplate:

PromptTemplate creates a single text prompt, whereas ChatPromptTemplate creates a structured list of chat messages.

---
# 7) LangChain Messages

In LangChain, a Message is a standardized Python object used to represent the different "voices" or "roles" in a conversation.

## The 4 Core Message Types:

### a) SystemMessage (The Director):

This is the invisible set of instructions that governs the AI's behavior.

The end-user never sees this. It dictates the persona, the rules, and the boundaries.

Example: "You are a sarcastic pirate. Always respond in pirate slang."

### b) HumanMessage (The User):

This is exactly what it sounds like. It is the raw input, question, or command provided by the human interacting with the application.

Example: "What is the capital of France?"

### c) AIMessage (The Model):

This represents the output generated by the LLM. When LangChain receives a response from Google or Hugging Face,
it automatically wraps the text inside an AIMessage object.

Example: "The capital of France be Paris, matey!"

### d) ToolMessage (The Worker - Advanced):

When you build advanced AI Agents, the AI can actually pause the conversation and run Python code (like searching Google or checking a database).

A ToolMessage is used to pass the results of that code back into the conversation so the AI can read it.

---
# 8) LangChain MessagePlaceholder

In LangChain, a MessagesPlaceholder is exactly what it sounds like: it is a designated "empty space" or "bucket" inside your prompt template that is specifically designed to hold a dynamic list of messages.

It is used to dynamically load prompts into the chat history.

---
# 9) Structured Output

In LangChain, a Structured Output refers to the practice of having language models return responses in a well defined data format (e.g. JSON), rather than having free-form text.

This makes the model output easier to parse and work with programatically.

e.g.

If you ask an LLM to name three colors, it doesn't give you a Python list. It gives you a single, flat string that looks like this:

"Here are three colors: \n1. Red \n2. Blue \n3. Green"

You cannot run a for loop over that string. You cannot easily extract "Blue" from it to save to a database.

An Structured Output acts as a translator to bridge this gap.

---
# 10) Typed Dictionary (TypedDict)

It is a way to define a dictionary in python in Python where you specify what keys and values should exist.

It helps to ensure that you dictionary follows a specific structure.

**Con:** It does not validate data at runtime.

---
# 11) Pydantic

Pydantic is a data validation and parsing library. It uses standard Python type hints to force your data to be exactly what you want it to be while your code is actively running.

### a) The Flaw with TypedDict (The "Ghost" Blueprint):

TypedDict is just a ghost. It tells your IDE (like VS Code) to warn you if you type something wrong, but the moment you hit "Run," TypedDict completely disappears.4

### b) Pydantic

Pydantic instead validates the code at runtime and throws an error if something is wrong.

---
# 12) Output Parsers

Not all LLMs are suitable to work with "with_structured_output()" function. Most of them don't support them. Hence we use Output Parsers to get structured output out of them.

Output Parsers can work with both type of LLMs, the ones who don't support "with_structured_output()" and also the ones who do. But we often use them for the first case.

Output Parsers make it easier to connect the result with "chains"

**NOTE:** with_structured_output() is a LangChain method that configures an LLM to return responses in a predefined structured format (such as a Pydantic model or TypedDict), without requiring a separate output parser.

---
# 13) Runnables

Runnable is a standardized interface. It is the fundamental "Lego block" of LangChain Expression Language (LCEL).

Before LCEL and Runnables were introduced, LangChain was a bit of a mess. Every component had a different way of being triggered:

- To use a Prompt, you had to call prompt.format()
- To use an LLM, you had to call model.predict()
- To use a Parser, you had to call parser.parse()

This made chaining them together a nightmare. You had to write a lot of custom Python "glue" code just to pass data from step A to step B.

LangChain threw all of that out and said: "From now on, every component must be a Runnable." Because everything is a Runnable, everything snaps together perfectly using the Python pipe operator (|).

You no longer have to worry about how the data gets from the Prompt to the LLM to the Parser. The Runnable interface handles the background data handoffs automatically.

Because they all share the same interface, every Runnable gives you these standard superpowers right out of the box:

### `.invoke()`

You used this. It takes a single input, runs the block, and returns a single output.

### `.batch()`

Instead of running a loop, you can pass a list of 50 customer reviews into chain.batch([review1, review2...]) and the Runnable will process them all concurrently in the background.

### `.stream()`

This yields the output chunk-by-chunk. If you are building a UI, you just call chain.stream() and the text will type itself onto the screen exactly like ChatGPT does,
without you having to write complex async generators.

---
# 14) RunnableLambda

RunnableLambda is a runnable primitive that allows you to apply custom Python functions within an AI pipeline.

It acts as a middleware between different AI components, enabling preprocessing, transformations, API calls, filtering and post processing in LangChain workflow.

---
# 15) RAG (Retrieval-Augmented Generation)

RAG is a technique where an LLM first retrieves relevant information from an external knowledge source and then uses that information to generate a more accurate answer.

## Benefits of using RAG:

### a) Use of up-to-date information.

### b) Better privacy.

### c) No limit of document size.

---
# 16) Document Loaders

In LangChain, a **Document Loader** is a specialized utility designed to bring external, unstructured data into your application and convert it into a standardized format that a Large Language Model (LLM) can understand and process.

Because LLMs can only work with text, document loaders act as the essential bridge between the raw data you have like PDFs, databases, websites, or API responses and the AI model you want to power with that data.

There are various types of document loaders in LangChain like text, pdf, csv, web page etc. You can learn how to use them by looking up on the internet.

Structure:
```python
Document(
	page_content="The actual text content."
	metadata={"source": "filename.pdf", ...}
)
```

---
# 17) Directory Loader

Directory loader is a document loader that lets you load multiple documents from a directory (folder) of files.

Structure:
```python
DirectoryLoader(
	path="... the path of the directory",
	glob="... tells which type of files to load",
	loader_cls="... tells which loader to use to read those files"
)
```

Here are examples of some different globs:
![[Pasted image 20260814130227.png]]


`load() vs lazy_load()`

- **load()**: 
	- Loads everything at once 
	- Returns a list of objects
	- Loads all the doucuments immediately into memory
	- Best when:
		- The number of documents is small.
		- You want everything loaded upfront.
	
-  lazy_load():
	- Loads the objects one by one.
	- Returns a iterator/generator of object.
	- Documents are not all loaded at once, they're fetched one at  a time as needed.
	- Best when:
		- You are dealing with large documents or lots of files.
		- You want to stream processing (e.g. chunking, embedding) without using lots of memory.

---
# 18) Text Splitting

Text Splitting is the process of breaking large chunks of text (like articles, PDFs, HTML pages or books) into smaller, manageable pieces (chunks) that an LLM can handle effectively. This has many advantages like making the prompt under model limitations, improving efficiency and accuracy, optimizing computational resources etc.

There are many types of text splitters in LangChain, some of the most common ones are: Length based, Text Structure Based, Document Structure Based, Semantic Meaning Based etc.

---
# 19) Vector Stores

A **vector store** is a system designed to **store** and **retrieve** data represented as **numerical vectors**.

## Key Features

1. **Storage** – Ensures that vectors and their associated metadata are retained, whether in-memory for quick lookups or on-disk for durability and large-scale use.

2. **Similarity Search** – Helps retrieve the vectors most similar to a query vector.

3. **Indexing** – Provide a data structure or method that enables fast similarity searches on high-dimensional vectors (e.g., approximate nearest neighbor lookups).

4. **CRUD Operations** – Manage the lifecycle of data—adding new vectors, reading them, updating existing entries, removing outdated vectors.

---
# 20) Vector Stores v/s Vector Databases

- **Vector Store**
  - Typically refers to a lightweight library or service that focuses on storing vectors (embeddings) and performing similarity search.
  - May not include many traditional database features like transactions, rich query languages, or role-based access control.
  - Ideal for prototyping, smaller-scale applications.
  - Examples: FAISS (where you store vectors and can query them by similarity, but you handle persistence and scaling separately).

- **Vector Database**
  - A full-fledged database system designed to store and query vectors.
  - Offers additional "database-like" features:
    - Distributed architecture for horizontal scaling
    - Durability and persistence (replication, backup/restore)
    - Metadata handling (schemas, filters)
    - Potential for ACID or near-ACID guarantees
    - Authentication/authorization and more advanced security
  - Geared for production environments with significant scaling, large datasets
## Use-Cases

1. Semantic Search
2. RAG
3. Recommender Systems
4. Image/Multimedia search

---
# 21) Retrievers

A **retriever** is a component in LangChain that fetches **relevant documents** from a data source in response to a user's query.

- There are multiple types of retrievers.
- All retrievers in LangChain are **runnables**.

`Retrievers v/s Document Loaders`

>Document loader gets documents into your application. Retriever finds relevant documents from your collection.


There are different types of Retrievers, some of the important ones are:

## 1) Wikipedia Retriever 

>A **Wikipedia Retriever** is a retriever that queries the **Wikipedia API** to fetch relevant content for a given query.
## How It Works

1. You give it a query (e.g., `"Albert Einstein"`).
2. It sends the query to Wikipedia's API.
3. It retrieves the **most relevant articles**.
4. It returns them as LangChain `Document` objects.

## 2) Vector Store Retriever

> A **Vector Store Retriever** in LangChain is the most common type of retriever that lets you search and fetch documents from a vector store based on **semantic similarity** using vector embeddings.

## How It Works

1. You store your documents in a vector store (like **FAISS, Chroma, Weaviate**).
2. Each document is converted into a **dense vector** using an embedding model.
3. When the user enters a query:
   - It's also turned into a vector.
   - The retriever compares the query vector with the stored vectors.
   - It retrieves the **top-k most similar** ones.

`Retrievers v/s similarity_search`

>Similarity search is a specific way of finding documents. A retriever is a general interface for finding documents.

Think about **transportation**.
### Similarity search = a car

It's one specific way of getting somewhere.

>Car → gets you from A to B

### Retriever = transportation interface

You say:

> "Get me from A to B."

The system could choose:

Car, Bus, Train, Taxi

Your application only cares that it **gets the result**.

## 3) Maximal Marginal Relevance (MMR)

> **"How can we pick results that are not only relevant to the query but also different from each other?"**

> **MMR** is an information retrieval algorithm designed to **reduce redundancy** in the retrieved results while maintaining **high relevance to the query**.

### Why MMR Retriever?

In regular similarity search, you may get documents that are:

- All very similar to each other
- Repeating the same info
- Lacking diverse perspectives

### MMR Retriever avoids that by:

- Picking the **most relevant document** first
- Then picking the next most relevant **and least similar to already selected docs**
- And so on...

### This helps especially in RAG pipelines where:

- You want your context window to contain **diverse but still relevant information**
- Especially useful when documents are **semantically overlapping**

## 4) Multi-Query Retriever

> Sometimes a single query might not capture all the ways information is phrased in your documents.

### For example:

**Query:**

> "How can I stay healthy?"

Could mean:

- What should I eat? 
- How often should I exercise? 
- How can I manage stress? 

A simple similarity search might miss documents that talk about those things but don't use the word **"healthy."**

### How It Works

1. Takes your original query.
2. Uses an LLM (e.g., GPT-3.5) to generate multiple semantically different versions of that query.
3. Performs retrieval for each sub-query.
4. Combines and deduplicates the results.

## 5) Contextual Compression Retriever

> The **Contextual Compression Retriever** in LangChain is an advanced retriever that improves retrieval quality by **compressing documents after retrieval** — keeping only the relevant content based on the user's query.

### Query

> "What is photosynthesis?"

### Retrieved Document (by a traditional retriever)

> *"The Grand Canyon is a famous natural site.*  
> *Photosynthesis is how plants convert light into energy.*  
> *Many tourists visit every year."*

### Problem

- The retriever returns the **entire paragraph**.
- Only one sentence is actually relevant to the query.
- The rest is **irrelevant noise** that wastes context window and may confuse the LLM.

### What Contextual Compression Retriever does

Returns only the relevant part, e.g.

> *"Photosynthesis is how plants convert light into energy."*

### How It Works

1. **Base Retriever** (e.g., FAISS, Chroma) retrieves N documents.
2. A **compressor** (usually an LLM) is applied to each document.
3. The compressor keeps only the parts relevant to the query.
4. Irrelevant content is discarded.

### When to Use

- Your documents are **long and contain mixed information**.
- You want to **reduce context length** for LLMs.
- You need to improve **answer accuracy in RAG pipelines**.

---
# 22) Fine Tuning

Fine-tuning is the process of taking an already trained AI model and training it further on a smaller, specialized dataset so that it becomes better suited to a particular task, behavior, or style.

## Example

Suppose you have a general LLM.

You give it:

> Convert this customer complaint into a professional response.

It might produce inconsistent responses.

You could create a dataset like:

Input:
"My order is late."

Output:
"We sincerely apologize for the delay. Your order is currently..."

Input:
"I received the wrong product."

Output:
"We apologize for the inconvenience. We will arrange..."

Input:
"I want to cancel my order."

Output:
"Certainly. We can help you cancel..."

After fine-tuning on many examples, the model learns the **desired behavior and style**.

## `Advantages of Fine-Tuning`

### 1. Better performance on a specific task:- Fine-tuning can make a model significantly better at a narrow task.

### 2. Consistent style and behavior:- Suppose you want every response to follow a particular format:

### 3. Can teach specialized behavior:- 

You can train a model for things like:

- Classification
- Text extraction
- Code generation
- Customer support
- Formatting
- Translation
- Domain-specific writing
- Structured outputs
### 4. Faster specialized workflows:- If the model has learned the desired behavior, you don't need to provide as much instruction in every request.


## `Disadvantages of Fine-Tuning`

### 1.  Computationally expensive:- Fine-tuning requires additional training.

### 2. Requires good training data:- This is probably the biggest practical problem.

### 3. Risk of overfitting:- If you train too heavily on a small dataset, the model can become too specialized.

### 4. Updating knowledge is inconvenient:- You may need to update the model frequently to keep up with the current trends.

---
# 23) RAG

**RAG stands for Retrieval-Augmented Generation.**

It is a technique where an LLM **retrieves relevant information from an external knowledge source and uses that information to generate its answer.**

The basic idea is:

> **Don't make the LLM rely only on what it learned during training. Give it the relevant information at the time of the question.**

## Why do we need RAG?

An LLM has limitations.

For example:
### 1. It may not know your private documents

Your research paper, Your company's documents, Your notes, Your database etc

The LLM wasn't necessarily trained on them.

### 2. Its knowledge can become outdated

Suppose you ask:

> "What is the company's current leave policy?"

The model may have no knowledge of a policy introduced yesterday.

### 3. You want answers grounded in specific sources

For example:

> "Answer only using my research paper."

RAG is very useful for this.

# The Stages of RAG are: 

## 1) Indexing

**Indexing** is the process of **preparing your knowledge base so that it can be efficiently searched at query time**.

This step consists of **4 sub-steps**.
### a) Document Ingestion

You load your source knowledge into memory.

### Examples

- PDF reports, Word documents
- YouTube transcripts, blog pages
- GitHub repos, internal wikis
- SQL records, scraped webpages

### Tools

- LangChain loaders (`PyPDFLoader`, `YouTubeLoader`, `WebBaseLoader`, `GitLoader`, etc.)

### b) Text Chunking

**Text Chunking** – Break large documents into small, semantically meaningful chunks.

### Why chunk?

- LLMs have context limits (e.g., 4K–32K tokens).
- Smaller chunks are more focused → better semantic search.

### Tools

- `RecursiveCharacterTextSplitter`
- `MarkdownHeaderTextSplitter`
- `SemanticChunker`

### c) Embedding Generation

**Embedding Generation** – Convert each chunk into a **dense vector (embedding)** that captures its **meaning**.

### Why embeddings?

- Similar ideas land close together in vector space.
- Allows fast, fuzzy semantic search.
### Tools

- `OpenAIEmbeddings`
- `SentenceTransformerEmbeddings`
- `InstructorEmbeddings`

### d) Storage in a Vector Store

**Storage in a Vector Store** – Store the vectors along with the **original chunk text + metadata** in a **vector database**.

### Vector DB Options

- **Local:** `FAISS`, `Chroma`
- **Cloud:** `Pinecone`, `Weaviate`, `Milvus`, `Qdrant`


## 2) Retrieval

**Retrieval** – Retrieval is the **real-time** process of finding the **most relevant pieces of information** from a **pre-built index** (created during indexing) based on the user's question.

It's like asking:

> "From all the knowledge I have, which 3–5 chunks are most helpful to answer this query?"


## 3) Augmentation

**Augmentation** refers to the step where the **retrieved documents** (chunks of relevant context) are **combined with the user's query** to form a new, enriched prompt for the LLM.


## 4) Generation

**Generation** – Generation is the final step where a **Large Language Model (LLM)** uses the **user's query** and the **retrieved & augmented context** to generate a response.

---
# 24) Tools

In LangChain, a **tool is a function that an LLM can decide to call to perform an action or access information**.

Think of it this way:

> **LLM = brain**
> **Tools = hands** 

An LLM is good at understanding language and deciding what should happen, but by itself it can't reliably do things like query a database, calculate a value, search the web, or call your own Python function.

Tools give it those abilities.

There are two types of tools in LangChain:

## 1) Built-in Tools

A **built-in tool** is a tool that LangChain already provides for you — it's **pre-built, production-ready**, and requires **minimal or no setup**.

You don't have to write the function logic yourself — you just import and use it.

| Tool                   | Purpose                   |
| ---------------------- | ------------------------- |
| `DuckDuckGoSearchRun`  | Web search via DuckDuckGo |
| `WikipediaQueryRun`    | Wikipedia summary         |
| `PythonREPLTool`       | Run raw Python code       |
| `ShellTool`            | Run shell commands        |
| `RequestsGetTool`      | Make HTTP GET requests    |
| `GmailSendMessageTool` | Send emails via Gmail     |
| `SlackSendMessageTool` | Post message to Slack     |
| `SQLDatabaseQueryTool` | Run SQL queries |
 `*These tools may be deprecated in the future.`


## 2) Custom Tools

A **custom tool** is a tool that you **define yourself**.
### Use them when:

- You want to call your own **APIs**
- You want to **encapsulate business logic**
- You want the LLM to interact with your **database, product, or app**

---
#  25) Toolkits

A **toolkit** is just a collection (bundle) of related tools that serve a common purpose — packaged together for **convenience and reusability**.

### e.g.

- A toolkit might be: `GoogleDriveToolKit`
- And it can contain the following tools:

  - `GoogleDriveCreateFileTool` — Upload a file
  - `GoogleDriveSearchTool` — Search for a file by name/content
  - `GoogleDriveReadFileTool` — Read contents of a file

---
# 26) Tool Binding

**Tool Binding** is the step where you **register tools with a Language Model (LLM)** so that:

1. The LLM knows what **tools are available**
2. It knows what **each tool does** (via description)
3. It knows what **input format to use** (via schema)

---
# 27) 

# Tool Calling

**Tool Calling** is the process where the **LLM (language model)** decides, during a conversation or task, that it needs to use a **specific tool (function)** and generates a structured output with:

- The **name of the tool**
- The **arguments** to call it with

>  **Important:** The LLM does **not actually run the tool**. It only suggests the tool and the input arguments. The actual execution is handled by **LangChain or your application**.

---
# 28) AI Agent

An AI agent is an intelligent system that receives a high-level goal from a user, and autonomously plans, decides, and executes a sequence of actions by using external tools, APIs, or knowledge sources — all while maintaining context, reasoning over multiple steps, adapting to new information, and optimizing for the intended outcome.

## Key Characteristics of an AI Agent

-  **Goal-driven**  
    You tell the agent **what you want**, not **how to do it**.
-  **Autonomous planning**  
    The agent breaks down the problem and sequences tasks on its own.
-  **Tool-using**  
    The agent calls APIs, calculators, search tools, etc.
-  **Context-aware**  
    Maintains memory across steps to inform future actions.
-  **Adaptive**  
    Rethinks the plan when things change, e.g., an API fails or data is unavailable.

---
# 29) ReAct

ReAct is a design pattern used in AI agents that stands for **Reasoning + Acting**.  

It allows a language model (LLM) to interleave internal reasoning (Thought) with external actions (like tool use) in a structured, multi-step process.

Instead of generating an answer in one go, the model thinks step by step, deciding what it needs to do next and optionally calling tools (APIs, calculators, web search, etc.) to help it.

### Example

```
User Query: Can you tell me the population of capital of France ?

Thought: I need to find the capital of France.

Action: search_tool
Action Input: "capital of France"

Observation: Paris

Thought: Now I need the population of Paris.

Action: search_tool
Action Input: "population of Paris"

Observation: 2.1 million

Thought: I now know the final answer.

Final Answer: Paris is the capital of France and has a population of ~2.1 million.
```


---
# 30) ReAct Agents in LangChain - Flowchart

> **ReAct (Reasoning + Acting)** interleaves reasoning (Thought) with actions (Tool use) in a loop until the agent can produce a final answer.

## Flow

```text
                    ┌───────────────────┐
                    │   1. User Input   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
              ┌────►│  2. LLM (Thought) │
              │     └─────────┬─────────┘
              │               │
              │               ▼
              │       ┌─────────────────────┐
              │       │ 3. Is the Final     │
              │       │    Answer Ready?    │
              │       └──────────┬──────────┘
              │                  │
              │          ┌───────┴───────┐
              │          │               │
              │         No              Yes
              │          │               │
              │          ▼               ▼
              │  ┌────────────────┐   ┌────────────────┐
              │  │ 4. Act         │   │ 7. Final       │
              │  │ Tool Selection │   │    Answer      │
              │  └───────┬────────┘   └───────┬────────┘
              │          │                    │
              │          ▼                    ▼
              │  ┌────────────────┐   ┌────────────────┐
              │  │ 5. Tool        │   │ 8. Response    │
              │  │    Execution   │   │    to User     │
              │  └───────┬────────┘   └────────────────┘
              │          │
              │          ▼
              │  ┌────────────────┐
              │  │ 6. Observation │
              │  └───────┬────────┘
              │          │
              └──────────┘
                 Loop repeats
```


# How ReAct Works

1. **User provides a question.**
2. **LLM reasons and decides the next step.**
3. **If the answer is ready → generate the Final Answer.**
4. **If not → LLM selects a tool and provides its input.**
5. **LangChain executes the tool.**
6. **The tool result (Observation) is sent back to the LLM.**
7. **The LLM reasons again using the new information.**
8. **The loop continues until a final answer is produced.**

## ReAct Loop

```text
Thought
   ↓
Action
   ↓
Tool Execution
   ↓
Observation
   ↓
Thought
   ↓
Action
   ↓
Tool Execution
   ↓
Observation
   ↓
   ...
   ↓
Final Answer
```

> **ReAct = Reasoning + Acting:** The agent repeatedly decides what to do, performs an action using a tool, observes the result, and uses that new information to decide its next action.
---
## Key Points

1. **Building Blocks** - Provides reusable components for LLM applications. - Examples: LLMs, prompts, retrievers, vector stores, tools, and output parsers. 
2. **Workflows** - Connects these components into chains and pipelines. - Allows data to flow from one component to another. 
3. **Tool & Agent Interaction** - Allows LLMs to use external tools, APIs, databases, calculators, search engines, etc. - Agents can dynamically decide which tools to use and in what order.

# Tags

- [[Generative_AI]]

## References

- [LangChain - CampusX](https://youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0&si=WJJIW9F_OOEjgyTw)
