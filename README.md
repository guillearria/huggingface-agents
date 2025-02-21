# Hugging Face AI Agents 🤖

[![Course](https://img.shields.io/badge/Course-Hugging%20Face-yellow)](https://huggingface.co/courses/ai-agents/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

## 📋 Overview

This repository contains implementations of AI agents developed while following the Hugging Face AI Agents Course. The goal is to provide practical examples and implementations of various AI agents, showcasing different capabilities and use cases.

## 🔗 Important Links

- [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction)
- [Official Course Repository](https://github.com/huggingface/agents-course)

## 🤖 Implemented Agents

### 1. Serverless Agent (Jupyter Notebook)
Located in `agents/dummy_agent_library.ipynb`, this is our first implementation using Jupyter notebook. It demonstrates basic agent capabilities in a serverless environment.

### 2. Todo Agent
Located in `agents/todo_agent/app.py`, this is our first implementation using Hugging Face Spaces and Gradio. It should be able to add, edit, and delete simple todo items.

*More agents will be added as I progress through the course.*

## 📚 Course Content

### Unit 1: Introduction to AI Agents

#### 1. Understanding Agents
- What is an Agent, and how does it work?
- How do Agents make decisions using reasoning and planning?
- Core concepts and fundamental principles

#### 2. The Role of LLMs (Large Language Models)
- How LLMs serve as the "brain" behind an Agent
- Understanding the Messages system for structured conversations
- Integration of LLMs with agent architecture

#### 3. Tools and Actions
- Integration of external tools for environment interaction
- Building custom tools for specific agent capabilities
- Best practices for tool development

#### 4. The Agent Workflow
- Understanding the core loop: Think → Act → Observe
- Implementation of decision-making processes
- Handling feedback and adaptation

### Unit 2: To be Announced
*Stay tuned for updates on upcoming content!*

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Basic understanding of machine learning concepts
- Familiarity with Hugging Face's ecosystem
- Jupyter Notebook (for serverless agent)

### Environment Setup

#### For Jupyter Notebook Agent
1. Clone this repository:
```bash
git clone https://github.com/yourusername/huggingface-agents.git
cd huggingface-agents
```

2. Set up your environment variables:
   - Create a `.env` file in the `agents/` directory
   - Add your required environment variables (refer to notebook)

3. Open the notebook:
```bash
jupyter notebook agents/dummy_agent_library.ipynb
```

#### For Other Agents (Coming Soon)
1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt  # Note: Will be added as agents are implemented
```

## 📝 Project Structure

```
huggingface-agents/
├── README.md
└── agents/
    ├── dummy_agent_library.ipynb  # Serverless agent implementation
    ├── .env                       # Environment variables (not tracked in git)
    └── ...                        # Future agent implementations
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Implement new agents
- Improve existing implementations
- Add documentation
- Report issues

## 📄 License

This project is intended for educational purposes as part of the Hugging Face AI Agents Course.
