<!-- markdownlint-disable MD013 MD033 MD041 -->

# Mega-Linter Runner

[![Version](https://img.shields.io/npm/v/npm-groovy-lint.svg)](https://npmjs.org/package/npm-groovy-lint)
[![Docker Pulls](https://img.shields.io/docker/pulls/nvuillam/mega-linter)](https://hub.docker.com/r/nvuillam/mega-linter)
[![Mega-Linter](https://github.com/nvuillam/mega-linter/workflows/Mega-Linter/badge.svg?branch=master)](https://nvuillam.github.io/mega-linter)
[![codecov](https://codecov.io/gh/nvuillam/mega-linter/branch/master/graph/badge.svg)](https://codecov.io/gh/nvuillam/mega-linter)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

<!-- welcome-phrase-start -->
**Mega-Linter** analyzes [**37 languages**](#languages), [**15 formats**](#formats), [**16 tooling formats**](#tooling-formats) , [**copy-pastes**](#other) and [**spell**](#other) in your repository sources, generate [**reports in several formats**](#reports), and can even [**apply formatting and auto-fixes**](#apply-fixes) with **auto-generated commit or PR**, to ensure all your projects are clean, whatever IDE/toolbox are used by their developers !
<!-- welcome-phrase-end -->

<!-- online-doc-start -->
See [**Mega-Linter Online Documentation Web Site**](https://nvuillam.github.io/mega-linter/)
<!-- online-doc-end -->

## Mega-Linter client

This package allows to run [Mega-Linter](https://nvuillam.github.io/mega-linter/) locally before running it in your CD/CI workflow, or simply to locally apply reformatting and fixes without having to install up to date linters for your files

## Installation

### Pre-requisites

You need to have [NodeJS](https://nodejs.org/en/) and [Docker](https://www.docker.com/) installed on your computer to run Mega-Linter locally with Mega-Linter Runner

### Global installation

```shell
npm install mega-linter-runner -g
```

### Local installation

```shell
npm install mega-linter-runner --save-dev
```

## Usage

```shell
mega-linter-runner [OPTIONS]
```

The options are only related to mega-linter-runner. For Mega-Linter options, please use a `.mega-linter.yml` [configuration file](#configuration)

| Option             | Description                                               |
|--------------------|-----------------------------------------------------------|
| `-p` `--path`      | Directory containing the files to lint (default: current directory)    |
| `--fix`            | Automatically apply formatting and fixes in your files    |
| `-r``--release`    | Allows to override Mega-Linter version used (default: v4 stable)  |
| `-h` `--help`      | Show mega-linter-runner help    |
| `-v` `--version`   | Show mega-linter-runner version    |

_You can also use `npx mega-linter-runner` if you do not want to install the package_

## Configuration

Default configuration is ready out of the box

You can define a [.mega-linter.yml](https://nvuillam.github.io/mega-linter/#configuration) configuration file at the root of your repository to customize or deactivate the included linters

## Linters

<!-- linters-table-start -->
### Languages

| <!-- --> | Language / Format | Linter | Configuration key | Fix |
| --- | ----------------- | -------------- | ------------ | ------- |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/bash.ico" alt="" height="32px" class="megalinter-icon"></a> | [**BASH**](descriptors/bash.md#readme) | [bash-exec](descriptors/bash_bash_exec.md#readme)| [BASH_EXEC](descriptors/bash_bash_exec.md#readme)|  |
| <!-- --> |  | [shellcheck](descriptors/bash_shellcheck.md#readme)| [BASH_SHELLCHECK](descriptors/bash_shellcheck.md#readme)|  |
| <!-- --> |  | [shfmt](descriptors/bash_shfmt.md#readme)| [BASH_SHFMT](descriptors/bash_shfmt.md#readme)| :heavy_check_mark: |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/c.ico" alt="" height="32px" class="megalinter-icon"></a> | [**C**](descriptors/c.md#readme) | [cpplint](descriptors/c_cpplint.md#readme)| [C_CPPLINT](descriptors/c_cpplint.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/clojure.ico" alt="" height="32px" class="megalinter-icon"></a> | [**CLOJURE**](descriptors/clojure.md#readme) | [clj-kondo](descriptors/clojure_clj_kondo.md#readme)| [CLOJURE_CLJ_KONDO](descriptors/clojure_clj_kondo.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/coffee.ico" alt="" height="32px" class="megalinter-icon"></a> | [**COFFEE**](descriptors/coffee.md#readme) | [coffeelint](descriptors/coffee_coffeelint.md#readme)| [COFFEE_COFFEELINT](descriptors/coffee_coffeelint.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/cpp.ico" alt="" height="32px" class="megalinter-icon"></a> | [**C++** (CPP)](descriptors/cpp.md#readme) | [cpplint](descriptors/cpp_cpplint.md#readme)| [CPP_CPPLINT](descriptors/cpp_cpplint.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/csharp.ico" alt="" height="32px" class="megalinter-icon"></a> | [**C#** (CSHARP)](descriptors/csharp.md#readme) | [dotnet-format](descriptors/csharp_dotnet_format.md#readme)| [CSHARP_DOTNET_FORMAT](descriptors/csharp_dotnet_format.md#readme)| :heavy_check_mark: |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/dart.ico" alt="" height="32px" class="megalinter-icon"></a> | [**DART**](descriptors/dart.md#readme) | [dartanalyzer](descriptors/dart_dartanalyzer.md#readme)| [DART_DARTANALYZER](descriptors/dart_dartanalyzer.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/go.ico" alt="" height="32px" class="megalinter-icon"></a> | [**GO**](descriptors/go.md#readme) | [golangci-lint](descriptors/go_golangci_lint.md#readme)| [GO_GOLANGCI_LINT](descriptors/go_golangci_lint.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/groovy.ico" alt="" height="32px" class="megalinter-icon"></a> | [**GROOVY**](descriptors/groovy.md#readme) | [npm-groovy-lint](descriptors/groovy_npm_groovy_lint.md#readme)| [GROOVY_NPM_GROOVY_LINT](descriptors/groovy_npm_groovy_lint.md#readme)| :heavy_check_mark: |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/java.ico" alt="" height="32px" class="megalinter-icon"></a> | [**JAVA**](descriptors/java.md#readme) | [checkstyle](descriptors/java_checkstyle.md#readme)| [JAVA_CHECKSTYLE](descriptors/java_checkstyle.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/javascript.ico" alt="" height="32px" class="megalinter-icon"></a> | [**JAVASCRIPT**](descriptors/javascript.md#readme) | [eslint](descriptors/javascript_eslint.md#readme)| [JAVASCRIPT_ES](descriptors/javascript_eslint.md#readme)| :heavy_check_mark: |
| <!-- --> |  | [standard](descriptors/javascript_standard.md#readme)| [JAVASCRIPT_STANDARD](descriptors/javascript_standard.md#readme)| :heavy_check_mark: |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/jsx.ico" alt="" height="32px" class="megalinter-icon"></a> | [**JSX**](descriptors/jsx.md#readme) | [eslint](descriptors/jsx_eslint.md#readme)| [JSX_ESLINT](descriptors/jsx_eslint.md#readme)| :heavy_check_mark: |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/kotlin.ico" alt="" height="32px" class="megalinter-icon"></a> | [**KOTLIN**](descriptors/kotlin.md#readme) | [ktlint](descriptors/kotlin_ktlint.md#readme)| [KOTLIN_KTLINT](descriptors/kotlin_ktlint.md#readme)| :heavy_check_mark: |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/lua.ico" alt="" height="32px" class="megalinter-icon"></a> | [**LUA**](descriptors/lua.md#readme) | [luacheck](descriptors/lua_luacheck.md#readme)| [LUA_LUACHECK](descriptors/lua_luacheck.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/perl.ico" alt="" height="32px" class="megalinter-icon"></a> | [**PERL**](descriptors/perl.md#readme) | [perlcritic](descriptors/perl_perlcritic.md#readme)| [PERL_PERLCRITIC](descriptors/perl_perlcritic.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/php.ico" alt="" height="32px" class="megalinter-icon"></a> | [**PHP**](descriptors/php.md#readme) | [php](descriptors/php_php.md#readme)| [PHP_BUILTIN](descriptors/php_php.md#readme)|  |
| <!-- --> |  | [phpcs](descriptors/php_phpcs.md#readme)| [PHP_PHPCS](descriptors/php_phpcs.md#readme)|  |
| <!-- --> |  | [phpstan](descriptors/php_phpstan.md#readme)| [PHP_PHPSTAN](descriptors/php_phpstan.md#readme)|  |
| <!-- --> |  | [psalm](descriptors/php_psalm.md#readme)| [PHP_PSALM](descriptors/php_psalm.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/powershell.ico" alt="" height="32px" class="megalinter-icon"></a> | [**POWERSHELL**](descriptors/powershell.md#readme) | [powershell](descriptors/powershell_powershell.md#readme)| [POWERSHELL_POWERSHELL](descriptors/powershell_powershell.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/python.ico" alt="" height="32px" class="megalinter-icon"></a> | [**PYTHON**](descriptors/python.md#readme) | [pylint](descriptors/python_pylint.md#readme)| [PYTHON_PYLINT](descriptors/python_pylint.md#readme)|  |
| <!-- --> |  | [black](descriptors/python_black.md#readme)| [PYTHON_BLACK](descriptors/python_black.md#readme)| :heavy_check_mark: |
| <!-- --> |  | [flake8](descriptors/python_flake8.md#readme)| [PYTHON_FLAKE8](descriptors/python_flake8.md#readme)|  |
| <!-- --> |  | [isort](descriptors/python_isort.md#readme)| [PYTHON_ISORT](descriptors/python_isort.md#readme)| :heavy_check_mark: |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/r.ico" alt="" height="32px" class="megalinter-icon"></a> | [**R**](descriptors/r.md#readme) | [lintr](descriptors/r_lintr.md#readme)| [R_LINTR](descriptors/r_lintr.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/raku.ico" alt="" height="32px" class="megalinter-icon"></a> | [**RAKU**](descriptors/raku.md#readme) | [raku](descriptors/raku_raku.md#readme)| [RAKU_RAKU](descriptors/raku_raku.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/ruby.ico" alt="" height="32px" class="megalinter-icon"></a> | [**RUBY**](descriptors/ruby.md#readme) | [rubocop](descriptors/ruby_rubocop.md#readme)| [RUBY_RUBOCOP](descriptors/ruby_rubocop.md#readme)| :heavy_check_mark: |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/rust.ico" alt="" height="32px" class="megalinter-icon"></a> | [**RUST**](descriptors/rust.md#readme) | [clippy](descriptors/rust_clippy.md#readme)| [RUST_CLIPPY](descriptors/rust_clippy.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/scala.ico" alt="" height="32px" class="megalinter-icon"></a> | [**SCALA**](descriptors/scala.md#readme) | [scalafix](descriptors/scala_scalafix.md#readme)| [SCALA_SCALAFIX](descriptors/scala_scalafix.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/sql.ico" alt="" height="32px" class="megalinter-icon"></a> | [**SQL**](descriptors/sql.md#readme) | [sql-lint](descriptors/sql_sql_lint.md#readme)| [SQL_SQL_LINT](descriptors/sql_sql_lint.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/tsx.ico" alt="" height="32px" class="megalinter-icon"></a> | [**TSX**](descriptors/tsx.md#readme) | [eslint](descriptors/tsx_eslint.md#readme)| [TSX_ESLINT](descriptors/tsx_eslint.md#readme)| :heavy_check_mark: |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/typescript.ico" alt="" height="32px" class="megalinter-icon"></a> | [**TYPESCRIPT**](descriptors/typescript.md#readme) | [eslint](descriptors/typescript_eslint.md#readme)| [TYPESCRIPT_ES](descriptors/typescript_eslint.md#readme)| :heavy_check_mark: |
| <!-- --> |  | [standard](descriptors/typescript_standard.md#readme)| [TYPESCRIPT_STANDARD](descriptors/typescript_standard.md#readme)| :heavy_check_mark: |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/default.ico" alt="" height="32px" class="megalinter-icon"></a> | [**Visual Basic .NET** (VBDOTNET)](descriptors/vbdotnet.md#readme) | [dotnet-format](descriptors/vbdotnet_dotnet_format.md#readme)| [VBDOTNET_DOTNET_FORMAT](descriptors/vbdotnet_dotnet_format.md#readme)| :heavy_check_mark: |

### Formats

| <!-- --> | Language / Format | Linter | Configuration key | Fix |
| --- | ----------------- | -------------- | ------------ | ------- |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/css.ico" alt="" height="32px" class="megalinter-icon"></a> | [**CSS**](descriptors/css.md#readme) | [stylelint](descriptors/css_stylelint.md#readme)| [CSS_STYLELINT](descriptors/css_stylelint.md#readme)| :heavy_check_mark: |
| <!-- --> |  | [scss-lint](descriptors/css_scss_lint.md#readme)| [CSS_SCSS_LINT](descriptors/css_scss_lint.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/env.ico" alt="" height="32px" class="megalinter-icon"></a> | [**ENV**](descriptors/env.md#readme) | [dotenv-linter](descriptors/env_dotenv_linter.md#readme)| [ENV_DOTENV_LINTER](descriptors/env_dotenv_linter.md#readme)| :heavy_check_mark: |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/graphql.ico" alt="" height="32px" class="megalinter-icon"></a> | [**GRAPHQL**](descriptors/graphql.md#readme) | [graphql-schema-linter](descriptors/graphql_graphql_schema_linter.md#readme)| [GRAPHQL_GRAPHQL_SCHEMA_LINTER](descriptors/graphql_graphql_schema_linter.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/html.ico" alt="" height="32px" class="megalinter-icon"></a> | [**HTML**](descriptors/html.md#readme) | [htmlhint](descriptors/html_htmlhint.md#readme)| [HTML_HTMLHINT](descriptors/html_htmlhint.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/json.ico" alt="" height="32px" class="megalinter-icon"></a> | [**JSON**](descriptors/json.md#readme) | [jsonlint](descriptors/json_jsonlint.md#readme)| [JSON_JSONLINT](descriptors/json_jsonlint.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/latex.ico" alt="" height="32px" class="megalinter-icon"></a> | [**LATEX**](descriptors/latex.md#readme) | [chktex](descriptors/latex_chktex.md#readme)| [LATEX_CHKTEX](descriptors/latex_chktex.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/markdown.ico" alt="" height="32px" class="megalinter-icon"></a> | [**MARKDOWN**](descriptors/markdown.md#readme) | [markdownlint](descriptors/markdown_markdownlint.md#readme)| [MARKDOWN_MARKDOWNLINT](descriptors/markdown_markdownlint.md#readme)| :heavy_check_mark: |
| <!-- --> |  | [markdown-link-check](descriptors/markdown_markdown_link_check.md#readme)| [MARKDOWN_MARKDOWN_LINK_CHECK](descriptors/markdown_markdown_link_check.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/protobuf.ico" alt="" height="32px" class="megalinter-icon"></a> | [**PROTOBUF**](descriptors/protobuf.md#readme) | [protolint](descriptors/protobuf_protolint.md#readme)| [PROTOBUF_PROTOLINT](descriptors/protobuf_protolint.md#readme)| :heavy_check_mark: |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/rst.ico" alt="" height="32px" class="megalinter-icon"></a> | [**RST**](descriptors/rst.md#readme) | [rst-lint](descriptors/rst_rst_lint.md#readme)| [RST_RST_LINT](descriptors/rst_rst_lint.md#readme)|  |
| <!-- --> |  | [rstcheck](descriptors/rst_rstcheck.md#readme)| [RST_RSTCHECK](descriptors/rst_rstcheck.md#readme)|  |
| <!-- --> |  | [rstfmt](descriptors/rst_rstfmt.md#readme)| [RST_RSTFMT](descriptors/rst_rstfmt.md#readme)| :heavy_check_mark: |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/xml.ico" alt="" height="32px" class="megalinter-icon"></a> | [**XML**](descriptors/xml.md#readme) | [xmllint](descriptors/xml_xmllint.md#readme)| [XML_XMLLINT](descriptors/xml_xmllint.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/yaml.ico" alt="" height="32px" class="megalinter-icon"></a> | [**YAML**](descriptors/yaml.md#readme) | [yamllint](descriptors/yaml_yamllint.md#readme)| [YAML_YAMLLINT](descriptors/yaml_yamllint.md#readme)|  |

### Tooling formats

| <!-- --> | Language / Format | Linter | Configuration key | Fix |
| --- | ----------------- | -------------- | ------------ | ------- |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/ansible.ico" alt="" height="32px" class="megalinter-icon"></a> | [**ANSIBLE**](descriptors/ansible.md#readme) | [ansible-lint](descriptors/ansible_ansible_lint.md#readme)| [ANSIBLE_ANSIBLE_LINT](descriptors/ansible_ansible_lint.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/arm.ico" alt="" height="32px" class="megalinter-icon"></a> | [**ARM**](descriptors/arm.md#readme) | [arm-ttk](descriptors/arm_arm_ttk.md#readme)| [ARM_ARM_TTK](descriptors/arm_arm_ttk.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/cloudformation.ico" alt="" height="32px" class="megalinter-icon"></a> | [**CLOUDFORMATION**](descriptors/cloudformation.md#readme) | [cfn-lint](descriptors/cloudformation_cfn_lint.md#readme)| [CLOUDFORMATION_CFN_LINT](descriptors/cloudformation_cfn_lint.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/dockerfile.ico" alt="" height="32px" class="megalinter-icon"></a> | [**DOCKERFILE**](descriptors/dockerfile.md#readme) | [dockerfilelint](descriptors/dockerfile_dockerfilelint.md#readme)| [DOCKERFILE_DOCKERFILELINT](descriptors/dockerfile_dockerfilelint.md#readme)|  |
| <!-- --> |  | [hadolint](descriptors/dockerfile_hadolint.md#readme)| [DOCKERFILE_HADOLINT](descriptors/dockerfile_hadolint.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/editorconfig.ico" alt="" height="32px" class="megalinter-icon"></a> | [**EDITORCONFIG**](descriptors/editorconfig.md#readme) | [editorconfig-checker](descriptors/editorconfig_editorconfig_checker.md#readme)| [EDITORCONFIG_EDITORCONFIG_CHECKER](descriptors/editorconfig_editorconfig_checker.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/gherkin.ico" alt="" height="32px" class="megalinter-icon"></a> | [**GHERKIN**](descriptors/gherkin.md#readme) | [gherkin-lint](descriptors/gherkin_gherkin_lint.md#readme)| [GHERKIN_GHERKIN_LINT](descriptors/gherkin_gherkin_lint.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/kubernetes.ico" alt="" height="32px" class="megalinter-icon"></a> | [**KUBERNETES**](descriptors/kubernetes.md#readme) | [kubeval](descriptors/kubernetes_kubeval.md#readme)| [KUBERNETES_KUBEVAL](descriptors/kubernetes_kubeval.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/openapi.ico" alt="" height="32px" class="megalinter-icon"></a> | [**OPENAPI**](descriptors/openapi.md#readme) | [spectral](descriptors/openapi_spectral.md#readme)| [OPENAPI_SPECTRAL](descriptors/openapi_spectral.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/puppet.ico" alt="" height="32px" class="megalinter-icon"></a> | [**PUPPET**](descriptors/puppet.md#readme) | [puppet-lint](descriptors/puppet_puppet_lint.md#readme)| [PUPPET_PUPPET_LINT](descriptors/puppet_puppet_lint.md#readme)| :heavy_check_mark: |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/snakemake.ico" alt="" height="32px" class="megalinter-icon"></a> | [**SNAKEMAKE**](descriptors/snakemake.md#readme) | [snakemake](descriptors/snakemake_snakemake.md#readme)| [SNAKEMAKE_LINT](descriptors/snakemake_snakemake.md#readme)|  |
| <!-- --> |  | [snakefmt](descriptors/snakemake_snakefmt.md#readme)| [SNAKEMAKE_SNAKEFMT](descriptors/snakemake_snakefmt.md#readme)| :heavy_check_mark: |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/tekton.ico" alt="" height="32px" class="megalinter-icon"></a> | [**TEKTON**](descriptors/tekton.md#readme) | [tekton-lint](descriptors/tekton_tekton_lint.md#readme)| [TEKTON_TEKTON_LINT](descriptors/tekton_tekton_lint.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/terraform.ico" alt="" height="32px" class="megalinter-icon"></a> | [**TERRAFORM**](descriptors/terraform.md#readme) | [tflint](descriptors/terraform_tflint.md#readme)| [TERRAFORM_TFLINT](descriptors/terraform_tflint.md#readme)|  |
| <!-- --> |  | [terrascan](descriptors/terraform_terrascan.md#readme)| [TERRAFORM_TERRASCAN](descriptors/terraform_terrascan.md#readme)|  |
| <!-- --> |  | [terragrunt](descriptors/terraform_terragrunt.md#readme)| [TERRAFORM_TERRAGRUNT](descriptors/terraform_terragrunt.md#readme)|  |

### Other

| <!-- --> | Language / Format | Linter | Configuration key | Fix |
| --- | ----------------- | -------------- | ------------ | ------- |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/copypaste.ico" alt="" height="32px" class="megalinter-icon"></a> | [**COPYPASTE**](descriptors/copypaste.md#readme) | [jscpd](descriptors/copypaste_jscpd.md#readme)| [COPYPASTE_JSCPD](descriptors/copypaste_jscpd.md#readme)|  |
| <img src="https://github.com/nvuillam/mega-linter/raw/master/docs/assets/icons/spell.ico" alt="" height="32px" class="megalinter-icon"></a> | [**SPELL**](descriptors/spell.md#readme) | [cspell](descriptors/spell_cspell.md#readme)| [SPELL_CSPELL](descriptors/spell_cspell.md#readme)|  |

<!-- linters-table-end -->