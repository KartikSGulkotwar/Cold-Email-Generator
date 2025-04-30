from langchain_groq import ChatGroq
import pandas as pd
import uuid


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key='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',
    # other params...
)
response = llm.invoke("First person to land on moon")
print(response.content)


from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://careers.nike.com/software-engineer/job/R-47110")
page_data = loader.load().pop().page_content
print(page_data)

from langchain_core.prompts import PromptTemplate
prompt_extract = PromptTemplate.from_template(
    """
    ### SCRAPED TEXT FROM WEBSITE:
    # {page_data}
    ### INSTRUCTION:
    The scraped text is from the career's page of a website.
    Your job is to extract job postings and return them in JSON format containing the following keys:
    `role`,`experience`, `skills` and `description`.
    Only return the VALID JSON.
    ### VALID JSON (NO PREAMBLE):"""
)
chain_extract = prompt_extract | llm
res = chain_extract.invoke(input={'page_data': page_data})
print(res.content)

from langchain_core.output_parsers import JsonOutputParser
json_parser = JsonOutputParser()
json_res = json_parser.parse(res.content)
json_res

df = pd.read_csv("my_portfolio.csv")
df
import chromadb
client = chromadb.PersistentClient('vectorstore')
collection = client.get_or_create_collection(name="portfolio")
if not collection.count():
    for _, row in df.iterrows():
        collection.add(documents=row["Techstack"],
                      metadatas={"links": row["Links"]},
                      ids=[str(uuid.uuid4())])
        
links = collection.query(query_texts=["Experience in Python", "Experience in React Native"], n_results=2).get('metadatas', [])
links


job = json_res
job['skills']

prompt_email = PromptTemplate.from_template(
        """
        ### JOB DESCRIPTION:
        {job_description}
        
        ### INSTRUCTION:
        You are Mohan, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating
        the seamless integration of business processes through automated tools. 
        Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
        process optimization, cost reduction, and heightened overall efficiency. 
        Your job is to write a cold email to the client regarding the job mentioned above describing the capability of AtliQ 
        in fulfilling their needs.
        Also add the most relevant ones from the following links to showcase Atliq's portfolio: {link_list}
        Remember you are Mohan, BDE at AtliQ. 
        Do not provide a preamble.
        ### EMAIL (NO PREAMBLE):
        
        """
        )

chain_email = prompt_email | llm
res = chain_email.invoke({"job_description": str(job), "link_list": links})
print(res.content)