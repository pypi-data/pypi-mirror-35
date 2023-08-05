# py

Port of [thisredone/py](https://github.com/thisredone/rb) to Python.

With 12 lines of Python, replace most of the command line tools that you use to process text inside of the terminal.

Here's the code:

```python
#!/usr/bin/env python

import re
import sys

per_line = sys.argv[1] == '-l'
stdin = [line.strip() for line in sys.stdin.readlines()]

if per_line:
    code = ' '.join(sys.argv[2:]).replace('{}', 'line')
    for line in stdin:
        print(eval(code))
else:
    code = ' '.join(sys.argv[1:]).replace('{}', 'stdin')
    for line in eval(code):
        print(line)
```

There's only one switch `-l` which runs your code on each line separately. Otherwise you get the whole stdin as an array of lines.

## Install

**Note**: `~/.local/bin` should be in your `PATH` for `--user` installs.

```bash
pip install [--user] py2
```

## Examples

Extract docker images from running containers:

```bash
> docker ps | py '{}[1:]' | py -l '{}.split()[1]'

ubuntu
postgres
```

Display how much time ago containers have exited:

```bash
> docker ps -a | py 'filter(lambda x: "Exited" in x, {})' | py -l '{}.split()[-1].ljust(20) + " => " + re.split(r"' '{2,}", {})[-2]'

angry_hamilton      => Exited (0) 18 hours ago
dreamy_lamport      => Exited (0) 3 days ago
prickly_hypatia     => Exited (0) 2 weeks ago
```

Sort `df -h` based on Use% (without header):

```bash
> df -h | ./py 'sorted({}[1:], key=lambda x: x.split()[-2])'

dev             3.8G     0  3.8G   0% /dev
tmpfs           3.8G     0  3.8G   0% /sys/fs/cgroup
run             3.8G  948K  3.8G   1% /run
tmpfs           775M   36K  775M   1% /run/user/1000
tmpfs           3.8G  417M  3.4G  11% /dev/shm
/dev/sda1       256M   43M  214M  17% /boot
/dev/sda2       117G   27G   84G  25% /
```

Sort `df -h` based on Use% (with header):

```bash
> df -h | ./py '[{}[0]] + sorted({}[1:], key=lambda x: x.split()[-2])'

Filesystem      Size  Used Avail Use% Mounted on
dev             3.8G     0  3.8G   0% /dev
tmpfs           3.8G     0  3.8G   0% /sys/fs/cgroup
run             3.8G  948K  3.8G   1% /run
tmpfs           775M   36K  775M   1% /run/user/1000
tmpfs           3.8G  417M  3.4G  11% /dev/shm
/dev/sda1       256M   43M  214M  17% /boot
/dev/sda2       117G   27G   84G  25% /
```
