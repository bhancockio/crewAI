from typing import List

from pydantic import BaseModel

from crewai.crew import Crew

"""
Goal:
- The purpose of this class it to store a series of Crews and Sequences.
- Once the proper sequence is created, it can be kicked off.

Notes:
- Needs to keep a list of Crews and Sequences.
- 


TODOS:
- Create a type that Crew and Sequence inherit from. Needs to implement the following abstract methods:
    - Kickoff, kickoff_for_each, kickoff_async, kickoff_for_each_async
"""


class Sequence(BaseModel):
    tasks: List[Crew]
