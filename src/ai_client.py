from google import genai

def generate_test_code(parsed_info: dict, api_key: str) -> str:
    
    client = genai.Client(api_key=api_key)

    # Prepare parsed_info for the prompt 
    class_name = parsed_info.get("class_name")
    parameters = parsed_info.get("parameters")
    public_methods = parsed_info.get("public_methods")

    # Prompt for the AI model
    prompt = f"""
    You are an expert Java developer specialized in unit testing.
    Your task is to write the complete code for a JUnit 5 test class using Mockito.

    Here is the information for the class to be tested:
    - Class name: {class_name}
    - Parameters required by its constructor: {parameters}
    - Public methods to test: {public_methods}

    STRICT RULES:
    1. Analyze the "Parameters required". Create a @Mock ONLY for complex dependencies. For primitive types (int, boolean) or standard classes (String), manually inject reasonable test values.
    2. Use @InjectMocks if possible, or instantiate the class manually passing the mocks.
    3. Cover both success (happy path) and error cases.
    4. Apply the Given-When-Then pattern using the comments // Given, // When, // Then, WITH THE FOLLOWING EXCEPTIONS:
    - Exception tests: Merge When and Then within assertThrows.
    - Trivial/mathematical functions: Omit the comments if the test is resolved in a single line.
    - Parameterized tests (@ParameterizedTest): Omit the Given comment since data is injected.
    5. RETURN ONLY JAVA CODE. Do not include explanations or markdown blocks (```java). The output must be pure and compilable.
    """
    
    # Call Gemini API
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt
    )
    
    return response.text
