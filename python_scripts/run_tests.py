import subprocess
import sys
import os

def build_cpp_tests():
    """Build C++ tests"""
    try:
        result = subprocess.run(['g++', '-o', '../tests/test_calculator', '../tests/test_calculator.cpp', '../src/calculator.cpp'],
                                capture_output=True,
                                text=True,
                                cwd=os.path.dirname(__file__))
        if result.returncode != 0:
            print("Build failed:")
            print(result.stderr)
            return False
        return True
    except Exception as e:
        print(f"Error building tests: {e}")
        return False

def run_cpp_tests():
    """Execute C++ tests and return results"""
    try:
        result = subprocess.run(['../tests/test_calculator'],
                                capture_output=True,
                                text=True,
                                cwd=os.path.dirname(__file__))
        print(result.stdout)
        return result.returncode == 0
    except Exception as e:
        print(f"Error running tests: {e}")
        return False

def main():
    if not build_cpp_tests():
        sys.exit(1)
    success = run_cpp_tests()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()