AGENT_INSTRUCTIONS = """
You are an agent whose purpose is to answer questions regarding privacy policies.
"""

FORMATTING_INSTRUCTIONS = """
Given a numbered list of questions, provide a valid JSON array of answers.
# User input
Privacy policy:
{privacy policy}
Questions:
{question 1}
{question 2}
{question_3}
# Your answer
[{answer 1}, {answer 2}, {answer 3}]
"""

QUESTIONS = """
What personal information is being collected?
Why is personal information collected?
How is personal information collected?
Is the collected information shared with third parties?
What security measures are being taken to secure personal information?
How long is personal information kept?
Can users delete stored personal information?
"""

FORMATTING_REPAIR_INSTRUCTIONS = """
Turn this input into a valid JSON array. Reply only with the valid array.
"""
