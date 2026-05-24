"""
Open Issues
Given an array of issue numbers and another array of pull request (PR) numbers, return an array of issues that remain
open after all PRs have been merged.

- A PR closes an issue if their digits are a rotation of each other. For example, issue 123 would be closed by PR 231 or
  312.
- A PR does not close an issue with the exact same number. For example, PR 123 does not close issue 123. So an issue with
  all the same number can't get closed.
- Either number may have leading zeros stripped. For example, PR 201 would close issue 12 (012, a rotation of 201).
  Similarily, issue 201 would be closed by PR 12.

Return the remaining open issues in the order they were given.

1. getOpenIssues([123, 234], [231]) should return [234].
2. getOpenIssues([123, 345, 16], [345, 231]) should return [345, 16].
3. getOpenIssues([456, 332, 12, 15], [201, 945, 180]) should return [456, 332, 15].
4. getOpenIssues([12, 115, 296, 170, 24], [17, 18, 19, 20, 21]) should return [115, 296, 24].
5. getOpenIssues([19, 95, 422, 395, 754, 102, 296, 709, 237, 4400, 1802], [395, 440, 9001, 95, 242, 21, 287, 169, 14])
    should return [95, 395, 754, 296, 709, 237, 1802].
"""

def is_rotation(a: int, b: int) -> bool:
    max_len: int = max(len(str(a)), len(str(b)))

    sa: str = str(a).zfill(max_len)
    sb: str = str(b).zfill(max_len)

    if sa == sb:
        return False

    return sb in (sa + sa)


def get_open_issues(issues: list[int], prs: list[int]) -> list[int]:
    remaining: list[int] = []

    for issue in issues:
        closed: bool = any(is_rotation(issue, pr) for pr in prs)

        if not closed:
            remaining.append(issue)

    return remaining


print(get_open_issues([123, 234], [231]))
print(get_open_issues([123, 345, 16], [345, 231]))
print(get_open_issues([456, 332, 12, 15], [201, 945, 180]))
print(get_open_issues([12, 115, 296, 170, 24], [17, 18, 19, 20, 21]))
print(get_open_issues([19, 95, 422, 395, 754, 102, 296, 709, 237, 4400, 1802], [395, 440, 9001, 95, 242, 21, 287, 169, 14]))
