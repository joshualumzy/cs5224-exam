# L02 — Concepts and Models (NIST)

Source: `Lecture 02 - Concepts and Models.pdf` (slides 3–47). Past-paper mapping verified against the papers.

---

## Scenario Plan (12 scenarios)

| # | Topic | Slides | Format | Past-paper link | Status |
|---|-------|--------|--------|-----------------|--------|
| 1 | Choosing SaaS / PaaS / IaaS (+ lift-and-shift, MySQL/RDS vs LAMP) | 8–17 | Production scenario | 2425S2 Q1, Q3, Q7; 2526S1 Q2, Q13, Q19; 2526S2 Q2, Q4, Q19 | ✅ |
| 2 | Responsibility split + pros/cons table (control vs responsibility, lock-in, privacy) | 19–20 | Production scenario | 2526S2 Q9; 2425S2 Q2, Q18 | ✅ |
| 3 | NIST 5 essential characteristics + 5/4/3 framework | 3–4 | Application scenario (no pure recall) | 2425S2 Q2, Q16 | ✅ |
| 4 | Service model variants (FaaS, DBaaS, StorageaaS etc.) and FaaS fit | 18 | Production scenario | 2425S2 Q19; 2526S1 Q1, Q4; 2526S2 Q7, Q12 | ✅ |
| 5 | Combining IaaS + PaaS + SaaS (data-residency example) | 14–15, 17 | Application scenario | 2526S2 Q24 | ✅ |
| 6 | Reference architecture: five actors + provider types + reference-model purpose | 21–27 | Application scenario (no pure recall) | — | ✅ |
| 7 | Cloud Broker: intermediation / aggregation / arbitrage | 34 | Production scenario | 2526S1 Q10 | ✅ |
| 8 | Service orchestration, cloud service management, portability, security/privacy (PI/PII) | 28–31 | Application scenario (no pure recall) | — | ✅ |
| 9 | Trust boundary + Auditor + Carrier | 32–33, 35 | Application scenario | 2425S2 Q8 | ✅ |
| 10 | Single vs multi-tenancy | 6 | Short scenario | 2425S2 Q12, Q14; 2526S1 Q6, Q14 | ✅ |
| 11 | Deployment models: public / private (on-site, outsourced, VPC) / community / hybrid | 36–46 | Production scenario | 2425S2 Q9, Q23, Q25; 2526S1 Q12; 2526S2 Q22, Q24 | ✅ |
| 12 | Sovereign cloud and data residency | 47 | Production scenario | 2425S2 Q16; 2526S1 Q25; 2526S2 Q5, Q23 | ✅ |

Gap scenarios (added after a coverage check against the cards found concepts not yet tested):

| # | Topic | Slides | Status |
|---|-------|--------|--------|
| G1 | Provider architecture: Service Orchestration layers vs Cloud Service Management, provider types | 22, 27, 28 | ✅ |
| G2 | Consumer use cases by service model and the abstraction ladder | 7, 9, 26 | ✅ |
| G3 | Re-test of mistakes: managed database (PaaS), self-service vs elasticity, metering vs billing, auditor vs carrier | 4, 12, 18, 29, 33, 35 | ✅ |

Not L02 (previously mis-mapped): 2526S1 Q5 is MapReduce; 2526S1 Q4 is FaaS cost (AWS Lambda), not MySQL; 2526S1 Q19 is scaling (PaaS), not lift-and-shift.

---

## Detailed Notes

### Concept 1: Choosing SaaS, PaaS or IaaS (S1)

**Core idea:** The three models differ in how much the consumer still manages. Consumer manages, by model: **IaaS** = Database, Integration, Runtime, Application, Data. **PaaS** = Data, Application. **SaaS** = Data only. The provider manages everything below that line, including the OS in IaaS. (Slide 19 draws it this way and is treated as ground truth for now. The official NIST definition and the 2526-S2 Q9 past-paper answer both have the IaaS consumer controlling the OS; this conflict is to be confirmed with the lecturer.)

| | Who uses it | You supply | Typical fit |
|--|--|--|--|
| IaaS (slides 8, 10, 11) | Admins, teams that need control | Runtime, database, code (the OS sits with the provider on slide 19; conflict noted in the responsibility table) | Move an existing system unchanged (lift-and-shift); a LAMP stack you install yourself |
| PaaS (slides 8, 12, 13) | Developers | Your application and data | Build or deploy on a ready-made platform: app server, managed database |
| SaaS (slide 8) | End users | Only your data | Use a finished application (email, accounting, CRM) |

- A **managed database** (for example AWS RDS running MySQL) is **PaaS**: it is platform software the developer builds into their own application (slide 18, database-as-a-service variant). The database layer moves from you to the provider; you keep your data, schema and application code.
- **Least-change move of an existing LAMP stack = IaaS**, because you still install and run every layer yourself. PaaS needs the app to fit the platform's supported environment (beyond slides: language and framework support).

> [!WARNING]
> **Mistake:** picking PaaS for "move our existing LAMP shop with the least change", and calling a managed MySQL service SaaS. A stack you install yourself is IaaS; a managed database is PaaS. SaaS is only a finished application that an end user uses.

> [!CAUTION]
> **Exam Trap (MCQ):** LAMP stack on virtual machines = IaaS; a managed database such as AWS RDS with MySQL = PaaS (2526-S2 Q4).

**Key one-liner:** The more layers the provider runs for you, the higher the model: you install it yourself, it is IaaS; you build on a ready platform, it is PaaS; you only use the finished app, it is SaaS.

---

### Concept 2: Responsibility split and pros and cons of each model (S2)

**Core idea:** Moving up from on-premise to IaaS to PaaS to SaaS, the provider manages more of the stack and the consumer less. In return, speed to start rises and freedom to customise falls (slides 19, 20).

| Model | Consumer manages (slide 19) | Pro (slide 20) | Con (slide 20) |
|--|--|--|--|
| On-premise | Everything | Highest flexibility | Long time-to-market |
| IaaS | Database, Integration, Runtime, Application, Data (slide 19 puts the OS with the provider; NIST and the 2526-S2 Q9 answer have the consumer manage it, so confirm with the lecturer) | Scalability, no hardware procurement | Privacy |
| PaaS | Data, Application | Database, frameworks, middleware ready | Vendor lock-in |
| SaaS | Data only | Reduces time-to-market | Lowest flexibility |

- **The consumer keeps its data in every model**, including SaaS. "The vendor handles everything, so we have no responsibility for the records" is false. (Legal accountability for the data staying with the owner is beyond slides.)
- **OS in IaaS (open conflict).** Slide 19 draws the OS in the provider's block and is treated as ground truth for now. The official NIST definition and the 2526-S2 Q9 model answer say the IaaS consumer manages the OS. To be confirmed with the lecturer.

**Key one-liner:** Each step up the models moves work from you to the provider and buys speed at the cost of flexibility, but your data always stays your responsibility.

---

### Concept 3: NIST essential characteristics and the 5/4/3 framework (S3)

**Core idea:** NIST defines **5 essential characteristics, 4 deployment models and 3 service models** (slides 3, 5). A service is only cloud if it shows the essential characteristics (slide 4).

| Characteristic (slide 4) | What it looks like in practice |
|--|--|
| **On-demand self-service** | The consumer provisions capability **by themselves, without human interaction with the provider**, usually via a service portal (NIST definition; slide 4 says only "via a service portal") |
| **Broad network access** | Reachable over the network from many device types |
| **Resource pooling** | Provider shares one pool across customers (multi-tenancy); you do not know or choose the physical location |
| **Rapid elasticity** | Capacity is provisioned **and released** quickly, even automatically, to scale out and in with demand (NIST definition; slide 4 says only "time to market/fast deployment") |
| **Measured service** | Pay per use, not a flat fee regardless of use |

- **Clue words:** "email the account manager", "raise a ticket" = no self-service (you cannot provision it yourself). "Flat monthly fee whatever you use" = no measured service. "Don't know which datacenter" = pooling. "Any device, browser" = broad network access.
- **Service models** are only SaaS, PaaS, IaaS. DBaaS, FaaS and similar are **variants** (slide 18). **Deployment models** are public, private, community, hybrid; FaaS is not one.

> [!WARNING]
> **Mistake:** confusing on-demand self-service with rapid elasticity (S3, G3). **Ground truth is the official NIST definition, not slide 4's shorthand.** Self-service = you provision it yourself, no human at the provider (usually a portal). Rapid elasticity = capacity scales out *and in* with demand. "A portal lets us create a server in minutes without contacting anyone" is **self-service**; "capacity automatically grows at the peak and shrinks afterwards" is **elasticity**. Provisioning that goes through the provider's staff by email or ticket is not self-service.

**Key one-liner:** The five essential characteristics are self-service, broad access, pooling, rapid elasticity and measured pay-per-use. Provisioning through the provider's staff means no self-service, and a flat fee means no metering.

---

### Concept 4: Variants of the service models (S4)

**Core idea:** The three NIST service models are SaaS, PaaS and IaaS. Offerings such as **Storage-, Database-, Security-, Communication-, Integration-, Testing- and Function-as-a-Service** are **variants** of them: each offers a single capability instead of a whole model (slide 18, "Everything-as-a-Service").

| Need | Variant (slide 18) |
|--|--|
| Keep files durably | Storage-as-a-Service |
| Managed database | Database-as-a-Service |
| Run a small piece of code with no server to manage | Function-as-a-Service (serverless computing) |
| Outside party scans for vulnerabilities | Security-as-a-Service |

- **Serverless** does not mean there is no server. A server exists, but the provider provisions and manages it, so the consumer has nothing to look after (slide 18 names FaaS as serverless computing; the meaning is beyond the L02 slides). Event-driven, short-lived behaviour is covered in L06.
- A **managed database (DBaaS) is platform software**: it sits with PaaS, not IaaS (see Concept 1).
- When a question asks for the variant, name the specific "X-as-a-Service". Naming the base model (IaaS, PaaS, SaaS) is not the same answer.

> [!WARNING]
> **Mistake:** calling a managed database "IaaS because the database is provided for you", and answering with SaaS/PaaS/IaaS when asked for the as-a-Service variant. A managed database is DBaaS, a PaaS-side offering, and the variants are named for the single capability they provide.

**Key one-liner:** Storage, database, function and security services are single-capability variants of the three NIST models, not extra models, and "serverless" means the provider runs the servers, not that none exist.

---

### Concept 5: Combining service models and meeting data-location rules (S5)

**Core idea:** Service models stack. A SaaS can be built using PaaS, and PaaS runs on IaaS: cloud services on ready-made environments on virtual servers on physical servers (slides 14, 17). One provider can be a consumer of another provider's layer.

- **Meeting a legal data-location rule (slide 15):** the consumer subscribes to a PaaS from Provider X. To meet the requirement, X hosts its platform on Provider Y's infrastructure, and Y's datacenter is **in the same region as the consumer**. The data therefore sits where the law requires, even though the consumer's contract is with X.
- The consumer's contract and SLA are with X, while the data physically sits with Y, so responsibility and audit span both (beyond slides, inferred from slide 15).
- **Pooling does not mean location is unimportant.** Resource pooling hides the exact machine in day-to-day use, but a provider can still place workloads in a chosen region to meet a legal rule.
- **Stacking is not hybrid cloud.** Service models (SaaS, PaaS, IaaS) say *what layer* is offered. Deployment models (public, private, community, hybrid) say *how and for whom* clouds are set up. Hybrid = two or more distinct clouds, connected for data and application interoperability (slide 45); for example, sensitive data on a private cloud while the application runs on a public one.

> [!CAUTION]
> **Exam Trap (MCQ):** an option saying "stacking PaaS on IaaS is hybrid cloud" is wrong: hybrid is about deployment models, not service-model layers. Another typical wrong option says data location can never be known or doesn't matter because of pooling.

**Key one-liner:** Service models stack in one provider chain (SaaS on PaaS on IaaS), and a provider can host its platform in the consumer's region to meet a legal rule, while hybrid cloud is a different axis: distinct clouds connected together.

---

### Concept 6: The five actors and the purpose of the reference model (S6)

**Core idea:** NIST's reference model describes **what** cloud services provide, not **how** to build them. It is **vendor and implementation independent** and is not the architecture of any specific cloud (slide 21). It gives a common framework to describe, discuss and develop a system-specific architecture.

| Actor (slides 23, 25) | Role | Matching symptom or clue |
|--|--|--|
| **Consumer** | Maintains a business relationship with, and uses services from, providers | The organisation using the service |
| **Provider** | Offers a cloud service | The company running the service |
| **Auditor** | Independent assessment of services, operations, performance and security | Security audit, privacy impact audit, performance audit (slide 22) |
| **Broker** | Manages use, performance and delivery of services and negotiates relationships between providers and consumers | Bundling several providers, negotiating contracts or price |
| **Carrier** | Connectivity and transport of cloud services from providers to consumers | Slow or broken path between provider and consumer while the provider's own servers are fine |

- **Match the symptom to the actor whose job it is.** Provider servers fine but pages slow = the path between them = carrier. The auditor reviews performance independently; it is not the first place to check a live problem (beyond slides: application of the role definitions).
- Auditor work = security, privacy and performance assessments. Price negotiation = broker.
- The provider is categorised by the service model it sells (SaaS, PaaS or IaaS provider), slide 27: reference only.

> [!WARNING]
> **Mistake:** naming the cloud auditor as the first place to check a live slowdown. Normal provider response times point to the carrier (the connectivity between provider and consumer). The auditor assesses independently, after the fact.

> [!CAUTION]
> **Exam Trap (MCQ):** "NIST's reference model is a blueprint for exactly how to build a cloud" or "the exact architecture of one vendor" is wrong. It describes the *what*, is vendor independent, and is not a specific cloud's architecture (slide 21).

**Key one-liner:** Consumer uses, provider offers, auditor independently checks, broker bundles and negotiates, carrier moves the traffic: pick the actor whose job matches the symptom.

---

### Concept 7: Cloud broker services (S7)

**Core idea:** A cloud broker helps consumers manage the integration of cloud services. It does so in three ways (slide 34):

| Broker service | What it does | Clue |
|--|--|--|
| **Service intermediation** | Provides value-added services on top of a provider's service | Adds single sign-on, a dashboard or reporting to one provider's service |
| **Service aggregation** | Combines and integrates multiple services into one or more new services; data integration; secure data movement between consumers and several providers | One integrated offering from several providers, with a single login |
| **Service arbitrage** | Flexibility to choose services from multiple agencies | Picks the best or cheapest provider for each job, without merging them |

- **Aggregation merges; arbitrage chooses.** Both involve several providers, but aggregation builds something new from them and arbitrage selects among them (choosing by price is the scenario's detail, beyond slides).
- Broker vs carrier: a broker manages services and relationships; a carrier only transports the traffic (Concept 6).

> [!CAUTION]
> **Exam Trap (MCQ):** an option calling "integrated offering from several providers with secure data movement" intermediation or arbitrage is wrong. That is **service aggregation** (2526-S1 Q10).

**Key one-liner:** Intermediation adds value on top of one service, aggregation merges several services into a new one, and arbitrage picks among providers.

---

### Concept 8: Cloud service management, portability and interoperability, security and privacy (S8)

**Core idea:** Cloud service management covers the functions a provider runs to operate the services it offers to consumers (slides 29, 30). It has three categories:

| Category (slide 29) | Contains | Test |
|--|--|--|
| **Business Support** | Customer Mgmt, Contract Mgmt, Inventory Mgmt, **Accounting & Billing**, Reporting & Auditing, **Pricing & Rating** | The commercial side: charging, contracts, pricing |
| **Provisioning/Configuration** | **Rapid Provisioning**, Resource Change, Monitoring & Reporting, **Metering**, SLA Management | The technical side: deploying, changing and measuring resources |
| **Portability/Interoperability** | Data Portability (copy data to and from, bulk data transfer), Service Interoperability (unified management interface), System Portability (VM image migration, app/service migration) | Moving away from, or working across, providers |

- **Metering measures usage; Accounting & Billing charges for it.** Metering is Provisioning/Configuration; billing is Business Support.
- **Portability vs interoperability:** portability = moving your data or system (VM images, apps) to another provider; interoperability = services from different providers working together. Without these, the consumer is locked in.
- **Security** is not a layer. It is **cross-cutting**: it spans all layers of the reference model and concerns all relevant actors. **Privacy** concerns Personal Information (PI) and Personally Identifiable Information (PII) held by providers (slide 31).
- Service orchestration, the provider's arrangement and coordination of resources across the Service Layer, the Resource Abstraction and Control Layer and the Physical Resource Layer, is in the diagram facts below (slide 28).

> [!WARNING]
> **Mistake (made twice, S8 and G3):** classing metering as Business Support because it is "consumer facing". Measuring usage is Provisioning/Configuration (technical). Pricing and billing, which charge for it, are Business Support.

**Key one-liner:** Business Support charges, Provisioning/Configuration deploys and measures, Portability/Interoperability gets you out of or across providers, and security cuts across every layer.

---

### Concept 9: Trust boundary, auditor and carrier (S9)

**Core idea:** A **trust boundary** is the logical perimeter around the IT resources an organisation trusts (slide 32). Moving to the cloud changes it in three ways: **increased security vulnerabilities**, **reduced operational governance control**, and **multi-tenancy means overlapping trust boundaries**.

- The boundary now has to include resources run by the provider, and on shared hardware it can overlap with other tenants' boundaries.
- **Cloud auditor (slide 33):** independent examination of cloud service controls (security controls, privacy impact, performance), verifying **compliance with regulation and security policy** and **conformance to standards**, **through review of objective evidence**. It is trusted over the provider's own claim because it is independent and works from evidence, not assertion.
- **Cloud carrier (slide 35):** provides connectivity and transport between consumers and providers. Cloud providers set up **SLAs with a cloud carrier** to provide consistent services, and the carrier may need to provide **dedicated and secured connections**. A provider's promise to its consumer is only as strong as the carrier's SLA beneath it (beyond slides).
- An outage while the provider's own servers stay up points to the carrier, not the provider (see Concept 6).

> [!WARNING]
> **Mistake:** explaining the auditor's credibility only as "unbiased". The reason to trust it is independence plus **review of objective evidence**, checked against regulation, security policy and standards.

**Key one-liner:** Moving to the cloud widens and overlaps your trust boundary and reduces your governance control, the auditor is trusted for independence plus objective evidence, and the carrier's SLA caps the provider's promise.

---

### Concept 10: Single tenancy vs multi-tenancy (S10)

**Core idea:** In **single tenancy**, each cloud consumer has a **separate instance** of the IT resource. In **multi-tenancy**, the provider **pools IT resources to serve multiple consumers**, and **one instance of the program serves multiple consumers (tenants)** (slide 6).

| | Single tenant | Multi-tenant |
|--|--|--|
| Instance | One per consumer | One shared by many consumers |
| Cost to provider | Higher: many instances to run, patch and maintain | Lower: one instance serves everyone, resources pooled and better used |
| Isolation | Strong: nothing shared | Weaker: tenants share the same instance and platform |
| Security concern | Smaller | Overlapping trust boundaries (slide 32): a flaw or a bad tenant can expose others' data |

- **The saving comes from pooling and sharing**, not from skipping customisation: one instance to run and maintain instead of one per customer.
- **The security trade-off is shared exposure.** Describe it as a shared-platform risk (overlapping trust boundaries), not a "single point of failure".
- A consumer who wants more isolation (for example a hospital group) asks for a separate, single-tenant copy and typically pays more.

> [!WARNING]
> **Mistake:** explaining multi-tenancy's lower cost as "no customisation needed per customer". The saving is pooling: one instance serves many tenants, so there is less to run and maintain and resources are used more fully.

**Key one-liner:** Multi-tenancy is cheaper because one instance and one pool serve many tenants, and the price is weaker isolation and overlapping trust boundaries; single tenancy buys isolation at higher cost.

---

### Concept 11: The four deployment models (S11)

**Core idea:** NIST's four deployment models are public, private, community and hybrid (slides 36–46). Choose by what the organisation needs.

| Model | Choose it when | Notes |
|--|--|--|
| **Public** (slide 38) | Low upfront cost with pay-as-you-go, available anytime and anywhere, maintenance handled by the provider; no IT team | Shared by all consumers |
| **Private** (slides 39, 40, 42) | High control, especially for sensitive data; restricted access; large-scale IT; maintenance mostly in-house | Concerns: limited SLA, reliability, security, availability, trust |
| **Community** (slides 43, 44) | Several organisations share operational and regulatory requirements and private cloud is too costly alone | Needs a clear governance structure; e.g. government, education, health care |
| **Hybrid** (slide 45) | Balance control and cost; keep sensitive data private while the application or web shop runs public | Two or more distinct clouds, connected for data and application interoperability |

- **Private cloud has two forms:** on-site (your premises) and **out-sourced** (dedicated resources hosted by a third party, reached from your enterprise network). Slide 41 also shows the **virtual private cloud (VPC)**: a secure, isolated environment **inside a public cloud**, customisable by you.
- **Out-sourced private vs VPC:** dedicated resources versus an isolated slice of shared public infrastructure.
- **The slide's open question on private hosting is security** ("Security? On-site vs out-sourced"), because physical control moves to a third party. It is a question to evaluate, not a verdict that it is weaker (beyond slides).
- When asked "why public", give the slide reasons (low upfront cost, anywhere access, provider maintenance), not "no specific requirements".

> [!WARNING]
> **Mistake:** justifying public cloud with "no specific requirements" and claiming out-sourced private is "obviously less secure". Use the slide reasons for public cloud (low upfront cost, anytime anywhere access, provider-handled maintenance), and treat on-site vs out-sourced security as an open question to evaluate.

> [!CAUTION]
> **Exam Trap (MCQ):** deployment choice is driven by needs (security and privacy for private, regulatory sharing for community, balancing control and cost for hybrid). An option saying one model is always best is wrong (2425-S2 Q25, 2526-S1 Q12).

**Key one-liner:** Match the model to the need: public for low cost with no IT team, private for control of sensitive data, community for shared regulation at shared cost, hybrid to balance control and cost across distinct clouds.

---

### Concept 12: Sovereign cloud and data residency (S12)

**Core idea:** A **sovereign cloud** exists to meet the regulatory and compliance needs of a country or jurisdiction. It **stores data (including metadata) within national borders**, helps the organisation **adhere to local data protection laws**, and **prevents foreign access to data under all circumstances** (slide 47).

- **Sovereign is not private.** Private cloud is exclusive control by one organisation. Sovereign is control by a country's jurisdiction. A private cloud can sit in another country or be operated by foreign staff, so it guarantees neither in-country metadata nor no foreign access.
- **Sovereign is not just choosing a region.** A region keeps data in a geography but does not by itself stop foreign access or cover metadata (beyond slides: the slide states the guarantees, not the comparison).
- **Located in-country is not enough.** An in-country datacenter run by foreign staff does not necessarily meet the requirement. Ask for guarantees on foreign access, local data protection law compliance and in-country storage of data and metadata.
- Do not justify the difference with cost. The distinction is jurisdiction.

> [!WARNING]
> **Mistake:** saying private cloud falls short of sovereign cloud because of cost at scale. The difference is jurisdiction: private = exclusive control by one organisation, sovereign = national control with no foreign access and data plus metadata kept within borders.

> [!CAUTION]
> **Exam Trap (MCQ):** "Private cloud" or "a public cloud region set in-country" as the answer to a data-sovereignty requirement is wrong when the question stresses no foreign access or metadata (2526-S1 Q25, 2526-S2 Q5).

**Key one-liner:** Sovereign cloud keeps data and metadata inside national borders and blocks foreign access under all circumstances, which neither a private cloud nor an in-country region guarantees on its own.

---

### Concept 13: Provider architecture, orchestration vs service management (G1)

**Core idea:** Inside the cloud provider (slide 22), **Service Orchestration** is the arrangement, coordination and management of computing resources to support the provider's activities. It has three layers, top to bottom (slide 28):

| Layer | Holds |
|--|--|
| **Service Layer** | The SaaS, PaaS and IaaS services offered to consumers |
| **Resource Abstraction and Control Layer** | The software that abstracts physical resources (for example splitting servers into virtual machines) and controls their allocation |
| **Physical Resource Layer** | Hardware and Facility (servers, buildings, power, cooling) |

- **Cloud Service Management** is a separate box alongside orchestration. It holds the service-related functions used by consumers and brokers: **Business Support** (billing, pricing), **Provisioning/Configuration** (rapid provisioning, metering, SLA management) and **Portability/Interoperability** (Concept 8).
- **Security and Privacy** are cross-cutting bars, not layers (Concept 8).
- A provider is categorised by the service model it sells (SaaS, PaaS or IaaS provider), slide 27.

> [!WARNING]
> **Mistake:** describing cloud service management as just "the provisioning of the service". It has three categories, and billing and pricing are Business Support, not provisioning.

**Key one-liner:** Orchestration is the three-layer stack (services, abstraction and control, physical) that runs the resources, while cloud service management is the separate set of business, provisioning and portability functions that consumers and brokers use.

---

### Concept 14: Consumer use cases by service model (G2)

**Core idea:** Slide 26 lists what consumers typically use each model for. The abstraction ladder (slides 7, 9) is tested in Concept 2.

| Model | Typical consumer use cases (slide 26) |
|--|--|
| **SaaS** | ERP, HR, Billing, Social Networks, Sales, Financials, CRM, Content Mgmt, Collaboration, Email & Office Productivity, Document Mgmt |
| **PaaS** | Business Intelligence, Database, Application Deployment, Development & Testing, Integration |
| **IaaS** | Storage, CDN, Backup & Recovery, Compute, Services Management, Platform Hosting |

- **Reference only (open book):** the lists are slide content to search for, not something to memorise.
- **Platform Hosting (IaaS) vs Application Deployment / Development & Testing (PaaS):** IaaS = you install and run the platform software yourself on rented machines; PaaS = the provider supplies the platform and you deploy your application on it.
- **CRM and ERP (SaaS) vs Business Intelligence (PaaS):** SaaS is a finished business application; BI on PaaS is tooling you build on.

**Key one-liner:** Finished business apps are SaaS, build-and-deploy tooling (development, database, BI) is PaaS, and raw capacity (storage, CDN, backup, compute, platform hosting) is IaaS.

---

### Diagram facts verified from the slide images (text extraction misses these)

- **Slide 19 (responsibility split).** Consumer manages: IaaS = Data, Application, Runtime, Integration, Database. PaaS = Data, Application. SaaS = Data only. The slide shows the IaaS provider managing OS, Virtualization, Server, Storage, Network. The official NIST definition and 2526-S2 Q9's model answer say the IaaS consumer manages the OS. Open conflict: the notes follow the slide for now, pending the lecturer.
- **Slide 28 (service orchestration, 3 layers).** Service Layer (SaaS, PaaS, IaaS) over Resource Abstraction and Control Layer over Physical Resource Layer (Hardware, Facility).
- **Slide 17.** SaaS develops using PaaS; PaaS runs on IaaS (physical server, virtual servers, ready-made environments, cloud services).

---

## Reference only (not tested)

- **Slide 22:** the reference-architecture picture. The Auditor box lists Security Audit, Privacy Impact Audit and Performance Audit; the Broker box lists Intermediation, Aggregation and Arbitrage; the Carrier sits across the bottom (slide 22).
- **Slide 27:** provider types: SaaS, PaaS and IaaS cloud provider, depending on the model sold.
- **Slide 31:** privacy concerns Personal Information (PI) and Personally Identifiable Information (PII) held by providers.
- **Slides 36, 38, 39, 43, 47:** the example provider names (Amazon, Microsoft, Google, Oracle, Salesforce, Heroku and others). Look them up if needed.
- **Slide 44:** community cloud architecture: Orgs 1 to 3 linked by shared policies and protocols, IAM, a cloud manager, and a cloud community holding storage, applications and services, security controls, data governance tool, reporting engine and logging engine.
- **Slide 46:** the hybrid picture contrasting two different clouds with five interconnected clouds.

## Not yet tested

- Nothing material left. The reference-only items above are lookup content for the open-book exam.
