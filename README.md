# CLI Wrapped 🖥️

## Overview
CLI Wrapped is a fun `AI-Generated` Python script that analyzes your bash history and provides a Spotify Wrapped-style report of your command-line activities. Get insights into your terminal habits, top commands, and even your CLI personality!

## Features
- 📊 Total command count
- 🏆 Top 10 most used commands
- 🌈 Command category breakdown
- ⏰ Average daily command calculation
- 🎉 Unique CLI personality assessment

## Prerequisites
- Python 3.x
- Bash history file (typically located at `~/.bash_history`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cli-wrapped.git
   cd cli-wrapped
   ```

2. Ensure the script is executable:
   ```bash
   chmod +x cli_wrapped.py
   ```

## Usage
Run the script directly:
```bash
python3 cli_wrapped.py
```

## Customization
- Modify the `history_file` parameter to use a different history file
- Extend command categories in the `get_command_categories()` method
- Add more CLI personalities in the `_assign_cli_personality()` method

## Example Output
```
🖥️  YOUR CLI WRAPPED 🖥️
============================

📊 Total Commands Executed: 1024

🏆 Top 10 Most Used Commands:
- git: 132 times
- cd: 87 times
- ls: 76 times
- code: 54 times
- pip: 42 times

🧑‍💻 Command Category Breakdown:
- Development: 256 commands
- Navigation: 178 commands
- File Management: 124 commands

⏰ Average Daily Commands: 2.80

🎉 Your CLI Personality:
You are: Developer 🚀
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.


## Disclaimer
This script provides a fun analysis of your bash history. Always be mindful of privacy and sensitive information.
