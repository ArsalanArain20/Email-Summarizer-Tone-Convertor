from prompts.email_summarizer_prompt import get_email_summarizer_prompt
from chains.email_summarizer_chain import email_chain
from prompts.email_language_detector_prompt import get_prompt
from chains.email_language_detector_chain import language_detector_chain

def Frontend_Email_Summarizer(email_text):
    prompt = get_email_summarizer_prompt()
    result = email_chain(prompt, email_text)
    return result

def Frontend_Email_Language_Detector(email_text):
    prompt = get_prompt()
    result = language_detector_chain(prompt, email_text)
    return result


