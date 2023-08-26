AGENT_INSTRUCTIONS = """
You are an agent which answers questions regarding privacy policies.
"""

QUESTIONS = """
1. What personal information is being collected?
2. Why is personal information collected?
3. How is personal information collected?
4. Is the collected information shared with third parties?
5. What security measures are being taken to secure personal information?
6. How long is personal information kept?
7. Can users delete stored personal information?
"""

TRANSFORM_TO_JSON_INSTRUCTIONS = """
Given the following enumerated list, create a corresponding stringified array where each enumerated element becomes an element in the array. Reply only with the valid array.
"""

VALIDATE_PRIVACY_POLICY_INSTRUCTIONS = """
Is the following input a privacy policy? Reply only with "Yes" or "No".
"""
