import scanner #librería a utilizar para scannear puertos

# Ejemplo de función
ports = scanner.getOpenPorts("http://www.google.com", [0-8080])
print("Open ports:", ports)
