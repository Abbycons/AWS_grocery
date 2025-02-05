import os
from app import create_app
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = create_app()

if __name__ == '__main__':
    # Get host and port from environment variables or use defaults
    host = os.getenv('HOST', 'localhost')
    port = int(os.getenv('PORT', 8080))
    
    print(f"Starting server on {host}:{port}")
    app.run(debug=True, host=host, port=port)
