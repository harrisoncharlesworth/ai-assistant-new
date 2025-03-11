# AI Assistant

A modern, scalable AI assistant built with FastAPI, featuring real-time communication, advanced NLP capabilities, and multi-model support.

## Features

- 🤖 Multi-model AI support (GPT-4, Claude, etc.)
- 🚀 Real-time WebSocket communication
- 🔄 Streaming responses
- 🎯 Context-aware conversations
- 🔌 Plugin system
- 🔐 Enterprise-grade security
- 📊 Usage analytics and monitoring

## Tech Stack

- FastAPI for high-performance async API
- PostgreSQL for persistent storage
- Redis for caching and real-time features
- Docker for containerization
- Kubernetes for orchestration
- Prometheus & Grafana for monitoring

## Installation

```bash
# Clone the repository
git clone https://github.com/harrisoncharlesworth/ai-assistant-new.git
cd ai-assistant-new

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration
```

## Development

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run development server
uvicorn src.main:app --reload

# Run tests
pytest

# Run linting
flake8 src tests

# Run type checking
mypy src
```

## Project Structure

```
ai-assistant-new/
├── src/
│   ├── api/           # API endpoints
│   ├── core/          # Core business logic
│   ├── models/        # Data models
│   ├── services/      # External service integrations
│   └── utils/         # Utility functions
├── tests/             # Test suite
├── docs/              # Documentation
│   ├── api/           # API documentation
│   └── architecture/  # Architecture diagrams
└── deployment/        # Deployment configurations
    ├── docker/        # Docker configurations
    └── k8s/           # Kubernetes manifests
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
