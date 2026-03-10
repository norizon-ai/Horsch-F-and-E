# Intranet Connector Configuration Guide

This document outlines how to configure the Intranet Connector service when deploying it as a container using Docker Compose or Kubernetes (Helm).

## Core Philosophy: Environment-Based Configuration

The connector is built on the principle of **separating configuration from code**. The application code is a generic engine, and its behavior is dictated entirely by configuration injected into it from the outside environment.

We use the Pydantic `BaseSettings` model, which means **every configuration parameter is controlled by an environment variable**. This is a standard and secure practice for containerized applications.

---

## 1. Docker Compose Configuration

For Docker Compose deployments, the easiest way to manage configuration is by using an `.env` file in the same directory as your `docker-compose.yml`.

### Step 1: Create an `.env` file

Create a file named `.env` and define your overrides in it.

```env
# .env

# --- Intranet Connector Configuration ---

# Change the crawling strategy to be exhaustive instead of smart
CRAWLER_STRATEGY=bfs

# Increase the crawl depth and page limit for a large intranet
CRAWLER_MAX_DEPTH=5
CRAWLER_MAX_PAGES=1000

# Customize the keywords for your specific business.
# Note: For lists, use a comma-separated string.
CRAWLER_RELEVANCE_KEYWORDS="internal-wiki,product-spec,sprint-review"

# Provide the secret auth token for your intranet
CRAWLER_AUTH_TOKEN="your-secret-auth-token-value"

# Only crawl pages under the /knowledge-base/ path
CRAWLER_URL_INCLUDE_PATTERNS="*/knowledge-base/*,*/handbook/*"
```

### Step 2: Reference in `docker-compose.yml`

Your `docker-compose.yml` file will automatically pick up the `.env` file from the same directory. You don't need to specify the variables again, making your Compose file clean and portable.

```yaml
# docker-compose.yml

version: '3.8'
services:
  intranet-connector:
    build: .
    # The 'env_file' directive is optional if the file is named '.env'
    # but is shown here for clarity.
    env_file:
      - .env
```

---

## 2. Kubernetes (Helm) Configuration

For Kubernetes, configuration is typically managed via a `values.yaml` file within a Helm chart. Helm translates these values into environment variables inside the Kubernetes Pod.

### Example `values.yaml`

A customer would edit the `values.yaml` file to configure their deployment.

```yaml
# values.yaml

# -- Intranet Connector Configuration
# These values will be mounted as environment variables in the pod.
connector:
  # -- Crawling strategy: "best_first", "bfs", or "dfs"
  strategy: "best_first"

  # -- Crawl depth and page limits
  maxDepth: 3
  maxPages: 500

  # -- Keywords for the 'best_first' scorer
  relevanceKeywords:
    - "engineering-handbook"
    - "postmortem"
    - "design-doc"

  # -- URL patterns to explicitly include
  urlIncludePatterns:
    - "*/wiki/*"
    - "*/guides/*"

  # -- Auth token for the intranet API
  # IMPORTANT: This should be stored in a Kubernetes Secret and referenced.
  # Do not store secrets in plain text in values.yaml.
  authToken: "your-secret-auth-token-value"

# In a real chart, you would use a secret like this:
# existingSecret: "name-of-your-k8s-secret"
# authTokenSecretKey: "intranet-token"
```

The Helm template for the Deployment (`templates/deployment.yaml`) would then use these values to populate the environment variables for the container.

---

## 3. Configuration Reference

This table lists all available environment variables that can be used to configure the Intranet Connector.

| Environment Variable             | Description                                                                                                 | Type          | Default Value                                                    |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------- | ---------------------------------------------------------------- |
| `CRAWLER_STRATEGY`               | The crawling strategy to use. Can be `best_first`, `bfs`, or `dfs`. `best_first` is recommended.              | `string`      | `best_first`                                                     |
| `CRAWLER_MAX_DEPTH`              | The maximum number of levels to crawl, starting from the initial page (depth 0).                            | `integer`     | `2`                                                              |
| `CRAWLER_MAX_PAGES`              | The absolute maximum number of pages to crawl in a single job.                                              | `integer`     | `100`                                                            |
| `CRAWLER_RELEVANCE_KEYWORDS`     | A comma-separated list of keywords used by the `best_first` scorer to prioritize URLs.                        | `string`      | `"guide,policy,documentation,project,report,onboarding,handbook"` |
| `CRAWLER_URL_INCLUDE_PATTERNS`   | A comma-separated list of wildcard URL patterns to include. If set, only URLs matching these patterns are crawled. | `string`      | `null` (not set)                                                 |
| `CRAWLER_AUTH_TOKEN`             | The secret bearer token used for making authenticated API calls to the intranet (e.g., for permissions).      | `string`      | `null` (not set)                                                 |

