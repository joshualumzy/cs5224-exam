# L06 Cards

Built by DeepSeek V4.1 Flash from the slide text of both PDFs (Part 1 = P1, Part 2 = P2, 32 slides each); diagram facts transcribed by Claude Haiku from the slide images (section at the end). **Skipped:** P1 s1, 2, 14 (section divider), 15 (break), 30-32; P2 s1, 2, 19 (break), 30-32. 'Type: Application' = can be tested in a scenario; 'Reference-only' = lookup. '(inferred)' = not stated on a slide. "Annotation" = Joshua's handwritten notes on the slides: not verified, may be wrong. Paper names: 2425-S2 = 24S2, 2526-S1 = 25S1, 2526-S2 = 25S2.

### L06-P1-C01 Cloud provider common features
- **Slides:** P1 s3
- **Type:** Reference-only
- **What it is:** Recall slide: providers offer "Basic and higher-level services with different levels of abstraction (IaaS, PaaS, SaaS)"; "Compute and storage resources – virtual servers, storage, networking, . . ."; "Deployment management services – load balancer, auto-scaling, monitoring, message queueing, . . ."; and a "User interface – graphical UI, CLI".
- **Look-alikes:** IaaS/PaaS/SaaS themselves (covered later in this lecture) — here they appear only as abstraction levels inside a feature list, not as the service models being compared.
- **Limits / trade-offs:** none stated.
- **Situation cues:** "which deployment-management service does a provider give me?"; "where do load balancer and auto-scaling sit?"; "what levels of abstraction exist?"
- **Past-paper Qs:** none

### L06-P1-C02 Cloud applications: ideal vs not ideal, and key challenges
- **Slides:** P1 s4-5
- **Type:** Application
- **What it is:** Cloud applications "Focus primarily on enterprise computing". "Ideal: Applications which can be divided into as many independent tasks as possible", e.g. "Web services, database services, search services, machine learning with large-scale models". "Not Ideal: Applications with a complex workflow and multiple dependencies", e.g. "high-performance computing e.g. part A -> part B -> part C", and "Applications with intense communication among concurrent instances" (networking issues, "bandwidth and latency"). "Key Challenges! Cloud Consumer – scale application to accommodate a dynamic load, recover after system failure, efficiently support checkpoint/restart"; "Cloud Provider – manage a large number of systems, provide quality of service guarantee".
- **Look-alikes:** the developer-side challenges on s6 (next card) — s5 splits challenges by consumer vs provider; MapReduce (P2) — an example of the "divided into independent tasks" ideal.
- **Limits / trade-offs:** non-partitionable workloads and communication-heavy apps fit poorly; latency/bandwidth suffer with intense inter-instance communication.
- **Situation cues:** "can this job be split into independent tasks?"; "a scientific simulation with strict step A→B→C"; "instances constantly talk to each other"; "who worries about scaling — consumer or provider?"
- **Past-paper Qs:** none

### L06-P1-C03 Developing cloud applications: challenges
- **Slides:** P1 s6
- **Type:** Application
- **What it is:** Four challenges: "Performance Isolation – Virtualisation shares VMs and multitenancy shares cloud application services ⇒ problem when utilisation is high!"; "Reliability – Server failures expected when a large number of servers cooperate to compute"; "Latency/Bandwidth Fluctuations – Due to sharing of resources"; "Data Logging – Necessary, but also need to limit it due to performance considerations" (it is the "way to recover -> backups", and "how often? you'll need to interrupt your app").
- **Look-alikes:** consumer/provider challenges on s5 — those are runtime operation concerns, these are development-time concerns; reliability here (server failures expected) vs high availability as a SaaS/PaaS provider characteristic (s18, s25).
- **Limits / trade-offs:** logging is needed for recovery but must be limited for performance, and backup frequency interrupts the app.
- **Situation cues:** "shared tenancy slows us at peak utilisation"; "with thousands of servers, failures are normal"; "network latency varies because resources are shared"; "how often should we back up without stopping the app?"
- **Past-paper Qs:** 25S2 Q15

### L06-P1-C04 Web-based architectural style
- **Slides:** P1 s7
- **Type:** Application
- **What it is:** "Reliance on Internet and web technology – high accessibility, web browser universality, ease of web-based service development"; "Cloud services use web technology as both the implementation medium as well as the management interface"; "Cloud applications typically use a web-based client-server architecture – web browser client and web server" (annotation: "API - 2 elements are communicating", "Some kind of contract between").
- **Look-alikes:** the three-tier web architecture (s8-9) — the concrete layering of that client-server style; SOAP/REST (s10-12) — the messaging protocols used over it.
- **Limits / trade-offs:** none stated beyond the listed benefits.
- **Situation cues:** "why do cloud apps use browsers as universal clients?"; "what acts as the contract between client and server?"; "web tech as both implementation and management interface".
- **Past-paper Qs:** none

### L06-P1-C05 Three-tier architecture of web applications
- **Slides:** P1 s8-9
- **Type:** Application
- **What it is:** "Three-tier architecture abstraction for a web application": 1 "Presentation layer – represents user-interface"; 2 "Application layer – represents implementation logic"; 3 "Data layer – comprises of persistent data stores". Slide 9 places them: presentation "sits on both the client and server side"; the application layer is where the "Web server receives client requests and retrieves the requested resources or generates web content based on application logic"; in the data layer "Web servers interact with application servers and the underlying database(s)". (diagram slide)
- **Look-alikes:** the web-based client-server style (s7) — the overall style; these are its three internal tiers; PaaS layered service models (s24) — "multi-tiered PaaS and IaaS" is a different kind of tiering (delivery models, not app tiers).
- **Limits / trade-offs:** none stated.
- **Situation cues:** "where does the UI logic live — client only or both sides?"; "which tier holds the persistent data?"; "which tier implements business logic?"
- **Past-paper Qs:** none

### L06-P1-C06 SOAP
- **Slides:** P1 s10
- **Type:** Reference-only
- **What it is:** "Web services technology – provides "as-a-service" cloud delivery models". "Simple Object Access Protocol (SOAP): Application protocol for web applications"; "Defines a common web service messaging format for request and response exchanges – based on XML and uses TCP or UDP as the transport protocols" (annotations: "protocol - set of rules defining communication btw 2 parties"; "structured format, larger enterprises, security important").
- **Look-alikes:** REST (s11-12) — SOAP is XML-based with a strict structured messaging format (suited to larger enterprises, security-sensitive uses), REST is the "lightweight option".
- **Limits / trade-offs:** none stated beyond the annotation that it suits structured formats, larger enterprises and security-important cases.
- **Situation cues:** "strict XML message format for enterprise web services"; "transport over TCP or UDP"; "need a formal contract between parties".
- **Past-paper Qs:** none

### L06-P1-C07 REST and its design principles
- **Slides:** P1 s11-12
- **Type:** Application
- **What it is:** "Representational State Transfer (REST): Software Architecture for distributed hypermedia systems"; "Supports client communication with stateless servers"; "Platform and language independent"; "Supports data caching" (annotation: "lightweight option", "hypermedia - different types of media"). Design principles: "Uniform interface", "Client-server decoupling", "Statelessness" (annotation: "when you connect again, the system has no knowledge of what happened previously"), "Cacheability" (annotation: "so you can return repeated requests faster"), "Layered system architecture", "Code on demand (optional)".
- **Look-alikes:** SOAP (s10) — formal XML protocol vs REST's lightweight architecture; Lambda statelessness (P2 s20, s24) — same "no memory of previous interactions" idea applied to functions.
- **Limits / trade-offs:** statelessness means the server keeps no knowledge of previous interactions; code-on-demand is optional.
- **Situation cues:** "lightweight, cacheable API across platforms and languages"; "server must not remember past requests"; "which of the six REST principles is optional?"
- **Past-paper Qs:** none

### L06-P1-C08 Web service APIs for cloud services
- **Slides:** P1 s13
- **Type:** Reference-only
- **What it is:** "Cloud services are naturally distributed – single service request might require message passing between multiple servers"; "Cloud services are accessed by different clients using different programming languages and technologies (e.g., Java, Python, . . .) – requires a standard interface for communication between clients and server" (annotation: "language agnostic"); "Web service APIs implement a standard communication interface for cloud services, e.g., REST API requests/responses are transferred on HTTP using formats such as XML and JSON".
- **Look-alikes:** REST (s11-12) — here REST APIs are the concrete realisation of the standard-interface idea; SOAP (s10) — the other messaging format.
- **Limits / trade-offs:** none stated.
- **Situation cues:** "clients in Java and Python must call the same service"; "why must cloud APIs be language agnostic?"; "what format do REST payloads use over HTTP?"
- **Past-paper Qs:** none

### L06-P1-C09 Basic cloud service models (recall)
- **Slides:** P1 s16
- **Type:** Reference-only
- **What it is:** (diagram slide) Recall image of the cloud service models IaaS, PaaS, SaaS (source: stackscale.com); text on the slide is only the image URL and caption.
- **Look-alikes:** the detailed SaaS/PaaS/IaaS cards that follow (C10-C12) — this is just the pictorial recall of the same three models.
- **Limits / trade-offs:** none stated.
- **Situation cues:** "which model manages which stack layer?"; "ordering IaaS/PaaS/SaaS by who manages what".
- **Past-paper Qs:** none

### L06-P1-C10 Software as a Service (SaaS)
- **Slides:** P1 s17-18
- **Type:** Application
- **What it is:** "Consumers execute developed applications by supplying data and obtaining the results"; "Provider develops and provides the application – running of application is transparent to the consumer" (diagram slide with "Services Provided by SaaS Providers"). SaaS provider characteristics: "Multi-tenanted applications", "Web access", "Centralised management of SaaS services", "Multi-device support", "Scalability under varying loads", "High availability", "API integration with other software".
- **Look-alikes:** PaaS (s19-20) — PaaS is for building apps, SaaS is for using a finished app with your data; IaaS (s21-22) — SaaS hides even the platform, IaaS gives raw infrastructure.
- **Limits / trade-offs:** running of the application is transparent — the consumer does not control how it runs.
- **Situation cues:** "just upload data and get results"; "no APIs, no deployment, thin browser client"; "multi-tenant app with subscription pricing"; "who fixes/updates the application?"
- **Past-paper Qs:** 24S2 Q7 (also L02)

### L06-P1-C11 Platform as a Service (PaaS)
- **Slides:** P1 s19-20
- **Type:** Application
- **What it is:** (diagram slide, "Overview of PaaS"; annotation: "used by application developers"). PaaS provider characteristics: "All in one – same IDE to develop, test, deploy, host, and maintain applications", "Web access to development platforms", "Offline access for developers", "Built-in scalability", "Collaborative platform for developers", "Diverse client tools" (examples: "Salesforce, Heroku, Digital Ocean").
- **Look-alikes:** SaaS (s17-18) — SaaS consumers only supply data; PaaS consumers build and deploy their own software; IaaS (s21-22) — IaaS gives VMs you configure yourself, PaaS gives the development platform; ELB/auto-scaling — per 25S1 Q19 these are not service models, whereas "built-in scalability" is a PaaS characteristic.
- **Limits / trade-offs:** none stated on these slides (trade-offs appear on s26).
- **Situation cues:** "app developer wants one IDE to develop, test, deploy, host and maintain"; "provider keeps the stack up to date"; "team needs a collaborative dev platform"; "who is the typical PaaS user?"
- **Past-paper Qs:** 25S1 Q13, 25S1 Q19, 25S2 Q2; also 24S2 Q3 (L02 main)

### L06-P1-C12 Infrastructure as a Service (IaaS)
- **Slides:** P1 s21-22
- **Type:** Application
- **What it is:** (diagram slide, "Overview of IaaS"). IaaS provider characteristics: "Web access to resources" (annotation: "LAMP stack - packaged dev env"), "Centralised physical resource management", "Elastic services and dynamic scaling", "Shared infrastructure across multiple users", "Precofigured VMs", "Metered services".
- **Look-alikes:** PaaS (s19-20) — IaaS gives preconfigured VMs, the consumer installs/configures the stack; SaaS (s17-18) — IaaS exposes infrastructure, SaaS hides everything; DBaaS — per 25S2 Q4 a managed database (PaaS-style) vs installing your own LAMP stack on IaaS.
- **Limits / trade-offs:** shared infrastructure across multiple users; metered (pay per use) services.
- **Situation cues:** "rent preconfigured VMs, metered"; "most control over the stack, most responsibility too"; "elastic scaling of raw compute"; "lift-and-shift of an existing environment".
- **Past-paper Qs:** 25S2 Q9 (also L02)

### L06-P1-C13 Data analytics application: choosing a model, SaaS route
- **Slides:** P1 s23-25
- **Type:** Application
- **What it is:** "Key Question! Which cloud service model to use, i.e., which "as-a-service" do you go for?" — answer: ". . . It depends!". SaaS route: "Application is located on the cloud"; "Clients use a thin client (web browser) to access application"; "Often built on top of multi-tiered PaaS and IaaS"; "Clients do not deal with underlying PaaS and IaaS"; "Clients do not deal with APIs"; "Various pricing mechanisms – free!, pay-as-you-go, subscription, etc.". Example key steps: "1 Access your favourite application or AI, 2 Give it your data, 3 Report on the analysis!".
- **Look-alikes:** PaaS route (s26-27) — there you build the pipeline yourself on provider tools; IaaS route (s28) — you even install the stack; the SaaS characteristics card (C10) — s24 adds the thin-client and pricing angle for this scenario.
- **Limits / trade-offs:** consumer has least control (no APIs, no underlying layers) but least work; pricing varies (free, pay-as-you-go, subscription).
- **Situation cues:** "analyst just wants to run analytics on their data"; "no infrastructure or API work allowed"; "browser-only access"; "which 'as-a-service' should we pick?"
- **Past-paper Qs:** 24S2 Q1, 24S2 Q7 (both also L02)

### L06-P1-C14 Data analytics application: PaaS route
- **Slides:** P1 s26-27
- **Type:** Application
- **What it is:** Consumer: "Creates software using tools and libraries from PaaS provider"; "Controls software deployment and configuration settings". Provider: "Installs and maintains software, libraries and middleware" (annotation: "keep things up to date"); "Handles the transparent infrastructure from the user"; "Exposes an API for PaaS consumers (programmers)"; "Provides integrated services of scalability, maintenance, and versioning, e.g., total application hosting, development, testing, and deployment environment". Example key steps: "1 Access a system with MongoDB, Express, React, Node.js (MERN)" (annotation: "package to build web application"), "2 Build your own data analytics pipeline", "3 Give it your data", "4 Report on the analysis!".
- **Look-alikes:** SaaS route (s23-25) — SaaS consumers do not deal with APIs, PaaS consumers get an exposed API and control deployment; IaaS route (s28) — there the consumer also installs and configures the MERN stack.
- **Limits / trade-offs:** consumer keeps control of deployment and configuration but not of the infrastructure (transparent, provider-managed).
- **Situation cues:** "developer builds a pipeline on provider tools but keeps deployment control"; "provider maintains middleware and scales for me"; "MERN stack available out of the box"; "who updates the libraries?"
- **Past-paper Qs:** 25S1 Q2

### L06-P1-C15 Data analytics application: IaaS route
- **Slides:** P1 s28
- **Type:** Application
- **What it is:** Key steps for the IaaS consumer: "1 Create a compute instance running Linux", "2 Install and configure MongoDB, Express, React, Node.js (MERN)", "3 Build your own data analytics pipeline", "4 Give it your data", "5 Report on the analysis!".
- **Look-alikes:** PaaS route (s26-27) — PaaS supplies the MERN system ready-made; SaaS route (s23-25) — SaaS supplies even the pipeline.
- **Limits / trade-offs:** most setup work for the consumer (install and configure everything), hence most control.
- **Situation cues:** "spin up a Linux VM and install everything yourself"; "full control of OS and stack"; "team can manage installations and configuration".
- **Past-paper Qs:** none

### L06-P1-C16 Service model choice: summary comparison
- **Slides:** P1 s29
- **Type:** Application
- **What it is:** (diagram slide — table) Summary comparing the three routes to the same data analytics outcome: IaaS = "Create a compute instance running Linux" + "Install and configure MongoDB, Express, React, Node.js (MERN)" + "Build your own data analytics pipeline" + "Give it your data" + "Report on the analysis"; PaaS = "Access a system with MongoDB, Express, React, Node.js (MERN)" + "Build your own data analytics pipeline" + same last two; SaaS = "Access your favourite application or AI" + "Give it your data" + "Report on the analysis".
- **Look-alikes:** the individual route cards (C13-C15) — this is their side-by-side summary; the responsibility-split question (24S2 Q18, P2 s24) — similar "who does what" comparison but across IaaS/PaaS/CaaS/FaaS in Part 2.
- **Limits / trade-offs:** less consumer work as you move IaaS → PaaS → SaaS, but (inferred) correspondingly less control.
- **Situation cues:** "which steps disappear as you move from IaaS to SaaS?"; "fastest path to a working analytics app?"; "who installs the database in each model?"
- **Past-paper Qs:** 25S2 Q4 (also L02)

### L06-P2-C01 MapReduce programming model: key idea
- **Slides:** P2 s3-4
- **Type:** Application
- **What it is:** "Supports arbitrarily divisible workload"; "Supports distributed computing on large data sets on multiple machines (clusters, public or private clouds, . . .)". "How large is the data? Web-scale data on the order of 100s of GBs to TBs to PBs"; "Input data will not likely fit on a single computer's hard drive"; "Needs a distributed file system, e.g. Google File System"; "Inspired by the map and reduce functions in functional programming languages". "Key Idea! Split data into blocks and assign each block to an instance/process for parallel execution"; "Merge partial results produced by individual instances after all instances have completed execution"; "Transforms a set of input <key, value> pairs into a set of output <key, value> pairs"; "SPMD (Same Program Multiple Data), where a master instance partitions the data and gathers the partial results like GPUs".
- **Look-alikes:** FaaS (s20) — also for scalable processing, but event-driven single-purpose functions, not batch data-parallel jobs; Spark (s18) — an alternative engine optimised for in-memory/real-time processing.
- **Limits / trade-offs:** web-scale inputs need a distributed file system; the model fits arbitrarily divisible workloads (cf. P1 s4: workflow-dependent apps are not ideal for the cloud).
- **Situation cues:** "count things across petabytes that no single disk can hold"; "same program, many data blocks, in parallel"; "split, process, then merge partial results"; "<key, value> pairs in, <key, value> pairs out".
- **Past-paper Qs:** none

### L06-P2-C02 MapReduce programme structure
- **Slides:** P2 s5
- **Type:** Application
- **What it is:** Programme structure: "1 Read (a lot of) data; 2 MAP (extract data you need from each record); 3 Shuffle and Sort data; 4 REDUCE (aggregate, summarise, filter, transform extracted data, etc.); 5 Write the results" (annotations: "as a programmer you only care about map and reduce — everything else is done internally!"; "imagine large scale operations on data e.g. Google search").
- **Look-alikes:** the execution steps (s7) — s7 is the runtime sequence with master/workers; s5 is the programmer's structural view; the word-count example (s8-11) — a concrete instance of this structure.
- **Limits / trade-offs:** the programmer codes only map and reduce; shuffle/sort and the rest are handled internally by the system.
- **Situation cues:** "which two functions does the developer write?"; "what happens between map and reduce?"; "extract then aggregate".
- **Past-paper Qs:** none (25S1 Q5 concerns s7 and s9)

### L06-P2-C03 MapReduce high-level view: mappers, reducers, shuffling
- **Slides:** P2 s6
- **Type:** Application
- **What it is:** (diagram slide) "Divided into two phases – map and reduce"; "Splits are processed in isolation by tasks called Mappers"; "Outputs from mappers, called intermediate outputs (IOs), are brought into a second set of tasks called Reducers"; "Process of reading intermediate output into a set of reducers is called shuffling"; "Reducers produce the final outputs (FOs)" (annotations: "intermediary output stored on local disk"; "you can have multiple layers of reducers e.g. convergence for ML algos"; "who coordinates the steps? some kind of master node").
- **Look-alikes:** programme structure (s5) — the programmer view; execution (s7) — the same phases as a step-by-step run with master and workers.
- **Limits / trade-offs:** intermediate outputs sit on local disk between phases (per annotation); multiple reducer layers possible for iterative convergence.
- **Situation cues:** "what is shuffling?"; "where do mapper outputs go?"; "what does a reducer produce?"; "who coordinates everything?"
- **Past-paper Qs:** none

### L06-P2-C04 MapReduce execution steps
- **Slides:** P2 s7
- **Type:** Application
- **What it is:** "1 Application starts a master instance, M worker instances for Map phase, and later R worker instances for Reduce phase"; "2 Master instance partitions input data into M segments"; "3 Each map instance reads its input data segment and processes the data"; "4 Results of the processing are stored on local disks of the servers where the map instance runs"; "5 When all map instances have finished processing their data, R reduce instances read the results and merge the partial results"; "6 Final results are written by the reduce instance to a shared storage server"; "7 Master instance monitors reduce instances and terminates application when all tasks are complete" (annotations: "where are all these machines? the more spread out -> more latency").
- **Look-alikes:** high-level view (s6) — the conceptual phases; here the concrete master/worker protocol; parallelism (s12) — the performance rules governing this execution.
- **Limits / trade-offs:** map results go to local disk (not shared storage) — only final results go to a shared storage server; spreading machines out adds latency.
- **Situation cues:** "where are map outputs written and why?"; "when do reduce instances start?"; "who partitions input and terminates the job?"; "final results written where?"
- **Past-paper Qs:** 25S1 Q5

### L06-P2-C05 MapReduce example: word counting
- **Slides:** P2 s8-11
- **Type:** Application
- **What it is:** "Given a text file, count the number of occurrences of all words in the file". "Map – data is partitioned into 4 smaller data files ⇒ split 0 to split 3"; "Shuffle: Each smaller data file (split) is evaluated by a map task; A map produces data (partition) or intermediate results that belongs to different reduce tasks"; "Merge and sort – partitions on arriving at a reduce task are merged into one file and sorted to produce a sorted file"; "Reduce – evaluates the sorted file to produce the final result"; "MapReduce programme developer codes only the map and reduce functions ⇒ shuffle, merge and sort are taken care off by the MapReduce system implementation" (s8 and s10 are diagram slides). Pseudo-code (s11): map — "tokenize line" and "while (tokenizer has more tokens) output <key,value> pair for word"; reduce — "int sum = 0; sum = total number of 1s; output <key,value> pair for word" (reduce "gets the word along with a list of 1s").
- **Look-alikes:** execution steps (s7) — general protocol; this applies it to counting words; programme structure (s5) — the abstract read/map/shuffle/reduce/write sequence this example follows.
- **Limits / trade-offs:** developer writes only map and reduce; the system handles shuffle, merge and sort.
- **Situation cues:** "count word occurrences across splits"; "map emits <word, 1> pairs"; "reduce sums the 1s per word"; "who does the merge and sort?"
- **Past-paper Qs:** 25S1 Q5 (s9)

### L06-P2-C06 MapReduce parallelism
- **Slides:** P2 s12
- **Type:** Application
- **What it is:** (diagram slide) "Master program creates data-localised tasks to minimise network communication" (annotation: "minimal communication -> minimum latency"); "Worker nodes switch between mapper and reducer" (annotation: "cost reduction: reuse the machine that did mapping to do reducing"); "Map workers run in parallel: Each has its own data set; Each creates intermediate local values from each input data set"; "Reduce workers run in parallel: May reduce intermediate data; There is an optimal number of reducers for best performance".
- **Look-alikes:** execution steps (s7) — the protocol being parallelised; FaaS elastic scaling (s20-21) — scaling of event functions, not of batch map/reduce workers.
- **Limits / trade-offs:** too many reducers hurts performance — there is an optimal number for best performance (per 25S1 Q3, too many workers overload the master); data locality is used to cut network communication.
- **Situation cues:** "why place tasks where the data lives?"; "reuse mapper machines as reducers"; "what happens with too many reducers/workers?"; "optimal worker count for best performance".
- **Past-paper Qs:** 25S1 Q3

### L06-P2-C07 MapReduce applications in industry
- **Slides:** P2 s13
- **Type:** Reference-only
- **What it is:** Google: "Indexing for Google search", "Organising articles in Google news", "Performing various user statistics". Meta: "Data Mining", "Optimising ads for users", "Detecting spam on Facebook".
- **Look-alikes:** none within this lecture — a factual list of who uses MapReduce for what.
- **Limits / trade-offs:** none stated.
- **Situation cues:** "what does Google use MapReduce for?"; "what does Meta use it for?"
- **Past-paper Qs:** none

### L06-P2-C08 Hadoop and HDFS
- **Slides:** P2 s14-15
- **Type:** Reference-only
- **What it is:** "Issue: Google MapReduce – closed source, developed by Google (2004) to process large amounts of raw data"; "Solution: Hadoop MapReduce – open source, developed by Apache + Yahoo". Hadoop "Presents MapReduce as an analytics engine with a distributed storage layer referred to as Hadoop Distributed File System (HDFS)"; "HDFS mimics Google File System (GFS)"; "Very popular implementation of MapReduce" (annotation: "large scale data processing").
- **Look-alikes:** GFS — the closed-source Google original that HDFS mimics; Spark (s18) — a different engine that can run on top of Hadoop.
- **Limits / trade-offs:** none stated.
- **Situation cues:** "open-source MapReduce?"; "what storage layer does Hadoop add?"; "which system does HDFS mimic?"
- **Past-paper Qs:** none

### L06-P2-C09 Hadoop architecture and multi-node deployment
- **Slides:** P2 s16-17
- **Type:** Reference-only
- **What it is:** (diagram slides) Hadoop stack: "Hadoop YARN — Yet Another Resource Negotiator — Resource Allocation Scheduler"; "Hadoop MapReduce — Computation"; "HDFS — Storage". Slide 17 shows Hadoop on multi-node with annotations "where is slow?" and "why store things on disk?".
- **Look-alikes:** HDFS (s15) — the storage layer within this architecture; Spark (s18) — replaces/extends the computation layer, not the storage layer.
- **Limits / trade-offs:** none stated (annotations hint disk I/O and slow nodes are pain points).
- **Situation cues:** "which Hadoop layer schedules resources?"; "which layer computes, which stores?"; "what does YARN stand for?"
- **Past-paper Qs:** none

### L06-P2-C10 Apache Spark vs Hadoop MapReduce
- **Slides:** P2 s18
- **Type:** Reference-only
- **What it is:** "Fast, in memory data processing engine"; "Can run independently or on top of Hadoop"; "Designed for real-time and advanced analytics" (annotation: "because nowadays more memory available than 5 years ago"). Comparison table: "Batch Processing — Spark: Yes (annotation: speedup) — Hadoop: Yes"; "Real-time Processing — Spark: Yes — Hadoop: No"; "Machine Learning — Spark: Built-in (MLlib) — Hadoop: Need external tools".
- **Look-alikes:** Hadoop MapReduce (s14-16) — batch-only, needs external tools for ML; Spark adds in-memory, real-time and MLlib.
- **Limits / trade-offs:** Hadoop has no real-time processing and needs external tools for machine learning; Spark's speedup comes from in-memory processing.
- **Situation cues:** "need real-time analytics on a cluster"; "built-in machine learning library"; "in-memory instead of disk-based processing".
- **Past-paper Qs:** none

### L06-P2-C11 Function-as-a-Service (FaaS) and serverless
- **Slides:** P2 s20-22
- **Type:** Application
- **What it is:** (s22 is a diagram slide) "Approach to build scalable, reactive, event-driven applications" (annotation: "there's an event, you want to react to it as fast as you can"); "Uses functions as unit of deployment – application is divided into smaller, single-purpose (Lambda) functions"; "Event triggers a lambda function and exits after execution"; "No idle capacity!" (annotation: "e.g. fire alarm -> you just react and run"); "Lambda is stateless" (annotation: "just like REST API!"). Serverless: "Build (serverless) applications without the need to provision or manage servers ⇒ consumer only pays when code is executing"; "No VMs/containers in the programming model"; "Vendor provides provision-free scalability, i.e., scale with workload"; "Use Cases: Web/mobile backends, real-time data processing, chatbots, virtual assistants, . . ." (annotation: "server is taken care of for you").
- **Look-alikes:** PaaS (P1 s19-20) — PaaS still has you manage deployment of an always-running app; FaaS runs single-purpose functions per event with no idle capacity; VMs/containers — absent from the FaaS programming model; REST APIs — similarly stateless.
- **Limits / trade-offs:** functions are stateless and exit after execution (see s24 for the persistence disadvantage); you pay only while code executes — no idle cost.
- **Situation cues:** "bursty, event-driven workload with long idle periods"; "fire alarm: react fast, then stop"; "no servers to provision, pay per execution"; "web/mobile backend or chatbot backend"; "function must remember something between calls?" (it can't).
- **Past-paper Qs:** 24S2 Q19, 25S1 Q4, 25S2 Q12, 25S2 Q25

### L06-P2-C12 FaaS best practices
- **Slides:** P2 s23
- **Type:** Application
- **What it is:** "Functions should perform only one action" (annotation: "lightweight"); "Functions should be self-contained ⇒ should not call other functions"; "Use as few libraries as possible".
- **Look-alikes:** the "single-purpose (Lambda) functions" idea from s20 — best practices operationalise it; microservices look-alike (inferred): both favour small single-purpose units, but s23 is about individual functions not calling each other.
- **Limits / trade-offs:** self-containment forbids function-to-function calls; minimal libraries keep functions lightweight.
- **Situation cues:** "should one function do two things?"; "can a lambda invoke another lambda?"; "how many libraries to bundle?"
- **Past-paper Qs:** none

### L06-P2-C13 FaaS vs PaaS vs Containers vs VMs
- **Slides:** P2 s24-25
- **Type:** Application
- **What it is:** "Provisioning time is much lower – ms vs minutes vs hours!"; "Ongoing administration is almost none"; "Allows for elastic scaling as each action is inherently scaled"; "No capacity planning required"; "Limited ability to persist connections and state must be kept in an external service or resource" (annotation: "disadvantage!", "stateless just like RESTApi", "cookies -> maintain state"). "FaaS provider manages all maintenance (similar to PaaS)"; "High availability is inherent in the FaaS model"; "Resource utilisation is excellent" (annotation: "another advantage: easier debugging cos functions are smaller"); "FaaS model has resource limits".
- **Look-alikes:** PaaS — similar provider-managed maintenance, but PaaS apps are long-running with provisioning in minutes not ms; VMs/containers — hours of provisioning time and ongoing administration; REST/cookies — state must be kept externally (e.g. cookies pattern).
- **Limits / trade-offs:** limited ability to persist connections and state (must use external service); FaaS has resource limits; in exchange: near-zero administration, inherent elastic scaling and high availability, no capacity planning.
- **Situation cues:** "need sub-minute provisioning"; "who maintains the servers in each model?"; "function must hold a connection open?" (can't — externalise state); "which model has inherent high availability?"
- **Past-paper Qs:** 24S2 Q18 (also L02), 25S2 Q7

### L06-P2-C14 How a lambda function runs
- **Slides:** P2 s26-27
- **Type:** Reference-only
- **What it is:** (s26 is a diagram slide) "Lambda function – your application logic, i.e., code you want to execute (Java, Node.js, Python, . . .)"; "Configuration – defines how your code is executed, i.e., configure event sources that invoke your functions"; "Example: Processing an event when an API gateway receives an HTTPS request"; "System takes care of code to integrate event source with lambda function, manage infrastructure that detects events and invoke lambda, etc.".
- **Look-alikes:** AWS Lambda setup steps (s28) — the concrete 3-step workflow for the same mechanism; FaaS concept card (s20) — here the mechanics of code + event-source configuration.
- **Limits / trade-offs:** the platform, not the developer, integrates event sources and manages the invoking infrastructure.
- **Situation cues:** "code + configuration: which part defines event sources?"; "HTTPS request hits an API gateway and triggers my function"; "who wires the event source to the function?"
- **Past-paper Qs:** none

### L06-P2-C15 Using AWS Lambda
- **Slides:** P2 s28-29
- **Type:** Reference-only
- **What it is:** 3 steps: "1 Create lambda service: Business logic (code); Configuration – region to run, AWS credentials, etc.; Event – the event that triggers a lambda function; 2 Deploy service created; 3 Invoke/test your service". Interfaces: "Web Interface: AWS Management Console"; "Command Line Interface: AWS SAM CLI" (Serverless Application Model); "There are also some 3rd party CLIs available".
- **Look-alikes:** how a lambda runs (s26-27) — the underlying mechanism; this is the operational how-to on AWS.
- **Limits / trade-offs:** none stated.
- **Situation cues:** "what are the three things you configure when creating a lambda?"; "which CLI is used for serverless apps on AWS?"; "create → deploy → invoke/test".
- **Past-paper Qs:** none


## Diagram facts (Claude Haiku, from slide images)

- P1 s8 three-tier: presentation (UI) / application (logic) / data (persistent stores).
- P1 s11 REST: distributed hypermedia; stateless servers; platform/language independent; caching. Red notes: "lightweight option", "hypermedia - different types of media".
- P1 s12 REST principles: uniform interface, client-server decoupling, statelessness, cacheability, layered system, code on demand (optional). Red: statelessness = system has no knowledge of previous connection; cacheability = repeated requests faster.
- P1 s16 pyramid: SaaS end users (Gmail, Trello, Slack, Office 365); PaaS software developers (Heroku, Cloud Foundry, OpenShift, Flynn); IaaS network architects/IT admins (AWS, Azure, VMware, Stackscale).
- P1 s17 SaaS: consumers supply data, obtain results; provider develops app, running transparent. Services: business, social networks, document mgmt, mail.
- P1 s18 SaaS provider traits: multi-tenanted, web access, centralised mgmt, multi-device, scalability under varying loads, high availability, API integration.
- P1 s19 PaaS diagram: consumer (app developer) -> load-balancing layer -> virtual dev/testing platform (runtime, frameworks, DBs, testing tools) -> virtualization layer -> dev/testing platform -> VMs; PaaS provider provides. Services: languages, frameworks, DBs, other tools. Red: "used by application developers".
- P1 s21 IaaS diagram: consumer (infrastructure architect) -> load balancing layer -> VMs -> virtual infra (compute/network/storage) -> virtualization layer -> physical infra; IaaS provider provides physical. Services: compute, network, storage, load balancers.
- P1 s22 IaaS provider traits: web access to resources, centralised physical mgmt, elastic/dynamic scaling, shared infra across users, preconfigured VMs, metered. Red: "LAMP stack - packaged dev env".
- P1 s23 Key question: which as-a-service? "It depends".
- P1 s25 SaaS example steps: access app/AI, give data, report.
- P2 s8 word count: mapper per line emits (word,1); reducer gets lists e.g. not,1,1 -> not,2; "for simplicity, we left out the sort phase".
- P2 s10 dataflow: input -> splits 0-3 -> map tasks -> partitions (colour per reducer) -> shuffle (merge & sort) "taken care by implementation" -> reduce tasks -> to HDFS. Map phase vs reduce phase (shuffle stage + reduce stage).
- P2 s13 uses: Google indexing/news/stats; Meta data mining/ads/spam.
- P2 s14-15 Hadoop: open-source MapReduce (Apache + Yahoo) vs Google closed (2004); HDFS mimics GFS.
- P2 s16 Hadoop stack: YARN (resource allocation/scheduler) / MapReduce (computation) / HDFS (storage).
- P2 s17 multi-node: local HDFS -> InputFormat -> splits -> RecordReaders -> (K,V) -> map -> partitioner -> shuffle (intermediate pairs exchanged by all nodes) -> sort -> reduce -> OutputFormat -> writeback to local HDFS. Blue note: "where is slow? why store things on disk?"
- P2 s22 nesting: event-driven computing ⊃ FaaS ⊃ serverless FaaS.
- P2 s23 FaaS best practices: one action (blue: lightweight); self-contained, should not call other functions; few libraries.
- P2 s26 Lambda: event source -> events -> lambda function -> services.
- P2 s28 Lambda 3 steps: create (code, config: region/credentials, triggering event), deploy, invoke/test.
- P2 s29 Console or AWS SAM CLI; 3rd-party CLIs.
