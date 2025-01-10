*NAME:* SAMPANGI NAGAVARDHAN    
*COMPANY:* CODTECH IT SOLUTIONS  
*ID:* CT08DS540  
*DOMAIN:* Cyber Security and Ethical Hacking  
*DURATION:* December 2024 to January 2025  
## **Task 1: File Integrity Checker**

### **Description**
A Python-based tool that calculates and compares hash values of files to monitor changes and ensure file integrity. 

### **Features**
- Calculates SHA-256 hash values for files.
- Monitors changes by comparing current hashes to stored ones.
- Detects new, modified, or deleted files.

### **Requirements**
- Python 3.x

### **Setup**
1. Clone the repository.
2. Install Python 3.x if not already installed.
3. Run the script with appropriate arguments.

### **Usage**
1. **Store hashes**:
   ```bash
   python file_integrity_checker.py --store "directory_to_monitor" --output "hashes.txt"
   ```
2. **Compare hashes**:
   ```bash
   python file_integrity_checker.py --compare "directory_to_monitor" --hashfile "hashes.txt"
   ```

### **Example**
To monitor changes in a directory:
```bash
python file_integrity_checker.py --store "my_folder" --output "hashes.txt"
python file_integrity_checker.py --compare "my_folder" --hashfile "hashes.txt"
```

