# Cold-Email-Generator

# Cold Email Generation Tool

An intelligent system that automates the creation of personalized cold emails for business outreach, leveraging advanced AI technologies and portfolio matching capabilities.

## Features

- **AI-Powered Email Generation**: Utilizes Groq LLM (Llama 3.3 70B) for intelligent, context-aware email content generation
- **Web Scraping**: Automatically extracts and analyzes job postings from career websites
- **Portfolio Matching**: Implements vector database using ChromaDB for efficient similarity search and portfolio matching
- **Structured Data Processing**: Uses pandas for efficient portfolio data management
- **Template-Based Generation**: Implements JSON parsing and template-based prompting for structured email generation
- **Temperature Control**: Fine-tuned response generation with controlled creativity levels

## Tech Stack

- **Language**: Python
- **AI/ML**: 
  - Groq LLM (Llama 3.3 70B)
  - LangChain
- **Database**: ChromaDB
- **Data Processing**: pandas
- **Web Scraping**: LangChain WebBaseLoader
- **Data Formats**: JSON

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cold-email-generation-tool.git
cd cold-email-generation-tool
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
export GROQ_API_KEY='your_groq_api_key'
```

## Usage

1. Prepare your portfolio data in CSV format (see `my_portfolio.csv` for reference)
2. Run the email generator:
```bash
python email_generator.py
```

## Project Structure

```
cold-email-generation-tool/
├── email_generator.py    # Main implementation file
├── projectdb.py         # Database operations
├── my_portfolio.csv     # Portfolio data
└── vectorstore/         # ChromaDB vector store
```

## How It Works

1. The system scrapes job postings from career websites
2. Extracts relevant information using LangChain and Groq LLM
3. Matches the job requirements with portfolio items using ChromaDB
4. Generates personalized cold emails based on the job description and matched portfolio items
5. Outputs the generated email content

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Groq for providing the LLM API
- LangChain for the framework and tools
- ChromaDB for vector database capabilities
