test:
	semgrep --validate --config=$$PWD/rules/python $$PWD/rules
	semgrep --validate --config=$$PWD/rules/javascript $$PWD/rules
	semgrep --test --strict --test-ignore-todo $$PWD/rules

output:
	semgrep --test --strict --test-ignore-todo --save-test-output-tar $$PWD/rules
