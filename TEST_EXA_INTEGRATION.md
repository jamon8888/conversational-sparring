# Exa Integration Test Plan

## Prerequisites
✅ strategic-research-sparring plugin installed
✅ Exa MCP server configured in .mcp.json
✅ Plugin enabled in ~/.claude/settings.json

## Step 1: Restart Claude Code
```bash
# Exit current session and restart Claude Code CLI
# Navigate to this directory
cd ~/Documents/test/conversational-sparring
```

## Step 2: Verify MCP Server is Loaded
When Claude Code starts, it should show:
```
Loading MCP server: exa
```

## Step 3: Test Basic Plugin Functionality
```bash
# Show sparring dashboard
/sparring

# Set a research goal
/sparring goal "Research AI search engines competitive landscape"
```

Expected output:
```
Strategic Objective set: Research AI search engines competitive landscape
Category: research | Impact: 7
Goal ID: abc123
```

## Step 4: Test Exa Search Integration

Ask Claude to use Exa for research:
```
Use Exa to search for recent developments in AI search engines
```

This should trigger the exa-search-expert skill, which will use tools like:
- web_search_exa
- web_search_advanced_exa
- deep_search_exa

## Step 5: Test Deep Research
```
Start a deep research session on "competitive analysis of Perplexity vs Google AI Overview"
```

This should:
1. Activate strategic-research-orchestrator skill
2. Use exa-search-expert for searches
3. Use comparative-analyzer for analysis
4. Synthesize findings with research-synthesizer

## Expected Exa Tools Available

Check that these MCP tools are available:
- ✅ web_search_exa
- ✅ web_search_advanced_exa
- ✅ deep_search_exa
- ✅ crawling_exa
- ✅ get_code_context_exa
- ✅ company_research_exa
- ✅ people_search_exa
- ✅ deep_researcher_start
- ✅ deep_researcher_check

## Troubleshooting

### If MCP server doesn't load:
```bash
# Check .mcp.json is valid
cat .mcp.json

# Verify exa-mcp-server package is accessible
npx -y exa-mcp-server --version
```

### If plugin commands don't work:
```bash
# Check plugin is enabled
cat ~/.claude/settings.json | grep strategic-research

# Verify plugin files exist
ls ~/.claude/plugins/strategic-research-sparring/
```

### If Exa tools return errors:
- Verify API key is correct: `95b61053-4dad-40ec-87e6-5760d8b1fdc2`
- Check API quota at https://exa.ai/dashboard
- Test API directly:
```bash
curl -X POST https://api.exa.ai/search \
  -H "x-api-key: 95b61053-4dad-40ec-87e6-5760d8b1fdc2" \
  -H "Content-Type: application/json" \
  -d '{"query": "AI search engines", "numResults": 3}'
```

## Success Criteria

✅ Plugin commands work (/sparring)
✅ Exa MCP tools are available
✅ Can perform neural searches via Exa
✅ Strategic research skills activate properly
✅ Research synthesis works end-to-end

## Next Steps After Success

1. Explore other research skills:
   - `/sparring domains` - See available research domains
   - Market analysis
   - Opportunity scoring
   - Scenario modeling

2. Set up research workflows:
   - Competitive analysis pipelines
   - Market intelligence gathering
   - Technology landscape mapping

3. Customize domain configs:
   - Add custom research patterns
   - Define research workflows
   - Set up knowledge repositories
