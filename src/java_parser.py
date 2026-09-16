import javalang

def parse_java_file(file_path: str) -> dict:
    
    with open(file_path, 'r', encoding='utf-8') as f:
        codigo = f.read()

    tree = javalang.parse.parse(codigo)
   
    info = {
        "class_name": None,
        "parameters": [],
        "public_methods": []
    }

    # name
    for path, node in tree.filter(javalang.tree.ClassDeclaration):
        info["class_name"] = node.name
        break 

    # parameters
    for path, node in tree.filter(javalang.tree.ConstructorDeclaration):
        #we only want the constructor with the most parameters, so we check if the current constructor has more parameters than the previous one
        actual_parameters = [param.type.name for param in node.parameters]
        if len(actual_parameters) > len(info["parameters"]):
            info["parameters"] = actual_parameters

    #methods
    for path, node in tree.filter(javalang.tree.MethodDeclaration):
        if node.modifiers and "public" in node.modifiers:
            info["public_methods"].append({
                "name": node.name,
                "parameters": [param.type.name for param in node.parameters]
            })

    return info