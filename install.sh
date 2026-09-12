#!/bin/bash
# Installation script for Anthropic Cybersecurity Skills
# Makes the skill available for Claude Code and Cursor

set -e

REPO_URL="https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git"
TARGET_DIR="$HOME/anthropic-cybersecurity-skills"
SKILLS_DIR="$HOME/.claude/skills"
SKILL_NAME="anthropic-cybersecurity-skills"

echo "Cloning the repository..."
if [ -d "$TARGET_DIR" ]; then
  echo "Directory $TARGET_DIR already exists. Updating..."
  git -C "$TARGET_DIR" pull --ff-only
else
  git clone "$REPO_URL" "$TARGET_DIR"
fi

echo "Installing skill to Claude Code/Cursor..."
mkdir -p "$SKILLS_DIR"
# Copy the .claude-plugin directory (which contains plugin.json and marketplace.json)
cp -r "$TARGET_DIR/.claude-plugin" "$SKILLS_DIR/$SKILL_NAME"

echo "Installation complete!"
echo "To use the skill, restart Claude Code or Cursor."
echo "The skill is now available at: $SKILLS_DIR/$SKILL_NAME"
echo "You can verify by checking that the following file exists:"
echo "  $SKILLS_DIR/$SKILL_NAME/plugin.json"