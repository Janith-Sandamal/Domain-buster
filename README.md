# 🔎 Advanced Subdomain Enumeration Tool

![Subdomain Enumeration](https://img.shields.io/badge/Enumeration-Subdomains-blue?style=flat-square) 
![Python](https://img.shields.io/badge/Python-3.7%2B-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-red?style=flat-square)

An advanced **domain and subdomain enumeration tool** that integrates multiple enumeration techniques using **Amass, Sublist3r, Assetfinder**, and other tools to enhance penetration testing capabilities. 🚀

---

## ⚡ Features

✅ **Integrates multiple enumeration tools** (Amass, Sublist3r, Assetfinder, etc.)  
✅ **Removes duplicate subdomains** for accurate results  
✅ **Saves results in JSON format** for easy analysis  
✅ **Command-line interface (CLI) for easy use**  
✅ **Modular and extensible** for adding more enumeration tools  

---

## 📌 Installation

### 🛠️ **Prerequisites**
Ensure you have the following dependencies installed:

```bash
sudo apt update && sudo apt install amass
git clone https://github.com/aboul3la/Sublist3r.git && cd Sublist3r && pip install -r requirements.txt
git clone https://github.com/ffuf/assetfinder.git && cd assetfinder && go build && sudo mv assetfinder /usr/local/bin/
```

## 🔧 Clone the Repository

```bash
git clone https://github.com/yourusername/subdomain_enum.git
cd subdomain_enum
pip install -r requirements.txt
```

## 🚀 Usage
### 📌 Basic Usage

```bash
python main.py -d example.com -t amass,sublist3r,assetfinder -o output.json
```

### 📌 Arguments

| Argument       | Description                                           | Required |
|---------------|-------------------------------------------------------|----------|
| `-d, --domain` | Target domain (e.g., `example.com`)                  | ✅ Yes |
| `-t, --tools`  | Enumeration tools (comma-separated: `amass,sublist3r,assetfinder`) | ✅ Yes |
| `-o, --output` | Output file to save results (`default: results.json`) | ❌ No  |

### 📌 Example Output

```bash
{
  "subdomains": [
    "api.example.com",
    "mail.example.com",
    "dev.example.com",
    "test.example.com"
  ]
}
```

## 📊 Tool Comparisons

| Tool         | Methodology          | Strengths                        |
|-------------|---------------------|---------------------------------|
| **Amass**    | OSINT, Passive, Active | Comprehensive, deep recon       |
| **Sublist3r**| Search Engine Scraping | Fast, lightweight               |
| **Assetfinder** | Public Data Sources | Quick enumeration, simple usage |


## 🔥 Planned Features

✅ **DNS resolution for subdomains**  
✅ **Multi-threading for faster execution**  
🔲 **Add support for more tools (e.g., Knock, Findomain)**  
🔲 **Export results in CSV format**  
🔲 **Add a web-based UI for visualization**  

## 🛠️ Troubleshooting
### If you encounter any issues, try:

```bash
python main.py --help
which amass
which assetfinder
pip install -r requirements.txt
```

## 📜 License

### This project is licensed under the MIT License. Feel free to modify and share!

## 🚀 Happy Hacking!


