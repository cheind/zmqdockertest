## About

This minimal working example benchmarks throughput metrics for ZMQ running bare-metal or virtualized through docker. 

**tl/dr** ZMQ virtualized using WSL2 on Windows achieves higher throughput than bare Windows (2x) or virtualized using Windows containers (10x).

## Method
The example code consists of single producer/consumer node interacting via `PUSH/PULL` sockets. The producer sends *N* pre-allocated messages each of size *B*. Each message contains a large byte array `np.array` and a wallclock timestamp of the sender. The consumer awaits *N* messages and performs minimal bookkeeping. `pickle` is used for serialization.

After the last message is consumed, the consumer a) computes the time elapsed *E* as the difference of the current consumer wallclock time and the message timestamp of the first message received and b) the sum of all bytes received *B*. The throughput is then computed as `B/E`.

The example may be run directly on the host OS or virtualized in docker. When run in bare OS, two processes are spawned. When run in Docker, two separate containers are used.

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
