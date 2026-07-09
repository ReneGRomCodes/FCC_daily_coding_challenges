/*
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
 */

function triageIssue(title, labels) {
    const tLower = title.toLowerCase();

    if (labels.length === 0) {
        const hasErrorBug = tLower.includes("error") || tLower.includes("bug");
        const hasFeatureAdd = tLower.includes("feature") || tLower.includes("add");

        if (hasErrorBug) { labels.push("bug", "needs triage"); }
        if (hasFeatureAdd) { labels.push("enhancement", "discussing"); }
    }

    else {
        const isGoodFirstIssue = labels.includes("needs triage") && (tLower.includes("simple") || tLower.includes("easy"));
        const isOnRoadmap = labels.includes("discussing") && (tLower.includes("planned") || tLower.includes("next"));

        if (isGoodFirstIssue) {
            labels.splice(labels.indexOf("needs triage"), 1);
            labels.push("good first issue");
        } else if (isOnRoadmap) {
            labels.splice(labels.indexOf("discussing"), 1);
            labels.push("on the roadmap");
        } else {
            if (labels.includes("needs triage")) { labels.splice(labels.indexOf("needs triage"), 1); }
            if (labels.includes("discussing")) { labels.splice(labels.indexOf("discussing"), 1); }
            labels.push("help wanted");
        }
    }

    if (tLower.includes("security")) { labels.push("critical"); }

    return labels;
}


console.log(triageIssue("app crashes with error", []));
console.log(triageIssue("app crashes with error", ["bug", "needs triage"]));
console.log(triageIssue("add dark mode", []));
console.log(triageIssue("add dark mode", ["enhancement", "discussing"]));
console.log(triageIssue("xss security bug", []));
console.log(triageIssue("security vulnerability in auth", []));
console.log(triageIssue("easy a11y fix", ["bug", "needs triage"]));
console.log(triageIssue("planned api migration", ["enhancement", "discussing"]));
console.log(triageIssue("improve security", ["enhancement", "discussing"]));
