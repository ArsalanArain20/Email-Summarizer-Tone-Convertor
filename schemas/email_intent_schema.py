from typing import Literal, Optional, List
from pydantic import BaseModel, Field

class EmailIntentSchema(BaseModel):
    intent: Literal[
        "complaint", 
        "request", 
        "inquiry", 
        "feedback", 
        "job_application", 
        "follow_up", 
        "spam", 
        "other"
    ] = Field(description="The primary intent of the email, chosen from predefined categories.")

    urgency: Literal["low", "medium", "high"] = Field(description="The urgency level based on the language of the email.")

    summary: str = Field(description="A brief summary of the email content.")

    key_phrases: Optional[List[str]] = Field(default=None, description="Important keywords or phrases found in the email.")

    sender_name: Optional[str] = Field(default=None, description="The name of the person who sent the email, if mentioned.")

    recipient_name: Optional[str] = Field(default=None, description="The name of the recipient or organization the email is intended for.")

    language: Optional[str] = Field(default=None, description="The language of the email, such as English, Urdu, Arabic, etc.")

    contains_attachment: Optional[bool] = Field(default=None, description="Whether the email appears to refer to or mention an attachment.")


class EmailActionSchema(BaseModel):
    action_items: Optional[List[str]] = Field(
        default=None,
        description="List of clear actions requested or suggested in the email."
    )

    deadline: Optional[str] = Field(
        default=None,
        description="Any date or time mentioned as a deadline (in natural language), e.g., 'by Friday' or 'before June 30'."
    )

    entities_involved: Optional[List[str]] = Field(
        default=None,
        description="Names of people, companies, or departments mentioned in the email."
    )

    requires_reply: Optional[bool] = Field(
        default=None,
        description="Does the email require a reply or response?"
    )

    meeting_request: Optional[bool] = Field(
        default=None,
        description="Whether the email is requesting or proposing a meeting."
    )

    mentioned_tools: Optional[List[str]] = Field(
        default=None,
        description="Mentions of tools or platforms (e.g., Zoom, Google Docs, Slack, JIRA, etc.) in the email."
    )