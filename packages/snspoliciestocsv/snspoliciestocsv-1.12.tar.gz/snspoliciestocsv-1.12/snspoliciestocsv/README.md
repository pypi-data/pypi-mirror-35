snspoliciestocsv
================

Description
-----------
A simple script to extract policies from a Stormshield Network Security device configuration file to CSV

Options
-------
```
$ python3 snspoliciestocsv.py -h
Usage: snspoliciestocsv.py [options]
Version: 1.11

Options:
  -h, --help            show this help message and exit

  Main parameters:
    -i INPUT_FILE, --input-file=INPUT_FILE
                        Partial or full Stormshield Network security appliance
                        configuration file. Ex: filter.cfg
    -o OUTPUT_FILE, --output-file=OUTPUT_FILE
                        Output csv file (default ./policies-out.csv)
    -s, --skip-header   Do not print the csv header
    -d DELIMITER, --delimiter=DELIMITER
                        CSV delimiter (default ";")
```

Examples
--------
#### exemple.txt
```
[Filter]
separator color="000000" comment="Allow VPN A to B" collapse="1"
pass inspection firewall log ipproto vpn-esp proto none from A to B	# Créée le 1970-01-01 00:00:01, par Serge (1.2.3.4)
separator color="000000" comment="Block B to C" collapse="1"
block from B to C port ssh	# Prenez un chewing-gum EmileCréée le 1970-01-01 00:00:02, par Odile (1.2.3.5)
block from A to G port ssh	# àloléCréée le 1970-01-01 00:00:02, par Léon (1.2.3.5)
```

#### policies-out.csv
```
type;log;from;to;ipproto;proto;port;comment;creation_date;user;ip_user
Allow VPN A to B;;;;;;;;;;
pass;log;A;B;vpn-esp;none;; ;1970-01-01 00:00:01;Serge;1.2.3.4
Block B to C;;;;;;;;;;
block;;B;C;;;ssh; Prenez un chewing-gum Emile;1970-01-01 00:00:02;Odile;1.2.3.5
block;;A;G;;;ssh; àlolé;1970-01-01 00:00:02;Léon;1.2.3.5
```

Dependencies and installation
-----------------------------
* Python 3 or superior (sorry but Python 2 is a pain with csv unicode stuff)
* The **easiest way** to setup everything: `pip install snspoliciestocsv` and then directly use `$ snspoliciestocsv`
* Or git clone that repository

Changelog
---------
* version 1.12 - 08/13/2018: Fixing the README layout on PyPI
* version 1.11 - 07/22/2017: Fixing some utf-8 issues, and adding the log column
* version 1.0 - 07/14/2017: Initial commit

Disclaimer and license
---------------------
* **I don't own anything on the Stormshield brand and am not affiliated with organization**
* snspoliciestocsv is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software  Foundation, either version 3 of the License, or (at your option) any later version. 
  * snspoliciestocsv is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
  * See the GNU Lesser General Public License for more details: http://www.gnu.org/licenses/  

Contact
-------
* Thomas Debize < tdebize at mail d0t com >