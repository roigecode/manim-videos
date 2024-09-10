
def encriptar(mensaje, e, n):
    return (mensaje**e) % n

def desencriptar(texto_cifrado, d, n):
    return (texto_cifrado**d) % n

if __name__ == '__main__':
    
    p = 61
    q = 53
    n = p*q
    e = 17
    d = 2753

    # Mensaje a enviar:
    m = 1994

    clave_publica = (e, n)
    clave_privada = (d, n)

    enc = encriptar(m, e, n)
    desc = desencriptar(enc, d, n)

    print(f"""\n
            Mensaje original: {m}\n
            Mensaje encriptado: {enc}\n
            Mensaje desencriptado {desc}\n
        """)