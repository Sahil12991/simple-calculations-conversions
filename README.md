# 🔥 Simple Calculations & Conversions (Python)

![demo](https://github.com/user-attachments/assets/af624df3-4b87-46f6-bb53-53f169f4e1f0)

A simple Python CLI project that provides multiple utility tools like:
- 🧮 Calculator
- 💱 Currency Converter
- 🌡️ Temperature Converter

This project was mainly built to learn **real Git + GitHub workflow**:
✅ repo setup  
✅ commits  
✅ branching  
✅ pushing  
✅ pull requests  
✅ merging  
✅ clean Python package structure  

---

## 🚀 Features

### 🧮 Calculator
- Add
- Subtract
- Multiply
- Divide

### 💱 Currency Converter
- USD → INR (example fixed rate)

### 🌡️ Temperature Converter
- Celsius → Fahrenheit
- Fahrenheit → Celsius

---

## 📂 Project Structure

```
simple-calculations-conversions/
 ├── app/
 │    ├── __init__.py
 │    ├── main.py
 │    ├── calculator.py
 │    ├── currency_converter.py
 │    ├── temp_converter.py
 ├── README.md
 ├── requirements.txt
 ├── .gitignore
```

---

## ⚙️ How to Run the App

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/simple-calculations-conversions.git
cd simple-calculations-conversions
```

### 2️⃣ Run the project
```bash
python3 -m app.main
```

---

## 🧠 Git + GitHub Workflow (Step-by-Step)

This section shows the full Git workflow used in this project.

---

## ✅ Step 1: Initialize Git Repo

```bash
git init
```

---

## ✅ Step 2: Create Folder & Files

```bash
mkdir app
cd app
touch __init__.py main.py calculator.py currency_converter.py temp_converter.py
cd ..
touch README.md requirements.txt .gitignore
```

---

## ✅ Step 3: Add Files and First Commit

```bash
git add .
git commit -m "Initial project setup"
```

---

## ✅ Step 4: Connect to GitHub (Remote Origin)

Add GitHub repo link:

```bash
git remote add origin https://github.com/<your-username>/simple-calculations-conversions.git
```

Check remote:

```bash
git remote -v
```

---

## ✅ Step 5: Push Main Branch to GitHub

```bash
git branch -M main
git push -u origin main
```

### What does `-u` mean?
`-u` sets upstream, so later you can simply use:
```bash
git push
```

---

## 🌿 Creating Feature Branches (Real Team Workflow)

Instead of coding directly in main, create a separate branch for each feature.

---

## 🧮 Calculator Feature Branch

### Create and switch to branch
```bash
git checkout -b feature/calculator
```

### Add code and commit
```bash
git add .
git commit -m "Added calculator feature"
```

### Push branch to GitHub
```bash
git push -u origin feature/calculator
```

---

## 💱 Currency Converter Feature Branch

### Switch back to main and pull latest changes
```bash
git checkout main
git pull origin main
```

### Create branch
```bash
git checkout -b feature/currency-converter
```

### Commit and push
```bash
git add .
git commit -m "Added currency converter feature"
git push -u origin feature/currency-converter
```

---

## 🌡️ Temperature Converter Feature Branch

### Switch back to main and pull latest changes
```bash
git checkout main
git pull origin main
```

### Create new branch
```bash
git checkout -b feature/temp-converter
```

### Commit and push
```bash
git add .
git commit -m "Added temperature converter feature"
git push -u origin feature/temp-converter
```

---

## 🔀 Merging Branches into Main

### Recommended Method: GitHub Pull Request
1. Go to GitHub repository
2. Click **Compare & Pull Request**
3. Select:
   - Base branch: `main`
   - Compare branch: `feature/temp-converter`
4. Click **Create Pull Request**
5. Click **Merge Pull Request**
6. (Optional) Delete the branch after merge

---

## 🔄 Update Local Main After Merge

After merging on GitHub, update your local main:

```bash
git checkout main
git pull origin main
```

---

## 🧹 Removing Unwanted macOS Files (.DS_Store)

macOS automatically creates `.DS_Store` files, which should not be in GitHub.

### Remove file from repo
```bash
git rm .DS_Store
```

### Add it to `.gitignore`
```bash
echo ".DS_Store" >> .gitignore
```

### Commit and push
```bash
git add .gitignore
git commit -m "Removed .DS_Store and added to gitignore"
git push
```

---

## 📌 Useful Git Commands

### Check status
```bash
git status
```

### Check branch list
```bash
git branch
```

### See all branches (including remote)
```bash
git branch -a
```

### Switch branch
```bash
git checkout branch_name
```

### Pull latest code
```bash
git pull origin main
```

### View commit history
```bash
git log --oneline
```

### Remove staged files (unstage)
```bash
git restore --staged .
```

### Show remote URLs
```bash
git remote -v
```

---

## 🛠️ Technologies Used
- Python 3
- Git
- GitHub

---

## 🎯 Future Improvements
- Add real-time currency conversion using API
- Add unit tests using `pytest`
- Improve CLI menu system
- Add logging
- Convert to a Flask web app
- Deploy online using Render / Railway / Vercel backend
- Add Docker support
- Add GUI version using Tkinter

---

## 👤 Author
**Sahil Harde**  
Learning Python + GitHub + Deployment 🚀

---

⭐ If you liked this project, consider giving it a star on GitHub!
