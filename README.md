# bank-statements

## Overview

In an increasingly financially complex world, maintaining consistent logs is crucial. Whether it's a side hustle, a spouse, or a subscription, there are many moving parts to track. Having juggled multiple jobs since the age of 16, I've experienced firsthand how overwhelming it can be to manage the mountain of bank statements piling up month after month.

This tool aims to track your personal finances, allowing you to collect valuable data on your spending habits and patterns. It is designed to be compatible with multiple accounts and flexible enough to grow alongside your financial complexity.

Dealing with the massive, metaphysical megastructure that is our economy can be daunting, but having your own finances down to a science is one of the best defenses for as long as we live in a numerical world.

## Core Features

- **Drag-and-Drop Uploads**: Drop emailed PDF statements straight into the application.
- **Automated Parsing**: Intelligent statement parsing using LLM-based extraction pipelines.
- **Excel Output**: Structured export of transaction data into `.xlsx` files.
- **Async Job Queue**: Non-blocking, concurrent parsing of multiple statements.
- **Dockerized Deployment**: Full containerization for consistent local or cloud operation.
- **Clean, Minimalist UI** *(Planned)*: Drag-and-drop interface with simple transaction review.
- **Configurable Rules Engine** *(Planned)*: Define custom logic for how transactions should be categorized.
- **Account Summaries** *(Planned)*: Auto-generate simple analytics on spending, income, and trends.


## Tech Stack

- **Backend**: Python (FastAPI)
- **Frontend**: React (planned)
- **Parsing/Extraction**: PyMuPDF, pdfplumber, LangChain
- **Queueing**: Celery + Redis
- **Excel Export**: openpyxl or pandas
- **Containerization**: Docker


## Why?

I wanted a tool that wasn't bloated, ad-ridden, privacy-invasive, or subscription-locked. Just a personal, open, scalable system I could use and control — no weird third-party aggregators skimming my financial data.

---

## Getting Started (Planned)

> Coming soon: Docker Compose setup, environment configs, first example parsers.

---

## License

MIT License. Do what you want — but if you improve it, I'd love to see.

---

## Author

William Brodhead

---

*(first commit coming soon)*

---

> "Master your finances, or they will master you."