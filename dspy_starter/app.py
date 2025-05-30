import dspy
from dotenv import load_dotenv
import os
from signatures.classify import Classify
from signatures.math_cot import MathCOT
import sys
from utils.command_parser import CommandParser

load_dotenv()


class DspyWrapper:
    def __init__(self, model_name: str):
        # print(os.environ)
        self.llm = dspy.LM(model_name, api_key=os.environ["OPEN_AI_API_KEY"])
        dspy.configure(lm=self.llm)

    def setupSignature(self):
        self.classify = dspy.Predict(Classify)
        self.mathcot = dspy.ChainOfThought(MathCOT)

    def classifySentence(self, word: str):
        response = self.classify(sentence=word)
        return response.sentiment

    def mathOperation(self, sentence: str):
        response = self.mathcot(question=sentence)
        print("MATCH_COT_RESPONSE", response)
        return response.answer


dspyWrapper = DspyWrapper('openai/gpt-4o-mini')
dspyWrapper.setupSignature()

commandParser = CommandParser()
if commandParser.isEnoughArgs():
    print("Sentence", commandParser.getSentence())
    # print(dspyWrapper.classifySentence(commandParser.getSentence()))
    print(dspyWrapper.mathOperation(commandParser.getSentence()))
