# Python-backend Code

## Installing Packages
pip install --upgrade pip
pip install git+https://github.com/deepset-ai/haystack.git#egg=farm-haystack[colab]
pip install fastapi nest-asyncio pyngrok uvicorn

## Creating a DocumentStore
import os
from haystack.document_stores import InMemoryDocumentStore
document_store = InMemoryDocumentStore()

## Preprocessing Documents
from bs4 import BeautifulSoup
from html import unescape

def clean_text(data):
  try:
    soup = BeautifulSoup(data, 'html.parser')
    t=soup.find("div", {"class": "document"})
    l=''
    for child in t.findChildren("p" , recursive=True):
      if child.name=='p':
        l+=unescape(child.text)
    return l
  except:
    return ""

from haystack.utils import clean_wiki_text, convert_files_to_docs

docs = convert_files_to_docs(dir_path="/content/python-3.11.2-docs-html", clean_func=clean_text, split_paragraphs=True)
document_store.write_documents(docs)

from haystack.utils import clean_wiki_text, convert_files_to_docs
docs = convert_files_to_docs(dir_path="/content/python-3.11.2-docs-html", clean_func=clean_text, split_paragraphs=True)
document_store.write_documents(docs)

## Initialize Retriever
from haystack.nodes import BM25Retriever,EmbeddingRetriever

retriever = EmbeddingRetriever(document_store=document_store, embedding_model="flax-sentence-embeddings/all_datasets_v3_mpnet-base", model_format="sentence_transformers")

document_store.update_embeddings(retriever, batch_size=128)

## Initialize Reader
from haystack.nodes import FARMReader
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)

## Initialize Generator
from haystack.nodes import Seq2SeqGenerator
generator = Seq2SeqGenerator(model_name_or_path="vblagoje/bart_lfqa")

## Import and create a Pipeline
from haystack.pipelines import GenerativeQAPipeline
from haystack.utils import print_answers
pipe = GenerativeQAPipeline(generator, retriever)

## Function to fetch answers
async def search(query):
  prediction = pipe.run(query=query, params={"Retriever": {"top_k": 10}, "Generator": {"top_k": 1}})
  answer=prediction['answers'][0].answer
  return answer
  
## Simple API endpoint to access the model
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware as CORSMiddleware
import nest_asyncio
from pyngrok import ngrok
import uvicorn

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],)

@app.get('/get/{query}')
async def query(query):
  answer = await search(query)
  return {'answer':answer}

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
ngrok.disconnect(ngrok_tunnel.public_url)

