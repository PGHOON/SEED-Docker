# Use Ubuntu version 20.04
FROM ubuntu:20.04

# Update the package list and install the packages we'll use(ssh, sudo, systemd, docker, vim, gcc)
RUN apt-get update && apt-get install -y openssh-server sudo systemd && apt-get install -y docker.io && apt-get install -y vim && apt-get install -y build-essential && apt-get install git && apt-get install iputils-ping && apt-get clean

# Create the SSH directory and set the appropriate permissions
RUN mkdir /var/run/sshd
RUN chmod 0755 /var/run/sshd

# Add a user named "seed" with the password "seed"
RUN useradd -m seed
RUN echo "seed:seed" | chpasswd

# Allow password authentication
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Add sudo access
RUN usermod -aG sudo seed

# Expose the default SSH port
EXPOSE 22

# Start the SSH service and the init system when the container starts
CMD ["/sbin/init", "&&", "/usr/sbin/sshd", "-D"]


############################################################################################

##how to build the dockerfile to the docker image##
#docker build -t 'docker_image_name' .

##how to run the docker container using the image you built##
#docker run --privileged -d -p 'port':22 'docker_image_name'
###You must run the container with the privileged option to use DinD(Docker in Docker)###

##how to connect the SSH server##
#ssh seed@localhost