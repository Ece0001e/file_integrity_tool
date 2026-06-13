# File Integrity Tool

A Python tool that generates SHA-256 hashes for files and verifies file integrity.

## Features
- Generate file hashes with SHA-256
- Verify file integrity
- Store hash information in JSON format
- Track file size and creation timestamp
- Comprehensive error handling

## Requirements
- Python 3.6 or higher

## Installation

Clone the repository:
```bash
git clone https://github.com/Ece0001e/file_integrity_tool.git
cd file_integrity_tool
```

## Usage

Run the tool:
```bash
python file_integrity_tool.py
```

### Menu Options:
1. **Create Integrity record** - Generate a SHA-256 hash for a file and save it as a JSON record
2. **Verify Integrity** - Check if a file matches its stored integrity record
3. **Exit** - Close the program

### Example:
```
---File Integrity Tool---
1. Create Integrity record
2. Verify Integrity
3. Exit
Enter: 1
Enter Filename: myfile.txt
✓ Integrity record saved as myfile.txt.json
```

## Record Format

The integrity records are saved as JSON files with the following structure:
```json
{
    "filename": "myfile.txt",
    "sha256": "abc123...",
}
```

## License
MIT
