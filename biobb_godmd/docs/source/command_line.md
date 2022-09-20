# BioBB GODMD Command Line Help
Generic usage:
```python
biobb_command [-h] --config CONFIG --input_file(s) <input_file(s)> --output_file <output_file>
```
-----------------


## Godmd_run
Wrapper of the GOdMD tool module.
### Get help
Command:
```python
godmd_run -h
```
    /bin/sh: godmd_run: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_pdb_orig_path** (*string*): Input PDB file to be used as origin in the conformational transition. File type: input. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/data/godmd/1ake_A.pdb). Accepted formats: PDB
* **input_pdb_target_path** (*string*): Input PDB file to be used as target in the conformational transition. File type: input. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/data/godmd/4ake_A.pdb). Accepted formats: PDB
* **input_aln_orig_path** (*string*): Input GOdMD alignment file corresponding to the origin structure of the conformational transition. File type: input. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/data/godmd/1ake_A.aln). Accepted formats: ALN, TXT
* **input_aln_target_path** (*string*): Input GOdMD alignment file corresponding to the target structure of the conformational transition. File type: input. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/data/godmd/4ake_A.aln). Accepted formats: ALN, TXT
* **input_config_path** (*string*): Input GOdMD configuration file. File type: input. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/data/godmd/params.in). Accepted formats: IN, TXT
* **output_log_path** (*string*): Output log file. File type: output. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/reference/godmd/godmd.log). Accepted formats: LOG, OUT, TXT, O
* **output_ener_path** (*string*): Output energy file. File type: output. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/reference/godmd/godmd_ene.out). Accepted formats: LOG, OUT, TXT, O
* **output_trj_path** (*string*): Output trajectory file. File type: output. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/reference/godmd/godmd_trj.mdcrd). Accepted formats: TRJ, CRD, MDCRD, X
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **godmdin** (*object*): ({}) GOdMD options specification..
* **binary_path** (*string*): (discrete) Binary path..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
### JSON

## Godmd_prep
Helper bb to prepare inputs for the GOdMD tool module.
### Get help
Command:
```python
godmd_prep -h
```
    /bin/sh: godmd_prep: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_pdb_orig_path** (*string*): Input PDB file to be used as origin in the conformational transition. File type: input. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/data/godmd/1ake_A.pdb). Accepted formats: PDB
* **input_pdb_target_path** (*string*): Input PDB file to be used as target in the conformational transition. File type: input. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/data/godmd/4ake_A.pdb). Accepted formats: PDB
* **output_aln_orig_path** (*string*): Output GOdMD alignment file corresponding to the origin structure of the conformational transition. File type: output. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/data/godmd/1ake_A.aln). Accepted formats: ALN, TXT
* **output_aln_target_path** (*string*): Output GOdMD alignment file corresponding to the target structure of the conformational transition. File type: output. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/data/godmd/4ake_A.aln). Accepted formats: ALN, TXT
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **gapopen** (*number*): (12.0) Standard gap penalty: score taken away when a gap is created..
* **gapextend** (*number*): (2.0) Penalty added to the standard gap penalty for each base or residue in the gap..
* **datafile** (*string*): (EPAM250) Scoring matrix file used when comparing sequences..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
### JSON
