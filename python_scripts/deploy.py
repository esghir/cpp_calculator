import os
import subprocess
import sys

def deploy_application(environment):
    """Deploy the application to specified environment"""
    print(f"Deploying to {environment} environment...")

    try:
        # Simulate deployment steps
        subprocess.run(['cp', '../src/calculator', f'./{environment}/'])
        print(f"Successfully deployed to {environment}")
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: deploy.py <environment>")
        sys.exit(1)

    environment = sys.argv[1]
    success = deploy_application(environment)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
