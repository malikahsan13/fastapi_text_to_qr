# 🔄 Text to QR Code Generator API

A robust and efficient RESTful API built with FastAPI that converts text content into QR code images. This service provides a simple yet powerful endpoint for generating QR codes on-the-fly, returning them as base64-encoded images for seamless integration with web and mobile applications.

## 🌟 Features

- **Instant QR Code Generation**: Convert any text input into high-quality QR codes
- **Base64 Encoding**: Returns QR codes as base64-encoded strings for easy frontend integration
- **CORS Enabled**: Cross-Origin Resource Sharing configured for seamless access from any domain
- **Input Validation**: Built-in validation to ensure non-empty text inputs
- **High Performance**: Built on FastAPI for lightning-fast async request handling
- **Customizable QR Parameters**: Configurable QR code version, box size, and border settings
- **Error Handling**: Comprehensive error responses with appropriate HTTP status codes

## 🚀 Tech Stack

- **Framework**: FastAPI 0.109.2
- **Server**: Uvicorn 0.27.1 (ASGI server)
- **QR Code Generation**: qrcode library
- **Data Validation**: Pydantic 2.6.1
- **Package Manager**: uv ( blazing fast Python package installer)
- **Python Version**: Python 3.8+

## 📡 API Endpoints

### POST /generate_qr

Generates a QR code from the provided text input.

**Request Body:**
```json
{
  "text": "Your text here"
}
```

**Response (Success - 200 OK):**
```json
{
  "qr_code": "iVBORw0KGgoAAAANSUhEUgAA..."
}
```

**Response (Error - 400 Bad Request):**
```json
{
  "error": "Text cannot be empty"
}
```

**cURL Example:**
```bash
curl -X POST "http://localhost:8000/generate_qr" \
     -H "Content-Type: application/json" \
     -d '{"text": "https://github.com"}'
```

**JavaScript/Fetch Example:**
```javascript
fetch('http://localhost:8000/generate_qr', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    text: 'Hello, World!'
  })
})
.then(response => response.json())
.then(data => {
  const img = document.createElement('img');
  img.src = `data:image/png;base64,${data.qr_code}`;
  document.body.appendChild(img);
});
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- uv package manager (recommended) or pip

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd fastapi_text_to_qr
```

### Step 2: Install Dependencies

#### Option A: Using uv (Recommended - Faster)

```bash
# Install uv if you haven't already (Windows)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Install uv if you haven't already (Linux/Mac)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

uv pip install -r requirements.txt
```

#### Option B: Using Traditional pip

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at: `http://localhost:8000`

### Step 5: Access Interactive API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📁 Project Structure

```
fastapi_text_to_qr/
│
├── main.py                 # Main application file with FastAPI app and endpoints
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── .gitignore            # Git ignore rules
```

## 🏗️ Architecture & Implementation Details

### Core Components

1. **FastAPI Application**: Main app instance with CORS middleware configuration
2. **QR Code Generator**: Utilizes the `qrcode` library for QR code creation
3. **Image Processing**: Converts QR codes to PNG format in memory
4. **Base64 Encoding**: Encodes binary image data for JSON transmission

### Key Features Implementation

- **Async/Await**: Leverages Python's async capabilities for efficient request handling
- **Memory Efficiency**: Uses `io.BytesIO()` for in-memory image processing
- **Input Sanitization**: Validates and sanitizes text input before QR generation
- **Error Handling**: Returns appropriate HTTP status codes and error messages

## 🔧 Configuration

### CORS Settings

The application is configured to accept requests from any origin with the following settings:

```python
allow_origins=["*"]
allow_credentials=True
allow_methods=["*"]
allow_headers=["*"]
```

**Note**: For production, restrict `allow_origins` to specific domains.

### QR Code Parameters

Default QR code generation parameters:
- **Version**: 1 (controls size)
- **Box Size**: 10 pixels
- **Border**: 5 modules
- **Fill Color**: Black
- **Background**: White

These can be customized in the [main.py:27-31](main.py#L27-L31) generate_qr function.

## 🚀 Usage Examples

### Python Example

```python
import requests
import base64
from PIL import Image
from io import BytesIO

# Generate QR code
response = requests.post(
    "http://localhost:8000/generate_qr",
    json={"text": "https://example.com"}
)

if response.status_code == 200:
    qr_data = response.json()["qr_code"]
    
    # Decode and save image
    img_data = base64.b64decode(qr_data)
    img = Image.open(BytesIO(img_data))
    img.save("qrcode.png")
    print("QR code saved successfully!")
```

### React Example

```jsx
import React, { useState } from 'react';

function QRGenerator() {
  const [text, setText] = useState('');
  const [qrCode, setQrCode] = useState('');

  const generateQR = async () => {
    const response = await fetch('http://localhost:8000/generate_qr', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });
    const data = await response.json();
    setQrCode(data.qr_code);
  };

  return (
    <div>
      <input 
        value={text} 
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter text"
      />
      <button onClick={generateQR}>Generate QR</button>
      {qrCode && <img src={`data:image/png;base64,${qrCode}`} alt="QR Code" />}
    </div>
  );
}
```

## 🔮 Future Enhancements

- [ ] Add support for custom QR code colors
- [ ] Implement QR code size customization
- [ ] Add error correction level options (L, M, Q, H)
- [ ] Rate limiting for API endpoints
- [ ] Authentication and API key management
- [ ] Docker containerization
- [ ] CI/CD pipeline setup
- [ ] Unit and integration tests
- [ ] Database logging for analytics
- [ ] Batch QR code generation
- [ ] QR code scanning/decoding endpoint
- [ ] Support for QR code logos/embedded images

## 🧪 Testing

Test the API using the built-in Swagger UI or with tools like:
- Postman
- cURL
- Thunder Client (VS Code extension)

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Malik Ahsan**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [qrcode](https://github.com/lincolnloop/python-qrcode) - QR code generation library
- [Uvicorn](https://www.uvicorn.org/) - Lightning-fast ASGI server

---

⭐ If you find this project helpful, consider giving it a star!
