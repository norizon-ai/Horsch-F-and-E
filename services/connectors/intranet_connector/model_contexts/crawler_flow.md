Intranet Crawling Sequence Flow


  This flow details the step-by-step process from receiving a crawl job to publishing extracted content, focusing on leveraging Crawl4AI
  effectively as specified in the documentation.

  ---


  1. Job Reception and Initialization
   * The Intranet Connector service listens to the crawl.requested topic on the message bus.
   * Upon receiving a message with source_type: INTRANET, it acknowledges the message and parses the job details, extracting the start_url,
     domain, and any necessary authentication_credentials.


  2. Dynamic Crawler Configuration
   * Before starting the crawl, the service constructs a CrawlerRunConfig object tailored for the specific intranet job. This configuration is
     key to an efficient and targeted crawl.
   * Crawling Strategy: BestFirstCrawlingStrategy is selected. This is the ideal choice for an intranet, as it uses a scoring mechanism to
     prioritize exploring pages that are more likely to be relevant (e.g., documentation, guides) over less important content (e.g., old
     announcements, event calendars).
   * Streaming: The configuration will explicitly set stream=True. This is critical for performance and real-time processing, allowing the
     service to process and publish each page's content as it's discovered, rather than waiting for the entire crawl to complete.
     BestFirstCrawlingStrategy.
   * Filtering (Filter Chains): A FilterChain is created to ensure the crawler is efficient and stays within bounds:
       * `DomainFilter`: This is the most critical filter. It is configured with allowed_domains set to the intranet's domain from the job
         message, preventing the crawler from leaving the target site.
       * `ContentTypeFilter`: Configured to only allow text/html content. This prevents the crawler from wasting resources downloading binary
         files like PDFs, images, or zip archives.
       * `URLPatternFilter` (Optional but Recommended): Configured to exclude known low-value URL patterns, such as /calendar/, /users/, or
         /events/, further focusing the crawl on valuable knowledge content.


  3. Asynchronous Crawler Execution
   * The service instantiates the AsyncWebCrawler and calls await crawler.arun(start_url, config=config).
   * Because streaming is enabled, this call returns an asynchronous iterator. The service enters an async for result in ... loop to process
     each page's result as it becomes available.


  4. Per-Page Processing Loop
  For each result object yielded by the crawler:
   * Step 4a: Content Extraction: The service extracts the core information directly from the result object provided by Crawl4AI:
       * content = result.content
       * source_uri = result.url
       * metadata['title'] = result.metadata.get('title')
   * Step 4b: Permissions Fetching (Critical External Step): !!! TO BE IMPLEMENTED LATER !!!
       * The crawler's primary job is content extraction. As noted in the specification, fetching permissions is a separate, critical step.
       * Using the result.url, the connector makes a direct API call to the intranet's internal permissions or authorization endpoint (e.g.,
         https://intranet.api/permissions?page_url={result.url}). This is handled by the httpx library.
       * The permissions data (e.g., ["group:all-employees"]) is retrieved.
   * Step 4c: Data Merging and Formatting:
       * The content extracted by Crawl4AI (Step 4a) and the permissions fetched via the direct API call (Step 4b) are combined into a single
         JSON object, adhering to the content.raw.received message format specified in feature_specification.md.
   * Step 4d: Publish to Message Bus:
       * The final, formatted JSON object is published to the content.raw.received topic on the message bus for the next stage of the ingestion
         pipeline.


  5. Crawl Completion and Error Handling
   * The async for loop continues until the BestFirstCrawlingStrategy completes its run (e.g., max_depth or max_pages is reached, or no more
     valid links are found).
   * Error Handling: If any step within the loop fails for a specific page (e.g., the permission API call fails), the error is logged. The
     system will employ a retry mechanism for that specific page. If it repeatedly fails, the page URL is logged as a failure, but the overall
     crawl continues for other pages.
   * Job Completion: Once the crawl is finished, the service logs a final "Crawl Complete" message for the job and returns to listening for new
     messages. If the entire crawl job fails catastrophically, the original message is sent to a dead-letter queue for manual inspection.
