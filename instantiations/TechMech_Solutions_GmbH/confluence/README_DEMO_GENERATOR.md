# Confluence Demo Generator

Generate realistic fictional Confluence pages for trade fair demos using OpenAI.

## Overview

This tool generates a complete fictional Confluence space structure for **TechMech Solutions GmbH**, a fictional German automation company. It creates 50+ realistic technical documentation pages in German across 8 different spaces (Engineering, Projects, Compliance, Quality, Service, Meetings, IT, HR).

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Your OpenAI API Key

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Or pass it directly via command line (see below).

### 3. Generate the Confluence Pages

```bash
python generate_confluence.py --api-key "your-api-key-here"
```

This will:
- Parse `confluence_structure.md`
- Generate realistic German content for each page using `gpt-4o-mini`
- Save all pages to `generated_confluence/` folder organized by space

## Usage Options

### Basic Usage

```bash
python generate_confluence.py --api-key "sk-..."
```

### Custom Options

```bash
python generate_confluence.py \
  --api-key "sk-..." \
  --model "gpt-3.5-turbo" \
  --structure "./custom_structure.md" \
  --output "./my_confluence" \
  --limit 10
```

### Command Line Arguments

- `--api-key` (required): Your OpenAI API key
- `--model` (optional): OpenAI model to use (default: `gpt-4o-mini`)
  - Recommended: `gpt-4o-mini` (cheap and fast)
  - Alternative: `gpt-3.5-turbo` (cheaper but lower quality)
- `--structure` (optional): Path to structure file (default: `confluence_structure.md`)
- `--output` (optional): Output directory (default: `generated_confluence/`)
- `--limit` (optional): Limit number of pages (useful for testing)

## Output Structure

The generator creates the following folder structure:

```
generated_confluence/
├── ENG/              # Engineering Space
│   ├── Engineering_-_Home.md
│   ├── Produktlinien.md
│   ├── RoboCell_RC-3000_Serie.md
│   └── ...
├── PRJ/              # Projects Space
│   ├── Projects_-_Home.md
│   └── ...
├── CMP/              # Compliance Space
├── QM/               # Quality Management Space
├── SRV/              # Service Space
├── MTG/              # Meetings Space
├── IT/               # IT & Software Space
└── HR/               # HR & Admin Space
```

Each page includes:
- Metadata (title, space, parent page, hierarchy level)
- Realistic German technical content
- Proper Confluence-style formatting

## Cost Estimation

Using `gpt-4o-mini` for ~150 pages:
- Estimated cost: $0.10 - $0.30 USD
- Generation time: 5-10 minutes

Using `gpt-3.5-turbo`:
- Even cheaper, but content quality may vary

## Testing the Generator

To test with just a few pages:

```bash
python generate_confluence.py --api-key "sk-..." --limit 5
```

This generates only the first 5 pages, useful for testing before full generation.

## Generated Content

Each page contains realistic German technical documentation including:
- Technical specifications
- Process descriptions
- Standards and guidelines
- Meeting notes
- Project documentation
- Compliance information
- Quality procedures

The content is contextually appropriate for the page title and parent hierarchy.

## Integration with Confluence Connector

After generation, you can:

1. **Point your connector** to the `generated_confluence/` folder
2. **Index the content** as if it were a real Confluence space
3. **Demonstrate search and retrieval** capabilities at the trade fair

## Customization

### Modify the Structure

Edit `confluence_structure.md` to add/remove pages or spaces, then regenerate.

### Adjust Content Style

Modify the `ContentGenerator.generate_content()` method in `generate_confluence.py` to change:
- Content length
- Technical depth
- Language style
- Formatting preferences

### Change Company Context

Update the `company_context` in the `ContentGenerator` class to generate content for a different fictional company.

## Troubleshooting

### "OpenAI API Error"
- Check your API key is valid
- Ensure you have credits in your OpenAI account
- Try a different model if rate limited

### "File not found"
- Make sure you're running from the `demo_confluence_assistant/` directory
- Or provide full paths to `--structure` and `--output`

### Content in Wrong Language
- The generator is designed for German content
- Modify the prompt in `ContentGenerator` for other languages

## License

For internal demo use only.
