FROM gcc:latest

# Install dependencies
RUN apt-get update && apt-get install -y \
    cmake \
    python3 \
    python3-pip \
    lcov \
    gcovr

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Build project
RUN mkdir build && \
    cd build && \
    cmake -DCMAKE_BUILD_TYPE=Debug .. && \
    make