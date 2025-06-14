from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

def language_detector_chain(prompt,email):
    llm = ChatOpenAI(model = "gpt-3.5-turbo", temperature = 0.2)
    parser = StrOutputParser()
    chain = prompt | llm | parser
    result = chain.invoke({"email": email})
    return result
