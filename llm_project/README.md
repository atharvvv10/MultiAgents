# 🧠 MultiAgents LLM Project — Local AI Agent Framework

The **MultiAgents LLM Project** is a modular Python framework designed to run, test, and simulate multiple LLM-powered agents in one place. It supports offline operation for HuggingFace models, simulated LLM clients for OpenAI and Gemini, and real local models through Ollama. Perfect for experimentation, research, and development without needing API keys or constant internet access.

---

## 📂 Folder Structure
```bash
MultiAgents/llm_project/
├── demo/ # Example scripts to showcase agent capabilities
│ └── run_demo.py
├── src/ # Core agent implementations
│ └── agent_clients.py
├── tests/ # Unit & integration tests
│ └── test_agents.py
├── requirements.txt # Dependencies (torch, transformers, etc.)
└── README.md # Documentation
```


---

## 💡 Features

- **Simulated Agents**: OpenAI and Gemini agents can generate mock responses without API calls.  
- **Offline HuggingFace Models**: Run models like GPT-2 locally using `transformers`.  
- **Real Local Models**: Integrate and run Ollama agents for actual LLM inference locally.  
- **Unified Interface**: Interact with all agents through a consistent async framework.  
- **Extensible**: Easily add new agents or models as needed.

---

## 🧪 Demo Overview (`demo/run_demo.py`)

The demo runs all agents sequentially:

```bash
async def demo_openai():           # Simulated OpenAI responses
async def demo_gemini():           # Simulated Gemini responses
async def demo_huggingface():      # Offline HuggingFace model
async def demo_ollama():           # Real local Ollama model
Example output:

pgsql
Copy code
🔷 OpenAI Response: Simulated response from OpenAI for: Hello
🟣 Gemini Response: Simulated response from Gemini for: Hello
🟡 HuggingFace Response: Generated text from local GPT-2
🟢 Ollama Response: Real AI output from tinyllama
✅ Demo completed successfully
```
## ⚙️ Setup & Installation
Clone the repository

```bash
Copy code
git clone https://github.com/atharvvv10/MultiAgents.git
cd MultiAgents/llm_project
Install dependencies
```
```bash
Copy code
pip install -r requirements.txt
Setup Ollama (optional, for real local agents)
```
Install Ollama: Download

Pull a model:

```bash
Copy code
ollama pull tinyllama
```
## ▶️ Running the Demo
```bash
-Copy code
-PYTHONPATH=. python demo/run_demo.py
-Observe responses from all agents (simulated, offline, or real).

Easily switch between agents or add new ones in src/agent_clients.py.
```

## 📝 Agent Capabilities Overview

OpenAIAgent -✅ Offline	Simulated responses, no API calls <br>
GeminiAgent -✅ Offline	Simulated responses, no API calls <br>
HuggingFaceAgent -✅ Offline	Runs local transformer models (GPT-2, etc.) <br>
OllamaAgent	-⚡ Local	Real model inference via Ollama CLI <br>

## 🚀 Contributing
1.Fork the repo and create a feature branch.

2.Add or improve agent clients, demos, or tests.

3.Submit a PR with clear description and tests.
