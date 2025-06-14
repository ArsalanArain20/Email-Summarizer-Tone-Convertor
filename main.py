from prompts.email_summarizer_prompt import get_email_summarizer_prompt
from chains.email_summarizer_chain import email_chain


def Frontend_Email_Summarizer(email_text):
    prompt = get_email_summarizer_prompt()
    result = email_chain(prompt, email_text)

    return result



