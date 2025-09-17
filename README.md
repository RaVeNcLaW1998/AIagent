AI Coding Agent with Gemini

This project is a local AI coding assistant powered by Google’s Gemini API.

It accepts user prompts, plans function calls, and can list, read, write, and execute Python files in a working directory.

Features

-List files and directories

-Read file contents (with a character limit)

-Write or update Python files

-Run Python files with optional arguments

-Function-calling loop for step-by-step execution planning

Project Structure
.
├── main.py                 # Entry point: AI agent loop
├── config.py               # Configuration (model, limits)
├── .env                    # API key (DO NOT commit)
│
├── functions/
│   ├── get_files_info.py   # Lists files
│   ├── get_file_content.py # Reads file content
│   ├── write_file.py       # Writes/updates files
│   ├── run_python_file.py  # Runs Python scripts
│   └── call_function.py    # Dispatcher for tool calls
│
├── *.pyc                   # Compiled helper files

⚙️ Setup
1. Clone the repo
git clone https://github.com/RaVeNcLaW1998/AIagent.git
cd AIagent

2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

2. Install dependencies with uv

If you don’t already have uv installed:

curl -LsSf https://astral.sh/uv/install.sh | sh

Then, install dependencies:

uv sync

This will read your pyproject.toml / uv.lock and set up everything automatically.


Important: Never commit .env to GitHub. Add it to .gitignore.

Usage

Run the agent with a user prompt:

python main.py "List files in the calculator directory"


Verbose mode (shows token counts + intermediate results):

python main.py "Read the content of app.py" --verbose

Example Tasks

List files: "Show me all files in ./calculator"

Read content: "Open calculator.py and show first lines"

Write file: "Create a new file test.py with print('Hello AI')"

Run file: "Run test.py"

Security Notes

All file operations are sandboxed inside the working directory (./calculator by default).

Your API key is read from .env only—never hardcode keys.

Rotate your key if it’s exposed.

Config

Model: Defined in config.py → MODEL = "gemini-2.0-flash-001"

Read limit: MAX_CHARS = 10000 (prevents huge file reads)
