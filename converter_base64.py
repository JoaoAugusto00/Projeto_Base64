import base64

def converter_para_base64(texto):
    
    texto_bytes = texto.encode('utf-8')
    
    base64_bytes = base64.b64encode(texto_bytes)
    
    base64_string = base64_bytes.decode('utf-8')
    return base64_string

if __name__ == "__main__":
    texto_original = input("Digite a string que deseja converter para Base64: ")
    resultado = converter_para_base64(texto_original)
    print(f"String em Base64: {resultado}")