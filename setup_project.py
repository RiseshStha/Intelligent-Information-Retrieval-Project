import os
import sys
import subprocess
import platform

def print_step(step, message):
    print(f"\n[{step}] {message}")

def check_command(command, name):
    try:
        subprocess.check_call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        return True
    except subprocess.CalledProcessError:
        print(f"[ERROR] {name} is not installed or not in PATH.")
        return False

def install_pip_requirements(requirements_file):
    if os.path.exists(requirements_file):
        print(f"       Installing from {requirements_file}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
    else:
        print(f"       [WARNING] {requirements_file} not found.")

def main():
    print("=" * 50)
    print("Project Setup Script")
    print("=" * 50)
    
    # Check Prerequisites
    print_step("1/5", "Checking Prerequisites...")
    if not check_command("python --version", "Python"): return
    if not check_command("cmd /c npm --version", "Node.js"): return
    
    # Install Backend Dependencies
    print_step("2/5", "Installing Backend Dependencies...")
    install_pip_requirements(os.path.join("backend", "requirements.txt"))
    
    # Install Frontend Dependencies
    print_step("3/5", "Installing Frontend Dependencies...")
    frontend_dir = os.path.join(os.getcwd(), "frontend")
    if os.path.exists(frontend_dir):
        # Use cmd /c for Windows compatibility
        subprocess.check_call("cmd /c npm install", cwd=frontend_dir, shell=True)
    else:
        print("[ERROR] Frontend directory not found!")
        return

    # Generate Machine Learning Models
    print_step("4/5", "Checking Models...")
    model_path = os.path.join("backend", "models", "nb_classifier.pkl")
    if not os.path.exists(model_path):
        print("       Running training script...")
        try:
            subprocess.check_call([sys.executable, "run_task2_classification.py"])
        except subprocess.CalledProcessError:
            print("[ERROR] Training failed.")
            return
    else:
        print("       Models exist. Skipping.")

    # Database Setup
    print_step("5/5", "Setting up Database...")
    backend_dir = os.path.join(os.getcwd(), "backend")
    
    subprocess.check_call([sys.executable, "manage.py", "makemigrations"], cwd=backend_dir)
    subprocess.check_call([sys.executable, "manage.py", "migrate"], cwd=backend_dir)
    
    print("\n" + "=" * 50)
    print("SETUP COMPLETE")
    print("=" * 50)
    print("Run: python run_project.py")
    print("=" * 50)

if __name__ == "__main__":
    main()
