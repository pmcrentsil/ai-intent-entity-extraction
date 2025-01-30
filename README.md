# Charter AI Intent Extraction

## Overview

This repository provides a **Proof of Concept (PoC)** for real-time **intent and entity extraction** from call transcripts using **Azure OpenAI (GPT-4o-mini)**. It simulates **multi-turn conversations**, dynamically extracts **predefined intents**, and outputs structured **JSON** results.

The PoC demonstrates how Charter can leverage **LLMs** to **dynamically identify intents** (set by the user) and **extract entities** (defined by the LLM). This allows for flexible intent recognition without the need for **predefined entity rules**.

---

## Features

- **Real-time multi-turn processing**: Simulates live call center interactions.  
- **Dynamic intent recognition**: Users specify intents dynamically via CLI.  
- **LLM-driven entity extraction**: No need for hardcoded entity rules.  
- **Azure OpenAI Integration**: Uses `gpt-4o-mini` for fast, efficient processing.  
- **Streaming Simulation**: Processes calls incrementally with delays to mimic real-time.  
- **JSON Output**: Returns structured data for easy downstream integration.  

---

## How It Works

1. **User defines intents & entities**:  
   - Intents: What kind of calls should be identified (e.g., `cancel service`, `billing issue`).
   - Entities: What information should be extracted (e.g., `customer_name`, `invoice_number`).

2. **Multi-turn conversation simulation**:  
   - Loads **predefined call transcripts** from `transcripts.py`.  
   - Each turn is processed with a **3-second delay** to mimic real-time conversation.  

3. **Processing via Azure OpenAI**:  
   - The system message defines the expected intents.  
   - The LLM **processes** the transcript incrementally.  
   - Extracted results are **formatted as JSON**.  

---

## Setup

### Prerequisites
- Python 3.8+
- Azure OpenAI Subscription
- `pip install -r requirements.txt`

### Configuration
Update `main.py` with your **Azure OpenAI API endpoint** and **API key**:

```python
azure_endpoint = "https://your-openai-endpoint.azure.com/"
api_key = "your-api-key"
