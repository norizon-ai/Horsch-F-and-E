│ │ Implementation Plan: Complete Intranet Connector Pipeline                                                      │ │
│ │                                                                                                                │ │
│ │ Strategy: Incremental Integration with Comprehensive Testing                                                   │ │
│ │                                                                                                                │ │
│ │ Phase 1: Queue Integration & End-to-End Testing (Priority: HIGH)                                               │ │
│ │                                                                                                                │ │
│ │ 1.1 Integrate Publisher with Crawler                                                                           │ │
│ │                                                                                                                │ │
│ │ - Goal: Connect the existing DataPublisher to the crawler                                                      │ │
│ │ - Approach: Modify crawler.py to use the publisher instead of just yielding data                               │ │
│ │ - Why First: Establishes the core data flow and validates our publisher works with real data                   │ │
│ │                                                                                                                │ │
│ │ 1.2 Create Integration Test Suite                                                                              │ │
│ │                                                                                                                │ │
│ │ - Goal: Test the complete crawler → queue → ingestion worker flow                                              │ │
│ │ - Components:                                                                                                  │ │
│ │   - Local RabbitMQ Setup: Docker Compose for development testing                                               │ │
│ │   - Mock Queue Tests: Use existing MockPublisher for unit tests                                                │ │
│ │   - Real Queue Tests: End-to-end tests with actual RabbitMQ                                                    │ │
│ │   - Elasticsearch Integration: Test data reaches final destination                                             │ │
│ │ - Why Important: Catches integration issues early and provides confidence in deployments                       │ │
│ │                                                                                                                │ │
│ │ Phase 2: Service Integration Layer (Priority: MEDIUM)                                                          │ │
│ │                                                                                                                │ │
│ │ 2.1 Job Listener Implementation                                                                                │ │
│ │                                                                                                                │ │
│ │ - Goal: Subscribe to crawl.requested topic and trigger crawling jobs                                           │ │
│ │ - Approach: Create job consumer that parses crawl requests and initiates crawler                               │ │
│ │ - Integration: Use existing CrawlJob model from models/intranet_models.py                                      │ │
│ │                                                                                                                │ │
│ │ 2.2 Service Health & Monitoring                                                                                │ │
│ │                                                                                                                │ │
│ │ - Goal: Add FastAPI health endpoints and proper error handling                                                 │ │
│ │ - Components:                                                                                                  │ │
│ │   - Health check endpoints                                                                                     │ │
│ │   - Retry mechanisms with exponential backoff                                                                  │ │
│ │   - Dead letter queue handling                                                                                 │ │
│ │   - Logging and metrics collection                                                                             │ │
│ │                                                                                                                │ │
│ │ Phase 3: Production Readiness (Priority: LOW)                                                                  │ │
│ │                                                                                                                │ │
│ │ 3.1 Configuration Management                                                                                   │ │
│ │                                                                                                                │ │
│ │ - Goal: Environment-based configuration for different deployments                                              │ │
│ │ - Approach: Extend CrawlerSettings with queue and service configs                                              │ │
│ │                                                                                                                │ │
│ │ 3.2 Docker & Deployment                                                                                        │ │
│ │                                                                                                                │ │
│ │ - Goal: Containerized deployment with proper orchestration                                                     │ │
│ │ - Components: Docker Compose for local development, production deployment configs                              │ │
│ │                                                                                                                │ │
│ │ ---                                                                                                            │ │
│ │ Testing Strategy: Mock-First, Integration-Driven                                                               │ │
│ │                                                                                                                │ │
│ │ Unit Testing (Build on Existing)                                                                               │ │
│ │                                                                                                                │ │
│ │ - ✅ Keep existing mock publisher tests - they're well-designed                                                 │ │
│ │ - ✅ Expand crawler tests - test new publishing integration                                                     │ │
│ │ - ✅ Add configuration tests - validate all settings combinations                                               │ │
│ │                                                                                                                │ │
│ │ Integration Testing (New Priority)                                                                             │ │
│ │                                                                                                                │ │
│ │ - Local End-to-End: RabbitMQ + Elasticsearch in Docker                                                         │ │
│ │ - Mock Integration: Test components together with mocks                                                        │ │
│ │ - Performance Testing: Validate crawling performance with real queues                                          │ │
│ │                                                                                                                │ │
│ │ Development Workflow                                                                                           │ │
│ │                                                                                                                │ │
│ │ 1. Start with Mock Tests: Fast feedback loop for development                                                   │ │
│ │ 2. Validate with Integration Tests: Catch real-world issues                                                    │ │
│ │ 3. Manual Testing: Use existing ingestion worker for validation                                                │ │
│ │                                                                                                                │ │
│ │ ---                                                                                                            │ │
│ │ Why This Approach?                                                                                             │ │
│ │                                                                                                                │ │
│ │ ✅ Advantages:                                                                                                  │ │
│ │                                                                                                                │ │
│ │ - Low Risk: Build on proven components (crawler works, ingestion worker works)                                 │ │
│ │ - Fast Feedback: Mock tests enable rapid development iteration                                                 │ │
│ │ - Real Validation: Integration tests catch actual deployment issues                                            │ │
│ │ - Incremental: Each phase delivers working functionality                                                       │ │
│ │                                                                                                                │ │
│ │ ✅ Answers Your Questions:                                                                                      │ │
│ │                                                                                                                │ │
│ │ - Mock Ingestion Worker? → No need! It already exists and works                                                │ │
│ │ - Mock Queue? → Yes, but also real queue testing for comprehensive coverage                                    │ │
│ │ - How to Test? → Multi-layered approach from unit mocks to full integration                                    │ │
│ │                                                                                                                │ │
│ │ ---                                                                                                            │ │
│ │ Implementation Order:                                                                                          │ │
│ │                                                                                                                │ │
│ │ 1. Connect Publisher to Crawler (2-3 hours)                                                                    │ │
│ │ 2. Create Docker Test Environment (2-4 hours)                                                                  │ │
│ │ 3. Build Integration Test Suite (4-6 hours)                                                                    │ │
│ │ 4. Add Job Listener (3-4 hours)                                                                                │ │
│ │ 5. Production Polish (2-4 hours)                                                                               │ │
│ │                                                                                                                │ │
│ │ Total Estimate: 13-21 hours of focused development work.                                                       │ │
│ │                                                                                                                │ │
│ │ ---                                                                                                            │ │
│ │ Next Steps if Approved:                                                                                        │ │
│ │                                                                                                                │ │
│ │ 1. Start with crawler → publisher integration (immediate win)                                                  │ │
│ │ 2. Set up local RabbitMQ + Elasticsearch (enables real testing)                                                │ │
│ │ 3. Create comprehensive test suite (provides confidence for future changes)                                    │ │
│ │ 4. Iterate through remaining components (job listener, health endpoints)                                       │ │
│ │                                                                                                                │ │
│ │ This approach leverages existing working components while systematically filling the integration gaps with     │ │
│ │ proper testing at each step.      