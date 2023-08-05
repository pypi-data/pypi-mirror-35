:toc:

[id="readme"]
= README: The `newdoc` script

[id="installation"]
== How do I install the script?

The script is now compatible with both Python 3 (for Fedora and community distributions) and Python 2.7 (for RHEL 7 and macOS).

It hasn't been tested on Windows.

[discrete]
=== Procedure

. Clone this repository somewhere on your system:
+
[subs=+quotes]
----
$ git clone git@gitlab.cee.redhat.com:ccs-tools/newdoc.git
----

. In your shell configuration, add an alias to the `newdoc` script.
+
** If you are using Fedora or a community Linux distribution:
+
[subs=+quotes]
----
alias newdoc="python**3** _path-to-cloned-repo_/newdoc.py"
----
+
For example, if you are using the `bash` shell, you might add something like the following in your `~/.bashrc` file:
+
[subs=+quotes]
----
alias newdoc="python3 __/home/msuchane/RH/newdoc/__newdoc.py"
----

** If you are using RHEL 7:
+
[subs=+quotes]
----
alias newdoc="python**2** __/home/msuchane/RH/newdoc/__newdoc.py"
----
+
For example, if you are using the `bash` shell, you might add something like the following in your `~/.bashrc` file:
+
[subs=+quotes]
----
alias newdoc="python2 __/home/msuchane/RH/newdoc/__newdoc.py"
----

** If you are using macOS:
+
[subs=+quotes]
----
alias newdoc="python**2** __/Users/msuchane/RH/newdoc/__newdoc.py"
----
+
For example, if you are using the `bash` shell, you might add something like the following in your `~/.bashrc` file:
+
[subs=+quotes]
----
alias newdoc="python2 __/Users/msuchane/RH/newdoc/__newdoc.py"
----

[discrete]
=== Notes

* If you prefer `newdoc` to generate file without the explanatory comments, change the alias to include the `--no-comments` option:
+
[subs=+quotes]
----
alias newdoc="_python3_ __/home/msuchane/RH/newdoc/__newdoc.py *--no-comments*"
----

* In order for the alias to take effect in your current shell session as well, reload the configuration file. For example, with `bash`:
+
----
$ source ~/.bashrc
----

[id="new-module"]
== How do I add a new module?

[discrete]
=== Prerequisites

* Install the script. See xref:installation[] for details.

[discrete]
=== Procedure

. In the directory where modules are located, use the `newdoc` script to create a new file:
+
[subs=+quotes]
----
_modules-dir_]$ newdoc _--procedure_ "_Setting up thing_"
----
+
The script also accepts the `--concept` and `--reference` options. You can use these short forms instead: `-p`, `-c`, and `-r`.

. Rewrite the information in the template with your docs.

[id="new-assembly"]
== How do I add a new assembly?

[discrete]
=== Prerequisites

* Install the script. See xref:installation[] for details.

[discrete]
=== Procedure

. In the directory where assemblies are located, use the `newdoc` script to create a new file:
+
[subs=+quotes]
----
_assemblies-dir_]$ newdoc --assembly "_Achieving thing_"
----
+
You can use the short form of the option instead: `newdoc -a "_Achieving thing_"`.

. Rewrite the information in the template with your docs.
+
Add AsciiDoc include statements to include modules. See link:https://asciidoctor.org/docs/asciidoc-syntax-quick-reference/#include-files[Include Files] in the AsciiDoc Syntax Quick Reference.


[id="configuration"]
== Configuration

`newdoc` enables you to configure multiple aspects of its behavior:

* Custom templates for assemblies and modules,
* How IDs are capitalized when converted from a title,
* What symbol is used to replace spaces in IDs.

These options can be set in the `newdoc.ini` configuration file, which is located:

* On Fedora, RHEL, and other Linux distributions, in `~/.config/newdoc/newdoc.ini`
* On macOS, in `~/Library/Preferences/newdoc/newdoc.ini`

The configuration file is not created automatically: if you want to set custom options, create it using a plain text editor.

The file must always start with the `[newdoc]` header. An example configuration is available in this repo at `examples/newdoc.ini`.


[discrete]
=== Custom templates

In the config file, you can set paths to custom AsciiDoc template files for each module type. The options are:

* `assembly_template`
* `concept_template`
* `procedure_template`
* `reference_template`

For example, to use a custom template for reference modules, use:

[subs=+quotes]
----
reference_template = _~/.config/newdoc/my-reference-template.adoc_
----

`newdoc` performs substitutions on the templates using the Python `string.template` library. The following strings are replaced:

* `${module_title}` with the entered title of the module
* `${module_id}` with the generated ID of the module
* `${filename}` with the generated file name of the module

For more details on the template syntax, see: link:https://docs.python.org/3/library/string.html#template-strings[]


[discrete]
=== ID substitutions

* The `id_case` option in the config file controls how the letter case should change from the title to the ID:
+
`id_case = lowercase`:: All letters in the ID will be lower-case
`id_case = capitalize`:: The first letter will be upper-case, the rest lower-case
`id_case = preserve`:: Keep the capitalization as entered in the title

* The `word_separator` option lets you choose the symbol (or string) used to replace spaces in the ID. The default is a dash:
+
----
word_separator = -
----

== Additional resources

* link:https://redhat-documentation.github.io/modular-docs/[Modular Documentation Reference Guide]
* link:https://redhat-documentation.github.io/asciidoc-markup-conventions/[AsciiDoc Mark-up Quick Reference for Red Hat Documentation]



