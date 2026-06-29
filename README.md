# 🧠 Research-Mind

## Overview

Research-Mind is a **Multi-Agent AI Research System** that automates the research process using multiple AI agents. The system searches the web, extracts relevant information from webpages, generates a structured research report, and evaluates the report using a dedicated critic agent.

The project is built using **LangChain**, **OpenAI**, **Tavily Search API**, **BeautifulSoup**, and **Streamlit**.

---

## Features

* Multi-Agent Architecture
* AI-powered Web Research
* Intelligent Webpage Content Extraction
* Automated Research Report Generation
* AI-based Report Evaluation
* Interactive Streamlit User Interface
* Modular and Extensible Design

---

## System Workflow

```text
User Query
     │
     ▼
Search Agent
     │
     ▼
Web Search (Tavily)
     │
     ▼
Reader Agent
     │
     ▼
BeautifulSoup Scraper
     │
     ▼
Writer Chain
     │
     ▼
Research Report
     │
     ▼
Critic Chain
     │
     ▼
Final Report + Feedback
```

---

## Project Components

### 🔍 Search Agent

* Built using `create_react_agent`
* Uses the Tavily Search Tool
* Searches the web for relevant sources based on the user's query

### 📖 Reader Agent

* Built using `create_react_agent`
* Uses the URL Scraper Tool
* Extracts clean, readable content from webpages using BeautifulSoup

### ✍️ Writer Chain

Implemented using LangChain Expression Language (LCEL):

```python
prompt | llm | StrOutputParser()
```

Responsibilities:

* Combines collected research
* Organizes information
* Generates a detailed research report

### 📝 Critic Chain

Implemented using LCEL:

```python
critic_prompt | llm | StrOutputParser()
```

Responsibilities:

* Reviews the generated report
* Assigns a quality score
* Provides feedback and suggestions for improvement

---

## Tools

### Web Search Tool

* Tavily Search API
* Retrieves relevant search results

### URL Scraper Tool

* BeautifulSoup
* Extracts readable webpage content
* Removes unnecessary HTML elements

---

## Technologies Used

* Python
* LangChain
* OpenAI API
* Tavily API
* BeautifulSoup
* Streamlit
* Requests

---

## Future Improvements

* PDF Report Export
* Source Citations
* Multi-source Verification
* RAG Integration
* Conversation Memory
* Multi-LLM Support

