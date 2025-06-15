from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import sys
import os
# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from schemas.email_intent_schema import EmailIntentSchema,EmailActionSchema

def EmailIntentChain(email_text: str):
    # Load .env settings
    load_dotenv()

    model1 = ChatOpenAI(
    model_name="gpt-3.5-turbo-1106",
    temperature=0.1
    
    )

    model2 = ChatOpenAI(
        model_name="gpt-4-0613",
        temperature=0.1
      
    )

    # ✅ Structured Output Setup (no need to call twice)
    intent_chain = model1.with_structured_output(EmailIntentSchema,method="function_calling")
    action_chain = model2.with_structured_output(EmailActionSchema,method="function_calling")

    # ✅ Run Parallel Chain
    parallel_chain = RunnableParallel({
        "intent_data": intent_chain,
        "action_data": action_chain
    })

    result = parallel_chain.invoke(email_text)
    return result

