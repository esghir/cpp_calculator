FROM gcc:latest

# Install dependencies
RUN apt-get update && apt-get install -y \
    cmake \
    python3 \
    python3-pip \
    python3-venv \
    lcov \
    gcovr

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Clean, build project, and run tests
RUN rm -rf build && \
    mkdir build && \
    cd build && \
    cmake -DCMAKE_BUILD_TYPE=Debug .. && \
    make && \
    ctest --output-on-failure