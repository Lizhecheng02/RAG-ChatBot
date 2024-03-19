## This Repo is for creating RAG system using LangChain and Streamlit

### Python Environment

#### 1. Install Packages

```b
pip install -r requirements.txt
```

#### 2. Set Api Key

- Create a new ``openai api key``, link: https://platform.openai.com/api-keys.

<img src="Images/create_api_key.png" alt="create_api_key" style="zoom:80%;" />

- Copy it into .env file

​	Set ``OPENAI_API_KEY="Your API KEY"``

#### 3. Run Simple Version On Colab (only support one pdf file)
- Import ``colab.ipynb`` into ``Google Colab``.

- Drag your pdf file into ``Google Colab`` and change the file name in the code.
```
loader = PyPDFLoader("data.pdf")
```

- Input your ``openai api key`` in the ``ChatOpenAI()``.

```
llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key="")
```

- You can change embedding model by searching on ``HuggingFace``.
```
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/xxxxxxx")
```

- Ask question and get answer on ``Google Colab``.

<img src="Images/simple colab version.png" style="zoom:80%;" />	

#### 4. Run Streamlit On Colab
- Import ``localtunnel.ipynb`` into ``Google Colab``.


- Input your ``openai api key`` in the ``ChatOpenAI()``.
```
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.1,
    openai_api_key=""
)
```

- You can change embedding model by searching on ``HuggingFace``.
```
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/xxxxxxx",
    model_kwargs={"device": "cpu"}
)
```

- You can get three urls, but you **don't need to** click any of them, stop this cell.

<img src="Images/npx url.png" alt="npx url" style="zoom:80%;" />

- Run the next cell, get the ``tunnel password``.

<img src="Images/get curl password.png" alt="get curl password" style="zoom:80%;" />

- Run the above cell again, you can see three urls. Click the **last url** and you will see the web page below.

<img src="Images/password UI.png" alt="password UI" style="zoom:80%;" />

- Enter the ``tunnel password``, which you got in the previous step. Then you can see the ``Streamlit WebUI``.

<img src="Images/streamlit ui.png" alt="streamlit ui" style="zoom:80%;" />


#### 5. Run Streamlit On Local Computer

```
streamlit run app.py
```

After running this command, you can see the WebUI as the image above. On the **left side**, you can choose "Browse files" to upload multiple files as long as they are pdf, doc or txt format. If you encounter the error **AxiosError: Request failed with status code 403** while uploading the file. Try the command below.

```
streamlit run app.py --server.enableXsrfProtection false
```

Then you should be able to upload files successfully, like the image below.

<img src="Images/upload files.png" style="zoom:80%;" />

You need to wait for some time to let the embedding model convert all files into high dimensional vectors and store them into a database. You will see a new folder in your local computer.

<img src="Images/new folder.png" style="zoom:150%;" />

#### 6. Compare RAG With Original ChatGPT
```
python compare.py
```
The code is almost the same as ``colab.ipynb``, just add the response from original ``ChatGPT``. When you enter the question, you can see responses from both RAG system and original ChatGPT.