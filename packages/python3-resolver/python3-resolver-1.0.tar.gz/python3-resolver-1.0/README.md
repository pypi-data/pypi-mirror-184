# Python3 - DNS Resolver

This is a simple script to resolve DNS A/AAAA records.

It only uses builtin modules.

## Usage

### Shell

If ran from the shell - use the following parameters:

* **-n/--hostname** => The hostname/DNS-record to resolve
* **-p/--protocol** => IP-Protocol to return (_optional; one of '4/6/46'_)

```bash
python3 resolver.py -h
> usage: DNS Resolver [-h] -n HOSTNAME [-p {4,6,46}]
> 
> Script to resolve A/AAAA DNS records
> 
> options:
>   -h, --help            show this help message and exit
>   -n HOSTNAME, --hostname HOSTNAME
>                         The hostname/DNS-record to resolve
>   -p {4,6,46}, --protocol {4,6,46}
>                         IP-Protocol to return

python3 resolver.py -n superstes.eu
> ['89.43.33.99', '2a05:8280:f:42ea::3']

python3 resolver.py -n superstes.eu -p 4
> ['89.43.33.99']

python3 resolver.py -n unsetdomain.com
> []
```

### Programmatically

You can import the resolver from other python modules/scripts.

Per example if the scripts are saved in the same directory.

```bash
ls .
> resolver.py
> program.py
```

```python3
from resolver import resolve, resolve_ipv4, resolve_ipv6

resolve('superstes.eu')
# list(['89.43.33.99', '2a05:8280:f:42ea::3'])

resolve_ipv4('superstes.eu')
# list(['89.43.33.99'])

resolve_ipv6('superstes.eu')
# list(['2a05:8280:f:42ea::3'])
```
