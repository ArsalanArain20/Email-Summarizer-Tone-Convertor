from langchain.prompts import PromptTemplate

def get_prompt():
    prompt = PromptTemplate(
            input_variables=["email"],
            validate_template=True,
            template = """
            You are a professional language detection assistant designed to analyze email content. 
            Your task is to detect and list **all** languages present in the following email.

            If the email is written in more than one language, list each language clearly.

            Email:
            {email}

            Please list the detected language(s) in the following format:
            Detected language(s):
            """ )
    return prompt

