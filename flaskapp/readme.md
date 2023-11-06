1. docker build -t flaskbase_v1 flaskapp/
2. docker run -d -p 5000:5000 flaskbase_v1
3. docker ps -a
4. docker stop id(example:7a61fb535d22)
5. docker rm id(example:7a61fb535d22)