# Exa Prompting Best Practices

The Exa API is a neural search engine designed for LLMs. Unlike traditional keyword search engines, Exa understands meaning and semantics. To get the best results, you need to prompt it effectively.

## Core Principles

1.  **Phrasing for Neural Search**:
    - **Don't ask questions**: Instead of "What are the best marketing strategies?", phrase your query as the _answer_ or the _content_ you expect to find.
    - **Think "Autocomplete"**: Imagine you are writing a sentence that ends with the link you want.
    - **Bad**: "Who is the CEO of Anthropic?"
    - **Good**: "The current CEO of Anthropic is"

2.  **Use Autoprompt (`use_autoprompt: true`)**:
    - Exa has a built-in `autoprompt` feature (default is often true in libraries, but check specific tool implementation). It intelligently rewrites your query to be more effective for neural search.
    - **When to use**: Generally always, unless you have a highly specific, optimized query string.

3.  **Keyword vs. Neural Search**:
    - **Neural (default)**: Best for broad topics, exploring concepts, and finding answers to complex questions where phrasing varies. Use for: "strategic frameworks for SaaS growth".
    - **Keyword**: Best for finding specific names, identifiers, error codes, or exact quotes. Use for: "error 404 on /api/v1/login".

## Prompting Patterns

### Finding Lists & Collections

If you want a list of resources, prompt with a sentence describing a list.

- **Query**: "Here is a list of the top 10 CRM software providers for small businesses:"
- **Query**: "The best resources for learning semiotics in branding are:"

### Finding Discussion & Opinions

- **Query**: "discussion about the impact of AI on creative industries site:reddit.com"
- **Query**: "hacker news thread regarding new CSS features"

### Finding Companies/Competitors

- **Query**: "fast growing B2B SaaS startups in the healthcare space"
- **Job Titles**: "hiring for Head of Growth" (implies growth stage companies)

### Finding Academic/Technical Papers

- **Query**: "PDF research paper on transformer architecture efficiency"
- **Query**: "Abstract: deep reinforcement learning for robotic control"

## Filtering Strategies

Exa's power is multiplied when you combine neural search with filters.

- **`include_domains`**: Restrict search to high-quality sources.
  - `["nytimes.com", "wsj.com"]` for news.
  - `["github.com"]` for code.
  - `["arxiv.org"]` for papers.
- **`exclude_domains`**: Remove noise.
  - Exclude major social media if you want long-form content: `["twitter.com", "instagram.com"]`.
- **`start_published_date`**: Essential for "recent" or "news" related queries.
  - Use specific dates (e.g., "2023-01-01") to ensure freshness.

## Example Workflows for Research

### 1. Broad Exploration

- **Goal**: Understand a new market category.
- **Tool**: `exa_search` (type: neural)
- **Query**: "comprehensive guide to the generator maintenance market structure"

### 2. Targeted Fact Retrieval

- **Goal**: Find a specific statistic.
- **Tool**: `exa_search` (type: neural)
- **Query**: "The global market size for electric vehicles in 2024 was"

### 3. Finding Similar Content (`find_similar`)

- **Goal**: You found one perfect article, now you want more like it.
- **Action**: Take the URL of the perfect article.
- **Tool**: `exa_find_similar`
- **Input**: URL of the source article.

## Specialized Search Patterns

### Code Context (`get_code_context_exa`)

- **Goal**: Find implementation examples or libraries.
- **Best Practice**: Describe the coding problem, not just keywords.
- **Prompt**: "Here is a Python implementation of a RAG pipeline using LangChain:"
- **Filter**: `include_domains=["github.com", "stackoverflow.com", "huggingface.co"]`

### People Search (`people_search_exa`)

- **Goal**: Find experts or candidates.
- **Best Practice**: Describe the person's profile or bio.
- **Prompt**: "The LinkedIn profile of a Senior AI Engineer at OpenAI who specializes in reinforcement learning:"

### Company Research (`company_research_exa`)

- **Goal**: Market mapping.
- **Best Practice**: Describe the company description in a list format.
- **Prompt**: "List of Series B startups building AI agents for legal tech:"

### Deep Researcher (`deep_researcher_start`)

- **Goal**: Autonomous deep dive.
- **Best Practice**: Provide a broad, open-ended research goal.
- **Prompt**: "Investigate the current state of solid-state battery technology, covering key players, recent breakthroughs, and manufacturing challenges."
