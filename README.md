# Learning LangChain #
## Build AI Applications with LLMs
### by Mayo Oshin & Nuno Campos
[Learning LangChain](https://www.amazon.com/Learning-LangChain-Building-Applications-LangGraph/dp/1098167287)
- - - - 
# Table of Contents
1. [LLM Fundamentals with LangChain](#llm-fundamentals-with-langchain)
2. [RAG Part I: Indexing Your Data](#rag-part-i-indexing-your-data)
3. [RAG Part II: Chatting with Your Data](#rag-part-ii-chatting-with-your-data)
4. Using LangGraph to Add Memory to Your Chatbot
5. Cognitive Architectures with LangGraph
6. Agent Architecture
7. Agents II
8. Patterns to Make the Most of LLMs
9. Deployment: Launching Your AI Application into Production
10. Testing: Evaluation, Monitoring, and Continuous Improvement
11. Building with LLMs


## LLM Fundamentals with LangChain

We will be using Gradio to build web UIs to launch our applications.
Be sure to install the library into your environment:

`pip install --upgrade gradio`

For more information, see the [Quickstart](https://www.gradio.app/guides/quickstart) guide.
<br>
<br>

Install the LangChain libraries.

`pip install langchain langchain-openai langchain-community`

`pip install langchain-text-splitters langchain-postgres`
<br>
<br>

Optional libraries.


`pip install langchain-groq`
<br>
<br>

**Topics**
1. Chat Message Interfaces
   - HumanMessage
   - AIMessage
   - SystemMessage
   - ChatMessage
2. PromptTemplate
3. Structured Output
4. Runnable Interface

 
## RAG Part I: Indexing Your Data

**Topics**
1. Embeddings
2. Convert Documents to Text
3. Splitting Text Into Chunks
4. Generate Text Embeddings
5. Store Embeddings in a Vector Store
6. Tracking Changes to Documents
7. Indexing Optimization
8. RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval
9. ColBERT: Optimizing Embeddings

The examples in this chapter require [PGVector](https://github.com/pgvector/pgvector), an open-source vector similarity search from Postgres 
<br> You will need to install [Docker Desktop](https://docs.docker.com/get-started/get-docker/).<br>
After installing, run the following command in your terminal.

`docker run 
    --name pgvector-container 
    -e POSTGRES_USER=langchain 
    -e POSTGRES_PASSWORD=langchain 
    -e POSTGRES_DB=langchain 
    -p 6024:5432 
    -d pgvector/pgvector:pg16`



## RAG Part II: Chatting with Your Data