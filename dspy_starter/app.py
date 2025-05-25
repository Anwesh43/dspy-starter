import dspy
from dotenv import load_dotenv
import os

load_dotenv()


class DspyWrapper:
    def __init__(self, model_name: str):
        # print(os.environ)
        self.llm = dspy.LM(model_name, api_key=os.environ["OPEN_AI_API_KEY"])
        dspy.configure(lm=self.llm)

    def setupSignature(self):
        self.classify = dspy.Predict('sentence -> sentiment:bool')

    def classifySentence(self, word: str):
        response = self.classify(sentence=word)
        return response.sentiment


dspyWrapper = DspyWrapper('openai/gpt-4o-mini')
dspyWrapper.setupSignature()
print(dspyWrapper.classifySentence(
    "it's a charming and often affecting journey."))
