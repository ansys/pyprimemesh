# Meshing service Linux-based Dockerfile

# Unpack zip as builder stage
FROM rockylinux:8 as builder

# Define the working directory
WORKDIR /prime

# Install tar to unpack
RUN yum -y install tar

# Add the binary files
COPY LINX64.tar.gz .

# Unpack and modify permissions
RUN tar -zxvf LINX64.tar.gz && \
    rm LINX64.tar.gz

RUN chmod -R 0755 meshing

# Build image stage
# Based on rockylinux:8
FROM rockylinux:8

# Define the working directory
WORKDIR /prime

# Copy unpacked files from builder stage
COPY --from=builder /prime .

# Install the libnsl
RUN yum -y install libnsl

# Install the glibc-langpack-en package
RUN yum -y install glibc-langpack-en

# Set locale environment variables
ENV LANG=en_US.utf-8 \
    LC_ALL=en_US.utf-8
	
# Set env for image
ENV AWP_ROOT251="/prime"

# Add container labels
LABEL org.opencontainers.image.authors="ANSYS Inc."
LABEL org.opencontainers.image.vendor="ANSYS Inc."

ENTRYPOINT [ "/prime/meshing/Prime/runPrime.sh", "server", "--ip", "0.0.0.0" ]
