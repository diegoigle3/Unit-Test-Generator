import sys
import os

from java_parser import parse_java_file
from ai_client import generate_test_code
from test_writer import save_test_file

def main():
    # 1. Validate command line arguments
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <path_to_java_file>")
        sys.exit(1)

    # 2. Extract the file path
    file_path = sys.argv[1]

    # 3. Retrieve the API Key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set")
        sys.exit(1)

    # 4. Orchestrate the flow
    try:
        print(f"Parsing file: {file_path}")
        parsed_info = parse_java_file(file_path)

        print("Generating test code with Gemini...")
        raw_code = generate_test_code(parsed_info, api_key)
        
        print("Saving test file...")
        class_name = parsed_info.get("class_name")
        saved_path = save_test_file(raw_code, class_name)
    
        print(f"Success! Test generated at: {saved_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()