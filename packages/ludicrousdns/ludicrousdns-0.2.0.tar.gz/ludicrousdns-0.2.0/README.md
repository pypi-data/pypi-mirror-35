# ludicrousdns
`ludicrousdns` aims to be ludicrously speedy and ridicously reliable.

## Installation
```
pip install ludicrousdns
```

## TODO
- Detect wildcard DNS
- Add per resolver rate-limiting
- Limit simultaneous connections (for example through number of coroutines)
- Add benchmark to measure CPU- and network usage
- Add timeout to connections, for example with [https://github.com/aio-libs/async-timeout](async_timeout)
