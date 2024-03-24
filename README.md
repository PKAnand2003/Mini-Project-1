# Py-QnA
This project aims to develop a Python-based program called Py-QnA, which utilizes state-of-the-art natural language processing techniques to generate answers to questions from academic literature. The program is designed to provide context-aware and accurate responses to user-provided questions in natural language, specifically focusing on providing answers from academic literature. <p>
Academic literature contains a wealth of information on various topics but accessing that information can be a time-consuming and tedious task. Py-QnA streamlines this process by using advanced natural language processing techniques to quickly and accurately extract the information needed to answer a question. This will be particularly useful for researchers, students and educators who need to access information from academic literature quickly and efficiently.<p>
In addition to providing answers, Py-QnA also has the capability to generate explanations and elaborations on the answers provided, this will help the users to understand the reasoning behind the answer and will be very useful in fields like education and research.
## Objectives
The program uses the RoBERTa language model, which is a transformer-based model that is trained on a massive amount of data and fine-tuned to understand natural language, making it a powerful tool for generating answers to questions from academic literature. Additionally, the program uses the python module Haystack to extract structured information from unstructured text data, making it easy to extract specific types of information from academic literature. <p>
Overall, this project is aimed at providing a powerful and versatile tool that can help users quickly and easily generate answers to questions from academic literature in natural language. Its ability to understand context and provide accurate and relevant responses makes it an asset for a wide range of applications.
## Proposed System
The proposed system utilizes state-of-the-art natural language processing techniques, specifically deep learning and transformer-based models, to generate answers to questions from academic literature. <p>
The new system utilizes the RoBERTa language model, which is fine-tuned on a large dataset of academic literature and is designed to understand natural language and provide context-aware responses. Additionally, the system uses the python module Haystack to extract structured information from unstructured text data, making it easy to extract specific types of information from academic literature.<p>
This new system addresses the limitations of traditional question answering systems by providing context-aware and accurate responses to user-provided questions in natural language. The use of the RoBERTa language model and Haystack library allows the system to understand the natural language and extract specific information from the academic literature. This makes the new system more versatile and accurate than traditional rule-based or information retrieval-based systems
## System Architecture
The project is divided into 2 main components as shown in Figure 3.1- a Python back-end and an HTML front-end. The backend is hosted on the PaaS service Google Colab and the frontend is hosted on the website Glitch.<p>
### System Design
![image](https://github.com/PKAnand2003/Mini-Project-1/assets/139564679/13bf1b26-bbb3-44eb-88de-6e090d7f1e57) <p>
The program uses the python-based framework Haystack (7) for the NLP processing. Haystack is a Python framework that is used to extract structured information from unstructured text data. It is particularly useful for tasks such as question answering and information retrieval.<p>
The module works by first pre-processing the text data, which includes cleaning and normalizing the text, tokenizing it, and converting it into a format that can be easily processed by machine learning models. The pre-processed text is then passed through a neural network-based model, such as RoBERTa, which is trained to understand natural language and extract relevant information from the text.
## Algorithm
Step 1: Text data is collected and pre-processed, which includes cleaning the text and storing in a flexible database for easy indexing and fast retrieval.<br>
Step 2: The pre-processed text is then passed through a neural network-based model- the Retriever, which is trained to understand natural language and extract relevant information from the text.<br>
Step 3: Use the output of the retriever model to extract structured information from the text, such as named entities and relationships between entities.<br>
Step 4: The extracted information is then used to generate answers to questions or to retrieve relevant information from the text.<br>
Step 5: The output is returned to the user in the form of a structured response, such as a list of relevant documents or a specific answer to a question.<br>
### Program Flowchart
![image](https://github.com/PKAnand2003/Mini-Project-1/assets/139564679/211a1725-5ec8-467d-864f-52231e8345f1)

