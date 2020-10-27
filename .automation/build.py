# !/usr/bin/env python3
"""
Automatically generate source code
"""
import json
import logging
import os
import re
import sys
from shutil import copyfile

import jsonschema
import yaml

import megalinter

BRANCH = 'master'
URL_ROOT = "https://github.com/nvuillam/mega-linter/tree/" + BRANCH
URL_RAW_ROOT = "https://github.com/nvuillam/mega-linter/raw/" + BRANCH
TEMPLATES_URL_ROOT = URL_ROOT + "/TEMPLATES"
DOCS_URL_ROOT = URL_ROOT + "/docs"
DOCS_URL_DESCRIPTORS_ROOT = DOCS_URL_ROOT + "/descriptors"
DOCS_URL_RAW_ROOT = URL_RAW_ROOT + "/docs"
REPO_HOME = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + '..'
REPO_ICONS = REPO_HOME + '/docs/assets/icons'

VERSIONS_FILE = REPO_HOME + '/linter-versions.json'
HELPS_FILE = REPO_HOME + '/linter-helps.json'


# Automatically generate Dockerfile parts
def generate_dockerfile():
    descriptor_and_linters = []
    # Get install instructions at descriptor level
    descriptor_files = megalinter.utils.list_descriptor_files()
    for descriptor_file in descriptor_files:
        with open(descriptor_file) as f:
            descriptor = yaml.load(f, Loader=yaml.FullLoader)
            if 'install' in descriptor:
                descriptor_and_linters += [descriptor]
    # Get install instructions at linter level
    linters = megalinter.utils.list_all_linters()
    for linter in linters:
        if hasattr(linter, 'install'):
            descriptor_and_linters += [vars(linter)]
    # Gather all dockerfile commands
    docker_from = []
    docker_arg = []
    docker_other = []
    apk_packages = []
    npm_packages = []
    pip_packages = []
    gem_packages = []
    for item in descriptor_and_linters:
        # Collect Dockerfile items
        if 'dockerfile' in item['install']:
            item_label = item.get('linter_name', item.get('descriptor_id', ''))
            docker_other += [
                f"# {item_label} installation"
            ]
            for dockerfile_item in item['install']['dockerfile']:
                if dockerfile_item.startswith('FROM'):
                    docker_from += [dockerfile_item]
                elif dockerfile_item.startswith('ARG'):
                    docker_arg += [dockerfile_item]
                else:
                    docker_other += [dockerfile_item]
            docker_other += [""]
        # Collect python packages
        if 'apk' in item['install']:
            apk_packages += item['install']['apk']
        # Collect npm packages
        if 'npm' in item['install']:
            npm_packages += item['install']['npm']
        # Collect python packages
        if 'pip' in item['install']:
            pip_packages += item['install']['pip']
        # Collect ruby packages
        if 'gem' in item['install']:
            gem_packages += item['install']['gem']
    # Replace between tags in Dockerfile
    # Commands
    replace_in_file(f"{REPO_HOME}/Dockerfile", "#FROM__START",
                    "#FROM__END", "\n".join(docker_from))
    replace_in_file(f"{REPO_HOME}/Dockerfile", "#ARG__START",
                    "#ARG__END", "\n".join(docker_arg))
    replace_in_file(f"{REPO_HOME}/Dockerfile", "#OTHER__START",
                    "#OTHER__END", "\n".join(docker_other))
    # apk packages
    apk_install_command = 'RUN apk add --update --no-cache \\\n                ' + \
                          " \\\n                ".join(
                              list(dict.fromkeys(apk_packages)))
    replace_in_file(f"{REPO_HOME}/Dockerfile", "#APK__START",
                    "#APK__END", apk_install_command)
    # NPM packages
    npm_install_command = 'RUN npm install --no-cache \\\n                ' + \
                          " \\\n                ".join(
                              list(dict.fromkeys(npm_packages)))
    replace_in_file(f"{REPO_HOME}/Dockerfile", "#NPM__START",
                    "#NPM__END", npm_install_command)
    # Python pip packages
    pip_install_command = 'RUN pip3 install \\\n          ' + \
                          " \\\n          ".join(
                              list(dict.fromkeys(pip_packages)))
    replace_in_file(f"{REPO_HOME}/Dockerfile", "#PIP__START",
                    "#PIP__END", pip_install_command)
    # Ruby gem packages
    gem_install_command = "RUN echo \'gem: --no-document\' >> ~/.gemrc && \\\n" + \
                          '    gem install \\\n          ' + \
                          " \\\n          ".join(
                              list(dict.fromkeys(gem_packages)))
    replace_in_file(f"{REPO_HOME}/Dockerfile", "#GEM__START",
                    "#GEM__END", gem_install_command)


# Automatically generate a test class for each linter class
# This could be done dynamically at runtime, but having a physical class is easier for developers in IDEs
def generate_linter_test_classes():
    linters = megalinter.utils.list_all_linters()
    megalinter.utils.list_all_linters()
    for linter in linters:
        lang_lower = linter.descriptor_id.lower()
        linter_name_lower = linter.linter_name.lower().replace('-', '_')
        test_class_code = f"""# !/usr/bin/env python3
\"\"\"
Unit tests for {linter.descriptor_id} linter {linter.linter_name}
This class has been automatically generated by .automation/build.py, please do not update it manually
\"\"\"

from unittest import TestCase

from megalinter.tests.test_megalinter.LinterTestRoot import LinterTestRoot


class {lang_lower}_{linter_name_lower}_test(TestCase, LinterTestRoot):
    descriptor_id = '{linter.descriptor_id}'
    linter_name = '{linter.linter_name}'
"""
        file = open(
            f"{REPO_HOME}/megalinter/tests/test_megalinter/linters/{lang_lower}_{linter_name_lower}_test.py",
            'w')
        file.write(test_class_code)
        file.close()
        logging.info('Updated ' + file.name)


# Automatically generate README linters table and a MD file for each linter
def generate_documentation():
    descriptor_files = megalinter.utils.list_descriptor_files()
    linters_by_type = {'language': [], 'format': [], 'tooling_format': [], 'other': []}
    descriptors = []
    for descriptor_file in descriptor_files:
        descriptor = megalinter.utils.build_descriptor_info(descriptor_file)
        descriptors += [descriptor]
        descriptor_linters = megalinter.utils.build_descriptor_linters(
            descriptor_file)
        linters_by_type[descriptor_linters[0].descriptor_type] += descriptor_linters
    # Build descriptors documentation
    for descriptor in descriptors:
        generate_descriptor_documentation(descriptor)
    # Build README linters table and linters documentation
    linters_tables_md = []
    process_type(linters_by_type, 'language', 'Languages', linters_tables_md)
    process_type(linters_by_type, 'format', 'Formats', linters_tables_md)
    process_type(linters_by_type, 'tooling_format',
                 'Tooling formats', linters_tables_md)
    process_type(linters_by_type, 'other', 'Other', linters_tables_md)
    linters_tables_md_str = "\n".join(linters_tables_md)
    logging.info("Generated Linters table for README:\n" +
                 linters_tables_md_str)
    replace_in_file(f"{REPO_HOME}/README.md", "<!-- linters-table-start -->",
                    "<!-- linters-table-end -->", linters_tables_md_str)
    # Update welcome phrase
    welcome_phrase = f"Automatically detect [**{len(linters_by_type['language'])} languages**](#languages), " + \
                     f"[**{len(linters_by_type['format'])} formats**](#formats), " + \
                     f"[**{len(linters_by_type['tooling_format'])} tooling formats**](#tooling-formats) " + \
                     ", [**copy-pastes**](#other) and [**spell**](#other) in your " + \
                     "repository sources and apply their related linters to ensure your projects are clean !"
    replace_in_file(f"{REPO_HOME}/README.md", "<!-- welcome-phrase-start -->",
                    "<!-- welcome-phrase-end -->", welcome_phrase)


# Generate a MD page for a descriptor (language, format, tooling_format)
def generate_descriptor_documentation(descriptor):
    descriptor_md = [
        "<!-- markdownlint-disable MD003 MD020 MD033 MD041 -->",
        "<!-- Generated by .automation/build.py, please do not update manually -->"
    ]
    # Title
    descriptor_md += [f"# {descriptor.get('descriptor_label', descriptor.get('descriptor_id'))}",
                      ""]
    # Criteria used by the descriptor to identify files to lint
    descriptor_md += [
        "## Linted files",
        ""]
    if descriptor.get('active_only_if_file_found', None) is not None:
        descriptor_md += [
            f"- Activated only if file is found: `{descriptor.get('active_only_if_file_found')}`"]
    if len(descriptor.get('file_extensions', [])) > 0:
        descriptor_md += ['- File extensions:']
        for file_extension in descriptor.get('file_extensions'):
            descriptor_md += [f"  - `{file_extension}`"]
        descriptor_md += [""]
    if len(descriptor.get('file_names', [])) > 0:
        descriptor_md += ['- File names:']
        for file_name in descriptor.get('file_names'):
            descriptor_md += [f"  - `{file_name}`"]
        descriptor_md += [""]
    if len(descriptor.get('file_contains', [])) > 0:
        descriptor_md += ['- Detected file content:']
        for file_contains_expr in descriptor.get('file_contains'):
            descriptor_md += [f"  - `{file_contains_expr}`"]
        descriptor_md += [""]
    # Mega-linter variables
    descriptor_md += [
        "## Mega-linter configuration",
        "",
        "| Variable | Description | Default value |",
        "| ----------------- | -------------- | -------------- |"]
    descriptor_md += [
        f"| {descriptor.get('descriptor_id')}_FILTER_REGEX_INCLUDE | Custom regex including filter |  |",
        f"| {descriptor.get('descriptor_id')}_FILTER_REGEX_EXCLUDE | Custom regex excluding filter |  |",
        ""
    ]
    # List of linters
    lang_lower = descriptor.get('descriptor_id').lower()
    descriptor_md += [
        "## Linters",
        "",
        "| Linter | Configuration key |",
        "| ------ | ----------------- |"]
    for linter in descriptor.get('linters', []):
        linter_name_lower = linter.get('linter_name').lower().replace('-', '_')
        linter_doc_url = f"{DOCS_URL_DESCRIPTORS_ROOT}/{lang_lower}_{linter_name_lower}.md"
        descriptor_md += [
            f"| [{linter.get('linter_name')}]({doc_url(linter_doc_url)}) | "
            f"[{linter.get('name', descriptor.get('descriptor_id'))}]({doc_url(linter_doc_url)}) |"]
    # Add install info
    if descriptor.get('install', None) is not None:
        descriptor_md += ["",
                          "## Behind the scenes"]
        descriptor_md += ["",
                          "### Installation",
                          ""]
        descriptor_md += get_install_md(descriptor)
    # Write MD file
    file = open(
        f"{REPO_HOME}/docs/descriptors/{lang_lower}.md", 'w')
    file.write("\n".join(descriptor_md) + "\n")
    file.close()
    logging.info('Updated ' + file.name)


# Build a MD table for a type of linter (language, format, tooling_format), and a MD file for each linter
def process_type(linters_by_type, type1, type_label, linters_tables_md):
    linters_tables_md += [
        f"### {type_label}",
        "",
        "| <!-- --> | Language / Format | Linter | Configuration key |",
        "| --- | ----------------- | -------------- | ------------ |"]
    descriptor_linters = linters_by_type[type1]
    prev_lang = ''
    for linter in descriptor_linters:
        lang_lower = linter.descriptor_id.lower()
        linter_name_lower = linter.linter_name.lower().replace('-', '_')

        # Append in general linter tables (for README)
        descriptor_label = f"**{linter.descriptor_label}** ({linter.descriptor_id})" \
            if hasattr(linter, 'descriptor_label') else f"**{linter.descriptor_id}**"
        if prev_lang != linter.descriptor_id and \
                os.path.exists(REPO_ICONS + '/' + linter.descriptor_id.lower() + '.ico'):
            icon_html = icon(f"{DOCS_URL_RAW_ROOT}/assets/icons/{linter.descriptor_id.lower()}.ico",
                             '', '', descriptor_label, 32)
        elif prev_lang != linter.descriptor_id and \
                os.path.exists(REPO_ICONS + '/default.ico'):
            icon_html = icon(f"{DOCS_URL_RAW_ROOT}/assets/icons/default.ico",
                             '', '', descriptor_label, 32)
        else:
            icon_html = '<!-- -->'
        descriptor_url = doc_url(f"{DOCS_URL_DESCRIPTORS_ROOT}/{lang_lower}.md")
        descriptor_id_cell = f"[{descriptor_label}]({descriptor_url})" if prev_lang != linter.descriptor_id else ''
        prev_lang = linter.descriptor_id
        linter_doc_url = f"{DOCS_URL_DESCRIPTORS_ROOT}/{lang_lower}_{linter_name_lower}.md"
        linters_tables_md += [
            f"| {icon_html} | {descriptor_id_cell} | [{linter.linter_name}]({doc_url(linter_doc_url)})"
            f"| [{linter.name}]({doc_url(linter_doc_url)}) |"]

        # Build individual linter doc
        linter_doc_md = [
            "<!-- markdownlint-disable MD033 MD041 -->",
            "<!-- Generated by .automation/build.py, please do not update manually -->"
        ]
        # Header image as title
        if hasattr(linter, 'linter_banner_image_url') and linter.linter_banner_image_url is not None:
            linter_doc_md += [
                image_link(linter.linter_banner_image_url, linter.linter_name,
                           doc_url(linter.linter_url), "Visit linter Web Site", "center", 150),
                "",
                '## Linter'
            ]
        # Text + image as title
        elif hasattr(linter, 'linter_image_url') and linter.linter_image_url is not None:
            linter_doc_md += [
                "# " + logo_link(linter.linter_image_url, linter.linter_name,
                                 linter.linter_url, "Visit linter Web Site", 100) + linter.linter_name
            ]
        # Text as title
        else:
            linter_doc_md += [f"# {linter.linter_name}"]

        # Linter URL & version
        linter_doc_md += ["",
                          f"- Web Site: [**{linter.linter_url}**]({doc_url(linter.linter_url)})"]
        # Add version info
        with open(VERSIONS_FILE) as json_file:
            linter_versions = json.load(json_file)
            if linter.linter_name in linter_versions and linter_versions[linter.linter_name] != '0.0.0':
                linter_doc_md += [f"- Version: **{linter_versions[linter.linter_name]}**"]

        # How to configure this linter
        linter_doc_md += [
            "",
            "## Configuration",
            ""]
        # Linter-specific configuration
        linter_doc_md += [
            f"### {linter.linter_name} configuration",
            ""]
        # Rules configuration URL
        if hasattr(linter, 'linter_rules_configuration_url') and linter.linter_rules_configuration_url is not None:
            linter_doc_md += [
                f"- [Configure {linter.linter_name} rules]({linter.linter_rules_configuration_url})"]
        else:
            linter_doc_md += [
                f"- {linter.linter_name} has no known capability to configure custom rules"]
        # Default rules riles
        if linter.config_file_name is not None:
            config_file = f"TEMPLATES{os.path.sep}{linter.config_file_name}"
            if os.path.exists(f"{REPO_HOME}{os.path.sep}{config_file}"):
                linter_doc_md += [f"  - If custom {linter.config_file_name} is not found, "
                                  f"[{linter.config_file_name}]({TEMPLATES_URL_ROOT}/{linter.config_file_name})"
                                  " will be used"]
        if hasattr(linter, 'linter_rules_inline_disable_url') and linter.linter_rules_inline_disable_url is not None:
            linter_doc_md += [
                f"- [Disable {linter.linter_name} rules in files]({linter.linter_rules_inline_disable_url})"
            ]
        else:
            linter_doc_md += [
                f"- {linter.linter_name} has no known capability to inline-disable rules"
            ]
        linter_doc_md += ['']
        # Mega-linter variables
        activation_url = "https://github.com/nvuillam/mega-linter#activation-and-deactivation"
        linter_doc_md += [
            "### Mega-linter configuration",
            "",
            f"- Enable {linter.linter_name} by adding `{linter.name}` in [ENABLE_LINTERS variable]({activation_url})",
            f"- Disable {linter.linter_name} by adding `{linter.name}` in [DISABLE_LINTERS variable]({activation_url})",
            "",
            "| Variable | Description | Default value |",
            "| ----------------- | -------------- | -------------- |"]
        if hasattr(linter, 'variables'):
            for variable in linter.variables:
                linter_doc_md += [
                    f"| {variable['name']} | {variable['description']} | {variable['default_value']} |"
                ]
        linter_doc_md += [
            f"| {linter.name}_ARGUMENTS | User custom arguments to add in linter CLI call<br/>"
            f"Ex: `-s --foo \"bar\"` |  |",
            f"| {linter.name}_FILTER_REGEX_INCLUDE | Custom regex including filter<br/>"
            f"Ex: `\\/(src\\|lib)\\/` | Include every file |",
            f"| {linter.name}_FILTER_REGEX_EXCLUDE | Custom regex excluding filter<br/>"
            f"Ex: `\\/(test\\|examples)\\/` | Exclude no file |"
        ]
        if linter.config_file_name is not None:
            linter_doc_md += [
                f"| {linter.name}_FILE_NAME | {linter.linter_name} configuration file name</br>"
                f"Use `LINTER_DEFAULT` to let the linter find it | "
                f"`{linter.config_file_name}` |",
                f"| {linter.name}_RULES_PATH | Path where to find linter configuration file | "
                "Workspace folder, then Mega-Linter default rules |"
            ]
        linter_doc_md += [f"| {linter.name}_DISABLE_ERRORS | Run linter but disable crash if errors found | `false` |"]
        if linter.files_sub_directory is not None:
            linter_doc_md += [
                f"| {linter.descriptor_id}_DIRECTORY | Directory containing {linter.descriptor_id} files "
                f"| `{linter.files_sub_directory}` |"
            ]
        linter_doc_md += [
            "",
            "## Behind the scenes",
            ""]
        # Criteria used by the linter to identify files to lint
        linter_doc_md += [
            "### How are identified applicable files",
            ""]
        if linter.active_only_if_file_found is not None:
            linter_doc_md += [
                f"- Activated only if file is found: `{linter.active_only_if_file_found}`"]
        if len(linter.file_extensions) > 0:
            linter_doc_md += ['- File extensions:']
            for file_extension in linter.file_extensions:
                linter_doc_md += [f"  - `{file_extension}`"]
            linter_doc_md += [""]
        if len(linter.file_names) > 0:
            linter_doc_md += ['- File names:']
            for file_name in linter.file_names:
                linter_doc_md += [f"  - `{file_name}`"]
            linter_doc_md += [""]
        if len(linter.file_contains) > 0:
            linter_doc_md += ['- Detected file content:']
            for file_contains_expr in linter.file_contains:
                linter_doc_md += [f"  - `{file_contains_expr}`"]
            linter_doc_md += [""]

        linter_doc_md += [
            "",
            "### Example calls",
            ""
        ]
        for example in linter.examples:
            linter_doc_md += [
                "```shell",
                example,
                "```",
                ""]
        # Add help info
        with open(HELPS_FILE) as json_file:
            linter_helps = json.load(json_file)
            if linter.linter_name in linter_helps:
                linter_doc_md += ["",
                                  "### Help content",
                                  "",
                                  "```shell"]
                linter_doc_md += linter_helps[linter.linter_name]
                linter_doc_md += ["```"]
        # Installation doc
        linter_doc_md += ["",
                          "### Installation on mega-linter Docker image",
                          ""]
        item = vars(linter)
        merge_install_attr(item)
        linter_doc_md += get_install_md(item)
        # Write md file
        file = open(
            f"{REPO_HOME}/docs/descriptors/{lang_lower}_{linter_name_lower}.md", 'w')
        file.write("\n".join(linter_doc_md) + "\n")
        file.close()
        logging.info('Updated ' + file.name)
    linters_tables_md += [""]
    return linters_tables_md


def get_install_md(item):
    linter_doc_md = []
    if 'dockerfile' in item['install']:
        linter_doc_md += ["- Dockerfile commands :"]
        linter_doc_md += ['```dockerfile']
        linter_doc_md += item['install']['dockerfile']
        linter_doc_md += ['```',
                          ""]
    if 'apk' in item['install']:
        linter_doc_md += ["- APK packages (Linux):"]
        linter_doc_md += md_package_list(item['install']['apk'], "  ",
                                         "https://pkgs.alpinelinux.org/packages?branch=edge&name=")
    if 'npm' in item['install']:
        linter_doc_md += ["- NPM packages (node.js):"]
        linter_doc_md += md_package_list(item['install']
                                         ['npm'], "  ", "https://www.npmjs.com/package/")
    if 'pip' in item['install']:
        linter_doc_md += ["- PIP packages (Python):"]
        linter_doc_md += md_package_list(item['install']
                                         ['pip'], "  ", "https://pypi.org/project/")
    if 'gem' in item['install']:
        linter_doc_md += ["- GEM packages (Ruby) :"]
        linter_doc_md += md_package_list(item['install']
                                         ['gem'], "  ", "https://rubygems.org/gems/")
    return linter_doc_md


def doc_url(href):
    if href.startswith('https://github') and "#" not in href:
        return href + "#readme"
    return href


def image_link(src, alt, link, title, align, maxheight):
    return f"""
<div align=\"{align}\">
  <a href=\"{link}\" target=\"blank\" title=\"{title}\">
    <img src=\"{src}\" alt=\"{alt}\" height=\"{maxheight}px\">
  </a>
</div>"""


def logo_link(src, alt, link, title, maxheight):
    return f"<a href=\"{link}\" target=\"blank\" title=\"{title}\">" \
           f"<img src=\"{src}\" alt=\"{alt}\" height=\"{maxheight}px\"></a>"


def icon(src, alt, _link, _title, height):
    return f"<img src=\"{src}\" alt=\"{alt}\" height=\"{height}px\"></a>"


def merge_install_attr(item):
    if 'descriptor_install' not in item:
        return
    for elt, elt_val in item['descriptor_install'].items():
        if elt in item['install']:
            if elt == 'dockerfile':
                item['install'][elt] = ['# Parent descriptor install'] + elt_val + \
                                       ['# Linter install'] + \
                                       item['install'][elt]
            else:
                item['install'][elt] = elt_val + item['install'][elt]


def md_package_list(package_list, indent, start_url):
    res = []
    for package_id_v in package_list:
        if package_id_v.startswith('@'):
            package_id = package_id_v
        else:
            package_id = package_id_v.split("@")[0].split(":")[0]
        res += [f"{indent}- [{package_id}]({start_url}{package_id})"]
    return res


def replace_in_file(file_path, start, end, content):
    # Read in the file
    with open(file_path, 'r') as file:
        file_content = file.read()
    # Replace the target string
    replacement = f"{start}\n{content}\n{end}"
    regex = rf"{start}([\s\S]*?){end}"
    file_content = re.sub(regex, replacement, file_content, re.DOTALL)
    # Write the file out again
    with open(file_path, 'w') as file:
        file.write(file_content)
    logging.info('Updated ' + file.name)


# Apply descriptor JSON Schema to every descriptor file
def validate_descriptors():
    with open(f"{REPO_HOME}/megalinter/descriptors/jsonschema.json", 'r') as schema_file:
        descriptor_schema = schema_file.read()
        descriptor_files = megalinter.utils.list_descriptor_files()
        errors = 0
        for descriptor_file in descriptor_files:
            with open(descriptor_file, 'r') as descriptor_file1:
                logging.info('Validating ' + os.path.basename(descriptor_file))
                descriptor = descriptor_file1.read()
                try:
                    jsonschema.validate(instance=yaml.load(descriptor, Loader=yaml.FullLoader),
                                        schema=yaml.load(descriptor_schema, Loader=yaml.FullLoader))
                except jsonschema.exceptions.ValidationError as validation_error:
                    logging.error(
                        f"{os.path.basename(descriptor_file)} is not compliant with JSON schema")
                    logging.error(f"reason: {validation_error.message}")
                    errors = errors + 1
        if errors > 0:
            raise ValueError(
                "Errors have been found while validating descriptor YML files, please check logs")


def copy_files():
    copyfile(f"{REPO_HOME}{os.path.sep}README.md", f"{REPO_HOME}{os.path.sep}docs{os.path.sep}index.md")


if __name__ == '__main__':
    logging.basicConfig(force=True,
                        level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        handlers=[
                            logging.StreamHandler(sys.stdout)
                        ])
    # noinspection PyTypeChecker
    validate_descriptors()
    generate_dockerfile()
    generate_linter_test_classes()
    generate_documentation()
    copy_files()
