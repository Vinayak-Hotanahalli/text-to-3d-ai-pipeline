# Import BaseModel to define structured input
from pydantic import BaseModel

# Import List for type hinting a list of strings
from typing import List

# Define a class to represent input containing a list of text prompts
class InputClass(BaseModel):
    text: List[str]
