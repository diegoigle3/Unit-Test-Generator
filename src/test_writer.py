import os

def save_test_file(raw_code: str, class_name: str) -> str:

    output_dir = "output"
    file_name = f"{class_name}Test.java"
    full_path = os.path.join(output_dir, file_name)

    
    os.makedirs(output_dir, exist_ok=True)

    # Clean the markdown formatting from the AI response
    clean_code = raw_code.replace("```java\n", "").replace("```java", "").replace("```", "").strip()

    # Write the clean code to the file safely
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(clean_code)
    
    return full_path