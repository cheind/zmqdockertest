## ZMQ Throughput

|Os|Container Backend|Transport|Bytes/Sec|
|--|--|--|--|
|Ubuntu 20.4|Linux|TCP/IP|1.4GiB/Sec|
|Ubuntu 20.4|Linux|IPC|1.6GiB/Sec|
|Windows 10.1904|WSL2|ICP|1.5GiB/Sec|
|Windows 10.1904|WSL2|TCP/IP|1.5GiB/Sec|
|Windows 10.1904|Windows Container|TCP/IP|154.4MiB/sec|
|Windows 10.1904|no-container|TCP/IP|604.2MiB/sec|

## Run

### Docker
Linux and Windows (WSL2)
```
docker-compose up
```

Windows (Windows Container Backend)
```
docker-compose -f docker-compose.win.yml up
```

### Bare
```
conda create -n zmqtest python=3.8 pip
conda activate zmqtest
pip install -r requirements.txt
python -m src
```
