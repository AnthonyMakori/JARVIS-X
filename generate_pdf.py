from fpdf import FPDF

# Create PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", 'B', 16)

# Title
pdf.cell(0, 10, "JARVIS-X: Tony Stark Inspired Desktop AI Assistant", ln=True, align="C")
pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, "Author: Anthony Sanny", ln=True, align="C")
pdf.cell(0, 10, "Date: February 2026", ln=True, align="C")
pdf.ln(10)

# Sections content
sections = {
    "1. Overview": """JARVIS-X is a desktop-first AI assistant designed to Tony Stark’s J.A.R.V.I.S Level. It is fully local, privacy-focused, and modular, allowing users to interact with a smart AI that listens, speaks, and performs tasks autonomously.

The project leverages a local large language model (LLM) to understand commands and context, combined with a memory system to store short-term and long-term interactions.""",

    "2. Objectives": """- Provide a fully local, private AI assistant.
- Enable wake-word activated voice commands "Hey Jarvis".
- Allow autonomous decision-making through agent-based architecture.
- Implement system monitoring and proactive suggestions.
- Offer a modular and extensible framework for future expansion.""",

    "3. System Architecture": """Modules:
- Brain: Interfaces with local LLM to generate intelligent responses and context-aware outputs.
- Voice: Handles wake-word detection, speech-to-text conversion (Whisper), and text-to-speech (pyttsx3).
- Memory: Maintains both short-term (session) and long-term (database) memories for context.
- Agents: Specialized modules to perform autonomous tasks (SystemAgent, ResearchAgent, DevAgent).
- Tools: Provides system control commands (open apps, get system stats, file management).
- FastAPI API: Exposes endpoints for external integration and modular expansion.
- Plugins: Future module integration (IoT, trading, smart home, etc.).""",

    "4. Features": """- Wake-word Activation: “Hey Jarvis” triggers listening mode.
- Speech Interaction: Local STT and TTS allow conversational commands and feedback.
- Memory System: Stores previous commands and responses to maintain context.
- Autonomous Agents: JARVIS can take initiative, monitor system health, or proactively suggest actions.
- Modular & Expandable: Designed to easily integrate new agents, tools, and plugins.
- Proactive Monitoring: Alerts user when system performance is high or tasks need attention.""",

    "5. Workflow Example": """1. User says: "Hey Jarvis, open Chrome."
2. JARVIS detects wake word, converts speech to text.
3. LLM processes command, chooses the correct tool (open_app) or agent.
4. System executes action.
5. Response is saved in memory and spoken back to user.

Autonomous Example:
- JARVIS notices CPU is 90%
- Speaks: "CPU usage is high. Do you want me to close unused apps?""""",

    "6. Technical Details": """- Local LLM: Mistral 7B Instruct / Llama 3 8B quantized for CPU efficiency.
- Memory Storage: SQLite database.
- Voice Input: Porcupine wake word + Whisper for STT.
- Voice Output: pyttsx3 TTS engine.
- Agent Framework: Python classes allow multi-agent orchestration.
- FastAPI Backend: API endpoints for modular expansion and external integration.""",

    "7. Future Enhancements": """- Vision Module: Real-time screen analysis and document reading.
- Mobile Dashboard: Flutter app for remote interaction.
- Plugin Marketplace: Add new capabilities like smart home, crypto tracking, or trading bots.
- Advanced Agents: Multi-step autonomous workflows with reasoning.""",

    "8. Intended Final Functionality": """When complete, JARVIS-X will:
1. Listen & Respond — always-on wake-word detection and conversation.
2. Act Proactively — suggest optimizations, take system actions, monitor apps.
3. Reason with Context — remember past commands and conversations.
4. Manage Tasks & Data — research, summarize, edit code files, organize information.
5. Expand Easily — add plugins, new agents, or integrate mobile dashboards.
6. Operate Fully Locally — no internet dependency for core AI."""
}

# Add content to PDF
for section, text in sections.items():
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, section, ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 8, text)
    pdf.ln(5)

# Output PDF
pdf.output("JARVIS-X_Project_Overview.pdf")
print("PDF generated successfully: JARVIS-X_Project_Overview.pdf")
