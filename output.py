# Import BaseModel for structured data models
from pydantic import BaseModel

# Import List to define list type
from typing import List

# Define a class to represent output containing a list of text responses
class OutputClass(BaseModel):
    text: List[str] = []
