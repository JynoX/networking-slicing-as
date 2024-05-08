# Networking Slice Manager

## Overview
This project aims to develop a networking slice manager, facilitating the dynamic activation and deactivation of network slices via both a graphical user interface (GUI) and command-line interface (CLI), tailored to meet diverse network requirements. The implementation encompasses three operational modes: `Work`, `Conference`, and `Emergency`.

The network topology comprises:
- 1 Software-Defined Networking (SDN) controller (`c1`)
- 5 OpenFlow switches (`s1`, `s2`, `s3`, `s4`, `s5`)
- 9 Hosts (`h1`, `h2`, `h3`, `h4`, `h5`, `ps`, `vc1`, `vc2`, `ds`)