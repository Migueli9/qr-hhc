import qrcode
import uuid
import os
from flask import Flask, redirect, abort, request

FORMS_URL = "https://forms.gle/aiUnyHzVRGQQPonY9"

app = Flask(__name__)

ultimo_token = str(uuid.uuid4())

def generar_token():
    global ultimo_token
    ultimo_token = str(uuid.uuid4())

def generar_token():
    global ultimo_token
    ultimo_token = str(uuid.uuid4())

@app.route("/")
def home():
    generar_token()
    link_temporal = f"{request.host_url}forms/{ultimo_token}"
    return f"""
    <h2>QR HHC Activo</h2>
    <p>Link actual:</p>
    <p>{link_temporal}</p>
    """

@app.route("forms/<token>")
def acceder_forms(token):
    global ultimo_token

    if token == ultimo_token:
        generar_token()
        return redirect(FORMS_URL)
    else:
        return abort(403, "QR expirado")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

