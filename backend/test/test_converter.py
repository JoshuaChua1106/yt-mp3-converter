import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.converter import run_converter

# Test with a single video
test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 

print("--- Starting Converter ---")
success = run_converter(test_url, 'test_downloads')

if success:
    print("--- SUCCESS: MP3 is in the 'downloads' folder ---")
else:
    print("--- FAILED: Check the error message above ---")