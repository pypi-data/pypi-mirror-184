# SEDA

<p align="center">
    <em>A Python toolkit to build <b>S</b>erverless <b>E</b>vent-<b>D</b>riven <b>A</b>pplications on AWS.</em>
    <br><em>Documentation: <a href="https://seda.domake.io"><del>https://seda.domake.io</del></a> (pending)</em>
</p>
<p align="center">
    <a href="https://github.com/mongkok/seda/actions">
        <img src="https://github.com/mongkok/seda/actions/workflows/test-suite.yml/badge.svg" alt="Test">
    </a>
    <a href="https://codecov.io/gh/mongkok/seda">
        <img src="https://img.shields.io/codecov/c/github/mongkok/seda?color=%2334D058" alt="Coverage">
    </a>
    <a href="https://www.codacy.com/gh/mongkok/seda/dashboard">
        <img src="https://app.codacy.com/project/badge/Grade/x" alt="Codacy">
    </a>
    <a href="https://pypi.org/project/seda">
        <img src="https://img.shields.io/pypi/v/seda" alt="Package version">
    </a>
</p>

## Installation

```sh
pip install seda
```

## Example

**main.py**:

```py
from datetime import datetime

from seda import Seda


seda = Seda()


@seda.schedule("cron(* * * * ? *)", args=("minutes",))
async def myschedule(timespec: str = "auto") -> None:
    seda.log.info(f"myschedule: {datetime.now().isoformat(timespec=timespec)}")


@seda.task
async def mytask(timespec: str = "auto") -> None:
    seda.log.info(f"mytask: {datetime.now().isoformat(timespec=timespec)}")
```

## Tasks

```py
await mytask()
```

## One time tasks

```py
from datetime import datetime, timedelta


mytask.at(datetime.now() + timedelta(minutes=5))
```

## Deploy

```sh
seda deploy -A main.seda -F myfunction
```

## ASGI

```sh
pip install seda[asgi]
```

**main.py**:

```py
from fastapi import FastAPI
from seda import Seda


app = FastAPI()
seda = Seda(app)
```

## Commands

```sh
seda cmd env -F myfunction
```

```sh
seda python 'import sys;print(sys.version)' -F myfunction
```
