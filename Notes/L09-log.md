# L09 Log

---

## S1. Prod and staging behave differently

**Scenario:** A startup's production was built over three months by one engineer clicking in the AWS console; a second engineer later built staging by hand from the same wiki page. A bug appears only in production. Q1: most likely cause given how the environments were built, and how the difference creeps in? Q2: the team moves to IaC: step by step, how does that stop it recurring, and one other way it improves how they test changes?

**Your answer:** Q1: "Configuration drift: the production environment and the wiki page don't reflect the same configuration, so staging was built without what causes the bug." Q2: "We can use software best practices: version control, CI/CD, testing, documentation. Before, something probably changed and the wiki was not updated; with version control everyone has the latest version and can manage versions, avoiding drift. It also makes testing repeatable and consistent, deterministic."

**Grade: about 60%.** Q1 about 70%: drift is right; how it creeps in was thin (not said: fixes clicked into production over three months never reach the wiki), and the second source was missed: a manual rebuild is error-prone, so a skipped step or a different default makes staging differ even from a perfect wiki. Q2 about 50%: version control named, but the core mechanism missed: both environments are *built from the same code*, so they are identical by construction, and every change is made by editing that code and re-applying, so the code is always the true record. "Repeatable, deterministic" is a label; the testing benefit is creating a production-like test environment on demand and running infrastructure changes through the CI/CD pipeline before production.

**Correct:** Q1: manual management is "manual and time-consuming, complex and error-prone" and suffers "configuration drift" (s5). Over three months, small fixes are clicked straight into production and never written into the wiki, so the wiki describes an older production; and rebuilding by hand from a long page invites a missed step or a different default setting. Nothing records what production actually contains, so nobody can find the difference. Q2: (1) the whole environment is written as code (s6); (2) production and staging are both created by running that same code, only parameters such as size differ, so they match by construction; (3) any change is made by editing the code, reviewing it in version control and re-applying, never by clicking, so the code always says exactly what is running and every change is visible in history (s7); (4) the code replaces the wiki. Testing: spin up a fresh production-like environment from the code whenever needed and tear it down after (s9), and run infrastructure changes through the CI/CD pipeline so they are tested before production (s7, s9).

---

## S2. Steps vs desired state

**Scenario:** An imperative script: create 3 VMs → create a load balancer → attach the 3 VMs. Since the first run, one VM was deleted by hand and the team now wants 5 VMs. Q1: what happens if the script is simply rerun; what must the engineer do to reach 5 working VMs with this script; how would a declarative tool handle it (mechanism)? Q2 (MCQ, false statement): A. declarative ends in the same state from an empty or partly built account; B. imperative suits a quick one-off task; C. with declarative the developer controls the exact creation order; D. imperative needs the developer to know the current state; E. declarative can overcomplicate a simple task.

**Your answer:** Q1: "Rerunning creates three more VMs and a second load balancer with those three attached, so I have a group of two VMs and a group of three, each with its own load balancer. To get to five, the engineer would have to somehow attach the groups together. A declarative tool just says: I want my end state to be 5 VMs with a load balancer." Q2: "C."

**Grade: about 70%.** Q1 about 55%: the rerun outcome is right. The fix is vague ("attach the groups together"): the point is that the engineer must first find out the current state himself (2 VMs, 1 load balancer) and write new steps for that exact starting point. The declarative mechanism is missing: stating the end state is the input, not how the tool gets there. Q2 100%.

**Correct:** Q1: the script blindly repeats its steps, so it creates 3 more VMs and a second load balancer: 5 VMs split across two load balancers, plus clean-up work ("less idempotent", s13). With imperative, "the developer needs to keep track of the system state and manage any necessary changes" (s10): check what exists (2 VMs, 1 load balancer), then write new steps: create 3 VMs and attach them to the existing load balancer. That script only works from that exact starting point. Declarative (s10, s12): the file says "5 VMs behind 1 load balancer"; the tool reads what actually exists, compares it with the file, and makes only the difference: creates 3 VMs and attaches them. Running it again changes nothing (idempotent). The same file works from an empty account or a half-built one ("starting point does not matter"), it repairs the hand-deleted VM ("adapts well to configuration drift"), and going from 3 to 5 is a one-number edit ("changes to destination handled automatically"). Q2: C. Declarative gives "less control" (s13); the tool decides the order (Terraform builds a dependency graph, s26).

---

## S3. A server fails at 3 a.m.

**Scenario:** An online shop runs on one server, `shop01`, hand-tuned and patched for four years; its disk fails at 3 a.m. and the shop is down until the sysadmin rebuilds it the next day. Q1: redesign so a 3 a.m. failure needs nobody: the setup, what happens step by step when a server dies, and IaC's role. Q2 (MCQ): best kept as a pet? A. web servers behind a load balancer; B. encoding workers pulling from a queue; C. old on-premise server running a one-of-a-kind licensed app nobody can rebuild; D. interruptible batch workers; E. containers running a stateless API.

**Your answer:** Q1: "Use AWS CloudFormation and specify that I want one disk running at all times. When the server dies there should be a self-healing kind of thing: AWS detects that a server has died and spins up a new instance. So IaC's role is the self-healing." Q2: "C."

**Grade: about 65% (regraded after his challenge).** Q1 about 40%: automatic detect-and-replace is right, and one auto-replaced server is a valid answer: the question asked for "nobody wakes up", not zero downtime, and his cost point holds (a definition costs nothing, so a single server with automatic replacement means paying for one server and accepting a few minutes of downtime). Still wrong: IaC's role. IaC does not watch servers; it defines the server so an identical copy is built in minutes with no hand-tuning. Detecting and replacing is done by health checks and auto-scaling (self-healing IaC is a future trend, s38-39). The steps (stop routing, launch from definition, discard the dead one) were missing. Q2 100%.

**His challenge:** "Nothing says the company needs multiple servers; aren't we paying for them all? Can't the servers be configured but not running, so one comes up only when needed?" Right: the cheap design is one running server plus a stored definition; the trade-off is downtime while the replacement boots. Several running servers cost more but give no downtime; pick by how much a few minutes of outage costs the shop.

**Correct:** Q1: treat servers as cattle (s20-21). Cheapest: one server built from IaC code inside an auto-scaling group of size 1 (pay for one; a few minutes of downtime on failure). No downtime: several identical web servers, all created from the same IaC code, behind a load balancer, with no unique data on any of them (orders and sessions in a separate database, L06). When one dies: (1) the load balancer's health check sees it stop answering and stops sending it traffic; (2) the remaining servers keep serving, so customers notice nothing; (3) the auto-scaling group sees one server fewer than wanted and starts a fresh one from the same definition (beyond slides, AWS docs); (4) the dead one is thrown away, not repaired. IaC's role: because the server is described in code, a replacement is identical and ready in minutes instead of a day of hand-tuning ("rapid, consistent deployment", s21). Q2: C, a pet is individually cared for and needs manual repair (s19); something that cannot be rebuilt from a definition cannot be cattle.

---

## S4. Choosing a tool

**Scenario:** A company runs on AWS and Google Cloud and wants one tool and workflow for both; its engineers are Python developers who want loops and conditions ("one database per country in this list"). Q1: which tool(s) fit and why; why are CloudFormation and Azure Resource Manager poor choices? Q2 (MCQ): true about Google Infra Manager? A. own template language unrelated to Terraform; B. you write a Terraform configuration and Infra Manager deploys it onto Google Cloud; C. also deploys application code, no other tool needed; D. can manage AWS too; E. imperative.

**Your answer:** Q1: "Pulumi, because it supports infrastructure code in familiar languages like Python. CloudFormation and ARM only work in their own clouds; they are not cloud agnostic. Terraform is cloud agnostic but doesn't let you write Python." Q2: "B."

**Grade: about 85%.** Q1 about 75%: Pulumi and the reasons against CloudFormation/ARM are right, but he never showed that Pulumi meets the first requirement (one tool for both clouds); the slides do not say it, so the answer should state it. Q2 100%.

**Correct:** Q1: Pulumi: code in Python with loops and conditions, "flexibility for more complex logic" (s33), and it works across clouds (beyond slides, Pulumi docs). Terraform is also defensible: multi-cloud and cloud agnostic (s23), with a large provider registry (s24); its own language is declarative and does have loops (beyond slides, Terraform docs), but it is not Python. CloudFormation and CDK are AWS only; ARM is Azure only (s15-16), so the Google Cloud half would need a second tool and workflow. AWS CDK is Python too, but still AWS only. Q2: B (s18); application deployment uses Cloud Build and Cloud Deploy (C false); it is for Google Cloud (D false); Terraform is declarative (E false).

---

## S5. Terraform in a team

**Scenario:** A team of four uses Terraform for production and wants dev and staging too. Engineer 1: copy the whole folder three times and edit each copy. Engineer 2: one folder and one state file for all three. Q1: what goes wrong with each, what structure instead and why it works? Q2 (MCQ): config has a network, 10 subnets inside it, 5 unrelated buckets; what does Terraform do? A. all 16 one at a time in file order; B. all 16 at once; C. network first, then subnets in parallel, buckets in parallel from the start; D. buckets first; E. number resources by hand.

**Your answer:** Q1: "Engineer 1 could introduce configuration drift between dev, staging and production, and Git merge conflicts when we merge. Engineer 2: maybe the state file becomes more complex? Actually the configuration shouldn't be in the state file, it should be in modules; the state file is something else. Modules is the structure to use." Q2: "C."

**Grade: about 50%.** Q1 about 30%: Engineer 1's copies diverging is right in idea; merge conflicts are not the issue (separate folders are never merged). Engineer 2's problem missed, with the configuration and the state file confused. Modules right, but separate state per environment missing, and no "why it works". Q2 100%.

**Correct:** Q1: Engineer 1: a fix made in one copy (e.g. production's security setting) is forgotten in the others, so the copies diverge and staging no longer tests what production runs. Engineer 2: the configuration (`.tf` files) is what you want; the state file is Terraform's record of what it actually created (s26), used to compare wanted with real. One state for all environments means every plan and apply covers dev, staging and production together, so a mistake made while changing dev can change or destroy production in the same run. Structure: write the infrastructure once as a module (s26 reusable components); each environment is a small configuration that calls the module with its own settings (sizes, counts) and has its own state file. One definition → environments cannot diverge and a fix reaches all; separate state → an apply in dev can only touch dev. Q2: C: Terraform builds a resource graph and creates non-dependent resources in parallel (s26).

**Follow-up question:** "Is the per-environment configuration a separate file, or inside the module?" Separate: the module is its own folder of `.tf` files with input variables; each environment is its own small folder whose configuration calls the module with its values, and each environment folder has its own state file.

---

## S6. Drift and security after IaC

**Scenario:** Everything is in Terraform. During a 2 a.m. outage the on-call engineer opens a firewall port by hand in the console and forgets; the code still says closed. Q1: name of the situation; how to detect it automatically; what happens at the next `terraform apply` and why that could be a problem? Q2 (MCQ, false): A. access keys in shared IaC code risk a breach; B. in GitOps an engineer reads the change in Git and applies it by hand; C. a security mistake in IaC code spreads to every environment, so the code needs continuous checking; D. a manual change can break compliance; E. self-healing IaC monitors, analyses against a baseline, then creates and carries out a fix.

**Your answer:** Q1: "Configuration drift. The team finds out through the state file, when Terraform compares the live system against the configuration. At the next apply, Terraform has to plan first so it knows what to do; if it runs apply directly it might assume the port is closed." Q2: "B."

**Grade: about 55%.** Q1 about 40%: drift right. Detection half right: the comparison is the right idea, but "automatically" was the point: run `terraform plan` on a schedule and alert when it shows changes. Next apply wrong: `terraform apply` makes its own plan first, checking the real cloud, so it does see the open port and closes it, silently undoing the 2 a.m. fix and possibly bringing the outage back. Q2 100%.

**Correct:** Q1: configuration drift (s5, s35): the live system no longer matches the code. Detect: run `terraform plan` automatically, e.g. nightly in the CI/CD pipeline; plan reads the real infrastructure, compares it with the configuration and lists the changes needed; any listed change means drift, so the pipeline alerts the team (reasoning; plan s28). Next apply: apply generates the execution plan itself (s29: "An execution plan has been generated"), sees the port open while the code says closed, and closes it: the hand fix is undone, possibly by someone applying an unrelated change, and the outage may return. Proper habit: after an emergency hand change, put it into the code (or revert it) through the normal review, so the code stays the true record. Compliance (s37): the open port may also break a security standard until it is fixed. Q2: B; GitOps deploys changes from Git to the system automatically (s38).

---

## Gap set

**G1.** Infrastructure kept in Git as a long script of AWS CLI commands, every change reviewed by pull request; staging and production still drift apart. Two reasons why. **Your answer:** "A command can be added to or run on one environment and not the other, so they aren't synced; with IaC one code is applied to both." **Grade: 50%.** One reason, right. Missing the second: the script only replays steps; it never compares with what is running, so a hand change in the console is never seen, and rerunning the script cannot bring a drifted environment back (it would duplicate or fail instead). **Correct:** (1) steps get run on one environment and not the other, so the script does not describe either environment's real state; (2) imperative scripts do not compare desired with actual, so manual changes go unnoticed and cannot be corrected by rerunning (less idempotent, s13; declarative "adapts well to configuration drift", s12).

**G2.** Config says 4 VMs, state records 4; one VM deleted by hand; `terraform apply` with no edits. Step by step and end result? **Your answer:** "Apply restores the four VMs, reversing the deletion. Wait: Terraform compares the configuration with the state file, sees no changes; the state file tracks the live system, so the deletion goes unnoticed." **Grade: 40%.** First instinct (back to 4) right, but the mechanism was reasoned the wrong way: the state file does not update itself when someone changes the cloud. **Correct:** (1) apply first refreshes: it reads the real cloud and finds 3 VMs; (2) compares with the configuration (4) and plans "1 to add"; (3) shows the plan and asks for "yes"; (4) creates 1 VM; (5) updates the state file to 4. End: 4 VMs (s25, s29-30; refresh: reasoning, Terraform docs).

**G3.** 3 identical Terraform-built servers in an auto-scaling group behind a load balancer; one crashes. **Your answer:** B. **Grade: 100%.**

**G4.** Dev and production in one folder with one state file; a dev database change; plan also lists a production database change. Why, and what structural fix? **Your answer:** "One state file tracks both, so when the dev database changes so does production. Fix: separate dev and production into different modules." **Grade: 50%.** Why: right that one state and one configuration cover both, so every plan covers production too. Fix wrong: modules alone, inside one folder with one state, still put both environments in every run. **Correct:** separate folders with **separate state files** per environment, each calling one shared module with its own settings; a plan in dev then cannot see or touch production.

**Gap-set result: about 60%.** The configuration vs state-file confusion appeared twice (S5, G2): star the INDEX row.
