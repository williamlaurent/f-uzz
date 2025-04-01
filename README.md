# 🚀 F-uzz

Fuzzing Websites to Find Juicy Information.

There are many free fuzzing bots on GitHub. This tool helps discover hidden files, directories, and endpoints on websites using wordlists. Feel free to recode and develop it, but don't forget to give credit and link back to my GitHub.

## ⚡ Usage
```bash
python3 fuzz.py  # Make sure to fill list.txt with your target URLs.
```

## 🎯 One-Shot Execution
```bash
python3 fuzz.py && cat results.txt
```

## 📥 Installation
Clone the repository:
```bash
git clone https://github.com/williamlaurent/f-uzz.git
cd f-uzz
```
Install dependencies:
```bash
pip install -r requirements.txt
```
If `requirements.txt` is missing, install manually:
```bash
pip install requests colorama
```

## 🔧 How It Works
1. Add your target domains to `list.txt`:
   ```
   example.com
   test.com
   ```
2. Add fuzzing wordlists to `fuzz.txt`:
   ```
   admin
   login
   config.php
   ```
3. Run the script:
   ```bash
   python3 fuzz.py
   ```
4. Results will be saved in `results.txt`.

## 🎨 Output Interpretation
- ✅ **Green** → 200 OK responses
- ❌ **Red** → Connection errors
- ⚠️ **Yellow** → Timeouts
- 🚫 **Magenta** → User-aborted process

## 👨‍💻 Author
Made by **will and crew** 👨‍💻
