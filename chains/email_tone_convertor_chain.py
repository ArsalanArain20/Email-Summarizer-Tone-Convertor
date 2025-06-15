# Imports
import sys
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Email Tone Converter & Response Suggestion Chain
def Email_Response_Suggestion(response_prompt,suggestion_promot,email_content,target_tone):
    load_dotenv()
    parser = StrOutputParser()
    model1 = ChatOpenAI(model="gpt-4",temperature=0.2)
    model2 = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.5)
    
    
    # Run both in parallel and return combined result
    parallel_chain = RunnableParallel( {
    "response": RunnableSequence(response_prompt, model1, parser),
    "suggestion": RunnableSequence(suggestion_promot, model2, parser),
    })
    
    chain = parallel_chain.invoke({"email_content":email_content,"target_tone":target_tone})
    return chain