#!/bin/bash

# Install Python (assuming apt package manager)
sudo apt update
sudo apt install python3 python3-pip python3-venv -y

# Create and activate virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Install required libraries
pip install json
pip install typing

echo "Python environment setup complete."