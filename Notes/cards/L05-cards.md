# L05 Cards

Built by DeepSeek V4.1 Flash from the slide text; diagram facts transcribed by Claude Haiku from the slide images. Built from the layout-preserved slide text of L05 (41 slides). Slides 4, 5, 7–11, 19, 21, 22, 24–26, 29, 34, 37 and 39 are diagram slides whose transcription is in the Diagram facts section at the end, so their cards use only the text present and are marked "(diagram slide, see Diagram facts at the end)". **Skipped:** slide 1 (title), 2 (outline), 39 (next week), 40 (references), 41 (feedback form). 'Type: Application' = can be tested in a scenario; 'Reference-only' = lookup. '(inferred)' = not stated on a slide. Paper names follow L04-cards: 2425-S2 = 24S2, 2526-S1 = 25S1, 2526-S2 = 25S2.

### L05-C01 Virtualisation: definition and why
- **Slides:** 3
- **Type:** Application
- **What it is:** **"Enables a single physical infrastructure to function as multiple logical infrastructure or resource"**. **"Many OSs can run and share a single hardware (one-to-many improves utilisation)"**, applied to **"processor, memory, storage, network"**. Why: **"Improve resource utilisation through sharing – lower cost, improve scalability, etc."**
- **Look-alikes:** Virtualisation vs multitenancy — virtualisation makes **logical infrastructure** out of physical infrastructure (slide 36 says it is the **"abstraction of physical resources"**), multitenancy is many tenants on one software instance; one-to-many here means many OSs on one machine, not many users on one app (inferred); utilisation vs scalability — both are listed as payoffs of the same sharing.
- **Limits / trade-offs:** None stated on this slide; the "cons" appear on slide 6 (performance overhead, single point of failure).
- **Situation cues:** "many workloads could share one box", "we are paying for hardware that sits idle", "run several operating systems on the same server", "one-to-many".
- **Past-paper Qs:** 25S2 Q3

### L05-C02 Before virtualisation: the 1:1 relationship
- **Slides:** 4
- **Type:** Reference-only
- **What it is:** **(diagram slide, see Diagram facts at the end)** The pre-virtualisation picture: **"Physical Infrastructure"** with a **"1:1 relationship with physical infra"** — one workload to one physical machine.
- **Look-alikes:** 1:1 here vs **many:1** after virtualisation (slide 5) — the two slides are the before/after pair; 1:1 vs one-to-many — the same contrast stated at slide 3.
- **Limits / trade-offs:** The 1:1 binding is the problem virtualisation removes; the slide states no consequence itself (inferred).
- **Situation cues:** "each application gets its own server", "nothing is shared", "utilisation is low".
- **Past-paper Qs:** none

### L05-C03 After virtualisation: many:1
- **Slides:** 5
- **Type:** Reference-only
- **What it is:** **(diagram slide, see Diagram facts at the end)** The post-virtualisation picture: **"Virtual Infrastructure"**, labelled **"many:1"** — many workloads served by one physical infrastructure.
- **Look-alikes:** many:1 vs 1:1 (slide 4); many:1 vs many OSs on one hardware (slide 3) — the same idea expressed as a ratio versus as a count.
- **Limits / trade-offs:** None stated on the slide.
- **Situation cues:** "several servers' worth of work on one host", "consolidate".
- **Past-paper Qs:** none

### L05-C04 Virtualisation: pros and cons
- **Slides:** 6
- **Type:** Application
- **What it is:** **Pros — Hardware Independence:** removes the **"software-hardware dependencies in traditional non-virtualised environment"**. **Resource Consolidation:** **"increase hardware utilisation, load balancing, . . ."**. **Resource Replication:** **"rapid scaling as resources are virtual (created as virtual disk images)"**. **Cons — Performance overhead**; **Single point of failure – virtualisation software**.
- **Look-alikes:** Consolidation vs replication — consolidation packs existing workloads onto fewer machines, replication spins up new ones as **virtual disk images** for scaling; consolidation vs the L02 idea of provider resource pooling (map lists 24S2 Q12 as L02 with L05 second) — here the benefit is stated as utilisation and load balancing, not cost to the consumer; performance overhead vs binary-translation overhead (slide 14) — one is the general con, the other its cause under full virtualisation (inferred link).
- **Limits / trade-offs:** The virtualisation software itself becomes a **single point of failure**, and running virtualised costs **performance overhead**.
- **Situation cues:** "the hypervisor crashed and took every VM with it", "we doubled the number of VMs per host", "we need more capacity this week without new hardware", "the same image is the basis for the new machines".
- **Past-paper Qs:** 24S2 Q10; 24S2 Q12 (L02 main, L05 second)

### L05-C05 The four types of virtualisation
- **Slides:** 7
- **Type:** Reference-only
- **What it is:** **(diagram slide, see Diagram facts at the end)** The taxonomy: **"Processor virtualisation, Memory virtualisation, Storage virtualisation, Network virtualisation"** — one card set (C06–C09) follows in that order.
- **Look-alikes:** These are the *resources* being virtualised; the *approaches* on slide 12 (full, para, hardware-assisted) are how the guest is made to run — different axes (inferred).
- **Limits / trade-offs:** None stated.
- **Situation cues:** "which resource is being abstracted", "pool of virtual processors".
- **Past-paper Qs:** none

### L05-C06 Processor virtualisation
- **Slides:** 8
- **Type:** Application
- **What it is:** **(diagram slide, see Diagram facts at the end)** **"Abstracting physical processor to pool of virtual processors"**. Diagram layers, top to bottom: **"guest (users)"**, **"virtualization layer"**, **"actual hardware"**.
- **Look-alikes:** The three layers vs the hypervisor discussion (slide 12) — the **virtualization layer** is the VMM's position in the stack; a pool of virtual processors vs one vCPU per VM — the pool is the shared abstraction the VMs draw from (inferred).
- **Limits / trade-offs:** None stated.
- **Situation cues:** "how many virtual CPUs can I hand out", "the CPU is shared between guests", "where does the virtualization layer sit".
- **Past-paper Qs:** none

### L05-C07 Memory virtualisation
- **Slides:** 9
- **Type:** Reference-only
- **What it is:** **(diagram slide, see Diagram facts at the end)** **"Providing virtual main memory to the VMs that are abstracted from the physical main memory"**.
- **Look-alikes:** Memory virtualisation vs storage virtualisation (slide 10) — **main memory** given to VMs versus **multiple logical storage**; the abstraction vs the physical DIMMs underneath (inferred).
- **Limits / trade-offs:** None stated on the slide.
- **Situation cues:** "each VM needs to believe it owns its RAM", "the guest's memory is not the physical memory".
- **Past-paper Qs:** none

### L05-C08 Storage virtualisation
- **Slides:** 10
- **Type:** Reference-only
- **What it is:** **(diagram slide, see Diagram facts at the end)** **"Providing multiple logical storage that is abstracted from multiple physical storage"**.
- **Look-alikes:** Storage vs memory virtualisation — one abstracts **multiple physical storage** devices into logical storage, the other abstracts **main memory**; logical storage vs virtual disk images (slide 6) — the image is what replication creates on top of it (inferred).
- **Limits / trade-offs:** None stated.
- **Situation cues:** "many disks presented as one", "logical volumes over physical arrays".
- **Past-paper Qs:** none

### L05-C09 Network virtualisation
- **Slides:** 11
- **Type:** Reference-only
- **What it is:** **(diagram slide, see Diagram facts at the end)** **"Process of abstracting physical network components to form a virtual network"**.
- **Look-alikes:** A virtual network vs the physical network components it abstracts; this vs container network isolation in Docker — Docker **"manages Docker objects such as images, containers, networks"** (slide 31), which is object management, not the same as abstracting physical network components (inferred).
- **Limits / trade-offs:** None stated.
- **Situation cues:** "VMs need their own virtual network", "abstract the switch ports".
- **Past-paper Qs:** none

### L05-C10 Virtualisation software: the hypervisor/VMM and privilege rings
- **Slides:** 12
- **Type:** Application
- **What it is:** **"Hypervisor or Virtual Machine Manager (VMM)"** — **"Software that sits between VMs and physical infrastructure"**; **"Allows IaaS provider to manage VMs and execute consumer's guest OS"** (slide text reads "guide OS") ; **"Physical infrastructure resources are shared among the consumer's VMs"**. Three approaches: **"Full Virtualisation, Para Virtualisation, Hardware-Assisted Virtualisation"**. **"Depending on the type of virtualisation approach, the virtualisation software and guest OS will run in different privileged levels"** — annotation: **"how does the guest talk to the hardware?"**; **"only privileged instructions (OS instructions) should reach the hardware"**; **"lower the ring number higher the privilege"**.
- **Look-alikes:** Hypervisor vs VMM — the same software under two names on this slide; virtualisation *software* vs virtualisation *approach* — the software is the VMM, the approach is how guest instructions reach hardware; ring number vs privilege — **lower ring = higher privilege**, so ring 0 is the most privileged (inferred direction of the stated rule).
- **Limits / trade-offs:** Only privileged instructions may reach hardware, so every design has to answer how the guest's OS instructions get there — that constraint drives the three approaches (inferred).
- **Situation cues:** "which ring does the VMM run in", "what stops a guest OS from issuing privileged instructions directly", "which approach avoids translating instructions".
- **Past-paper Qs:** none

### L05-C11 Full virtualisation: how it works
- **Slides:** 13
- **Type:** Application
- **What it is:** **"VM can run different guest OSs"**; **"Guest OS is not aware that it is virtualised"**; **"VMM at ring 0 provides all the virtual infrastructures needed for VMs, i.e., guest OS communicates with hardware through VMM"**; **"VMM translates guest OS instruction with instructions for the physical hardware"** — **Binary translation**, **software-assisted**. Annotations: **"VMM mimics the hardware"**, **"Talks to guest OS on hardware's behalf"**, **"Then translates the instruction to hardware"**.
- **Look-alikes:** Full vs para virtualisation — full keeps the guest OS **unaware** and translates, para needs a **modified** guest that makes hypercalls (slide 15); binary translation vs direct execution — the slide 18 table names the technique "Binary Translation and direct execution"; unaware guest vs hypervisor-independent guest — slide 18 answers "Yes" for full.
- **Limits / trade-offs:** The guest's unawareness is bought with translation on every privileged instruction (inferred from the mechanism); the cons are on slide 14.
- **Situation cues:** "run an unmodified Windows and Linux guest on the same host", "the guest OS cannot tell it is virtual", "the VMM mimics the hardware".
- **Past-paper Qs:** 24S2 Q5

### L05-C12 Full virtualisation: pros and cons
- **Slides:** 14
- **Type:** Application
- **What it is:** **Pros:** **"Provides VMs with best isolation and security"**; **"Different OSs can run simultaneously"**; **"Virtual guest OS can easily be migrated to native hardware"**; **"Easy to install and use – no changes to guest OS"**. **Cons:** **"Binary translation overhead – reduced system performance"**; **"Need for correct combination of hardware and software – hardware may not have drivers for virtualisation software"**.
- **Look-alikes:** "best isolation and security" vs the hypervisor's own attack surface (slides 24–26) — the isolation is the strongest of the three approaches, not absolute (inferred); "no changes to guest OS" vs para's "overhead of guest OS kernel modifications" (slide 16) — the trade the two approaches make; migration to native hardware vs migration to other hosts (slide 16 con for para).
- **Limits / trade-offs:** You pay **binary translation overhead** and need a **correct hardware/software combination**; in exchange you get the best isolation, simultaneous different OSs, and easy migration to native hardware.
- **Situation cues:** "the guest OS must stay unmodified", "we need the strongest isolation", "performance dropped after virtualising", "the vendor has no driver for the hypervisor".
- **Past-paper Qs:** none

### L05-C13 Para virtualisation: hypercalls
- **Slides:** 15
- **Type:** Application
- **What it is:** **"Modified guest OS replaces OS requests with hypercalls – also called OS-assisted virtualisation"**. **"Hypercalls – system calls with privilege to communicate directly between OS and hypervisor without translation"**. **"Guest OS knows it is running in a virtualised environment"**. Annotations: **"OS-assisted"**, **"VMM doesnt do translation"**, **"It gives guest OS an interface to talk to hardware"**.
- **Look-alikes:** Hypercall vs system call — a hypercall is described as a **system call with privilege** aimed at the hypervisor rather than the hardware; para vs full — the guest is **modified and aware** here, unmodified and unaware there (slide 13); "VMM gives an interface" vs "VMM mimics the hardware" — an interface replaces the imitation.
- **Limits / trade-offs:** Requires modifying the guest OS to make hypercalls; the price list is on slide 16.
- **Situation cues:** "the guest OS is aware it is virtualised", "no translation is happening", "the OS calls the hypervisor directly".
- **Past-paper Qs:** none

### L05-C14 Para virtualisation: pros and cons
- **Slides:** 16
- **Type:** Application
- **What it is:** **Pros:** **"Eliminates overhead of binary translation – improves performance"**; **"No need for special hardware"**. **Cons:** **"Overhead of guest OS kernel modifications"**; **"Modified guest OS cannot migrate to run on physical hardware"**; **"VMs lack backward compatibility, difficult to migrate to other hosts"**.
- **Look-alikes:** This con set vs full virtualisation's "can easily be migrated to native hardware" (slide 14) — the exact mirror image; "no need for special hardware" vs hardware-assisted virtualisation, which does need a **hardware (processor) extension** (slide 17); kernel modification overhead vs binary translation overhead — you swap one overhead for the other.
- **Limits / trade-offs:** Para virtualisation buys performance but locks the guest to the hypervisor: it **cannot run on physical hardware** and is **difficult to migrate to other hosts**.
- **Situation cues:** "we can patch the guest kernel", "performance matters more than portability", "the VM will not boot on bare metal", "moving to another hypervisor is painful".
- **Past-paper Qs:** none

### L05-C15 Hardware-assisted virtualisation
- **Slides:** 17
- **Type:** Application
- **What it is:** **"IaaS Consumer"**; **"Hardware (processor) extension supports virtualisation – guest states are stored in virtual machine control structures"**; **"OS requests directly trap the hypervisor – eliminates binary translation and guest OS modification"**; **"VMM has the highest root privilege, while guest OS and user applications have the same non-root privilege"**. Annotations: **"native virtualization"**, **"hardware steps in"**.
- **Look-alikes:** Trap vs hypercall — a trap is the guest's request being caught by hardware/VMM without the guest cooperating, a hypercall is the modified guest calling out; hardware-assisted vs full — both leave the guest unmodified, but here nothing is translated because the hardware traps; "VMM highest root privilege" vs the ring model (slide 12) — root privilege is the same idea expressed for this approach (inferred).
- **Limits / trade-offs:** Depends on a **hardware (processor) extension**; the slide's payoff is that it **eliminates binary translation and guest OS modification**.
- **Situation cues:** "the CPU supports virtualisation extensions", "guest states live in VM control structures", "guest OS and apps run non-root while the VMM is root", "no translation and no kernel patch".
- **Past-paper Qs:** none

### L05-C16 Comparing full, para and hardware-assisted virtualisation
- **Slides:** 18
- **Type:** Reference-only
- **What it is:** Summary **"from perspective of guest OS"**. Technique — Full: **"Binary Translation and direct execution"**; Para: **"Hypercalls"**; Hardware-Assisted: **"OS requests trap to VMM without binary translation or para virtualisation"**. Guest OS modification? — **No / Yes / No**. Compatibility — **Excellent / Poor / Excellent**. Is guest OS hypervisor independent? — **Yes / No / Yes**. Popular vendors — **VMware ESX / Xen / Microsoft, Virtual Iron, XenSource**. Annotations: full = **"no need guest OS modification but incur translation overhead"**; para = **"avoid overhead but needs to modify guest OS to make hypercalls"**; hardware-assisted = **"best of both worlds"**.
- **Look-alikes:** Compatibility vs hypervisor independence — in this table they move together (Excellent/Yes, Poor/No, Excellent/Yes), so they are not independent dimensions (inferred); "best of both worlds" vs full's "no modification" — hardware-assisted also needs no modification, but avoids the translation that full pays.
- **Limits / trade-offs:** The table is the trade in one line: no modification but translation overhead (full), no overhead but modification (para), neither cost (hardware-assisted, at the price of hardware support — inferred).
- **Situation cues:** "which approach keeps the guest OS hypervisor independent", "which one has poor compatibility", "which vendor belongs to which approach", "best of both worlds".
- **Past-paper Qs:** none

### L05-C17 Where the virtualisation layer sits
- **Slides:** 19
- **Type:** Reference-only
- **What it is:** **(diagram slide, see Diagram facts at the end)** The transition question only: **"next.. where does virtualization layer sit?"** — the position of the layer in the stack, answered by the two hypervisor types on slide 20.
- **Look-alikes:** This positioning question vs the three *approaches* (C11–C15) — the approaches are about instruction handling, this is about placement (inferred).
- **Limits / trade-offs:** None stated.
- **Situation cues:** "does the hypervisor sit on the hardware or on an OS", "where in the stack is the virtualization layer".
- **Past-paper Qs:** none

### L05-C18 Hypervisors: Type 1 vs Type 2
- **Slides:** 20
- **Type:** Application
- **What it is:** **"Two Types"**. **Type 1** — **"Also called Bare Metal (or native) – runs on physical infrastructure without any help from the host OS"**. **Type 2** — **"Hosted (or embedded) – requires the help of host OS to communicate with underlying infrastructure"**; **"e.g. VirtualBox, Parallels…"**. Annotation: **"runs directly on hardware"**; the slide's table is **"from perspective of hypervisor"**.
- **Look-alikes:** Type 1 vs Type 2 — help from a **host OS** or none at all; "bare metal / native" vs "hosted / embedded" — two names per type; Type 1 vs hardware-assisted virtualisation — "native" is used loosely both for a bare-metal hypervisor and for hardware-assisted virtualisation ("native virtualization", slide 17), so read which slide you are on (inferred caution).
- **Limits / trade-offs:** Slide 21 associates bare metal with **"larger scale applications"** and slide 22 hosted with **"smaller applications"**; no cost or performance figure is stated.
- **Situation cues:** "does the hypervisor need an OS underneath", "is VirtualBox Type 1 or Type 2", "the hypervisor runs straight on the hardware", "a desktop machine running VMs alongside its own OS".
- **Past-paper Qs:** 24S2 Q5 (second part, Type 1 vs containers)

### L05-C19 Bare-metal (Type 1) hypervisor
- **Slides:** 21
- **Type:** Application
- **What it is:** **(diagram slide, see Diagram facts at the end)** The **Bare Metal Hypervisor** stack: **"no host OS"**, annotated **"for larger scale applications"**; the hypervisor runs directly on the hardware (slide 20).
- **Look-alikes:** Bare metal vs hosted — absence of a host OS is the whole distinction; bare metal vs "running on physical infrastructure" (slide 20) — the same statement, one as a stack picture.
- **Limits / trade-offs:** Positioned for **larger scale applications**; no reason for the link is given on the slide.
- **Situation cues:** "there is no host OS in the stack", "the datacenter host runs the hypervisor directly", "large scale VM hosting".
- **Past-paper Qs:** none

### L05-C20 Hosted (Type 2) hypervisor
- **Slides:** 22
- **Type:** Application
- **What it is:** **(diagram slide, see Diagram facts at the end)** The **Hosted Hypervisor** stack, annotated **"for smaller applications"**; it **"requires the help of host OS to communicate with underlying infrastructure"** (slide 20), e.g. **VirtualBox, Parallels**.
- **Look-alikes:** Hosted vs bare metal — one extra layer (the host OS) in the stack; "for smaller applications" vs "larger scale applications" (slide 21) — the slide's own sizing rule, not a benchmark (inferred).
- **Limits / trade-offs:** Depends on the host OS to reach the infrastructure; sized by the slide for **smaller applications**.
- **Situation cues:** "a desktop app that runs VMs", "VirtualBox on my laptop", "the host OS must be running first".
- **Past-paper Qs:** none

### L05-C21 Hypervisor vendors and their type
- **Slides:** 23
- **Type:** Reference-only
- **What it is:** Vendor table. **Type 1:** **Xen — University of Cambridge Computer Laboratory**; **VMWare ESXi — VMware, Inc.**; **Hyper-V — Microsoft**; **KVM — Open virtualization alliance**. **Type 2:** **VMWare workstation — VMware, Inc.**; **Oracle Virtualbox — Oracle Corporation**; **Parallels Desktop — Parallels**.
- **Look-alikes:** ESXi vs Workstation — same vendor, different type (ESXi Type 1, Workstation Type 2); KVM vs Xen — both Type 1 but different approaches per slide 18 (Xen is the para-virtualisation vendor, KVM appears only here); VirtualBox's vendor is Oracle while slide 20 lists it as a Type 2 example — consistent, but the name is spelled "Virtualbox" here.
- **Limits / trade-offs:** None stated; the table is a lookup.
- **Situation cues:** "is Hyper-V Type 1 or Type 2", "which VMware product is bare metal", "name a Type 2 hypervisor".
- **Past-paper Qs:** none

### L05-C22 Hypervisor security attacks
- **Slides:** 24, 25, 26
- **Type:** Application
- **What it is:** Two attack surfaces: **"Host OS — Compromise the Host OS"** and **"Guest OS — Compromise the Guest OS"**; annotation **"less likely for hypervisor to get compromised"**. **Host OS attack:** **"highest privilege -> hypervisor"**; **"if host OS compromised hypervisor can compromise the guest OSes"**. **Guest OS attack:** **"if guest OS compromised hypervisor not compromised"**; **"virus is isolated"**. (Slides 25 and 26 carry the attack diagrams; details pending.)
- **Look-alikes:** Host OS compromise vs guest OS compromise — attacks travel *down* from a compromised host OS to the guests, but a compromised guest stays contained; "hypervisor has the highest privilege" (slide 17) vs "less likely for hypervisor to get compromised" — high privilege is the asset, low likelihood is the mitigation.
- **Limits / trade-offs:** Isolation is one-directional: guests do not reach the hypervisor, but a compromised host OS reaches every guest. Slide 25 is the counterweight to full virtualisation's "best isolation and security" (inferred).
- **Situation cues:** "one tenant's VM is infected — do the others fall", "the host OS was compromised, are the VMs safe", "where does a virus stop spreading".
- **Past-paper Qs:** none

### L05-C23 Containers vs VMs
- **Slides:** 27
- **Type:** Application
- **What it is:** Framing question **"do we really need a full fledged VM?"**. **"Containers allow existence of multiple isolated user space instances, e.g., Docker"**; **"Containers share the host system's kernel with other containers ⇒ lightweight"**. Annotation: **"quickly develop, deploy, test…"**.
- **Look-alikes:** Container vs VM — a container shares the **host system's kernel**, a VM carries a guest OS on top of the hypervisor; isolation of **user space instances** vs isolation of whole machines — the slide's "isolated" sits alongside "share the kernel", so the isolation is within one kernel (inferred); lightweight vs the VM alternatives' overheads (slides 14, 16).
- **Limits / trade-offs:** Sharing the kernel is what makes containers **lightweight**; the slide states no isolation guarantee, and sharing a kernel is the weaker boundary compared with a VM (inferred from "shares the host system's kernel" vs slide 14's "best isolation and security").
- **Situation cues:** "we do not need a whole OS per app", "many small services on one host", "start-up must be fast", "the container is lighter than the VM".
- **Past-paper Qs:** 24S2 Q15, 25S1 Q18

### L05-C24 Docker: what it is
- **Slides:** 28
- **Type:** Application
- **What it is:** **"Open Platform for developing, shipping and running applications"**; **"Enables you to separate your applications from your infrastructure so that you can deliver software quickly"**; **"Ability to package and run an application in a loosely isolated environment called a container"**; **"Containers are lightweight and contain everything needed to run the application ⇒ portability!"**; **"Uses the idea of namespaces to provide the isolated workspace"**; **"Written in the Go programming language and takes advantage of several features of the Linux kernel"**. Annotation: **"how does Docker run on Mac?… virtualization"**.
- **Look-alikes:** Image vs container — here the app is packaged; slide 32 defines the image as the read-only template and slide 33 the container as its runnable instance; namespaces vs a hypervisor — namespaces give the isolated workspace inside one kernel, a hypervisor separates kernels; "portability" vs running on Mac — the annotation points out Docker on Mac still relies on virtualisation, so portability is of the package, not of the kernel (inferred).
- **Limits / trade-offs:** Relies on **Linux kernel features**, so on a Mac it needs virtualisation (the slide's own annotation); "loosely isolated" is the slide's own hedge.
- **Situation cues:** "ship the whole runtime with the app", "it works on my machine", "the same image runs in dev and prod", "why does Docker need a VM on macOS".
- **Past-paper Qs:** 25S2 Q10; 24S2 Q2 (L02 main, L05 second — portability)

### L05-C25 Docker architecture
- **Slides:** 29
- **Type:** Reference-only
- **What it is:** **(diagram slide, see Diagram facts at the end)** **"Docker Architecture"**: **"Uses a client-server architecture"**, with a **"daemon… background processes listening for requests"** (annotation); source given as the Docker overview docs.
- **Look-alikes:** Client-server here vs "client and daemon communicate using a REST API" (slide 31) — the architecture at a glance versus the protocol; daemon as a background process vs the daemon's duties listed on slide 31 (inferred).
- **Limits / trade-offs:** None stated.
- **Situation cues:** "what talks to what in Docker", "the daemon is a background process".
- **Past-paper Qs:** none

### L05-C26 Docker Desktop
- **Slides:** 30
- **Type:** Reference-only
- **What it is:** **"Easy to install application for your host OS – enables you to build and share containerised applications and microservices"**; **"Includes Docker daemon, Docker client, Docker compose, . . ."**.
- **Look-alikes:** Docker Desktop vs Docker Engine — Desktop is a **bundle** that includes the daemon and client (inferred bundle reading from "Includes"); Desktop vs a container — Desktop is the installable application on the host OS, not a container.
- **Limits / trade-offs:** None stated; it is described as easy to install rather than the only way to run Docker (inferred).
- **Situation cues:** "how do I install Docker on my laptop", "what comes in the box".
- **Past-paper Qs:** none

### L05-C27 Docker client and daemon
- **Slides:** 31
- **Type:** Application
- **What it is:** **Docker Client:** **"Primary way users interact with Docker"**; **"Can communicate with more than one daemons"**. **Docker daemon:** **"Building, running and distributing the Docker containers"**; **"Listens for Docker API requests"**; **"Manages Docker objects such as images, containers, networks, etc."**; **"Can also communicate with other daemons to manage Docker services"**. **"Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface"**.
- **Look-alikes:** Client vs daemon — the client is the user's interface, the daemon does the building/running/distributing; either side can talk to several of the other — the slide says so of both; a daemon-to-daemon link vs a client-to-daemon link — both exist and both serve services management (inferred).
- **Limits / trade-offs:** None stated; the connection has three carrying options (REST API, UNIX socket, network interface).
- **Situation cues:** "who builds the container", "what listens for API requests", "can one client drive two hosts", "over what does the client reach the daemon".
- **Past-paper Qs:** none

### L05-C28 Docker registries and images
- **Slides:** 32
- **Type:** Application
- **What it is:** **Docker registries — "Stores images"**; **"Docker Hub is a public registry that anyone can use, and Docker looks for images on Docker Hub by default"**. **Images — "Read-only template with instructions for creating a Docker container"**; **"Often based on another image, but you can also create your own using a Dockerfile"**.
- **Look-alikes:** Registry vs image — the registry stores, the image is the stored artefact; image vs container — the image is a **read-only template**, the container is its runnable instance (slide 33); Docker Hub vs a registry — Hub is one public registry, not the only one (inferred from "a public registry").
- **Limits / trade-offs:** Images are read-only, so any change must be made by building a new image (inferred from "read-only template"); by default pulls come from Docker Hub.
- **Situation cues:** "where do images live", "what is a Dockerfile for", "the image is built on another image", "we need a private registry".
- **Past-paper Qs:** none

### L05-C29 Docker containers
- **Slides:** 33
- **Type:** Application
- **What it is:** **"Runnable instance of an image"**; **"Can create, start, stop, move, or delete a container using the Docker API"**; **"Can control how isolated a container's elements are from other containers or the host machine"**. Annotation: **"super lightweight"**.
- **Look-alikes:** Container vs image — instance versus template; how isolated a container's elements are vs the container sharing the host kernel (slide 27) — the tunable isolation lives inside a shared kernel (inferred); Docker API vs Docker client — the client is how users interact, the API is what the daemon listens for (slide 31).
- **Limits / trade-offs:** Isolation is a setting you control, not a fixed guarantee (slide wording "Can control how isolated…"); containers are described as **super lightweight**.
- **Situation cues:** "start and stop a container", "tune how isolated one container is", "the same image run twice gives two containers".
- **Past-paper Qs:** none

### L05-C30 Virtualisation and cloud service models
- **Slides:** 34
- **Type:** Reference-only
- **What it is:** **(diagram slide, see Diagram facts at the end)** A diagram titled **"Virtualisation and Cloud Service Models"** with the labels **"VMs"**, **"docker"** and **"multitenancy"** placed against the service models; the text itself does not say which model sits where (diagram transcription pending).
- **Look-alikes:** VMs vs Docker — two virtualisation technologies in the same picture; multitenancy vs both — a sharing arrangement rather than a technology (slide 36).
- **Limits / trade-offs:** Cannot be stated until the diagram is transcribed (inferred).
- **Situation cues:** "which service model do containers fit", "where do VMs sit in IaaS/PaaS/SaaS".
- **Past-paper Qs:** none

### L05-C31 Multitenancy: provider and consumer views
- **Slides:** 35
- **Type:** Application
- **What it is:** **Cloud Providers:** **"A single instance of software runs on a server and serves multiple tenants"**; **"Enable multiple users (tenants) to share the same application, e.g., cloud platforms, cloud services, etc."** (annotation: **"e.g. Dropbox, email"**). **Cloud Consumers:** **"Dedicated instance of software with customised view"**; **"Tenants isolation ensures that tenants do not have access to data and configuration information that it does not own"**.
- **Look-alikes:** "A single instance" (provider) vs "Dedicated instance" (consumer) — the same arrangement seen from the two sides, not a contradiction; single instance vs one instance per user — multitenancy is explicitly shared; tenant isolation vs virtualisation — isolation here is about **data and configuration information**, not hardware (slide 36 separates them).
- **Limits / trade-offs:** The consumer's dedicated view has to be produced from a single shared instance, and isolation is what stops cross-tenant access (inferred).
- **Situation cues:** "all customers use one deployment", "each customer sees only their own data", "one software instance, many tenants", "SaaS like Dropbox or email".
- **Past-paper Qs:** none

### L05-C32 Multitenancy vs virtualisation
- **Slides:** 36
- **Type:** Application
- **What it is:** **Multitenancy — "Dedicated consumer instance of software"**. **Virtualisation — "Abstraction of physical resources"**. **"In multitenancy, giving consumers an instance of the software (tenant usage & data isolation) is possible because of virtualisation"**.
- **Look-alikes:** The pair is the classic mix-up: virtualisation abstracts **physical resources**, multitenancy gives a **dedicated software instance**; note the direction of dependence — virtualisation **enables** multitenancy, not the reverse; "dedicated instance" here is the consumer's view, the provider still runs a single instance (slide 35).
- **Limits / trade-offs:** Multitenancy depends on virtualisation for tenant usage and data isolation; the slide gives no case where multitenancy exists without it (inferred).
- **Situation cues:** "is multitenancy the same as virtualisation", "what makes per-tenant isolation possible", "which one abstracts hardware".
- **Past-paper Qs:** 25S1 Q6

### L05-C33 Multitenancy example
- **Slides:** 37
- **Type:** Reference-only
- **What it is:** **(diagram slide, see Diagram facts at the end)** A worked **"Multitenancy Example"**; the slide text carries only the heading, so what the example depicts is not recoverable from the text.
- **Look-alikes:** To be filled from the diagram; slide 35's examples (**Dropbox, email**) are the only concrete instances named in text.
- **Limits / trade-offs:** Not stated.
- **Situation cues:** "show me tenants sharing one application".
- **Past-paper Qs:** none

### L05-C34 Multitenancy characteristics
- **Slides:** 38
- **Type:** Application
- **What it is:** Six characteristics. **Usage/Tenant Isolation — "one tenant's behaviour does not affect other tenants"**. **Data Security — "separate procedures for each tenant"**. **Recovery — "backup, restore"**. **Scalability — "usage by tenants and tenant numbers can increase"**. **Metered Usage — "each tenant is charged only for features being used"**. **Data Tier Isolation — "databases, tables, etc., can be isolated or allowed as shared resources among tenants"**. Annotation: **"different tenants will have different agreements, think Dropbox"**, **"e.g. you have 500mb, I have 1gb, someone has 1Tb, etc…"**.
- **Look-alikes:** Usage/Tenant Isolation vs Data Tier Isolation — one is behaviour not leaking between tenants, the other is whether databases/tables are isolated or shared; Data Security ("separate procedures") vs Data Tier Isolation — procedures versus data layout; Metered Usage vs the Dropbox storage annotation — the annotation illustrates differing agreements/quotas, which is the metering idea applied (inferred); scalability of usage vs scalability of tenant numbers — both listed under one heading.
- **Limits / trade-offs:** Data Tier Isolation is explicitly a choice: **"can be isolated or allowed as shared resources among tenants"** — sharing is permitted, not prohibited; isolation is per tenant, so per-tenant procedures, backups and charges all have to be maintained (inferred).
- **Situation cues:** "one tenant's batch job must not slow another", "each tenant needs its own backup", "tenants on different plans with different quotas", "do tenants share tables or get their own".
- **Past-paper Qs:** 24S2 Q14; 25S1 Q14 (L01 main, L05 second — map gives no L05 slide)

---

## Coverage

| Slide | Card(s) |
|---|---|
| 1, 2 | skipped (title, outline) |
| 3 | L05-C01 |
| 4 | L05-C02 (diagram, see Diagram facts) |
| 5 | L05-C03 (diagram, see Diagram facts) |
| 6 | L05-C04 |
| 7 | L05-C05 (diagram, see Diagram facts) |
| 8 | L05-C06 (diagram, see Diagram facts) |
| 9 | L05-C07 (diagram, see Diagram facts) |
| 10 | L05-C08 (diagram, see Diagram facts) |
| 11 | L05-C09 (diagram, see Diagram facts) |
| 12 | L05-C10 |
| 13 | L05-C11 |
| 14 | L05-C12 |
| 15 | L05-C13 |
| 16 | L05-C14 |
| 17 | L05-C15 |
| 18 | L05-C16 |
| 19 | L05-C17 (diagram, see Diagram facts) |
| 20 | L05-C18 |
| 21 | L05-C19 (diagram, see Diagram facts) |
| 22 | L05-C20 (diagram, see Diagram facts) |
| 23 | L05-C21 |
| 24, 25, 26 | L05-C22 (diagram, see Diagram facts) |
| 27 | L05-C23 |
| 28 | L05-C24 |
| 29 | L05-C25 (diagram, see Diagram facts) |
| 30 | L05-C26 |
| 31 | L05-C27 |
| 32 | L05-C28 |
| 33 | L05-C29 |
| 34 | L05-C30 (diagram, see Diagram facts) |
| 35 | L05-C31 |
| 36 | L05-C32 |
| 37 | L05-C33 (diagram, see Diagram facts) |
| 38 | L05-C34 |
| 39, 40, 41 | skipped (next week, references, feedback) |

Past-paper rows used: 24S2 Q5, Q10, Q14, Q15; 25S1 Q6, Q18; 25S2 Q3, Q10 (all 8 main L05 rows), plus second-lecture rows 24S2 Q2 and 25S1 Q14, marked as such. Nothing in the repo was modified.

## Diagram facts (Haiku transcription of the slide images; small labels approximate)

- **s4 Before virtualisation:** two stacks, each Applications on one OS (Linux left, Windows right), each directly on its own physical infrastructure (Processor, Memory, Storage, Network). Caption "1:1 relationship with physical infra".
- **s5 After virtualisation:** two VMs (Applications + OS each) sit on one "Virtual infrastructure" layer over one shared physical set (Processor, Memory, Storage, Network). Caption "many:1".
- **s7 Types:** processor, memory, storage, network virtualisation.
- **s8 Processor:** VMs see virtual processors (VP1..VP8); the virtualisation layer builds a "virtual processor pool" from the "physical multicore shared processor pool" (P1..P4). Labels: guest (users) / virtualization layer / actual hardware.
- **s9 Memory:** VMs see Vmem; "virtual main memory pool" built from the "physical shared distributed main memory pool" (MM1..MM4).
- **s10 Storage:** VMs see VDisks; "virtual disk storage pool" (VD1..VD7) built from the "physical shared disk storage pool" (D1..D4).
- **s11 Network:** hosts connect through "virtual private networks"; the virtualisation layer provides vNICs, vSwitches, vRouters, vFirewalls, virtual load balancer, built over the "physical network" (NICs, switches, routers, firewalls, load balancers).
- **s19:** break slide ("next.. where does virtualization layer sit?").
- **s21 Bare-metal hypervisor:** VMs (Guest OS + virtual processor/memory/storage/network) on a Hypervisor directly on physical shared infrastructure. Red: "no host OS", "for larger scale applications".
- **s22 Hosted hypervisor:** VMs on a Hypervisor which sits on a Host Operating System on the physical infrastructure. Red: "for smaller applications". Normal applications can also run directly on the host OS beside the VMs.
- **s24 Security:** two attack targets, "Compromise the Host OS" and "Compromise the Guest OS". Red: "less likely for hypervisor to get compromised".
- **s25 Host OS attack:** attacker compromises the host OS; red: "highest privilege -> hypervisor; if host OS compromised hypervisor can compromise the guest OSes".
- **s26 Guest OS attack:** a compromised guest OS tries to attack the neighbouring guest OS and the hypervisor; red: "if guest OS compromised hypervisor not compromised, virus is isolated".
- **s29 Docker architecture:** Client (docker run / build / pull) talks to the Docker Host (Docker daemon, with Images and Containers), which pulls from a Registry (Images, Extensions, Plugins). "Uses a client-server architecture"; daemon = background processes listening for requests.
- **s34 Virtualisation and service models:** three columns, each over a virtualisation layer on physical shared infrastructure: IaaS (infrastructure architects, VMs); PaaS (application developers, application run-time + database instances, development platform, docker); SaaS (application consumers, application + database instances with config files, hosted application, multitenancy).
- **s37 Multitenancy example:** Organization A and Organization B, each with a cloud service consumer, both use one multitenant application running on a hosting virtual server in the cloud.
- **s39:** next week is Applications and Paradigms (Part 1).
