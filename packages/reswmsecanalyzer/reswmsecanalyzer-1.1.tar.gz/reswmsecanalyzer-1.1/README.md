RES Workspace Manager application security rule analyzer
========================================================

Description
-----------
A simple script to visualize and find bypasses in RES Workspace Manager application restrictions

Features
--------
* Finding possible paths to reach a targeted resource such as an executable program
* Visually displaying rules as an oriented graph

Options
-------
```
$ python reswmsecanalyzer.py -h
Usage: reswmsecanalyzer.py [options]
Version: 1.0

Options:
  -h, --help            show this help message and exit

  Main parameters:
    -i INPUT_FILE, --input-file=INPUT_FILE
                        sec_globauth.xml file containing the security rules
    -t TARGET, --target=TARGET
                        Program or file name you want to reach, globbing
                        format accepted (Ex: cmd.exe, *cmd*)

  Optional parameters:
    -g, --graph         Draw and show the graph with matplot
    -o OUTPUT_GRAPH, --output-graph=OUTPUT_GRAPH
                        Filename to save the png graph (Ex. -o test.png)
```

Prerequisites
-------------
On a protected environment (physical/logical/virtualized workstation):
* The **whole configuration** is stored in this directory  
 `C:\Program Files (x86)\RES Software\Workspace Manager\Data\DBCache\Objects\`
* The **application security rules** are stored in this file  
 `C:\Program Files (x86)\RES Software\Workspace Manager\Data\DBCache\Objects\sec_globauth.xml`
* **Workspace access control** (if implemented) is defined in the following file  
 `C:\Program Files (x86)\RES Software\Workspace Manager\Data\DBCache\Objects\workspaces.xml`
 
Examples
--------
* Some **example rules and their associated graphs** are provided in the [`reswmsecanalyzer/examples`](reswmsecanalyzer/examples/) folder. For each example, a **pretty-print** version `_prettyprint.xml` is also included
* For the [`reswmsecanalyzer/examples/multiple-rules`](reswmsecanalyzer/examples/multiple-rules):
  * The policy defined in the RES Console looks like:
  ![](reswmsecanalyzer/examples/multiple-rules/policy_example.png)
  * Searching a path to `cmd` gives that:
  ```
  $ python reswmsecanalyzer.py -i examples/multiple-rules/sec_globauth.xml -t cmd -g
  [+] Number of enabled rules: 4
  [+] Possible path to 'cmd.exe': ['.', 'calc.exe', 'cmd.exe']
  [+] Possible path to 'cmd.exe': ['.', 'notepad.exe', 'cmd.exe']
  ```
  ![](reswmsecanalyzer/examples/multiple-rules/graph_to_cmd.png)

Dependencies and installation
------------------------------
* The easiest way: `pip install reswmsecanalyzer`
* Or `pip install -r requirements.txt`
* Or installing manually each dependency:
  * Python NetworkX: `apt-get install python-networkx` or `pip install networkx`
  * Python Matplotlib: `apt-get install python-matplotlib` or `pip install matplotlib`  
  
Roadmap
-------
* Improve the possible path output description
* Add csv output
* Take into account edge constraints such as workspace access control
* Use some dynamic representation, like D3JS