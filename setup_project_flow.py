import os

# Define your base project name
PROJECT_NAME = "my_agent_bot"

# Define folder structure
folders = [
    f"{PROJECT_NAME}/docs",
    f"{PROJECT_NAME}/config",
    f"{PROJECT_NAME}/src",
    f"{PROJECT_NAME}/src/routes",
    f"{PROJECT_NAME}/src/agent",
    f"{PROJECT_NAME}/src/agent/tools",
    f"{PROJECT_NAME}/src/agent/knowledge",
    f"{PROJECT_NAME}/src/services",
    f"{PROJECT_NAME}/src/data",
    f"{PROJECT_NAME}/src/models",
    f"{PROJECT_NAME}/src/utils",
    f"{PROJECT_NAME}/src/tests/unit",
    f"{PROJECT_NAME}/src/tests/integration",
    f"{PROJECT_NAME}/migrations",
    f"{PROJECT_NAME}/docker",
    f"{PROJECT_NAME}/ci-cd",
    f"{PROJECT_NAME}/logs"
]

# Define files to be created (path + optional default content)
files = {
    f"{PROJECT_NAME}/README.md": f"# {PROJECT_NAME}\n\nAgentic-based AI bot project structure.",
    f"{PROJECT_NAME}/requirements.txt": "# Add Python dependencies here\n",
    f"{PROJECT_NAME}/.gitignore": "logs/\n__pycache__/\n.env\n*.pyc\n",
    f"{PROJECT_NAME}/config/default.yaml": "env: development\nlogging: true\n",
    f"{PROJECT_NAME}/config/production.yaml": "env: production\nlogging: true\n",
    f"{PROJECT_NAME}/config/secrets.template.env": "# TEMPLATE\nOPENAI_API_KEY=\nDB_URI=\n",
    f"{PROJECT_NAME}/docs/architecture.md": "# Architecture Overview\n",
    f"{PROJECT_NAME}/docs/design_decisions.md": "# Design Decisions\n",
    f"{PROJECT_NAME}/src/main.py": "def main():\n    print('Starting Agentic Bot...')\n\nif __name__ == '__main__':\n    main()\n",
    f"{PROJECT_NAME}/src/app.py": "from fastapi import FastAPI\napp = FastAPI()\n\n@app.get('/')\ndef root():\n    return {'message': 'Agentic Bot Running!'}\n",
    f"{PROJECT_NAME}/src/routes/api.py": "# Define API routes here\n",
    f"{PROJECT_NAME}/src/agent/brain.py": "# Orchestration and decision engine logic\n",
    f"{PROJECT_NAME}/src/agent/memory.py": "# Memory management logic\n",
    f"{PROJECT_NAME}/src/agent/planner.py": "# Multi-step planning logic\n",
    f"{PROJECT_NAME}/src/agent/tools/tool_base.py": "# Base class for tools\n",
    f"{PROJECT_NAME}/src/agent/tools/external_api_tool.py": "# Example API tool integration\n",
    f"{PROJECT_NAME}/src/agent/tools/db_access_tool.py": "# Example DB access tool\n",
    f"{PROJECT_NAME}/src/agent/knowledge/retriever.py": "# RAG retrieval logic\n",
    f"{PROJECT_NAME}/src/agent/knowledge/knowledge_base.py": "# Knowledge base management\n",
    f"{PROJECT_NAME}/src/services/user_service.py": "# Example user-related services\n",
    f"{PROJECT_NAME}/src/services/auth_service.py": "# Authentication-related logic\n",
    f"{PROJECT_NAME}/src/services/logging_service.py": "# Logging and telemetry logic\n",
    f"{PROJECT_NAME}/src/data/ingestion.py": "# Data ingestion scripts\n",
    f"{PROJECT_NAME}/src/data/preprocessor.py": "# Preprocessing logic for training or inference\n",
    f"{PROJECT_NAME}/src/models/llm_wrapper.py": "# Wrapper around LLM models (OpenAI, HF, etc)\n",
    f"{PROJECT_NAME}/src/utils/config_loader.py": "# Config file loading logic\n",
    f"{PROJECT_NAME}/src/utils/helpers.py": "# Utility helper functions\n",
    f"{PROJECT_NAME}/docker/Dockerfile": "FROM python:3.10-slim\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\nCMD ['python', 'src/main.py']\n",
    f"{PROJECT_NAME}/docker/docker-compose.yaml": "version: '3.8'\nservices:\n  app:\n    build: .\n    ports:\n      - '8000:8000'\n",
    f"{PROJECT_NAME}/ci-cd/pipeline.yaml": "# CI/CD pipeline configuration\n",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"✅ Created folder: {folder}")

# Create files
for filepath, content in files.items():
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"📝 Created file: {filepath}")

print("\n🎉 Project structure created successfully!")
