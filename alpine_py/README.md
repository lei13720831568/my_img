docker build -t imageName:tag .
docker run -d -p 31234:8888 -v /home/data/notebooks:/data/notebooks imageName:tag