<div align="center">

# 🧠 MultiAgents LLM Project  
### Local, Modular & Extensible AI Agent Framework

A fully modular Python framework for running, testing, and simulating multiple LLM-powered agents — **locally**, **offline**, and **without API keys**.  
Supports:
- Simulated OpenAI & Gemini agents  
- Local HuggingFace models  
- Real local models via **Ollama**  
- Unified async agent interface  

Perfect for **research**, **offline AI development**, **agent prototyping**, and **multi-agent experiments**.

</div>

---

# 📂 Folder Structure

```bash
MultiAgents/llm_project/
│
├── demo/
│   └── run_demo.py              # Shows all agent capabilities
│
├── src/
│   └── agent_clients.py         # Core agent implementations
│
├── tests/
│   └── test_agents.py           # Unit & integration tests
│
├── requirements.txt             # Dependencies (torch, transformers, etc.)
└── README.md                    # This documentation
```

---

# 💡 Key Features

### 🔷 1. Simulated Agents (Offline, No API Keys Needed)
- **OpenAI Agent (Simulated)**
- **Gemini Agent (Simulated)**  
Both generate realistic mock responses **without internet**.

### 🟡 2. Offline HuggingFace Models
Run LLMs (like **GPT-2**) using `transformers`.  
Ideal for offline experiments & local inference.

### 🟢 3. Real Local Models via Ollama
Supports **actual LLM inference** using:
```bash
ollama run tinyllama
```

### ⚙️ 4. One Unified Async Interface
All agents follow the same function pattern:
```python
await agent.generate_response("hello")
```

### 🚀 5. Modular & Extensible
Add new agents by:
- extending the base client  
- adding a function  
- updating the demo  

---

# 🧪 Demo Overview (`demo/run_demo.py`)

The demo runs all agents sequentially:

### 🔧 Demo functions
```python
async def demo_openai()         # Simulated OpenAI agent
async def demo_gemini()         # Simulated Gemini agent
async def demo_huggingface()    # Offline HuggingFace model
async def demo_ollama()         # Real local Ollama model
```

### 📌 Example Output
```
🔷 OpenAI Response: Simulated response from OpenAI for: Hello
🟣 Gemini Response: Simulated response from Gemini for: Hello
🟡 HuggingFace Response: Generated text from local GPT-2
🟢 Ollama Response: Real output from tinyllama
✅ Demo completed successfully
```

---

# ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/atharvvv10/MultiAgents.git
cd MultiAgents/llm_project
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

# ⚡ (Optional) Setup Ollama for Local LLMs

### Install Ollama (macOS/Linux/Windows)  
➡️ https://ollama.ai/download

### Pull a model (example: TinyLlama)
```bash
ollama pull tinyllama
```

---

# ▶️ Running the Demo

```bash
PYTHONPATH=. python demo/run_demo.py
```

You’ll see responses from:
- Simulated OpenAI  
- Simulated Gemini  
- Offline HuggingFace GPT-2  
- Local Ollama model  

---

# 📝 Agent Capabilities Summary

| Agent Type | Mode | Description |
|------------|------|-------------|
| **OpenAIAgent** | 🟩 Offline | Simulated OpenAI responses |
| **GeminiAgent** | 🟩 Offline | Simulated Gemini responses |
| **HuggingFaceAgent** | 🟨 Offline | Runs GPT-2 or any HF model |
| **OllamaAgent** | ⚡ Local | Real model inference via `ollama` |

---

# 🧩 How to Add a New Agent

1. Open `src/agent_clients.py`  
2. Create a new class:
```python
class MyNewAgent:
    async def generate_response(self, text):
        ...
```
3. Add the agent to `run_demo.py`  
4. Write tests under `tests/`

The framework is intentionally simple & extendable.

---

# 🚀 Contributing

We welcome contributions in:
- New agent types  
- Better demos  
- Test improvements  
- Integrating more local models  

### Steps:
1. Fork the repo  
2. Create a feature branch  
3. Add your improvements  
4. Submit a pull request  

If modifying major logic → PR moderation workflow will request **moderator approval**.

---

# ⭐ Credits

Built and maintained by **@atharvvv10**  
Part of the MultiAgents modular AI ecosystem.


