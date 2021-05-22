# semgrep-rules

Curated collection of [Semgrep](https://semgrep.dev/) rules.

Rules in this repository have the following severity labels:
* `WARNING` - Code patterns that have a high chance of resulting in vulnerabilities.
* `INFO` - Areas that would be interesting look at during a code review.

Rules are written to minimize false negatives at the expense of a higher false
positive rate which is a good trade-off for code reviews but would not be ideal
for use in a CI system.
