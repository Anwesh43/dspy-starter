import dspy


class MathCOT(dspy.Signature):
    question: str = dspy.InputField()
    answer: float = dspy.OutputField()
