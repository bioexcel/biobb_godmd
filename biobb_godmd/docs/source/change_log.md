# Biobb GOdMD changelog

## [Unreleased]

## What's new in version [5.4.0](https://github.com/bioexcel/biobb_godmd/releases/tag/v5.4.0)?

### Changes

* [UPDATE] Update to biobb_common 5.4.0.
* [UPDATE] `godmd_run`: an execution skipped by the `restart` property now records the parameters of the GOdMD configuration file in its provenance, like the executions that run.
* [FIX] `godmd_prep`: a structure with fewer than 50 residues no longer stops the block with a `TypeError`; the short sequence warning is written to the log.
* [FIX] `godmd_run`: `input_config_path` is optional in the `GOdMDRun` class too, as documented and as in the `godmd_run()` function.
* [UPDATE] `godmd_run`: the `container_working_dir` property is gone: the GOdMD command runs inside the sandbox, also in containers.
* [UPDATE] Python 3.11 to 3.13.

## What's new in version [5.3.1](https://github.com/bioexcel/biobb_amber/releases/tag/v5.3.1)?

### Changes

* [UPDATE] Containers logic for GoDMD_prep

## What's new in version [5.3.0](https://github.com/bioexcel/biobb_amber/releases/tag/v5.3.0)?

### Changes

* [UPDATE] Update to biobb_common 5.3.1

## What's new in version [5.2.1](https://github.com/bioexcel/biobb_amber/releases/tag/v5.2.1)?

### Changes

* [UPDATE] Update to biobb_common 5.2.2

## What's new in version [5.2.0](https://github.com/bioexcel/biobb_amber/releases/tag/v5.2.0)?

### Changes

* [UPDATE] Update to biobb_common 5.2.0

## What's new in version [5.1.2](https://github.com/bioexcel/biobb_godmd/releases/tag/v5.1.2)?

### Changes

* [UPDATE]: Update to GodMD 1.7

## What's new in version [5.1.1](https://github.com/bioexcel/biobb_godmd/releases/tag/v5.1.1)?

### Changes

* [UPDATE]: Update to GodMD 1.6

## What's new in version [5.1.0](https://github.com/bioexcel/biobb_godmd/releases/tag/v5.1.0)?

### Changes

* [UPDATE]: Update to biobb_common 5.1.0

## What's new in version [5.0.0](https://github.com/bioexcel/biobb_godmd/releases/tag/v5.0.0)?

### Changes

* [CI/CD](env.yaml): Update biobb_common version.
* [CI/CD](linting_and_testing.yml): Update set-up micromamba.
* [Typing](ALL): Update typing from python 3.8 style to python 3.9
* [CI/CD](linting_and_testing): Update GA test workflow to Python >3.9
* [TYPING](ALL): Fix typing errors
* [DOCS](.readthedocs.yaml): Updating to Python 3.9
* [FEATURE](__init__): Importing submodules when a module is loaded
* [CI/CD](godmd): Adapting conf.yml to the new confReader


## What's new in version [4.2.0](https://github.com/bioexcel/biobb_godmd/releases/tag/v4.2.0)?
In version 4.2.0 the dependency biobb_common has been updated to 4.2.0 version.

### New features

* Update to biobb_common 4.2.0 (general)

## What's new in version [4.1.0](https://github.com/bioexcel/biobb_godmd/releases/tag/v4.1.0)?
In version 4.1.0 the dependency biobb_common has been updated to 4.1.0 version.

### New features

* Update to biobb_common 4.1.0 (general)

## What's new in version [4.0.2](https://github.com/bioexcel/biobb_godmd/releases/tag/v4.0.2)?
In version 4.0.2 the module godmd_run and godmd_prep have been fixed.

### New features

* Fixes in godmd_run
* Fixes in godmd_prep

## What's new in version [4.0.1](https://github.com/bioexcel/biobb_godmd/releases/tag/v4.0.1)?
In version 4.0.1 the module godmd_run has been fixed.

### New features

* Fixes in godmd_run

## What's new in version [4.0.0](https://github.com/bioexcel/biobb_godmd/releases/tag/v4.0.0)?
In version 4.0.0 the dependency biobb_common has been updated to 4.0.0 version.

### New features

* Update to biobb_common 4.0.0 (general)

## What's new in version [3.8.0](https://github.com/bioexcel/biobb_godmd/releases/tag/v3.8.0)?
Biobb_godmd allows the calculation of protein conformational transitions using the GOdMD package.

### New features

* New Package Biobb_godmd

