# Information Retrieval Tool

Welcome to the Information Retrieval Tool by 6AMSolution!

## Overview

This tool helps users retrieve subdomains and WHOIS information for a given domain. It consists of a Python script (`get_info.py`) and a Bash script (`get_info.sh`).

## Installation

### Python Script

1. Make sure you have Python installed on your system. If not, [download and install Python](https://www.python.org/downloads/).

2. Install the required Python packages:

    ```bash
    pip install requests beautifulsoup4 python-whois
    ```

### Bash Script

No additional installations are needed for the Bash script.

## Usage

### Python Script

1. Open a terminal.

2. Navigate to the tool directory:

    ```bash
    cd /path/to/info-retrieval-tool
    ```

3. Run the Python script with the desired domain as an argument:

    ```bash
    python get_info.py example.com
    ```

### Bash Script

1. Open a terminal.

2. Navigate to the tool directory:

    ```bash
    cd /path/to/info-retrieval-tool
    ```

3. Make the Bash script executable:

    ```bash
    chmod +x get_info.sh
    ```

4. Run the Bash script with the desired domain as an argument:

    ```bash
    ./get_info.sh example.com
    ```

## GitHub Repository

The code is hosted on GitHub: [info-retrieval-tool](https://github.com/6amsolution/info-retrieval-tool)

### How to Use the Repository

1. Clone the repository:

    ```bash
    git clone https://github.com/6amsolution/info-retrieval-tool.git
    cd info-retrieval-tool
    ```

2. Copy your domain information retrieval scripts into the repository.

3. Add and commit changes:

    ```bash
    git add .
    git commit -m "Your commit message"
    ```

4. Push changes to GitHub:

    ```bash
    git push origin master
    ```

## Legal Considerations

Ensure that you have the right to scrape information from the websites you are querying and respect their terms of service.

## Tool Name

Feel free to suggest a name for the tool! If you have any ideas, let us know in the [issues](https://github.com/6amsolution/info-retrieval-tool/issues) section.

## License

This project is licensed under the MIT License.
