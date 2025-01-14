import subprocess
import sys

def build_cpp_tests():
    try:
        result = subprocess.run(
            ["cmake", "-S", ".", "-B", "build", "-DCMAKE_BUILD_TYPE=Debug"],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        result = subprocess.run(
            ["cmake", "--build", "build"],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error building tests: {e.stderr}")
        return False

def run_cpp_tests():
    try:
        result = subprocess.run(
            ["ctest", "--output-on-failure", "-C", "Debug", "--test-dir", "build"],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error running tests: {e.stderr}")
        return False

def main():
    if not build_cpp_tests():
        sys.exit(1)
    success = run_cpp_tests()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()