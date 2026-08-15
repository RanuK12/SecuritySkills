#!/bin/bash
# Claude Code/Cursor installation for security skills
npm install -g @openai/CLI @openai/cursor
# Initialize cursor with security model
cursor init --model gpt-4-turbo-0613 --security-skills-path ./skills
# Verify installation
cursor --version
