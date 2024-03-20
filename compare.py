from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_community.embeddings import HuggingFaceEmbeddings
from openai import OpenAI
from dotenv import load_dotenv
import warnings
import os
warnings.filterwarnings("ignore")

load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def response(question):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    original_output = completion.choices[0].message.content

    return original_output


loader = PyPDFLoader("data.pdf")
data = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(data)

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectorstore = Chroma.from_documents(
    documents=texts,
    embedding=embedding,
    persist_directory="chroma_store"
)

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0,
    openai_api_key=os.environ["OPENAI_API_KEY"]
)  # input your openai api key

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

while True:
    query = input()
    if query == "exit":
        break
    result = qa({"query": query})
    original_output = response(question=query)
    print("RAG ChatGPT:", result["result"])
    print("Original ChatGPT:", original_output)
    print("\n")
