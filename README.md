# AI-Powered Business Outreach Tool

A sophisticated cold email generation system designed for service companies to streamline their business development outreach. This tool leverages cutting-edge AI to create personalized outreach emails by analyzing job postings and matching them with relevant portfolio items.

## Project Overview

The tool addresses a common business challenge: connecting service providers with companies seeking specialized talent. For instance, when a company like Nike posts a job opening for a Principal Software Engineer, service companies like AtliQ can use this tool to create targeted outreach emails that highlight their relevant expertise and portfolio.

## Key Features

- **Intelligent Job Analysis**: Automatically extracts and processes job listings from company career pages
- **AI-Powered Email Generation**: Uses Groq LLM (Llama 3.3 70B) to create contextually relevant email content
- **Portfolio Matching**: Implements ChromaDB vector database for intelligent matching of portfolio items with job requirements
- **Streamlit Interface**: User-friendly web interface for easy interaction
- **Template-Based Generation**: Structured email generation with customizable templates
- **Data Processing**: Efficient handling of portfolio data using pandas

## Technical Architecture

The system follows a modular architecture:
1. **Frontend**: Streamlit-based web interface
2. **Processing Layer**: 
   - Web scraping for job listings
   - Data extraction and processing
   - Portfolio matching using vector embeddings
3. **AI Layer**: Groq LLM integration for intelligent content generation
4. **Storage**: ChromaDB for vector-based portfolio storage

## Getting Started

### Prerequisites

- Python 3.8+
- Groq API key (available at [Groq Console](https://console.groq.com/keys))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/business-outreach-tool.git
cd business-outreach-tool
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
Create a `.env` file in the app directory and add:
```
GROQ_API_KEY=your_api_key_here
```

### Running the Application

Start the Streamlit interface:
```bash
streamlit run app/main.py
```

## Project Structure

```
business-outreach-tool/
├── app/
│   ├── main.py           # Streamlit application
│   └── .env             # Environment variables
├── email_generator.py    # Core email generation logic
├── projectdb.py         # Database operations
├── my_portfolio.csv     # Portfolio data
└── vectorstore/         # ChromaDB vector store
```

## Usage Example

1. Enter the target company's careers page URL
2. The system automatically:
   - Extracts job listings
   - Matches relevant portfolio items
   - Generates a personalized outreach email
3. Review and customize the generated email as needed

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Groq for providing the LLM API
- LangChain for the framework and tools
- Streamlit for the web interface
- ChromaDB for vector database capabilities
