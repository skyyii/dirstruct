# dirstruct
A lightweight Python script that scans the current directory and writes the entire folder structure (including all files and subdirectories) to a `structure.txt` file.

## Features
- Generates tree-like visualizations
- Preserves hierarchical relationships
- Handles nested directories recursively
- Platform-independent (Windows/macOS/Linux)
- Zero dependencies

## Usage
1. Place `dirstruct.py` in your target directory
2. Run:
   ```bash
   python dirstruct.py
   ```
3. Find `structure.txt` in the same directory with your structure

## Example Output
```
project_root/
├── README.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils/
│       ├── helpers.py
│       └── config.json
├── data/
│   └── sample.csv
└── requirements.txt
```

## Requirements
- Python 3.6+

## License
MIT License - free for personal and commercial use
