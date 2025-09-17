# Port Scanner

## Objective

Designing and creating a Python-based port scanner that can conduct TCP, UDP, Ping, and Stealth (SYN) scans to evaluate network security was the aim of this project. The scanner was built with a Graphical User Interface (GUI) for user convenience and was intended to deliver comprehensive scan results, including open/closed ports, protocols, and software versions. 

### Skills Learned

- Designed and implemented a Python-based network scanning tool supporting TCP, UDP, Ping, and Stealth (SYN) scans.
- Applied socket programming and Scapy for custom packet crafting and analysis.
- Built a user-friendly GUI with Tkinter, enhancing usability for non-technical users.
- Implemented CSV/TXT export functionality, improving reporting and result management.
- Strengthened understanding of network protocols (TCP/IP, UDP, ICMP) and port states.
- Practiced secure coding principles and handled exceptions for stable runtime execution.
- Enhanced problem-solving and debugging skills by testing across different environments.
- Learned to document technical processes and testing results in a structured, academic style.

### Tools Used

- Python 3.12 – Core language for scanner development
- Scapy – Custom packet crafting for SYN and Ping scans
- Tkinter – GUI development for an interactive interface
- VS Code – Code editing and debugging environment
- Windows 11 – Development and testing platform
- Nmap – Benchmarking tool for validating scanner accuracy

## Steps
Created a functional flow diagram showing modules (Discovery → Scanner Engine → Service Detection → Results Normalisation → UI/Export) and data flows between CLI/GUI, scanner, and storage.

*Ref 1: Functional Flow Diagram*  <br/>

<img src="https://i.imgur.com/iQKfboU.png"/>
<br />
<br />
Implemented a prototype of the TCP connect and UDP scanning loops. <br/>

*Ref 2: TCP prototype*  <br/>
<img src="https://i.imgur.com/gtiEi2s.png"/>
<br />
<br />

*Ref 3: UDP prototype*  <br/>
<img src="https://i.imgur.com/s0ayEux.png"/>
<br />
<br />
Implement Stealth (SYN) scan using Scapy. <br/>

*Ref 4: SYN prototype*  <br/>
<img src="https://i.imgur.com/8RHnnMv.png"/>
<br />
<br />

Host discovery (ICMP/ping) and scanning orchestration. <br/>

*Ref 5: Ping prototype*  <br/>
<img src="https://i.imgur.com/juHP3sv.png"/>
<br />
<br />

Built basic banner-grabbing for common services. <br/>

*Ref 6: Banner grabber prototype*  <br/>
<img src="https://i.imgur.com/586fjIR.png"/>
<br />
<br />

Tkinter GUI & result presentation. <br/>

*Ref 6: GUI*  <br/>
<img src="https://i.imgur.com/C7Xx7Ks.png"/>
<br />
<br />

<img src="https://i.imgur.com/ajwOM2j.png"/>
<br />
<br />

<img src="https://i.imgur.com/0rTU0r8.png"/>
<br />
<br />

<img src="https://i.imgur.com/uHKfUvj.png"/>
<br />
<br />

<img src="https://i.imgur.com/7sme2tg.png"/>
<br />
<br />

Testing & validation.

*Ref 7: Test results*  <br/>
<img src="https://i.imgur.com/2Tb9iKM.png"/>
<br />
<br />

<img src="https://i.imgur.com/6Ywij7j.png"/>
<br />
<br />

<img src="https://i.imgur.com/4tSH1kU.png"/>
<br />
<br />

Result normalisation & CSV/TXT export.

*Ref 8: Export files*  <br/>

<img src="https://i.imgur.com/Pl5eR37.png"/>
<br />
<br />
