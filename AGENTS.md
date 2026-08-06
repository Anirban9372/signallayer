# SignalLayer - Developer Context

## What We're Building
Automated BSE (Bombay Stock Exchange) corporate 
announcement sentiment analysis system.

BSE publishes 200-500 PDF announcements daily covering:
mergers, earnings, board changes, regulatory filings.
Professional quant funds trade on these within milliseconds.
Small funds can't afford manual analysis teams.

SignalLayer's value: parse every announcement automatically,
classify sentiment (bullish/bearish/neutral), 
deliver structured JSON signals to quant fund clients.

## Who Is Writing This Code
Anirban - second year IT, IIEST Shibpur.
Strong math background (JEE Advanced level).
Knows: Python, C, basic ML, logistic regression.
Currently learning: neural networks.
Style: writes code himself, wants explanations for 
every suggested change. Never just generate — always teach.

## Architecture Decisions (and why)

### PDF Parsing: docling
BSE PDFs contain complex tables, embedded figures,
multi-column layouts. PyPDF2 and pdfplumber fail on these.
docling (IBM Research) converts them to clean markdown
preserving table structure. Critical for financial data.

### Vector Storage: Chroma
Lightweight, runs locally, no separate server process.
Good for our announcement volume (~500/day).
Upgrade to Weaviate only when scaling to multiple clients.

### Inference: Gemini Pro API (free tier)
No local GPU available (AMD Radeon 610M integrated only).
Gemini free tier: 1M context window, structured outputs
via instructor library. Sufficient for sentiment classification.
Upgrade to paid only when fund clients are paying us.

### Orchestration: smolagents
Minimal framework (1000 lines total).
Easy to understand internals - important since Anirban
wants to understand everything he runs.

## Code Style Rules
- Always explain WHY before suggesting a change
- Prefer simple readable code over clever one-liners  
- Every function must have a docstring explaining purpose
- Never use libraries without explaining what they do
- Flag any performance bottleneck immediately

## Current Status
Environment setup phase. Active development starts
in 2-3 weeks after neural networks learning phase.

## What NOT To Do
- Don't generate large code blocks without explanation
- Don't use libraries not in the tech stack without justification
- Don't skip error handling
- Don't store API keys in code files

## My Background
Second year IT student, IIEST Shibpur, third semester(just started this july).
Completed: Summer Analytics 2026 (IITG) — logistic regression 
through transformers, ensemble modeling, NHANES hackathon.
Currently learning: Deep Learning (NPTEL + Karpathy Zero to Hero)
College courses this semester: FL&A, OOP, DSA
C programming done. Moving to C++.
Starting SignalLayer development in 2-3 weeks.
