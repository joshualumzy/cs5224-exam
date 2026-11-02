"""Question bank for Mocks B and C (part 1).

Source tags: 24S2 = 2425-Sem2 paper, 25S1 = 2526-Sem1, 25S2 = 2526-Sem2. OWN = written for the mock.
Wording is the past paper's own, except: arrows fixed, one stray backtick removed (25S2 Q6), and the
"deployment*" correction in 24S2 Q25 applied. `ans` / `why` feed the answer key only, never the question sheet.
"""

# ---------------------------------------------------------------- MCQ (1 mark)
MCQ = {}
SA = {}


def mcq(src, lec, text, opts, ans, why):
    MCQ[src] = dict(src=src, lec=lec, text=text, opts=opts, ans=ans, why=why, marks=1)


def sa(src, lec, text, sample, marking, lines=5, table=None):
    SA[src] = dict(src=src, lec=lec, text=text, sample=sample, marking=marking, lines=lines, table=table, marks=2)


# ---- Real MCQs: Mock B ------------------------------------------------------
mcq("24S2 Q1", "L02",
    "Which one of the following would be the best use case for SaaS?",
    ["Applications with highly confidential and sensitive data",
     "A mobile application",
     "An application used by an organisation with people working around the world, where some have erratic or unreliable internet connections",
     "Organisations looking to reduce on-premises IT infrastructure and capital expenditure",
     "Applications that need a lot of user data"],
    "d", "Option (d). For the rest, SaaS is not a practical application to use.")

mcq("24S2 Q7", "L02",
    "Which of the following is an example of Software as a Service (SaaS)?",
    ["Microsoft Azure", "Amazon EC2", "Google Cloud Platform", "Google Photos", "Amazon EMR"],
    "d", "Option (d). Rest are all cloud provisions, either PaaS or IaaS.")

mcq("24S2 Q9", "L02",
    "Which of the following scenarios is best suited for using a hybrid cloud model?",
    ["A government agency hosting sensitive data", "A startup hosting a website", "A user hosting a blog",
     "A large enterprise with varying workloads", "A startup having a lot of data"],
    "d", "Option (d). Hybrid clouds allow balancing between private and public clouds.")

mcq("24S2 Q15", "L05",
    "What is one key advantage of using virtual machines over containers?",
    ["Requires less memory space", "More secure", "Faster startup time", "Easy to scale", "More cost-effective"],
    "b", "Option (b). Each VM is isolated, while containers can be impacted by the OS being compromised.")

mcq("25S1 Q7", "L01",
    "Assuming you are moving from an on-premise deployment to a cloud deployment, which is the most important area of concern?",
    ["Scalability", "Security", "Load Balancing", "Storage", "Bandwidth"],
    "b", "Security. The rest depend on SLAs and what you can get, but by going to the cloud your data is no longer under your control to some extent.")

mcq("25S1 Q8", "L03",
    "You are running a cloud environment and realise you need a load balancer. What is its primary purpose?",
    ["To ensure a high bandwidth between your application and the client",
     "To automatically adjust the necessary amount of computing resources that are used by your applications",
     "To distribute incoming service requests across multiple servers",
     "To ensure that data in the cloud is synchronised across multiple servers",
     "To manage the various computing resources within a datacenter"],
    "c", "Option (c).")

mcq("25S1 Q18", "L05",
    "You realise that using containerised applications in a datacenter environment gives you certain advantages. Which one of the following could be one of them?",
    ["Increases the physical size of the server infrastructure",
     "Eliminates the need for cloud-based applications",
     "Improves isolation between applications and operating system",
     "Reduces the number of physical servers needed",
     "Reduces the overall cost"],
    "c", "Option (c).")

mcq("25S2 Q1", "L03",
    "How does an Application Load Balancer enable reliability?",
    ["By routing traffic to the least busy instances", "By routing traffic away from failed instances",
     "By caching frequently accessed content", "By replacing failed instances", "By routing traffic to new instances"],
    "b", "Option (b).")

mcq("25S2 Q3", "L05",
    "Which one of the following statements is correct regarding virtualization?",
    ["Virtualization increases compatibility among hardware that use different standards",
     "Operating System virtualization is better suited for an application which requires direct communication with hardware resources",
     "In hardware-assisted virtualization, the guest operating system directly communicates with hardware resources",
     "Virtualization technology allows the isolation of applications running on the same server",
     "Virtualization allows multitenancy only when it is Type 2"],
    "d", "Option (d). Comes directly from the definition in some ways.")

mcq("25S2 Q5", "L02",
    "A public-sector platform must keep both data and metadata within one country's borders and prevent foreign access under all circumstances. Which cloud deployment model is the best fit?",
    ["Public Cloud", "Private Cloud", "Hybrid Cloud", "Sovereign Cloud", "Multi Cloud"],
    "d", "Option (d). Bookwork.")

mcq("25S2 Q17", "L04",
    "Your users are reporting increased levels of latency. On checking you notice that CPU usage is actually low. What may be the primary cause then?",
    ["Servers are overprovisioned", "Too many instances have been set up", "Horizontal scaling",
     "Network bottleneck", "Usage of CDNs"],
    "d", "Option (d). Most probable cause for increased latency.")

mcq("25S2 Q20", "L01",
    "Which one of the following is an optimal strategy to employ when you have a very large number of reads and write operations to a scalable cloud database?",
    ["Horizontal scaling", "Vertical scaling", "Increasing storage", "Cloud bursting", "Migrate to a faster database"],
    "a", "Option (a). Horizontal scaling lets you distribute these reads and writes across multiple nodes.")

mcq("24S2 Q18", "L06",
    "Out of the following five compute models, which one requires the most maintenance?",
    ["PaaS and VMs", "FaaS and Containers", "PaaS and Containers", "Containers and VMs", "PaaS and FaaS"],
    "d", "Option (d). PaaS is managed by the provider, while FaaS requires low maintenance.")

mcq("24S2 Q19", "L06",
    "You wish to migrate to the cloud to run a simple server side computation which maintains no state about clients. Which of the following is best suited for this purpose?",
    ["Amazon EC2", "REST", "SOAP", "AWS Lambda", "Amazon EMR"],
    "d", "Option (d). Use FaaS: computations are simple and no state is maintained.")

mcq("25S1 Q3", "L06",
    "Which one of the statements below about the number of workers in a MapReduce framework is correct?",
    ["Too many workers can reduce overall efficiency because it overloads the master node's task and increases data transfer overhead between workers",
     "The number of workers has no effect on performance, because MapReduce automatically balances tasks perfectly",
     "Using fewer workers than available CPUs is always better, because it reduces network usage and eliminates the risk of data skew",
     "MapReduce performance depends only on the size of the input data, not on the number of workers assigned",
     "Having too few workers is not efficient because total worker idle time increases"],
    "a",
    "Option (a). (b) is wrong as more workers usually reduces latency up to a point. (c) is wrong because some CPUs would sit idle and network is not the only overhead. (d) is wrong because the number of workers does affect latency. (e) is wrong because fewer workers mean each gets more tasks, which decreases idle time.")

mcq("25S1 Q4", "L06",
    "You have an idea for an app that finds local festivity celebration parties. During the few festivities throughout the year (e.g. New Year, National Day, etc.) many users will use your app to find the most suitable party for them to go to based on users' criteria. Which AWS service is the most suitable to the usage profile and also cost effective?",
    ["EC2: Virtual server to run your app", "S3: Store static app contents (party flyers, images) and serve directly to users",
     "Elastic Beanstalk: Managed EC2 with auto-scaling", "CloudFront: Cache contents and reduce latency for app users",
     "Lambda: App logic as a serverless function"],
    "e",
    "Option (e). Traffic is bursty during festive periods but not otherwise. Lambda has no continuous cost when idle. EC2 and EBS incur continuous cost even when idle. CloudFront and S3 are only for static content and do not handle app logic.")

mcq("25S1 Q5", "L06",
    "According to the MapReduce execution flow described in the slides, which statement most accurately describes the data flow and the division of responsibility between the developer and the system?",
    ["The developer codes the Map function, which writes intermediate data to a shared storage server, and the Reduce function, which reads from that shared storage to aggregate results",
     "The developer codes the Map and Reduce functions, but must also explicitly implement the \"Shuffle and Sort\" logic to ensure intermediate data is correctly grouped for the reducers",
     "The Master instance partitions the input data, assigns segments to Map instances, and then directly sends the intermediate output from each Map instance to the correct Reduce instance",
     "The developer's Map function writes intermediate results to the local disk of its worker node; the MapReduce system is then responsible for shuffling, merging, and sorting this data before feeding it to the developer's Reduce function",
     "Map instances run in parallel, and Reduce instances run in parallel. To optimize performance, a Reduce worker is always placed on the same node as the Map worker that generated its data, eliminating network shuffling"],
    "d", "Option (d). Bookwork.")

mcq("25S1 Q13", "L06",
    "Who amongst the following are primary users of PaaS?",
    ["Clients looking to use a software online", "Software developers", "System administrators",
     "Hardware engineers", "Network engineers"],
    "b", "Option (b).")

mcq("25S2 Q7", "L06",
    "Which requirement is the clearest sign that a workload is a poor fit for FaaS?",
    ["It is triggered by file uploads", "It requires long-lived stateful sessions and persistent in-process connections",
     "It performs short request-driven transformations", "It runs sporadically and scales by event volume",
     "It requires long-lived stateless sessions"],
    "b", "Option (b). The rest all work fine for FaaS.")

mcq("25S2 Q12", "L06",
    "Which of the following best describes a serverless application?",
    ["A serverless application is usually developed in the context of PaaS",
     "The developer of a serverless application needs to pay a small fee for the idle periods",
     "A serverless application does not need a server/host to run on",
     "The developer of a serverless application does not need to provision or manage any servers",
     "The developer of a serverless application has lower costs"],
    "d", "Option (d).")

mcq("25S2 Q8", "L10",
    "A company has already made significant investments in on-premise infrastructure. Migrating to the cloud would require substantial additional costs for integration. Which of the following is the most appropriate conclusion based on this scenario?",
    ["Cloud is always cheaper because it reduces upfront capital expenditure",
     "Reserved cloud pricing eliminates migration and integration costs",
     "On-premise solutions always have lower operational costs than cloud",
     "Past investments should not be considered when evaluating future decisions",
     "Cloud adoption may be less attractive due to high migration and integration costs"],
    "e", "Option (e). (a) ignores sunk costs: it may be cheaper later, but there is no guarantee. (b) and (c) are not really options. (d) cannot ignore sunk costs.")

# ---- Own MCQs: Mock B ------------------------------------------------------
mcq("OWN-B1", "L07 (own)",
    "A team clusters 1,000,000 customer records (each a vector of purchase attributes) into k = 5 groups using k-means written as a MapReduce job. During one round, what does the map step emit?",
    ["One pair per customer record: (the ID of its nearest centroid, that customer's vector)",
     "One pair per cluster: (cluster ID, the new centroid and the number of points in it)",
     "One pair per customer record: (customer ID, its distance to each of the 5 centroids)",
     "One pair per map task: (cluster ID, the sum of the vectors that task has seen)",
     "Nothing: the map step only reads the data, and the reduce step assigns each point to a cluster"],
    "a",
    "Option (a). The mapper only labels: for each point it finds the nearest current centroid and emits (clusterID, point). N points in, N pairs out, only k distinct keys. Averaging the points into a new centroid and counting them is the reducer's job ((b) describes the reducer's output). Source: L07 k-means slides (s8-10).")

mcq("OWN-B2", "L07 (own)",
    "A video-sharing site runs its upload web servers and its video-converting (encoding) software on the same auto-scaling group of servers. After one video goes viral, many long conversions start at once. Uploads begin to time out even though there is plenty of storage space. Which change most directly fixes this?",
    ["Increase the size of the storage bucket that holds the videos",
     "Put a content delivery network in front of the upload servers",
     "Run the encoders in their own auto-scaling group; the upload servers save the raw video and leave a job message in a queue, and the encoders pick jobs from that queue",
     "Have each upload server call an encoder directly and wait for the conversion to finish before replying to the user",
     "Replace the servers with one larger server type for both jobs"],
    "c",
    "Option (c). Encoding is CPU-heavy, uploading is I/O-heavy; on shared servers the encodings use all the CPU and uploads time out. Separate groups scale independently, and the queue lets an upload finish as soon as the file is saved, so a spike only lengthens the conversion backlog. (d) is synchronous, so uploads would still wait on busy encoders. (b) and (a) do not touch the CPU contention. (e) is vertical scaling and still shares one pool. Source: L07 video-app slides (s20-30) and my reasoning.")

mcq("OWN-B3", "L05 (own)",
    "A cloud provider runs the virtual machines of many customers on the same physical server. A program inside Customer X's VM is compromised and tries to read the memory that belongs to Customer Y's VM on that same server. Which component is mainly responsible for stopping this?",
    ["The virtual private cloud's network access rules",
     "The hypervisor, which logically separates the VMs on the server",
     "The elastic load balancer in front of the servers",
     "The multitenant application's separation of each customer's data",
     "The cloud broker that sits between customers and the provider"],
    "b",
    "Option (b). The hypervisor logically separates the VMs and gives each its own share of CPU, memory and storage. A VPC only isolates network traffic. Application-level multitenancy separates customers inside one app instance, not VMs on a server. This was Mock A's Q23 weak spot. Source: L05 virtualisation slides; 24S2 Q2 option (d) wording.")

# ---- Real MCQs: Mock C ------------------------------------------------------
mcq("24S2 Q3", "L02",
    "Which level of cloud service is usually provided for the application to run the development environment?",
    ["PaaS", "IaaS", "SaaS", "FaaS", "None of the above"],
    "a", "Option (a).")

mcq("24S2 Q10", "L05",
    "Your company uses virtual machines (VMs) and is experiencing resource contention (e.g., CPU, memory, disk I/O, or network). Which solution is most effective to address this issue comprehensively?",
    ["Add more physical servers", "Add more memory", "Use faster storage devices", "Increase your network speeds",
     "Optimise VM resource allocation"],
    "e", "Option (e). Adding more physical servers may help, but it depends more on how the virtualisation is set up.")

mcq("24S2 Q13", "L02",
    "Your company has built a SaaS that is meant to serve around 5000 customers. However, your SaaS has become very popular (yay!) and suddenly there is a demand from about 25000 users. This will lead to an increase in resource utilisation. What are the incremental maintenance costs (mainly management overheads such as configuring servers, patching, etc.) of adding these new resources?",
    ["About the same as before", "Twice the original cost", "Three times the original cost",
     "Four times the original cost", "Five times the original cost"],
    "a", "Option (a). Not much extra maintenance, since the extra resources come from the cloud, which is managed by the cloud provider. There are likely extra running costs.")

mcq("24S2 Q14", "L05",
    "What is the advantage of a single tenancy cloud environment over a multitenancy environment?",
    ["Lower costs due to shared resources", "Enhanced data security and isolation", "Faster scalability for user spikes",
     "Simplified resource management", "Reduced need for compliance controls"],
    "b", "Option (b).")

mcq("24S2 Q17", "L10",
    "Your company operates a multi-cloud environment (e.g., AWS and Azure) and is experiencing data synchronization issues between the clouds, such as incomplete transfers or data loss. What is the most likely cause?",
    ["Slow storage performance on one cloud", "Limited virtualisation on one cloud", "Incompatible cloud APIs",
     "Uneven resource provisioning (e.g., storage, compute, or network)", "Inconsistent security configurations"],
    "d", "Option (d). You could end up with less space for the data on one of the clouds.")

mcq("24S2 Q20", "L01",
    "What is a primary challenge when migrating legacy on-premise systems to the cloud?",
    ["Decreased performance", "Increased data compliance", "Increased management", "Increased costs", "Application compatibility"],
    "e", "Option (e). (b) is not an issue if you choose the right cloud.")

mcq("25S1 Q1", "L02",
    "What is a key benefit of using cloud-based databases compared to traditional on-premise non-cloud databases?",
    ["Increased security", "Lower upfront costs", "Increased accessibility and scalability", "Cheaper storage", "Lower latency"],
    "c", "Option (c). (a) and (d) are not guaranteed.")

mcq("25S1 Q2", "L06",
    "You are the founder of a start-up with very limited personnel. Your company handles the input and processing of infectious disease clinical trial data on the cloud. The data processing needs to be real-time. The data contain highly sensitive, personally identifiable information. However, you want to reduce as much manual work as you can due to your small team. Which service should you choose for this application?",
    ["IaaS", "FaaS", "CaaS", "PaaS", "SaaS"],
    "d", "Option (d). SaaS gives the least manual work, but the data processing cannot be real-time and data privacy is also a concern. PaaS minimises work while meeting the privacy and real-time requirements.")

mcq("25S1 Q12", "L02",
    "You are part of an e-commerce start-up and wish to understand the shopping patterns arising from last year's sales events. In order to do this, you have been tasked with doing the data analysis where you have a lot of data. Which cloud deployment will you choose as the best option?",
    ["Public cloud only", "Private cloud only", "Hybrid cloud", "Either Public or Private cloud", "Multi-cloud"],
    "d", "Option (d), as either would be fine depending on your needs.")

mcq("25S1 Q14", "L01",
    "A company wants to move its deployment to the cloud but is worried about the security threats in the cloud. Which one of the following is the major security threat that the company needs to worry about?",
    ["Unauthorized physical access", "Data breaches due to multi-tenancy", "Outdated antivirus software",
     "Limited user authentication methods", "Data leaks due to bad programming practices"],
    "b", "Option (b).")

mcq("25S1 Q15", "L03",
    "Which one of the following statements is NOT true about Cloud Computing?",
    ["Opex includes expenses like electricity and maintenance for on-premise IT resources",
     "Detecting spam in social media is a good example of a use case for MapReduce",
     "PaaS is the cloud service that is usually provided to run the development environment",
     "Elastic scaling can dynamically increase or decrease server resources based on a specific period",
     "Higher security threats are a disadvantage of using public PaaS for SaaS development"],
    "d", "Option (d). There is no specific time period; elastic scaling depends on the load.")

mcq("25S1 Q16", "UNMAPPED",
    "Your company has a policy of encrypting all data that is stored. Your data is hosted in a virtual private cloud and attached to it are multiple storage devices which has the data that must be encrypted. You have the following options available. Based on this, which one of the following options will allow you to do this? (if multiple options are possible choose the one that allows you the most choice)\n"
    "(i) Ask clients to encrypt their data before they give it to you\n"
    "(ii) Use third party encryption tools to encrypt the data\n"
    "(iii) Use native encryption tools available in the Operating System to encrypt the data\n"
    "(iv) Encrypt your data within the application before storing",
    ["(i) or (iii)", "Only (iv)", "(ii) or (iii) or (iv)", "(i) or (ii) or (iii)", "(iii) or (iv)"],
    "c", "Option (c). All of these are fine. Asking clients is risky in case they forget. (Not covered by any lecture slide.)")

mcq("25S1 Q19", "L06",
    "When expecting a huge variation in traffic, as a cloud engineer, we need to be able to ensure the application can scale dynamically based on demand. Which cloud computing service model would we use to implement scalability?",
    ["Elastic load balancer", "SaaS", "Auto-scaling", "PaaS", "None of the above"],
    "d", "Option (d), as it provides scaling. (a) and (c) are not service models.")

mcq("25S2 Q2", "L06",
    "You wish to build your own application and are operating in a highly competitive market where being first is more important than being perfect, and rapid iteration is critical. Which cloud service model is most appropriate?",
    ["IaaS", "FaaS", "CaaS", "PaaS", "SaaS"],
    "d", "Option (d). PaaS enables the fastest building and deployment. IaaS takes time while SaaS is too restrictive since you wish to build your own application.")

mcq("25S2 Q13", "L09",
    "A company manages development, staging, and production environments using Terraform. Which one of the following approaches best avoids duplication and ensures consistency?",
    ["Copy-paste configurations per environment", "Use separate state files", "Use only one environment",
     "Hardcode environment values", "Keep separate code repositories"],
    "b", "Option (b). Copy-paste leads to issues; one environment is error-prone because it is monolithic; hardcoding is not an option; separate code repositories are harder to manage.")

mcq("25S2 Q14", "L09",
    "Your company has recently gotten to grips with Terraform and wish to use it. However, they also wish to have automatic drift detection during continuous integration (the practice of merging code changes into a central repository frequently). Which of the following is the best approach to achieve this?",
    ["Run terraform apply daily", "Disable drift checks", "Use manual audits", "Periodically recreate the infrastructure",
     "Run terraform plan and provide an alert on changes"],
    "e", "Option (e).")

mcq("25S2 Q15", "L06",
    "Which of the following are signs of a highly available application?\n"
    "(i) Applications are protected behind multiple layers of security\n"
    "(ii) Spikes in user demand are met through automatically increasing resources\n"
    "(iii) A failure in one geographic region will trigger an automatic switch to resources in a different region\n"
    "(iv) Virtualized hypervisor-driven systems are deployed as mandated by company policy\n"
    "(v) Application developers ensure the necessary software updates are applied",
    ["(i) and (iii)", "(ii) and (iv)", "Only (v)", "(ii) and (iii)", "(i) and (v)"],
    "d", "Option (d). Security and keeping software updated do not directly translate into availability.")

mcq("25S2 Q18", "L03",
    "A company, GreatestCloudOfAll Inc, have noticed that their cloud infrastructure frequently scales up and down, which is causing great instability and hence extra costs. You have been called in as an expert to advise them. What would your advice be?",
    ["You just need to increase your number of instances and it'll be fine",
     "You can re-check your thresholds for scaling and also add a cooldown period which prevents further scaling during this period",
     "You can monitor it and over time just disable scaling as that will help in the long run in this case",
     "Best is manual scaling, nothing beats it!",
     "Reduce the overall cost by reducing your number of instances"],
    "b", "Option (b). The rest are not practical. A cooldown period gives resources time to adjust before any further change.")

mcq("25S2 Q19", "L02",
    "A company wishes to migrate its legacy application to the cloud quickly with minimal changes. Which approach from the following would be most suited (you can assume that all options listed are technically feasible)?",
    ["Refactor the application to use serverless functions and then deploy it",
     "Get a cloud provider to build a SaaS equivalent solution for you and then use it",
     "Rewrite the application using a PaaS platform which allows for easy deployment",
     "Use IaaS and move application as is from on-premise to cloud",
     "Keep it on-premise"],
    "d", "Option (d). (b) may not be a choice depending on the application. The rest all take much more time and effort. (e) is not really an option.")

# ---------------------------------------------------------------- Short answers (2 marks)
# ---- Real SAs: Mock B ------------------------------------------------------
sa("25S1 Q21", "L10",
   "AWS provides instances that are optimized for different workloads. Some instances are memory-optimized, others are I/O optimized. You are assigned a project to be run on AWS. The project requires 60 Peta FLOPs and 800,000 I/O operations to complete. Assume that compute and I/O operation are sequential. The details of each instance are provided below. Which instance should you choose to optimize your project cost? Please show your working.\n"
   "Tera = 10^12. Peta = 10^15. FLOP = Floating Point Operations. ms = 10^-3 seconds.",
   "c5a, total $43,200. Time = FLOPs / speed + I/O ops x latency; cost = time x price. "
   "m7: 60000/1 = 60000 s + 800000 x 3 ms = 2400 s = 62400 s x $1 = $62,400. "
   "i8: 60000 + 800 = 60800 s x $2 = $121,600. "
   "c5a: 60000/3 = 20000 + 1600 = 21600 s x $2 = $43,200. "
   "r7: 62400 s x $2 = $124,800. "
   "g4: 60000/30 = 2000 + 8000 = 10000 s x $5 = $50,000.",
   "2 marks: correct instance (c5a) with working. Slips seen before: giving seconds instead of dollars; mis-scaling Tera/Peta (60 PFLOP = 60,000 TFLOP).",
   lines=12,
   table=dict(head=["Name", "Computation speed (TeraFLOP/s)", "I/O latency (ms/IOop)", "Price ($/sec)"],
              rows=[["m7 (General purpose)", "1", "3", "1"], ["i8 (I/O optimized)", "1", "1", "2"],
                    ["c5a (Compute optimized)", "3", "2", "2"], ["r7 (Memory optimized)", "1", "3", "2"],
                    ["g4 (GPU)", "30", "10", "5"]]))

sa("25S1 Q24", "L10",
   "You are responsible for the cloud infrastructure in company WeAreAwesome Inc. As awesome as you are, you have however noticed that your VMs that are running on the cloud are costing more than they should. Given your understanding of Cloud Computing, you wish to optimise the cost of running the VMs. Give two ways in which you can achieve this.",
   "Eliminate over-provisioning; use reserved instances for predictable workloads; use spot instances for non-critical workloads; use auto-scaling to scale down as necessary.",
   "1 mark per valid way, two needed.")

sa("25S1 Q25", "L02",
   "While setting up a new cloud deployment, you are tasked with ensuring that data availability must be high and that you must also comply with data protection guidelines which mandate that you must store Singapore customer data only within Singapore. How can you ensure compliance in such a scenario while keeping costs down? Briefly explain your answer.",
   "Use a sovereign cloud, or select specific regions for data storage, and ensure that data replication occurs only within those regions.",
   "Must cover both: compliance (data stays in Singapore) AND availability (replicate, but only within the allowed region/zones).")

sa("25S2 Q24", "L02",
   "A bank wants to move away from its legacy application and modernise it with strict compliance and some sensitive data. Which cloud service and cloud deployment model would you use and why?",
   "Hybrid cloud: sensitive workloads on private cloud, non-sensitive on public cloud. Build the new application through PaaS for the modern services; any legacy infrastructure can stay on IaaS. Key points: not all data is sensitive, and the application has to be rebuilt, which implies PaaS.",
   "Needs both a deployment model (hybrid, with the reason) AND a service model (PaaS for the new build, IaaS for legacy). One without the other loses marks.")

sa("24S2 Q23", "L02",
   "Your company is using a public cloud environment but is facing some security concerns regarding its data. As the lead cloud engineer, you are asked to come up with the solution, while keeping costs down. How would you do it? Explain your answer.",
   "Move to a hybrid cloud: sensitive data on a private cloud, less sensitive workloads on the public cloud. You could also move everything to a private cloud, but that would be more expensive overall.",
   "Must reach hybrid and give the cost reason (private only costs more).")

# ---- Own SA: Mock B -------------------------------------------------------
sa("OWN-B4", "L03/L01 (own)",
   "A ticketing company sells concert tickets. Traffic is close to zero on most days, but when a popular concert goes on sale, demand jumps to about 200 times normal for roughly 30 minutes. The company's on-premise servers are sized for the peak, sit idle the rest of the time, and still crash on sale days. Propose two ways the company can cope with the spike without paying for idle capacity afterwards.",
   "Any two of: (1) move to the cloud with a load balancer plus automatic (elastic) scaling that adds servers during the sale and removes them afterwards; (2) hybrid with cloud bursting: keep the normal load on-premise and spill over to pre-deployed cloud resources only past a threshold, then burst back in; (3) put a CDN/cache in front for static pages and a queue or serverless functions behind the checkout so extra work is absorbed and billed per use; (4) pay-as-you-go on-demand instances only for sale windows.",
   "1 mark per way. Each way must say how capacity comes back DOWN after the spike (scale in, burst in, per-use billing). 'Horizontal scaling' alone, or 'buy more servers', earns nothing: it names a direction and ignores scaling back down (Mock A Q25 slip).")

# ---- Real SAs: Mock C -----------------------------------------------------
sa("24S2 Q21", "L10",
   "You are a cloud developer who is deploying your application (which has a steady-state workload) to AWS. Which pricing option would you choose and why?",
   "Reserved: typically used to run 24/7 over the long term, and the cost is lower than on-demand.",
   "Reserved + reason (steady/long-running; cheaper than on-demand).")

sa("24S2 Q22", "L03",
   "The company you work for is responsible for a large web server farm. You are tasked with increasing the availability of this farm to ensure little to no downtime. List two ways in which you can achieve this.",
   "Availability = high probability the system is operational at a given time. Use scaling (auto-scaling in particular), and have redundancy where server instances are in multiple zones/locations.",
   "1 mark per valid way. Load balancer with health checks routing away from failed instances also fits.")

sa("24S2 Q25", "L02",
   "Your workplace wishes to make the work environment a bit more fun. They are going to provide advanced collaboration services, such as video, chat, and an online whiteboard. Given the cost of hosting the infrastructure for this, they have decided that a cloud-based approach is the way to go. Which cloud computing deployment model would best suit your company's needs? Explain your answer.",
   "It depends. The main issue is data security and privacy and whether you require it. If not required, go public cloud; if it is, a hybrid or private model would work.",
   "Must tie the choice to the security/privacy requirement and give both branches.")

sa("25S1 Q23", "L04",
   "It is the upcoming holiday season and your application has gained a lot of traction. However, the downside is that your cloud infrastructure is struggling with this load. You have looked into auto-scaling and load-balancing already. List two other methods that you can use to help with this issue.",
   "Use caching, CDNs, optimise the database for faster query processing, etc.",
   "1 mark per valid way; auto-scaling and load balancing are excluded by the question.")

sa("25S2 Q21", "L04",
   "Assume that you are responsible for organising your cloud resources globally as the leader of an enterprise. Discuss at least two key factors that you should consider when deciding on cloud resource hosting.",
   "Availability; cost of the cloud by region; location for latency; location for legal requirements. The question is about hosting cloud resources globally, not about deployment or service models.",
   "1 mark per factor with a reason. Deployment/service model answers do not count.")

sa("25S2 Q25", "L06",
   "You are a Solutions Architect at a leading technology company. The IT division of the metropolitan MRT (Mass Rapid Transit) system has approached you to design a next-generation payment platform to support SimplyGo and phase out the legacy EZ-Link card system. A key concern is that during peak hours, the current system experiences high latency, resulting in long queues and poor commuter experience. The reason for this is that for each user, the system performs fare calculation, balance deduction, and displays the update immediately before letting the user pass through the gate.\n"
   "Your task is to propose two ways in which this payment platform can be scalable and also have low-latency.",
   "The primary issue is the sequence of operations before the gate opens. Do only what is necessary to let the user through and do the other operations later: asynchronous processing, where FaaS or a similar element helps. Scalability must be elastic, scaling up and down with the number of users.",
   "Needs (1) asynchronous offloading of non-essential steps and (2) elastic scaling that also scales down.")

# ---------------------------------------------------------------- Mock definitions
MOCK_B = dict(
    code="B", title="Mock B", minutes=110,
    subtitle="Mixed, all lectures L01-L10 (essentials round)",
    mcq=["24S2 Q1", "25S1 Q3", "25S2 Q17", "24S2 Q15", "OWN-B1", "25S1 Q8", "25S2 Q5", "25S2 Q7", "24S2 Q9", "25S1 Q18",
         "25S2 Q1", "25S1 Q13", "OWN-B3", "25S2 Q20", "24S2 Q18", "25S1 Q4", "24S2 Q7", "25S2 Q3", "25S1 Q7", "25S2 Q8",
         "OWN-B2", "24S2 Q19", "25S2 Q12", "25S1 Q5"],
    sa=["24S2 Q23", "25S1 Q21", "OWN-B4", "25S1 Q25", "25S2 Q24", "25S1 Q24"],
)

MOCK_C = dict(
    code="C", title="Mock C, Part 1", minutes=90,
    subtitle="Mixed, all lectures L01-L10 (the remaining 25 real questions)",
    mcq=["25S2 Q13", "24S2 Q10", "25S1 Q1", "25S2 Q18", "24S2 Q17", "25S1 Q14", "25S2 Q2", "24S2 Q13", "25S1 Q19", "25S2 Q15",
         "24S2 Q20", "25S1 Q16", "24S2 Q14", "25S2 Q14", "25S1 Q12", "24S2 Q3", "25S2 Q19", "25S1 Q2", "25S1 Q15"],
    sa=["25S2 Q25", "24S2 Q22", "25S1 Q23", "24S2 Q25", "25S2 Q21", "24S2 Q21"],
)
