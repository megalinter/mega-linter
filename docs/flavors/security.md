# security MegaLinter Flavor

![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter-security/v6-alpha)
![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter-security)

## Description

Optimized for security

## Usage

- [GitHub Action](https://megalinter.github.io/v6-alpha/installation/#github-action): **megalinter/megalinter/flavors/security@v6-alpha**
- Docker image: **megalinter/megalinter-security:v6-alpha**
- [mega-linter-runner](https://megalinter.github.io/v6-alpha/mega-linter-runner/): `mega-linter-runner --flavor security`

## Embedded linters

### Languages

| <!-- --> | Language | Linter | Configuration key | Additional  |
| :---: | ----------------- | -------------- | ------------ | :-----:  |
| <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/bash.ico" alt="" height="32px" class="megalinter-icon"></a> <!-- linter-icon --> | [**BASH**](https://megalinter.github.io/v6-alpha/descriptors/bash/) | [bash-exec](https://megalinter.github.io/v6-alpha/descriptors/bash_bash_exec/)| [BASH_EXEC](https://megalinter.github.io/v6-alpha/descriptors/bash_bash_exec/)| 
| <!-- --> <!-- linter-icon --> |  | [shellcheck](https://megalinter.github.io/v6-alpha/descriptors/bash_shellcheck/)| [BASH_SHELLCHECK](https://megalinter.github.io/v6-alpha/descriptors/bash_shellcheck/)| [![GitHub stars](https://img.shields.io/github/stars/koalaman/shellcheck?cacheSeconds=3600)](https://github.com/koalaman/shellcheck)
| <!-- --> <!-- linter-icon --> |  | [bandit](https://megalinter.github.io/v6-alpha/descriptors/python_bandit/)| [PYTHON_BANDIT](https://megalinter.github.io/v6-alpha/descriptors/python_bandit/)| [![GitHub stars](https://img.shields.io/github/stars/PyCQA/bandit?cacheSeconds=3600)](https://github.com/PyCQA/bandit) ![sarif](https://shields.io/badge/-SARIF-orange)

### Formats

| <!-- --> | Format | Linter | Configuration key | Additional  |
| :---: | ----------------- | -------------- | ------------ | :-----:  |

### Tooling formats

| <!-- --> | Tooling format | Linter | Configuration key | Additional  |
| :---: | ----------------- | -------------- | ------------ | :-----:  |
| <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/ansible.ico" alt="" height="32px" class="megalinter-icon"></a> <!-- linter-icon --> | [**ANSIBLE**](https://megalinter.github.io/v6-alpha/descriptors/ansible/) | [ansible-lint](https://megalinter.github.io/v6-alpha/descriptors/ansible_ansible_lint/)| [ANSIBLE_ANSIBLE_LINT](https://megalinter.github.io/v6-alpha/descriptors/ansible_ansible_lint/)| [![GitHub stars](https://img.shields.io/github/stars/ansible/ansible-lint?cacheSeconds=3600)](https://github.com/ansible/ansible-lint)
| <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/cloudformation.ico" alt="" height="32px" class="megalinter-icon"></a> <!-- linter-icon --> | [**CLOUDFORMATION**](https://megalinter.github.io/v6-alpha/descriptors/cloudformation/) | [cfn-lint](https://megalinter.github.io/v6-alpha/descriptors/cloudformation_cfn_lint/)| [CLOUDFORMATION_CFN_LINT](https://megalinter.github.io/v6-alpha/descriptors/cloudformation_cfn_lint/)| [![GitHub stars](https://img.shields.io/github/stars/aws-cloudformation/cfn-lint?cacheSeconds=3600)](https://github.com/aws-cloudformation/cfn-lint) ![sarif](https://shields.io/badge/-SARIF-orange)
| <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/dockerfile.ico" alt="" height="32px" class="megalinter-icon"></a> <!-- linter-icon --> | [**DOCKERFILE**](https://megalinter.github.io/v6-alpha/descriptors/dockerfile/) | [hadolint](https://megalinter.github.io/v6-alpha/descriptors/dockerfile_hadolint/)| [DOCKERFILE_HADOLINT](https://megalinter.github.io/v6-alpha/descriptors/dockerfile_hadolint/)| [![GitHub stars](https://img.shields.io/github/stars/hadolint/hadolint?cacheSeconds=3600)](https://github.com/hadolint/hadolint) ![sarif](https://shields.io/badge/-SARIF-orange)
| <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/kubernetes.ico" alt="" height="32px" class="megalinter-icon"></a> <!-- linter-icon --> | [**KUBERNETES**](https://megalinter.github.io/v6-alpha/descriptors/kubernetes/) | [kubeval](https://megalinter.github.io/v6-alpha/descriptors/kubernetes_kubeval/)| [KUBERNETES_KUBEVAL](https://megalinter.github.io/v6-alpha/descriptors/kubernetes_kubeval/)| [![GitHub stars](https://img.shields.io/github/stars/instrumenta/kubeval?cacheSeconds=3600)](https://github.com/instrumenta/kubeval)
| <!-- --> <!-- linter-icon --> |  | [kubeconform](https://megalinter.github.io/v6-alpha/descriptors/kubernetes_kubeconform/)| [KUBERNETES_KUBECONFORM](https://megalinter.github.io/v6-alpha/descriptors/kubernetes_kubeconform/)| [![GitHub stars](https://img.shields.io/github/stars/yannh/kubeconform?cacheSeconds=3600)](https://github.com/yannh/kubeconform)
| <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/terraform.ico" alt="" height="32px" class="megalinter-icon"></a> <!-- linter-icon --> | [**TERRAFORM**](https://megalinter.github.io/v6-alpha/descriptors/terraform/) | [tflint](https://megalinter.github.io/v6-alpha/descriptors/terraform_tflint/)| [TERRAFORM_TFLINT](https://megalinter.github.io/v6-alpha/descriptors/terraform_tflint/)| [![GitHub stars](https://img.shields.io/github/stars/terraform-linters/tflint?cacheSeconds=3600)](https://github.com/terraform-linters/tflint) ![sarif](https://shields.io/badge/-SARIF-orange)
| <!-- --> <!-- linter-icon --> |  | [terrascan](https://megalinter.github.io/v6-alpha/descriptors/terraform_terrascan/)| [TERRAFORM_TERRASCAN](https://megalinter.github.io/v6-alpha/descriptors/terraform_terrascan/)| [![GitHub stars](https://img.shields.io/github/stars/accurics/terrascan?cacheSeconds=3600)](https://github.com/accurics/terrascan) ![sarif](https://shields.io/badge/-SARIF-orange)
| <!-- --> <!-- linter-icon --> |  | [terragrunt](https://megalinter.github.io/v6-alpha/descriptors/terraform_terragrunt/)| [TERRAFORM_TERRAGRUNT](https://megalinter.github.io/v6-alpha/descriptors/terraform_terragrunt/)| [![GitHub stars](https://img.shields.io/github/stars/gruntwork-io/terragrunt?cacheSeconds=3600)](https://github.com/gruntwork-io/terragrunt) ![autofix](https://shields.io/badge/-autofix-green)
| <!-- --> <!-- linter-icon --> |  | [checkov](https://megalinter.github.io/v6-alpha/descriptors/terraform_checkov/)| [TERRAFORM_CHECKOV](https://megalinter.github.io/v6-alpha/descriptors/terraform_checkov/)| [![GitHub stars](https://img.shields.io/github/stars/bridgecrewio/checkov?cacheSeconds=3600)](https://github.com/bridgecrewio/checkov) ![sarif](https://shields.io/badge/-SARIF-orange)
| <!-- --> <!-- linter-icon --> |  | [kics](https://megalinter.github.io/v6-alpha/descriptors/terraform_kics/)| [TERRAFORM_KICS](https://megalinter.github.io/v6-alpha/descriptors/terraform_kics/)| [![GitHub stars](https://img.shields.io/github/stars/checkmarx/kics?cacheSeconds=3600)](https://github.com/checkmarx/kics)

### Other

| <!-- --> | Code quality checker | Linter | Configuration key | Additional  |
| :---: | ----------------- | -------------- | ------------ | :-----:  |
| <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/default.ico" alt="" height="32px" class="megalinter-icon"></a> <!-- linter-icon --> | [**REPOSITORY**](https://megalinter.github.io/v6-alpha/descriptors/repository/) | [devskim](https://megalinter.github.io/v6-alpha/descriptors/repository_devskim/)| [REPOSITORY_DEVSKIM](https://megalinter.github.io/v6-alpha/descriptors/repository_devskim/)| [![GitHub stars](https://img.shields.io/github/stars/microsoft/DevSkim?cacheSeconds=3600)](https://github.com/microsoft/DevSkim) ![sarif](https://shields.io/badge/-SARIF-orange)
| <!-- --> <!-- linter-icon --> |  | [dustilock](https://megalinter.github.io/v6-alpha/descriptors/repository_dustilock/)| [REPOSITORY_DUSTILOCK](https://megalinter.github.io/v6-alpha/descriptors/repository_dustilock/)| [![GitHub stars](https://img.shields.io/github/stars/Checkmarx/dustilock?cacheSeconds=3600)](https://github.com/Checkmarx/dustilock) ![sarif](https://shields.io/badge/-SARIF-orange)
| <!-- --> <!-- linter-icon --> |  | [gitleaks](https://megalinter.github.io/v6-alpha/descriptors/repository_gitleaks/)| [REPOSITORY_GITLEAKS](https://megalinter.github.io/v6-alpha/descriptors/repository_gitleaks/)| [![GitHub stars](https://img.shields.io/github/stars/zricethezav/gitleaks?cacheSeconds=3600)](https://github.com/zricethezav/gitleaks) ![sarif](https://shields.io/badge/-SARIF-orange)
| <!-- --> <!-- linter-icon --> |  | [secretlint](https://megalinter.github.io/v6-alpha/descriptors/repository_secretlint/)| [REPOSITORY_SECRETLINT](https://megalinter.github.io/v6-alpha/descriptors/repository_secretlint/)| [![GitHub stars](https://img.shields.io/github/stars/secretlint/secretlint?cacheSeconds=3600)](https://github.com/secretlint/secretlint) ![sarif](https://shields.io/badge/-SARIF-orange)
| <!-- --> <!-- linter-icon --> |  | [semgrep](https://megalinter.github.io/v6-alpha/descriptors/repository_semgrep/)| [REPOSITORY_SEMGREP](https://megalinter.github.io/v6-alpha/descriptors/repository_semgrep/)| [![GitHub stars](https://img.shields.io/github/stars/returntocorp/semgrep?cacheSeconds=3600)](https://github.com/returntocorp/semgrep) ![autofix](https://shields.io/badge/-autofix-green) ![sarif](https://shields.io/badge/-SARIF-orange)
| <!-- --> <!-- linter-icon --> |  | [syft](https://megalinter.github.io/v6-alpha/descriptors/repository_syft/)| [REPOSITORY_SYFT](https://megalinter.github.io/v6-alpha/descriptors/repository_syft/)| [![GitHub stars](https://img.shields.io/github/stars/anchore/syft?cacheSeconds=3600)](https://github.com/anchore/syft) ![sarif](https://shields.io/badge/-SARIF-orange)
| <!-- --> <!-- linter-icon --> |  | [trivy](https://megalinter.github.io/v6-alpha/descriptors/repository_trivy/)| [REPOSITORY_TRIVY](https://megalinter.github.io/v6-alpha/descriptors/repository_trivy/)| [![GitHub stars](https://img.shields.io/github/stars/aquasecurity/trivy?cacheSeconds=3600)](https://github.com/aquasecurity/trivy) ![sarif](https://shields.io/badge/-SARIF-orange)

