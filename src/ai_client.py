from google import genai

def generate_test_code(parsed_info: dict, api_key: str) -> str:
    
    client = genai.Client(api_key=api_key)

    # Prepare parsed_info for the prompt 
    class_name = parsed_info.get("class_name")
    parameters = parsed_info.get("parameters")
    public_methods = parsed_info.get("public_methods")

    # Prompt for the AI model
    prompt = f"""
    Eres un desarrollador experto en Java especializado en pruebas unitarias.
    Tu tarea es escribir el código completo de una clase de test para JUnit 5 usando Mockito.

    Aquí tienes la información de la clase a testear:
    - Nombre de la clase: {class_name}
    - Parámetros requeridos por su constructor: {parameters}
    - Métodos públicos que debes testear: {public_methods}

    REGLAS ESTRICTAS:
    1. Analiza los "Parámetros requeridos". Crea un @Mock SOLO para las dependencias complejas. Para tipos primitivos (int, boolean) o clases estándar (String), inyecta valores de prueba razonables manualmente.
    2. Usa @InjectMocks si es posible, o instancia la clase manualmente pasando los mocks.
    3. Cubre casos de éxito (happy path) y de error.
    4. Aplica el patrón Given-When-Then usando los comentarios // Given, // When, // Then, CON LAS SIGUIENTES EXCEPCIONES:
    - Tests de excepciones: Fusiona el When y Then dentro de assertThrows.
    - Funciones triviales/matemáticas: Omite los comentarios si el test se resuelve en una sola línea.
    - Tests parametrizados (@ParameterizedTest): Omite el Given ya que los datos se inyectan.
    5. DEVUELVE ÚNICAMENTE CÓDIGO JAVA. No incluyas explicaciones ni bloques de markdown (```java). El output debe ser puro y compilable.
    """
    
    # Call Gemini API
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt
    )
    
    return response.text
