"""
Issue Triage
Given a number of milliseconds since the last post on an issue, and the last message posted on the issue, determine what
you should do with the issue according to these rules:

- If the last message is less than 7 days ago, return "leave it"
- If the last message is 7 or more days ago and its content contains "bump" (case-insensitive), return "close it"
- Otherwise, return "bump it"

1. triage_issue(86400000, "Lets fix it") should return "leave it".
2. triage_issue(1209600000, "still waiting") should return "bump it".
3. triage_issue(864000000, "bump") should return "close it".
4. triage_issue(604800000, "Do we still want this?") should return "bump it".
5. triage_issue(604800000, "Bumping this") should return "close it".
6. triage_issue(345600000, "I'll make a PR") should return "leave it".
"""

def triage_issue(ms: int, message: str) -> str:
    days: float = ms / 86_400_000

    if days < 7:
        return "leave it"
    elif "bump" in message.lower():
        return "close it"
    else:
        return "bump it"


print(triage_issue(86400000, "Lets fix it"))
print(triage_issue(1209600000, "still waiting"))
print(triage_issue(864000000, "bump"))
print(triage_issue(604800000, "Do we still want this?"))
print(triage_issue(604800000, "Bumping this"))
print(triage_issue(345600000, "I'll make a PR"))
