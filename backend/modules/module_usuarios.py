def crear_usuario(nombre, email, plan):
    return {
        "nombre": nombre,
        "email": email,
        "plan": plan
    }

def obtener_usuario(email):
    return {"email": email, "plan": "Free"}
