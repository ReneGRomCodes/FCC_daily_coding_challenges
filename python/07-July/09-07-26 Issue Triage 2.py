"""
Issue Triage 2
Given an issue title and an array of current labels, return an updated array of labels based on the following rules:

If the issue doesn't have any labels, add:
- "bug" and "needs triage" if the title contains "error" or "bug"
- "enhancement" and "discussing" if the title contains "feature" or "add"

Otherwise, if the given labels contain:
- "needs triage" and the title contains "simple" or "easy", remove "needs triage" and add "good first issue"
- "discussing" and the title contains "planned" or "next", remove "discussing" and add "on the roadmap"
- Otherwise, if "needs triage" or "discussing" is present, remove it and add "help wanted"

If the title contains:
- "security", add a "critical" label

1. triage_issue("app crashes with error", []) should return ["bug", "needs triage"].
2. triage_issue("app crashes with error", ["bug", "needs triage"]) should return ["bug", "help wanted"].
3. triage_issue("add dark mode", []) should return ["enhancement", "discussing"].
4. triage_issue("add dark mode", ["enhancement", "discussing"]) should return ["enhancement", "help wanted"].
5. triage_issue("xss security bug", []) should return ["bug", "needs triage", "critical"].
6. triage_issue("security vulnerability in auth", []) should return ["critical"].
7. triage_issue("easy a11y fix", ["bug", "needs triage"]) should return ["bug", "good first issue"].
8. triage_issue("planned api migration", ["enhancement", "discussing"]) should return ["enhancement", "on the roadmap"].
9. triage_issue("improve security", ["enhancement", "discussing"]) should return ["enhancement", "help wanted", "critical"].
"""

def triage_issue(title: str, labels: list[str]) -> list[str]:
    t_lower: str = title.lower()

    if not labels:
        has_error_bug: bool = "error" in t_lower or "bug" in t_lower
        has_feature_add: bool = "feature" in t_lower or "add" in t_lower

        if has_error_bug:
            labels.extend(["bug", "needs triage"])
        if has_feature_add:
            labels.extend(["enhancement", "discussing"])


    else:
        is_good_first_issue: bool = "needs triage" in labels and ("simple" in t_lower or "easy" in t_lower)
        is_on_roadmap: bool = "discussing" in labels and ("planned" in t_lower or "next" in t_lower)

        if is_good_first_issue:
            labels.remove("needs triage")
            labels.append("good first issue")
        elif is_on_roadmap:
            labels.remove("discussing")
            labels.append("on the roadmap")

        else:
            if "needs triage" in labels:
                labels.remove("needs triage")
            if "discussing" in labels:
                labels.remove("discussing")
            labels.append("help wanted")

    if "security" in t_lower:
        labels.append("critical")

    return labels


print(triage_issue("app crashes with error", []))
print(triage_issue("app crashes with error", ["bug", "needs triage"]))
print(triage_issue("add dark mode", []))
print(triage_issue("add dark mode", ["enhancement", "discussing"]))
print(triage_issue("xss security bug", []))
print(triage_issue("security vulnerability in auth", []))
print(triage_issue("easy a11y fix", ["bug", "needs triage"]))
print(triage_issue("planned api migration", ["enhancement", "discussing"]))
print(triage_issue("improve security", ["enhancement", "discussing"]))
