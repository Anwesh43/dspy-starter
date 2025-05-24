import dspy
from dotenv import load_dotenv
import os
load_dotenv()


class DspyWrapper:
    def __init__(self, model_name: str):
        self.llm = dspy.lm(model_name, os.environ["OLLAMA_URL"])
        dspy.configure(lm=self.llm)

    def setupSignature(self):
        self.classify = dspy.Predict('sentence -> sentiment:bool')

    def classifySentence(self, word: str):
        print(self.classify(word))
