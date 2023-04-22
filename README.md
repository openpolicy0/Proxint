# Proxint
Input a url and a file of your proxys to see if the website will except your proxys
and use those proxys in proxychains tool ( apt install proxychains ) to add those proxys from your proxy list
nano /etc/proxychains.conf

```
IP status code | up or down | print proxy
==========================================
       200     |     ✅️     |   127.0.0.1
       404     |     ❌️     |     faild
```

# results
then get the output results of the proxys

```
status code     |           WORKS       |         FROM IP ADDRESS
=================================================================================
     404         |           DOWN ❌     |             faild
     404         |           DOWN ✅️     |             12.75.123.88
     404         |           DOWN ❌     |             faild
     404         |           DOWN ❌     |             faild
     404         |           DOWN ❌     |             faild
     404         |           DOWN ✅️     |             8.8.8.8
     404         |           DOWN ❌     |             faild
     404         |           DOWN ❌     |             faild
     404         |           DOWN ❌     |             faild
     404         |           DOWN ❌     |             faild
 ```

# installing Proxint
```
git clone https://github.com/openpolicy0/Proxint.git
cd Proxint
pip install-r requirements.txt 
```
