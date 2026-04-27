# B.Tech CSE (II YEAR – IV SEM) (2025-26)
# DEPARTMENT OF COMPUTER SCIENCE ENGINEERING & APPLICATIONS SPECIALIZATION IN ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING
# GLA UNIVERSITY
# 17km Stone, NH-2, Mathura-Del Road, P.O. Chaumuhan, Mathura – 281406 (Uttar Pradesh) India

---

## Project Title: Ai -driven smart procurement and spend optimization intelligence platform

**Team Leader:** Mehul chaudhary UR: 2415500292  
**Team Member 1:** Aditya Singh UR: 2415500035  
**Team Member 2:** Mehul Chaudhary Singh UR: 2415500292  
**Team Member 2:** Amit Kumar UR: 2415500061  
**Mentor Name:**Sir Preshit Desai 
**Signature:** _________________________

---

## Project Synopsis: Ai -driven smart procurement and spend optimization intelligence platform

### Cover
- **Project title:** Ai -driven smart procurement and spend optimization intelligence platform
- **Team number:** 23
- **Institute / Course:** GLA University, Mini-Project
- **Version:** v1.0
- **Date:** 28 Feb 2026

---

## 1. Overview

### Problem statement:
Individual investors struggle with real-time market analysis, emotional decision-making, and lack personalized, accessible trading guidance. Professional tools are expensive and complex.

### Goal:
Build an AI agent that delivers personalized stock market insights, trade recommendations, and risk alerts tailored to individual risk profiles and goals.

### Non-goals:
Autonomous trading execution, regulatory filings, or institutional-grade risk modeling in v1.

### Value proposition:
Conversational AI advisor with personalized profiling, real-time market monitoring, and emotion-aware guidance—accessible to beginners and experts alike.

---

## 2. Scope and Control

### 2.1 In-scope
- User profile creation and risk assessment
- Real-time stock market data analysis
- AI-driven buy/hold/sell recommendations
- Conversational advisory interface
- Portfolio tracking and performance insights
- Risk alerts and volatility notifications

### 2.2 Out-of-scope
- Live trading execution
- multi-asset class support (crypto/commodities)
- mobile apps
- advanced portfolio optimization in v1.

### 2.3 Assumptions
- Users have basic knowledge of stock markets
- Market data APIs provide reliable real-time data
- Users act responsibly on AI suggestions

### 2.4 Constraints
- Limited historical data availability
- API usage limits
- Academic project timeline

### 2.5 Dependencies
- Stock market data APIs
- News and sentiment analysis sources
- Cloud infrastructure for AI processing

### 2.6 Acceptance criteria and sign-off

**Acceptance Criteria:**
- GIVEN a user profile WHEN preferences are saved THEN personalized recommendations are generated
- GIVEN market volatility WHEN risk exceeds threshold THEN alerts are triggered
- System must generate responses within acceptable latency

**Sign-off table:**

| Stakeholder | Role | Decision area | Signature/Approval | Date |
|-------------|------|---------------|-------------------|------|
| Mr. Preshit Desai | Mentor | Scope, final acceptance | Approved | 05 Feb 2025 |
| Akshay Singh Chauhan | Product Lead | Release readiness | Approved | 04 Feb 2026 |

---

## 3. Stakeholders and RACI

| Activity | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|----------|------------------|------------------|---------------|--------------|
| Requirements | Divya Raj Varshney | Akshay Singh Chauhan | Mentor | Team |
| Design | Divya Raj Varshney & Manish Pratap Singh | Divya Raj Varshney & Manish Pratap Singh | Mentor | Team |
| Implementation | Akshay Singh Chauhan | Akshay Singh Chauhan | — | Team |
| Testing | Manish Pratap Singh | Akshay Singh Chauhan | Mentor | Team |
| Release | Manish Pratap Singh | Manish Pratap Singh | Mentor | Dept |

---

## 4. Team and Roles

| Member | Role | Responsibilities | Key skills | Availability | Contact |
|--------|------|------------------|------------|--------------|---------|
| Divya Raj Varshney | Product Lead | Scope, backlog, reviews | Product, APIs | 8 hrs/wk | divya.raj_cs.aiml23@gla.ac.in |
| Akshay Singh Chauhan | Tech Lead & Backend | Arch, APIs, security | Node, Express, SQL, WebSockets | 10 hrs/wk | akshay.chauhan_cs.aiml23@gla.ac.in |
| Akshay Singh Chauhan | Frontend | React UI, state, a11y | React, TS | 10 hrs/wk | akshay.chauhan_cs.aiml23@gla.ac.in |
| Manish Pratap Singh | QA & Docs | Test plan, E2E, docs | Playwright, writing | 8 hrs/wk | manish.singh_cs.aiml23@gla.ac.in |

---

## 5. Week-wise Plan and Assignments

| Week | Dates | Milestones | Akshay (Lead) | Akshay (Backend) | Manish (Frontend) | Divya (QA/Docs) | Deliverables | Status |
|------|-------|------------|------------------|------------------|------------------|------------------|--------------|--------|
| 1 | 1–7 Feb | Requirements freeze | Finalize scope | API contracts v0 | Wireframes | Test plan v0 | Draft SRS | Planned |
| 2 | 8–14 Feb | Architecture & DB | Arch review | Schema & migrations | UI kit | Test data | ERD, API spec v1 | Planned |
| 3 | 15–21 Feb | Backend scaffolding | Risks, unblock | Auth + Users API | Auth screens | Smoke tests | Auth module | Planned |
| 4 | 22–28 Feb | Frontend scaffolding | Sync | Listings API | Routing, forms | Accessibility checks | UI shells | Planned |
| 5 | 29 Sep–5 Fer Mar | Feature set A | Cut scope | Create/Edit listing E2E | Listing pages | CRUD tests | Feature A demo | Planned |
| 6 | 6–12 Mar | Feature set B | KPIs | Search API | Search UI + Profile | Perf tests | Feature B demo | Planned |
| 7 | 13–19 Mar | Hardening | Risk burn down | Bug fixes | Bug fixes | Regression suite | Test report | Planned |
| 8 | 20–26 Mar | Release & deck | Final sign-off | Release notes | Polish UI | User manual | v1.0, slides | Planned |

---

## 6. Users and UX

### 6.1 Personas
- **Beginner Investor:** Needs simple explanations and low-risk guidance
- **Active Trader:** Wants fast insights and technical indicators

### 6.2 Top User Journeys
User → Login → Set investment preferences → View market insights → Receive AI recommendations → Track portfolio

### 6.3 User Stories
As an investor, I want personalized trading suggestions so that I can make informed decisions without emotional bias.

### 6.4 Accessibility & Localization
- Simple language explanations
- Mobile-friendly interface
- English language support

---

## 7. Market and Competitors

### 7.1 Competitor table

| Competitor | Product | Target users | Key features | Pricing | Strengths | Weaknesses | Our differentiator |
|------------|---------|--------------|--------------|---------|-----------|------------|-------------------|
| TradingView | Advanced charting platform | Active traders, technical analysts | Interactive charts, 100+ indicators, screeners, social trading ideas, custom alerts | Freemium (Pro: $14.95/mo) | Professional-grade tools, 50M+ users, real-time data, strong community | Steep learning curve, overwhelming for beginners, generic alerts | Personalized conversational AI explains charts in plain language |
| Seeking Alpha | Investment research + news | Retail investors, long-term holders | Stock ratings, earnings transcripts, analyst articles, portfolio tracking, dividend tools | Freemium (Premium: $239/yr) | Expert opinions, comprehensive data, dividend focus | Information overload, paywall for best content, no real-time signals | Emotion-aware recommendations + real-time conversational guidance |
| Robinhood | Commission-free trading app | Millennial/Gen Z retail traders | Fractional shares, crypto trading, 24/7 trading, simple execution, basic news | Free (Gold: $5/mo) | Easy execution, gamified UX, popular with young users | Limited research tools, past outages, regulatory fines, no advisory layer | AI advisory companion with risk profiling vs execution-only focus |

### 7.2 Positioning
TradeMind AI focuses on personalized, conversational, and explainable AI-based trading advice.

**Measurable Delta:**
- Median listing time: ≤90s vs 3–5 min (general sites)
- Recommendation speed: ≤3s vs 24–48h (advisors)
- Trust factor: Campus-verified peers vs anonymous users

---

## 8. Objectives and Success Metrics

- **O1:** Onboarding - Median signup + email verify < 60s by 15 Feb 2026 (KPI: median seconds)
- **O2:** Search performance - p95 search latency ≤ 1s by 25 Feb 2026 (KPI: p95 ms)
- **O3:** Listing completion - ≥ 80% of started listings published by 05 Mar 2026 (KPI: completion rate)
- **O4:** Accessibility - 0 AA issues on core flows by release (KPI: a11y violations)

---

## 9. Key Features

| Feature | Description | Priority | Dependencies | Acceptance criteria |
|---------|-------------|----------|--------------|---------------------|
| Personalized Profiling | Builds a customized user profile based on risk tolerance, financial goals, investment horizon, and trading style | Must | SMTP | GIVEN a user completes the risk and goal questionnaire WHEN the profile is saved THEN personalized recommendations are generated successfully. |
| Market Monitoring | Continuously tracks real-time stock prices, trends, indicators, and relevant market signals. | Must | Auth, Storage | GIVEN a tracked stock WHEN market data updates THEN the latest price and trend are displayed within 10 seconds. |
| AI Trade Suggestions | Provides buy, hold, or sell recommendations with clear reasoning and risk explanation. | Must | Listings | GIVEN a stock query WHEN the user requests advice THEN the system returns a recommendation with explanation within 5 seconds. |
| Risk Alerts | Sends alerts for high volatility, price drops, or risk threshold breaches. | Should | Auth | GIVEN increased volatility WHEN risk exceeds limits THEN an alert notification is sent to the user. |
| Portfolio Insight and Tracking | Displays portfolio performance, diversification, and profit/loss analysis. | Could | Auth | GIVEN a user opens the portfolio dashboard WHEN data loads THEN accurate performance metrics are shown. |

---

## 10. Architecture

### 10.1 High-Level Architecture
The system follows a modular and scalable architecture designed to support real time data processing and personalized AI-driven advisory.

- **Clients:** Web-based Single Page Application (SPA) developed using React. The client provides dashboards, charts, and a conversational interface for user interaction.
- **Backend Services:**
  - Authentication Service: Handles user registration, login, and secure access.
  - Profile Service: Manages user risk profiles, investment goals, and preferences.
  - Market Analysis Service: Fetches and processes real-time and historical market data.
  - Recommendation Engine: Generates personalized buy/hold/sell suggestions using AI models.
- **Data Stores:**
  - MySQL Database: Stores user data, investment profiles, portfolios, and logs.
  - Object Storage: Stores charts, reports, and backtesting results if required.
- **Integrations:**
  - Market Data APIs (Yahoo Finance / Alpha Vantage)
  - LLM Provider (OpenAI / Groq)
  - SMTP service for alerts and notifications

### 10.2 API spec snapshot

| Endpoint | Method | Auth | Purpose | Request schema | Response schema | Codes |
|----------|--------|------|---------|----------------|-----------------|-------|
| /api/auth/register | POST | — | Create account | email, password | 201 {id} | 201, 400 |
| /api/profile/create | POST | JWT | Create investment profile | riskLevel, goals | 201 {listingId} | 201, 400, 401 |
| /api/market/analyze | GET | - | Analyze stock | symbol, timeframe | 200 {items[], total} | 200 |

### 10.3 Configuration and Secrets
- Environment variables managed using .env files
- Sensitive credentials are Git-ignored
- API keys rotated periodically
- Access restricted to authorized CI/CD pipelines.

---

## 11. Data Design

### 11.1 Core Entities
- **User:** Basic user information and authentication
- **Investment Profile:** Risk tolerance, goals, and preferences
- **Stock:** Stock metadata and market data
- **Portfolio:** User's investment holdings
- **Recommendation:** AI-generated trading suggestions

User data is securely stored with encryption and strict access control.

### 11.1 Data dictionary

| Entity | Field | Type | Null? | Allowed values | Source | Notes |
|--------|-------|------|-------|----------------|--------|-------|
| User | id | UUID | No | — | System | PK |
| User | email | String | No | RFC 5322 | User | Unique |
| InvestmentProfile | riskLevel | Enum | No | Low/Medium/High | User | PK |
| Stock | symbol | String | No | NSE/BSE codes | Market API | Indexed |
| Portfolio | totalValue | Decimal | No | ≥ 0 | System | — |

### 11.2 Schemas and Migrations
- ER Diagram included in appendix
- Database migrations version-controlled
- Rollback tested on staging environment

### 11.3 Privacy, Retention, Backup, and DR
- **Personally Identifiable Information (PII):** name, email
- **Retention policy:** delete inactive accounts after 12 months
- **Nightly automated backups**
- **RTO:** 4 hours
- **RPO:** 24 hours

---

## 12. Technical Workflow Diagrams
The following diagrams are included to explain system behavior:
- State Transition Diagram
- Sequence Diagram
- Use Case Diagram
- Data Flow Diagram (DFD)
- Entity Relationship Diagram (ERD)
- System Architecture Diagram

---

## 13. Quality: NFRs and Testing

### 13.1 Non-functional requirements

| Metric | SLI | Target (SLO) | Measurement |
|--------|-----|--------------|-------------|
| Availability | Uptime % | ≥ 99.0% | Uptime monitor |
| Latency | p95 | ≤ 1000 ms | APM |
| Error rate | 5xx % | ≤ 1% | Logs |
| Security | Critical CVEs | 0 | Vulnerability scanner |

### 13.2 Test plan

| Area | Type | Tools | Owner | Coverage target | Exit criteria |
|------|------|-------|-------|-----------------|---------------|
| Backend | Unit | Jest | Akshay | 70% | No P1/P2 defects |
| UI | E2E | Playwright | Manish | 60% | Pass rate ≥ 95% |
| API | Integration | Postman | Divya | All Scenarios | All critical pass |

### 13.3 Environments
- Development → Staging → Production
- Feature flags used for experimental features

---

## 14. Security and Compliance

### 14.1 Threat model (STRIDE)

| Asset | Threat | STRIDE | Impact | Likelihood | Mitigation | Owner |
|-------|--------|--------|--------|------------|------------|-------|
| Auth tokens | Theft | Spoofing | High | Medium | HTTPS, short TTL, rotation | Rohit |
| User data | SQLi | Tampering | High | Low | Parameterized queries, WAF | Rohit |

### 14.2 AuthN/AuthZ
- Email + password authentication
- JWT-based authorization
- Role-based access control

### 14.3 Audit and logging
- Log signups, logins, listing CRUD, reports; 90-day retention.

### 14.4 Compliance
- Academic project; follow institute policy; no third-party data sharing.

---

## 15. Delivery and Operations

### 15.1 Release plan
- Version v1.0 demo at project submission
- Incremental feature rollout

### 15.2 CI/CD and rollback
- CI pipeline: lint → test → build → deploy
- Rollback using previous container image

### 15.3 Monitoring and alerting

| Metric | Threshold | Alert to | Runbook |
|--------|-----------|----------|---------|
| p95 latency | > 1200 ms | Tech Lead | "API Latency" runbook |
| Error rate | > 2% | Tech Lead | "Error Spike" runbook |

### 15.4 Runbooks
- **API Latency:** check DB indexes → scale pods → revert change.
- **Error Spike:** inspect logs → roll back → create incident note.

### 15.5 Communication plan
- Standups Mon/Wed/Fri. Weekly status to mentor each Friday. Bi-weekly demo.

---

## 16. Risks and Mitigations

### 16.1 Risk heatmap

| Risk | Probability | Impact | Score | Mitigation | Owner | Status |
|------|-------------|--------|-------|------------|-------|--------|
| Schedule slip | Medium | High | 12 | Scope freeze, weekly demos | Akshay | Open |
| API Downtime | Medium | Medium | 9 | Indexes, EXPLAIN, caching | Akshay | Open |
| Model bias | Low | Medium | 6 | Size limits, compression | Akshay | Open |

---

## 17. Research and Evaluation

### 17.1 Study of Existing Platforms
Platforms like Zerodha Kite, Groww, Yahoo Finance, and TradingView offer rich market data and charting tools but lack personalized AI-driven advice. Users must interpret raw data themselves, which can overwhelm beginners. Emotional bias mitigation and explainable AI are limited. This motivated TradeMind AI, a conversational, personalized trading companion.

### 17.2 Evaluation Using Historical Data
TradeMind AI was backtested on historical stock data across bullish, bearish, and sideways markets. AI recommendations were compared with past prices to assess accuracy, adaptability, and risk management.

### 17.3 User Feedback
Students and simulated investors provided feedback on AI clarity, ease of interaction, trustworthiness, and overall experience. Feedback guided improvements in recommendation logic and usability.

### 17.4 KPI Tracking
Key metrics include response time (p95), recommendation accuracy, user engagement, and system uptime. Regular monitoring ensures reliability and continuous improvement.

---

## 18. Appendices

### 18.1 Glossary
- **AI:** Systems simulating human intelligence.
- **KPI:** Metrics measuring performance.
- **SLO:** Target service performance.
- **p95:** 95th percentile response time.

### 18.2 References
- Yahoo Finance: https://finance.yahoo.com
- Alpha Vantage: https://www.alphavantage.co
- NSE India: https://www.nseindia.com
- React: https://react.dev
- MDN Web Docs: https://developer.mozilla.org
- Scikit-learn: https://scikit-learn.org
- Trading AI Articles: https://towardsdatascience.com
- IEEE: "Machine Learning in Financial Markets" – https://ieeexplore.ieee.org
- Springer: "AI-Based Stock Trading Systems" – https://link.springer.com

---

**End of Project Synopsis**
