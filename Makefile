test:
	semgrep --validate --config=$$PWD/rules/python $$PWD/rules
	semgrep --validate --config=$$PWD/rules/javascript $$PWD/rules
	semgrep --test --strict --test-ignore-todo --dangerously-allow-arbitrary-code-execution-from-rules $$PWD/rules

output:
	semgrep --test --strict --test-ignore-todo --dangerously-allow-arbitrary-code-execution-from-rules --save-test-output-tar $$PWD/rules
