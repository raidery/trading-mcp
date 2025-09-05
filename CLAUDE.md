# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based trading MCP (Model Coordination Protocol) server that provides Chinese A-share market data analysis tools. The project uses the `akshare` library for financial data access and the `mcp` framework for creating an MCP server.

## Key Files and Structure

- `main.py`: Basic entry point with a simple "Hello World" function
- `mcp_server.py`: Main MCP server implementation using FastMCP
- `mcp/`: Directory containing utility functions
- `mcp/utils.py`: Logging setup and utility functions
- `pyproject.toml`: Project dependencies and metadata
- `requirements.txt`: Python dependencies (openai)
- `.cursorrules`: Development guidelines following agentic coding principles

## Commands for Development

### Install Dependencies
```bash
pip install -e .
```
or
```bash
pip install -r requirements.txt
```

### Run the Server
```bash
python mcp_server.py
```

### Run the Basic Entry Point
```bash
python main.py
```

## Architecture Overview

The project implements an MCP server using the FastMCP framework. The server provides tools for Chinese A-share market data analysis. The main components are:

1. **MCP Server (`mcp_server.py`)**: 
   - Initializes a FastMCP application
   - Provides system instructions for Chinese A-share market analysis
   - Implements an "echo" tool as an example
   - Runs on host 0.0.0.0, port 8999

2. **Utilities (`mcp/utils.py`)**:
   - Contains logging setup functions
   - Provides a `setup_logging` function for application logging

3. **Dependencies**:
   - `akshare`: For Chinese financial market data access
   - `mcp[cli]`: For MCP server functionality
   - `openai`: For OpenAI API integration

## Development Guidelines

Follow the agentic coding principles outlined in `.cursorrules`, which emphasize:
1. Starting with simple solutions
2. Designing at a high level before implementation
3. Frequent human feedback and clarification
4. Keeping implementations simple and avoiding complex features initially