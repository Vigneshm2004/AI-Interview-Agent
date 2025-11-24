# Contributing to AI-Interview-Agent

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow

## How to Contribute

### 1. Fork the Repository

```bash
git clone https://github.com/Vigneshm2004/AI-Interview-Agent.git
cd AI-Interview-Agent
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/YourFeatureName
```

### 3. Set Up Development Environment

```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### 4. Make Your Changes

- Follow PEP 8 style guidelines
- Add docstrings to functions
- Keep commits atomic and descriptive

### 5. Test Your Changes

```bash
python interview_agent.py
# Test the feature manually
```

### 6. Commit and Push

```bash
git add .
git commit -m "Add feature: Description of your change"
git push origin feature/YourFeatureName
```

### 7. Create a Pull Request

- Provide clear description of changes
- Reference any related issues
- Include testing notes

## Areas for Contribution

### High Priority

- [ ] Additional interview roles
- [ ] Question difficulty levels
- [ ] Performance dashboard
- [ ] Database integration

### Medium Priority

- [ ] Multi-language support
- [ ] ATS integration
- [ ] Docker containerization
- [ ] Unit tests

### Low Priority

- [ ] Documentation improvements
- [ ] UI enhancements
- [ ] Analytics features

## Development Guidelines

### File Structure

```
AI-Interview-Agent/
├── interview_agent.py      # Main agent logic
├── requirements.txt        # Dependencies
├── .env.example           # Environment template
├── README.md              # Documentation
└── venv/                  # Virtual environment
```

### Code Style

- Use meaningful variable names
- Keep functions focused and small
- Add comments for complex logic
- Follow PEP 8 standards

### Testing

Before submitting:

1. Test role selection (1, 2, 3)
2. Test voice input (if available)
3. Test feedback generation
4. Verify `.env` is not committed

## Reporting Bugs

When reporting bugs, include:

- Python version
- OS (Windows/macOS/Linux)
- Steps to reproduce
- Expected vs actual behavior
- Error messages

## Feature Requests

Suggest features by opening an issue with:

- Clear description
- Use case/motivation
- Proposed implementation (optional)

## Questions?

Feel free to open a discussion or contact the maintainer.

---

**Thank you for contributing!** 🎉
