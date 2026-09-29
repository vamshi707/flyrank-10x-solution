# FlyRank 10x Solution

## Problem

Customers need a simple way to discover products and get quick AI-assisted support.

This project combines product APIs, persistent data, authentication, caching, and an AI support classifier into one backend system.

## 10x Claim

The goal is to make product discovery and support decisions 10x easier and faster through a single integrated backend.

## Core Features

1. User authentication
2. Product management and search
3. Database-backed product storage
4. Cached product results
5. AI-powered support classification

## Required Concepts

| Concept | Where it lives |
|---|---|
| API endpoints | `backend/main.py` |
| Database | `backend/database.py` |
| Authentication | `backend/auth.py` |
| Caching | `backend/cache.py` |
| LLM integration | `backend/llm.py` |

No swaps were used.

## Project Structure

```text
flyrank-10x-solution/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── auth.py
│   ├── cache.py
│   ├── llm.py
│   ├── seed.py
│   ├── requirements.txt
│   ├── .gitignore
│   └── logs/
│
├── My 10x Solution - Vamshi Lavudya.md
└── README.md