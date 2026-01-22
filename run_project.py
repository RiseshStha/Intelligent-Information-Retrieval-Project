import os
import sys
import subprocess
import webbrowser
import threading
import time

def run_django():
    """Run Django backend server."""
    print("[Backend] Starting Django Server at http://127.0.0.1:8000...")
    cmd = [sys.executable, "manage.py", "runserver"]
    cwd = os.path.join(os.getcwd(), "backend")
    
    try:
        subprocess.run(cmd, cwd=cwd, check=True)
    except KeyboardInterrupt:
        print("\n[Backend] Stopping Django Server...")

def run_react():
    """Run React frontend server."""
    print("[Frontend] Starting Vite Server at http://localhost:5173...")
    cwd = os.path.join(os.getcwd(), "frontend")
    
    try:
        # Use cmd /c for Windows PowerShell compatibility
        subprocess.run("cmd /c npm run dev", cwd=cwd, shell=True, check=True)
    except KeyboardInterrupt:
        print("\n[Frontend] Stopping Vite Server...")

def open_browser():
    """Open browser after delay."""
    time.sleep(5)
    print("\n[System] Opening Browser...")
    webbrowser.open("http://localhost:5173")

def main():
    print("=" * 70)
    print("   Coventry University Research Search Engine")
    print("   Task 1: Search Engine + Task 2: Document Classification")
    print("   Python Launcher - Starts Both Backend & Frontend")
    print("=" * 70)
    print()
    print("Backend (Django):  http://127.0.0.1:8000")
    print("Frontend (React):  http://localhost:5173")
    print()
    print("Search Engine:     http://localhost:5173/")
    print("Classification:    http://localhost:5173/classification")
    print("Statistics:        http://localhost:5173/stats")
    print("Crawler:           http://localhost:5173/crawl")
    print("=" * 70)
    print()
    
    # Verify project directory structure
    if not os.path.exists("backend") or not os.path.exists("frontend"):
        print("[ERROR] Please run this script from the project root directory.")
        return

    # Create and start threads
    t_backend = threading.Thread(target=run_django)
    t_frontend = threading.Thread(target=run_react)
    t_browser = threading.Thread(target=open_browser)
    
    t_backend.start()
    t_frontend.start()
    t_browser.start()
    
    print("\n[System] Servers are starting... Press Ctrl+C to stop.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[System] Shutting down...")
        os._exit(0)

if __name__ == "__main__":
    main()
