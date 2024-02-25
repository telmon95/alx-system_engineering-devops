0x09. Web infrastructure design

README.md

2-secured_and_monitored_web_infrastructure

For every additional element, why you are adding it

What are firewalls for It establishes a barrier between a trusted internal networks and untrusted external networks

Why is the traffic served over HTTPS Traffic that is served over Hypertext Transfer Protocol Secure which in short is HTTPS encrypted and secure, which provides several important benefits for both website owners and users

What monitoring is used for monitoring is essencial to maintain reliability and security and it also provides raeltime insights and detects issues early.

How the monitoring tool is collecting data monitaring tool collects data through various mechanisms depending on the data that has to be monitored or application that needs observation.

Explain what to do if you want to monitor your web server QPS If you want to monitor your web server's QPS (Queries Per Second), you can follow these steps: * Choose a monitoring tool that supports measuring QPS metrics. * Configure the monitoring tool to monitor the web server where QPS data is needed. * Set up appropriate monitoring checks or probes to collect QPS data from the web server. * Define thresholds or alerting rules to trigger notifications if QPS exceeds or falls below acceptable levels. * Monitor and analyze the collected QPS data regularly to identify any performance issues, trends, or anomalies. * Take proactive measures to optimize server performance, scale resources as needed, or troubleshoot any issues impacting QPS.

    Terminating SSL at the load balancer level:
        While terminating SSL at the load balancer can offload SSL decryption from backend servers, it can be an issue for security and scalability reasons.
        Single point of failure: If the load balancer fails, all SSL termination would cease, disrupting the entire application's availability.
        Limited scalability: SSL termination at the load balancer can limit scalability since SSL decryption is a resource-intensive process. As traffic increases, the load balancer may become a bottleneck, impacting performance.
        Reduced security: Decrypting SSL at the load balancer exposes sensitive data (such as credentials, session tokens) on internal network segments, increasing the risk of data interception or unauthorized access.
    Having only one MySQL server capable of accepting writes:
        This setup poses several potential issues, primarily related to availability, reliability, and performance:
        Single point of failure: If the MySQL server goes down, all write operations will fail, causing downtime and potentially data loss.
        Scalability limitations: A single MySQL server may not handle high write loads efficiently, leading to performance degradation during peak periods.
        Data consistency: Without redundancy or failover mechanisms, there's a risk of data inconsistency or loss in case of hardware failure or database corruption.
        Limited geographic redundancy: Having a single writable MySQL server makes it challenging to implement geographically distributed redundancy or disaster recovery solutions.
    Having servers with all the same components (database, web server, and application server):
        This setup can introduce several issues related to scalability, resource utilization, and fault isolation:
        Resource contention: Combining multiple services on the same server can lead to resource contention, where one service monopolizes system resources, impacting the performance of others.
        Difficulty in scaling: Scaling individual components becomes challenging since they are tightly coupled. For example, scaling the database layer may require scaling the web and application servers as well, even if they don't require additional resources.
        Lack of fault isolation: If one component experiences issues or failures (e.g., database server crashes), it can impact the entire server, affecting all services hosted on it.
        Reduced flexibility: Having all components on the same server reduces flexibility in deployment and maintenance. Updates or changes to one component may require downtime or affect the availability of others.


