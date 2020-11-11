# Changelog

## Insiders (master)

- Add Visual Basic .NET language & dotnet-format
- Refactor removal of arguments for formatters (from custom class to Linter generic class)
- Perl: lint files with no extension containing Perl shebang
- Add automerge for PR issues from linter versions updates
- Fix ignored root files issue

## [4.4.0] 2020-11-05

- Add Python [iSort](https://pycqa.github.io/isort/)
- Quick fix "PR Comment" reporter (orange light emoji)
- Refresh fork

## [4.3.2] 2020-11-04

- Add spell checker **cspell**
- Add Github Action Workflow to automatically:
  - update linters dependencies
  - rebuild Mega-Linter documentation
  - create a PR with updates

- Apply fixes performed by linters:
  - User configuration (APPLY_FIXES vars)
  - Descriptors configuration: cli_lint_fix_arg_name set on linter in YML when it can format and/or auto-fix issues
  - Provide fixed files info in reports
  - Test cases for all fixable file types: sample_project_fixes
  - Generate README linters table with column "Fix"
  - Provide fix capability in linters docs
  - Update Workflows YMLs to create PR or commit to apply fixes

- Core Archi:
  - All linters now have a name different than descriptor_id
  - replace calls from os.path.exists to os.path.isfile and os.path.isdir

- Other:
  - fix Phive install
  - Upgrade linter versions & help

## [4.0.0] 2020-10-01

- Initial version
