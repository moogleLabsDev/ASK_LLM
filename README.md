# ASK_LLM

This project provides a platform for interacting with multiple large language models (LLMs) such as OpenAI, Gemini, Geema, Mistral, and more. It includes a web development portion to facilitate easy interaction with these models through a user-friendly interface.

## Overview

The platform allows users to:
- **Chat with Multiple LLMs**: Interact with various language models, each offering unique capabilities.
- **Web Interface**: A web application that provides a seamless experience for users to access and interact with different models.

## Features

1. **Multi-LLM Support**: 
   - Users can choose which LLM to interact with based on their needs.
   - Each model can be accessed via the web interface.

2. **Web Interface**:
   - User-friendly web interface for easy interaction with the models.
   - Responsive design for accessibility across devices.

3. **Session Management**:
   - Track and manage user sessions and interactions.
   - Store historical data for future reference and analytics.

## Getting Started

### Prerequisites

- Python 3.8+
- API keys for each LLM you plan to integrate (e.g., OpenAI, Gemini, Geema, Mistral)
- Database setup

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/Multi-LLM-Chat.git
   cd ASK_LLM
   ```

2. **Backend Setup:**
   - **Create a virtual environment and activate it:**
     ```sh
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
   - **Install backend dependencies:**
     ```sh
     pip install -r requirements.txt
     ```
   - **Set up environment variables:**
     Create a `.env` file in the root directory with necessary API keys and configuration.
   - **Run the backend server:**
     ```sh
     uvicorn Main:app --reload
     ```


