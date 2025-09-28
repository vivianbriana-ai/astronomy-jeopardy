pip install numpy matplotlib anthropic python-dotenv
import numpy as np
import matplotlib.pyplot as plt
import anthropic
import json
import os
 git init
   git add .
   git commit -m "Initial commit"
from dotenv import load_dotenv

# Load your specific .env.txt file first
load_dotenv('.env.txt')

# Get your API key
api_key = os.getenv('ANTHROPIC_API_KEY') #Ask for help getting API key to upload

# Verify it loaded (but don't print the actual key!)
if api_key:
    print("✓ API key loaded successfully")
    print(f"Key starts with: {api_key[:15]}...")  # Just show the beginning
    
    # Create the client AFTER confirming the key is loaded
    client = anthropic.Anthropic(api_key=api_key)
    print("✓ Anthropic client created successfully")
    
else:
    print("✗ No API key found. Check your .env.txt file!")
    print("Make sure your .env.txt file contains:")
    print("ANTHROPIC_API_KEY=your_actual_key_here")




