import dspy
from typing import Literal


class Classify(dspy.Signature):
    sentence = dspy.InputField()
    sentiment: Literal["positive", "negative", "neutral"] = dspy.OutputField()
