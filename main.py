from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import qrcode
import io
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_method=["*"],
    allow_headers=["*"]
)


@app.post("/generate_qr")
async def generate_qr(request: Request):
    data = await request.json()
    text = data.get("text", "")

    if not text.strip():
        return JSONResponse({"error": "Text cannot be empty"}, status_code=400)

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")

    qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return {"qr_code": qr_base64}
