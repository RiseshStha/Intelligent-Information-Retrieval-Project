# Troubleshooting Guide

## Common Issues and Solutions

### 1. PowerShell Execution Policy Error

**Error:**
```
npm : File D:\nodejs\npm.ps1 cannot be loaded because running scripts is disabled on this system.
```

**Solution:**
The `run_project.py` script has been updated to handle this automatically using `cmd /c npm run dev`.

If you still encounter issues, you can:
- Run commands manually using `cmd /c npm install` instead of `npm install`
- Or change PowerShell execution policy (as administrator):
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

---

### 2. Frontend Dependencies Not Installed

**Error:**
```
'vite' is not recognized as an internal or external command
```

**Solution:**
Install frontend dependencies first:
```bash
cd frontend
npm install
```

Or use:
```bash
cd frontend
cmd /c npm install
```

---

### 3. Backend Server Port Already in Use

**Error:**
```
Error: That port is already in use.
```

**Solution:**
- Stop any other Django servers running on port 8000
- Or change the port in `run_project.py`:
  ```python
  cmd = [sys.executable, "manage.py", "runserver", "8001"]
  ```

---

### 4. Frontend Server Port Already in Use

**Error:**
```
Port 5173 is in use, trying another one...
```

**Solution:**
Vite will automatically try another port. Check the console output for the actual port being used.

---

### 5. Module Not Found Errors (Backend)

**Error:**
```
ModuleNotFoundError: No module named 'django'
```

**Solution:**
Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

---

### 6. Model Not Found Error

**Error:**
```
Model not trained or loaded
```

**Solution:**
Train the classification model first:
```bash
python run_task2_classification.py
```

---

### 7. CORS Errors in Browser

**Error:**
```
Access to XMLHttpRequest blocked by CORS policy
```

**Solution:**
- Ensure backend is running on port 8000
- Check `backend/config/settings.py` has correct CORS settings
- Verify `CORS_ALLOWED_ORIGINS` includes `http://localhost:5173`

---

### 8. Database Migration Errors

**Error:**
```
You have unapplied migrations
```

**Solution:**
```bash
cd backend
python manage.py migrate
```

---

### 9. npm Not Found

**Error:**
```
'npm' is not recognized as an internal or external command
```

**Solution:**
- Install Node.js from https://nodejs.org/
- Restart your terminal after installation
- Verify installation: `node --version` and `npm --version`

---

### 10. Python Not Found

**Error:**
```
'python' is not recognized as an internal or external command
```

**Solution:**
- Install Python from https://www.python.org/
- Make sure to check "Add Python to PATH" during installation
- Or use `py` instead of `python` on Windows

---

## Quick Fixes

### Reset Everything
```bash
# Stop all servers (Ctrl+C)

# Reinstall frontend dependencies
cd frontend
rd /s /q node_modules
cmd /c npm install

# Reinstall backend dependencies
cd ../backend
pip install -r requirements.txt

# Retrain model
cd ..
python run_task2_classification.py

# Run project
python run_project.py
```

---

### Manual Server Start (if run_project.py fails)

**Terminal 1 - Backend:**
```bash
cd backend
python manage.py runserver
```

**Terminal 2 - Frontend:**
```bash
cd frontend
cmd /c npm run dev
```

---

## Still Having Issues?

1. Check that you're in the correct directory (`final task/`)
2. Verify Python version: `python --version` (should be 3.8+)
3. Verify Node version: `node --version` (should be 14+)
4. Check the console output for specific error messages
5. Review the documentation files (TASK2_*.md)

---

## Contact Information

If problems persist:
- Review `README.md` for setup instructions
- Check `TASK2_DOCUMENTATION.md` for detailed information
- Ensure all dependencies are installed correctly
