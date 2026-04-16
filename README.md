# AI Resume Screening System

## Overview
This project is an AI-powered Resume Screening System built using Python and LangChain.

## Features
- Skill Extraction
- Resume vs Job Matching
- Scoring (0–100)
- Explainable Output

## Pipeline
Resume → Extraction → Matching → Scoring → Explanation

## Approach
Due to limitations in local LLM performance, a hybrid approach was used:
- Extraction, Matching, and Scoring implemented using deterministic logic
- LangChain used for pipeline structuring

## Results
The system successfully evaluates candidates as:
- Strong candidate → High score
- Average candidate → Medium score
- Weak candidate → Low score

## Debugging
Initially, LLM-based extraction produced noisy outputs.
This was resolved by implementing rule-based extraction.

## How to Run
```bash
python main.py