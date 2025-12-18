🧠 Multi-Step Reasoning Agent with Self-Checking
Overview

This project implements a GenAI reasoning agent that solves structured word problems using a multi-step reasoning process and verifies its own answers before responding to the user.

The agent is designed to provide correct final answers with brief explanations, without exposing full internal chain-of-thought.

Problem Scope

The agent handles:

Arithmetic and logical reasoning

Time and duration calculations

Constraint-based decision problems

Input is a plain text question, and output is a structured response indicating success or failure.

Agent Design

The solution follows a three-phase pipeline:

Planner – Analyzes the question and creates a step-by-step plan

Executor – Performs the required reasoning and calculations

Verifier – Validates the solution and triggers retries if needed

This design improves reliability and reduces reasoning errors.

Key Features

Multi-step reasoning

Self-verification before final output

Retry mechanism on failed checks

Clear separation of planning, execution, and verification logic

Technology

Python

Large Language Model (LLM) API or mock interface

Modular prompt and agent design

Usage

The agent can be run via:

Command line interface

Notebook function

Simple API endpoint

The focus is on agent logic rather than UI.

Author

R Muralidharan
B.Tech – Instrumentation & Control Engineering, NIT Trichy
GitHub: https://github.com/Muralidharan-ramachandran
