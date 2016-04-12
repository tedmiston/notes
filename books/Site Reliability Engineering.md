# Site Reliability Engineering
*How Google Runs Production Systems*<br>
Edited by Betsy Beyer, Chris Jones, Jennifer Petoff & Niall Richard Murphy

- [Official site](https://g.co/SREBook)
- [Safari Books Online](https://www.safaribooksonline.com/library/view/site-reliability-engineering/9781491929117/)
- [O'Reilly](http://shop.oreilly.com/product/0636920041528.do)
- [Dan Luu's notes](http://danluu.com/google-sre-book/) [[HN]](https://news.ycombinator.com/item?id=11474002)

Software is run far longer than the amount of time it takes to implement.  Google's SRE team attempts to build *everything else* to support Google's apps and services post-development.  This book is a collection of principles, practices, and management to bring some of their ideas into your own organization.

---

### Foreword

- Google was scaling up at the time the sys admin role was being redefined (into DevOps)
- Google's way forward was the Site Reliability Engineer (SRE)
- Stories about building Google's infrastructure, but also how it studied & decided which tech to use
- In our "just show me the code" culture, "Google ... dared to think about the problems from first principles"
- "Stories like these are far more valuable than the code or designs they resulted in. Implementations are ephemeral, but the documented reasoning is priceless. Rarely do we have access to this kind of insight."
- not just scaling computer architecture, but also business process

### Preface

---

## I. Introduction

### 1. Introduction
### 2. The Production Environment at Google, from the Viewpoint of an SRE

---

## II. Principles

### 3. Embracing Risk
### 4. Service Level Objectives
### 5. Eliminating Toil
### 6. Monitoring Distributed Systems
### 7. The Evolution of Automation at Google
### 8. Release Engineering
### 9. Simplicity 

- "Software systems are inherently dynamic and unstable."
- You could only make it perfectly stable if you could prevent change (in the codebase, libraries, userbase, ...)
- SREs balance agility vs. stability

#### System Stability Versus Agility
#### The Virtue of Boring
#### I Won't Give Up My Code!
#### The "Negative Lines of Code" Metric

- Software gets bloated over time from adding new features, which also introduces the opportunity for more bugs
- "A smaller project is easier to understand, easier to test, and frequently has fewer defects."
- "Some of the most satisfying coding I’ve ever done was deleting thousands of lines of code at a time when it was no longer useful."

#### Minimal APIs
#### Modularity
#### Release Simplicity

#### A Simple Conclusion

- Software must be simple to be reliable
- Simplifying the steps of a task is not being lazy: it's clarifying what needs to be accomplished and the easiest path
- Saying "no" to features keeps the environment uncluttered from distractions to focus on real engineering

---

## III. Practices

### 10. Practical Alerting from Time-Series Data
### 11. Being On-Call
### 12. Effective Troubleshooting
### 13. Emergency Response
### 14. Managing Incidents
### 15. Postmortem Culture: Learning from Failure
### 16. Tracking Outages
### 17. Testing for Reliability
### 18. Software Engineering in SRE
### 19. Load Balancing at the Frontend
### 20. Load Balancing at the Datacenter
### 21. Handling Overload
### 22. Addressing Cascading Failures
### 23. Managing Critical State: Distributed Consensus for Reliability
### 24. Distributed Periodic Scheduling with Cron
### 25. Data Processing Pipelines
### 26. Data Integrity: What You Read Is What You Wrote
### 27. Reliable Product Launches at Scale

---

## IV. Management

### 28. Accelerating SREs to On-Call and Beyond
### 29. Dealing with Interrupts
### 30. Embedding an SRE to Recover from Operational Overload
### 31. Communication and Collaboration in SRE
### 32. The Evolving SRE Engagement Model

---

## V. Conclusions

### 33. Lessons Learned from Other Industries
### 34. Conclusion
