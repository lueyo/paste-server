from pydantic import BaseModel, Field

class TextModel(BaseModel):
    id : str = Field(..., description="Unique identifier for the text request, is a 5 character string")
    text: str = Field(..., title="Text", description="The text to be transmitted")
    timestamp: str = Field(..., title="Timestamp", description="The timestamp when the text was created or transmitted")