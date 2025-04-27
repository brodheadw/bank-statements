# bank-statements

**Bank Statements → Clean Excel Sheets, Automatically**

## Overview
**Bank-Statements** is a personal finance tool designed to simplify the painful task of logging, organizing, and analyzing your bank records.

In an increasingly financially complex world, maintaining consistent logs is critical. Whether it's tracking income from a side hustle, managing shared savings with a spouse, or supervising spending across multiple accounts, there are countless moving parts to stay on top of. Having juggled multiple jobs since the age of 16, I've struggled firsthand to wrangle the mountain of statements arriving month after month.

Dealing with the massive, metaphysical megastructure that is our economy can be overwhelming, so it is important to have your own finances down to a science for as long as we live in a numerical world.

This tool aims to make personal financial maintenance effortless: you simply drop your emailed bank statements into the application, and it automatically parses, categorizes, and logs them into a clean, standardized Excel spreadsheet.

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
