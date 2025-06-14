from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

def email_chain(prompt,emial_content):
    #Logic Building
    model1 = ChatOpenAI(model = 'chatgpt-4o-latest', temperature = 0.3)
    model2 = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.1)

    # Create Parser
    output_parser = StrOutputParser()

    # Create RunnableSequence

    chain = prompt | model1 | output_parser
    result = chain.invoke({"email": emial_content})
    return result

