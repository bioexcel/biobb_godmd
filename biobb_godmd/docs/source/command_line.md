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
    usage: godmd_run [-h] [--config CONFIG] --input_pdb_orig_path INPUT_PDB_ORIG_PATH --input_pdb_target_path INPUT_PDB_TARGET_PATH --input_aln_orig_path INPUT_ALN_ORIG_PATH --input_aln_target_path INPUT_ALN_TARGET_PATH [--input_config_path INPUT_CONFIG_PATH] --output_log_path OUTPUT_LOG_PATH --output_ene_path OUTPUT_ENE_PATH --output_trj_path OUTPUT_TRJ_PATH --output_pdb_path OUTPUT_PDB_PATH
    
    Computing conformational transition trajectories for proteins using GOdMD tool.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_pdb_orig_path INPUT_PDB_ORIG_PATH
                            Input PDB file to be used as origin in the conformational transition. Accepted formats: pdb.
      --input_pdb_target_path INPUT_PDB_TARGET_PATH
                            Input PDB file to be used as target in the conformational transition. Accepted formats: pdb.
      --input_aln_orig_path INPUT_ALN_ORIG_PATH
                            Input GOdMD alignment file corresponding to the origin structure of the conformational transition. Accepted formats: aln, txt.
      --input_aln_target_path INPUT_ALN_TARGET_PATH
                            Input GOdMD alignment file corresponding to the target structure of the conformational transition. Accepted formats: aln, txt.
      --input_config_path INPUT_CONFIG_PATH
                            Input configuration file (GOdMD run options). Accepted formats: in, txt.
      --output_log_path OUTPUT_LOG_PATH
                            Output log file. Accepted formats: log, out, txt.
      --output_ene_path OUTPUT_ENE_PATH
                            Output energy file. Accepted formats: log, out, txt.
      --output_trj_path OUTPUT_TRJ_PATH
                            Output trajectory file. Accepted formats: mdcrd.
      --output_pdb_path OUTPUT_PDB_PATH
                            Output structure file. Accepted formats: pdb.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_pdb_orig_path** (*string*): Input PDB file to be used as origin in the conformational transition. File type: input. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/data/godmd/1ake_A.pdb). Accepted formats: PDB
* **input_pdb_target_path** (*string*): Input PDB file to be used as target in the conformational transition. File type: input. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/data/godmd/4ake_A.pdb). Accepted formats: PDB
* **input_aln_orig_path** (*string*): Input GOdMD alignment file corresponding to the origin structure of the conformational transition. File type: input. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/data/godmd/1ake_A.aln). Accepted formats: ALN, TXT
* **input_aln_target_path** (*string*): Input GOdMD alignment file corresponding to the target structure of the conformational transition. File type: input. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/data/godmd/4ake_A.aln). Accepted formats: ALN, TXT
* **input_config_path** (*string*): Input GOdMD configuration file. File type: input. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/data/godmd/params.in). Accepted formats: IN, TXT
* **output_log_path** (*string*): Output log file. File type: output. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/reference/godmd/godmd.log). Accepted formats: LOG, OUT, TXT, O
* **output_ene_path** (*string*): Output energy file. File type: output. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/reference/godmd/godmd_ene.out). Accepted formats: LOG, OUT, TXT, O
* **output_trj_path** (*string*): Output trajectory file. File type: output. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/reference/godmd/godmd_trj.mdcrd). Accepted formats: TRJ, CRD, MDCRD, X
* **output_pdb_path** (*string*): Output structure file. File type: output. [Sample file](https://github.com/bioexcel/biobb_godmd/raw/master/biobb_godmd/test/reference/godmd/godmd_pdb.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **godmdin** (*object*): ({}) GOdMD options specification..
* **binary_path** (*string*): (discrete) Binary path..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_godmd/blob/master/biobb_godmd/test/data/config/config_godmd_run.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
godmd_run --config config_godmd_run.yml --input_pdb_orig_path 1ake_A.pdb --input_pdb_target_path 4ake_A.pdb --input_aln_orig_path 1ake_A.aln --input_aln_target_path 4ake_A.aln --input_config_path params.in --output_log_path godmd.log --output_ene_path godmd_ene.out --output_trj_path godmd_trj.mdcrd --output_pdb_path godmd_pdb.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_godmd/blob/master/biobb_godmd/test/data/config/config_godmd_run.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
godmd_run --config config_godmd_run.json --input_pdb_orig_path 1ake_A.pdb --input_pdb_target_path 4ake_A.pdb --input_aln_orig_path 1ake_A.aln --input_aln_target_path 4ake_A.aln --input_config_path params.in --output_log_path godmd.log --output_ene_path godmd_ene.out --output_trj_path godmd_trj.mdcrd --output_pdb_path godmd_pdb.pdb
```

## Godmd_prep
Helper bb to prepare inputs for the GOdMD tool module.
### Get help
Command:
```python
godmd_prep -h
```
    usage: godmd_prep [-h] [--config CONFIG] --input_pdb_orig_path INPUT_PDB_ORIG_PATH --input_pdb_target_path INPUT_PDB_TARGET_PATH --output_aln_orig_path OUTPUT_ALN_ORIG_PATH --output_aln_target_path OUTPUT_ALN_TARGET_PATH
    
    Prepares input files for the GOdMD tool.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_pdb_orig_path INPUT_PDB_ORIG_PATH
                            Input PDB file to be used as origin in the conformational transition. Accepted formats: pdb.
      --input_pdb_target_path INPUT_PDB_TARGET_PATH
                            Input PDB file to be used as target in the conformational transition. Accepted formats: pdb.
      --output_aln_orig_path OUTPUT_ALN_ORIG_PATH
                            Output GOdMD alignment file corresponding to the origin structure of the conformational transition. Accepted formats: aln, txt.
      --output_aln_target_path OUTPUT_ALN_TARGET_PATH
                            Output GOdMD alignment file corresponding to the target structure of the conformational transition. Accepted formats: aln, txt.
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
* **binary_path** (*string*): (water) Binary path..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_godmd/blob/master/biobb_godmd/test/data/config/config_godmd_prep.yml)
```python
properties:
  gapextend: '2'
  gapopen: '12.0'

```
#### Command line
```python
godmd_prep --config config_godmd_prep.yml --input_pdb_orig_path 1ake_A.pdb --input_pdb_target_path 4ake_A.pdb --output_aln_orig_path 1ake_A.aln --output_aln_target_path 4ake_A.aln
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_godmd/blob/master/biobb_godmd/test/data/config/config_godmd_prep.json)
```python
{
  "properties": {
    "gapopen": "12.0",
    "gapextend": "2"
  }
}
```
#### Command line
```python
godmd_prep --config config_godmd_prep.json --input_pdb_orig_path 1ake_A.pdb --input_pdb_target_path 4ake_A.pdb --output_aln_orig_path 1ake_A.aln --output_aln_target_path 4ake_A.aln
```
