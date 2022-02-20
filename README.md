# EIP_Module_SpiderFoot-OSINT

Proof of concept of a module for SpiderFoot for cibersecurity educational purposes only, <a href="https://eiposgrados.com/programas/master-en-ciberseguridad/">@eiposgrados</a>.


SpiderFoot is an open source intelligence (OSINT) automation tool. It integrates with just about every data source available and utilises a range of methods for data analysis, making that data easy to navigate.

# Installation SpiderFoot

```
$ git clone https://github.com/smicallef/spiderfoot.git
$ cd spiderfoot
$ pip3 install -r requirements.txt
```


This module allows you to obtain a list of emails based on a domain using the hunter.io API


# Installation Module
```
$ git clone https://github.com/adrihamel/EIP_Module_SpiderFoot-OSINT.git
$ cd EIP_Module_SpiderFoot-OSINT
```

Then copy the module sfp_email_discover.py inside of spiderfoot/modules

# Module execution

```
$ cd spiderfoot
$ python3 ./sf.py -l 127.0.0.1:5001
```

1- Go to 127.0.0.1:5001 and click on New Scan

![spiderfoot1](images/spiderfoot1.jpg)

2- Go to By Module and search Email Discover. Click to check

![spiderfoot2](images/spiderfoot2.jpg)

3- Finally, go to Run Scan Now and wait to load data.

![spiderfoot3](images/spiderfoot3.jpg)


# Test

![spiderfoot4](images/spiderfoot4.jpg)

![spiderfoot5](images/spiderfoot5.jpg)

![spiderfoot6](images/spiderfoot6.jpg)



