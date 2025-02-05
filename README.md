````markdown
# 🔥 Cybersecurity Automation Tool 🚀

This script automates the usage of various cybersecurity tools in **Kali Linux**, providing a **user-friendly interface** with predefined profiles for common commands.  
Instead of memorizing complex syntax, you can select a tool and execute it with ease.

---

## **📌 Features**

✅ **Dynamically Loads Tools from JSON** (`tools.json`)  
✅ **Automates Nmap, Nikto, Hashcat, Hydra, Gobuster, Metasploit & More**  
✅ **Multi-threaded Execution** for Faster Performance  
✅ **Error Handling & Logging** to `cybersecurity_tool_log.txt`  
✅ **Auto-Detects Missing Dependencies**  
✅ **Super Easy to Expand - Just Edit `tools.json`!**

---

## **🛠 Requirements**

- **Python 3.x**
- **Kali Linux** (or any Linux system with security tools installed)
- **Required tools installed** (Nmap, Nikto, Hashcat, Hydra, Gobuster, Metasploit, etc.)

---

## **🔧 Installation**

Clone the repository:

```bash
git clone https://github.com/yourrepo/cybersecurity-automation.git
cd cybersecurity-automation
```
````

Give execution permission:

```bash
chmod +x cybersecurity_tool.py
```

Run the script:

```bash
python3 cybersecurity_tool.py
```

---

## **📌 Usage**

1. Run `python3 cybersecurity_tool.py`
2. Select a **tool** from the menu.
3. Provide necessary input (target, file paths, options).
4. Let the tool run—results will be logged in `cybersecurity_tool_log.txt`.

---

## **📝 Adding More Tools (Super Easy!)**

This tool loads **all tool configurations** dynamically from a JSON file (`tools.json`).

To **add new tools**, just **edit** `tools.json` – No need to modify Python code! 🎉

### **📌 Example: Adding a New Tool**

Let's say you want to add **ffuf** (a fast web fuzzer).  
Open `tools.json` and **add this entry:**

```json
"ffuf": {
    "description": "Fast web fuzzer",
    "command": "ffuf -u {target}/FUZZ -w {wordlist}"
}
```

Now restart the script, and **ffuf will appear in the menu!** 🚀

### **📌 Example: Adding a Tool with Profiles**

If a tool has different scanning modes (e.g., `gobuster`), you can **define profiles** like this:

```json
"gobuster": {
    "description": "Directory and subdomain brute-force tool",
    "profiles": {
        "1": "dir -u",
        "2": "dns -d"
    },
    "command": "gobuster {options} {target}"
}
```

This allows users to **choose a mode** before execution.

---

## **🚀 Tools Included**

| Tool           | Description                       | Command Example                          |
| -------------- | --------------------------------- | ---------------------------------------- |
| **Nmap**       | Network scanning                  | `nmap -A target`                         |
| **Nikto**      | Web vulnerability scanning        | `nikto -h target`                        |
| **Hashcat**    | Password cracking                 | `hashcat -m 0 hash.txt wordlist.txt`     |
| **Gobuster**   | Directory & subdomain brute-force | `gobuster dir -u target -w wordlist.txt` |
| **Hydra**      | Password brute-forcing            | `hydra -L user -P wordlist target ssh`   |
| **Metasploit** | Penetration testing framework     | `msfconsole`                             |

---

## **⚠️ Disclaimer**

🚨 **For Educational Purposes Only!** 🚨  
This tool is meant for **ethical hacking & penetration testing**. **Unauthorized use is illegal.**

Use this tool **only on systems you have explicit permission to test.**  
The author is **not responsible for any misuse.**

---

## **🌟 Credits & Contribution**

- **Author:** [Your Name]
- **Want to add more tools?** PRs are welcome!
- **Found a bug?** Open an issue! 🚀

---

## **💻 Future Improvements**

- ✅ **Save scan results to a structured database**
- ✅ **Integrate AI-based attack recommendations**
- ✅ **Automate Metasploit exploit execution**
- ✅ **GUI for easier navigation**

🚀 **Happy Hacking!** 🔥

```

---

## **🔹 What's New in the README?**
✅ **Explains the JSON-based tool system**
✅ **Shows how to add new tools easily**
✅ **Better formatted and more structured**
✅ **Future improvements & contribution guidelines**

This version makes it **easier than ever** to **add new tools** and **expand functionality** without touching Python code! 🚀
```
