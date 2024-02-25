QUESTION 2 WEB INFASSTRUCTURE

1.What distribution algorithm your load balancer is configured with and how it works ? It uses round robin algorithm and it is the most common one requests are distributed across the group of servers sequentially. Request 1 is directed to server 1, request 2 to server 2, and so forth.

2.Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both .Active-Active Load Balancing: * In an Active-Active setup, all load balancers actively distribute traffic simultaneously. This means that multiple load balancers are operational and handling incoming requests at the same time. * Each load balancer in the Active-Active configuration actively participates in the distribution of incoming traffic, effectively sharing the load. * This setup offers better scalability, fault tolerance, and performance because the workload is distributed across multiple instances. * If one load balancer fails, the others continue to handle traffic seamlessly, ensuring high availability.

    Active-Passive Load Balancing:
        In an Active-Passive setup, one load balancer (the active node) handles all incoming traffic, while the other load balancer (the passive node) remains idle unless the active node fails.
        The passive node monitors the active node and takes over its duties only when the active node becomes unavailable due to failure or maintenance.
        This setup provides redundancy and failover capabilities, but it may not utilize resources as efficiently as Active-Active since the passive node remains idle until needed.
        Failover in an Active-Passive configuration usually involves some downtime or interruption during the transition from the active to the passive node.

    How a database Primary-Replica (Master-Slave) cluster works Master-slave replication enables data from one database server (the master) to be replicated to one or more other database servers (the slaves). The master logs the updates, which then ripple through to the slaves. If the changes are made to the master and slave at the same time, it is synchronous. The difference between the Primary node and the Replica node in regard to the application is that-, the primary node is regarded as the authoritative source, and the replica node (also known as slave) databases are synchronized to it(Master).

    What is the difference between the Primary node and the Replica node in regard to the application .Primary Database (Master):
        The primary database (or master) is the main database server that handles both read and write operations.
        All write operations, such as INSERTs, UPDATEs, and DELETEs, are performed on the primary database.
        The primary database is responsible for coordinating transactions and ensuring data consistency.

    Replica Databases (Replicas or Slaves):
        Replica databases (or slaves) are copies of the primary database.
        Replicas are used to offload read operations from the primary database, improving read scalability and performance.
        Replicas are asynchronously synchronized with the primary database. This means that changes made to the primary database are replicated to the replica databases with some delay, depending on the replication lag.
        Read operations, such as SELECT queries, can be distributed across replica databases to distribute the load and improve performannce.

    Where are SPOF SPOF stands for "Single Point of Failure." It refers to any component within a system that, if it fails, will cause the entire system to fail. Single points of failure are weaknesses in a system's n. design that can lead to downtime, data loss, or other undesirable consequences. Here are some common areas where SPOFs can exist:

    Hardware Components:
        Individual hardware components such as hard drives, power supplies, network interface cards, or memory modules can be single points of failure. If any of these components fail, they can disrupt the functioning of the entire system.
    Network Infrastructure:
        Network switches, routers, and cables can also represent single points of failure. If a critical network device fails or if there's a problem with the network connectivity, it can isolate parts of the system or bring down the entire network.
    Software Dependencies:
        Dependencies on specific software libraries, services, or APIs can create single points of failure. If a required software component fails or experiences issues, it can affect the functionality of the entire system.
    Power and Environmental Factors:
        Power outages or fluctuations, cooling system failures, or environmental hazards such as fires or floods can all lead to single points of failure if the system isn't adequately protected or redundant systems aren't in place.
    Human Factors:
        Human error or misconfiguration can introduce single points of failure into a system. For example, if only one person possesses critical knowledge or access rights and becomes unavailable, it can disrupt operations.
    Load Balancers and Redundancy:
        While load balancers are often used to distribute traffic and enhance reliability, they can themselves become single points of failure if there's no redundancy or failover mechanism in place. Similarly, if redundancy mechanisms are misconfigured or fail to activate properly, they can introduce single points of failure.
    Database Systems:
        In database systems, a single database server without replication or failover mechanisms can represent a single point of failure. If the database server fails, it can result in downtime and data loss.

6.Security issues (no firewall, no HTTPS) Not having a firewall and not using HTTPS can lead to several security issues, leaving systems vulnerable to various threats and attacks. Here are some of the potential security risks associated with these shortcomings:

    Unauthorized Access:
        Without a firewall, there is no barrier between the internal network and the external internet. This leaves the system exposed to unauthorized access attempts from malicious actors. Attackers can exploit open ports and unprotected services to gain entry into the system.

    Data Interception:
        Without HTTPS encryption, data transmitted between the server and clients is sent in plain text, making it susceptible to interception by eavesdroppers. This puts sensitive information, such as usernames, passwords, and personal data, at risk of being compromised.

    Man-in-the-Middle Attacks:
        In the absence of HTTPS, attackers can execute man-in-the-middle (MitM) attacks, where they intercept communications between the client and server. By inserting themselves into the communication path, attackers can eavesdrop on sensitive data or manipulate the data exchanged between the two parties.

    Data Tampering:
        Attackers can modify or tamper with data transmitted over unencrypted connections. This could lead to the injection of malicious code or the alteration of legitimate data, resulting in data integrity issues or the compromise of system functionality.

    Credential Theft:
        Without HTTPS encryption, login credentials transmitted over the network, such as usernames and passwords, can be captured by attackers using techniques like packet sniffing. Once obtained, these credentials can be used for unauthorized access to accounts or systems.

    DDoS Attacks:
        A firewall helps protect against Distributed Denial of Service (DDoS) attacks by filtering incoming traffic and blocking malicious requests. Without a firewall, systems are more vulnerable to DDoS attacks, which can overwhelm servers, disrupt services, and lead to downtime.

    Exposure of Vulnerabilities:
        Operating without a firewall and HTTPS can expose vulnerabilities in the system to potential attackers. Unprotected services and open ports provide entry points for exploitation, increasing the likelihood of successful attacks targeting known vulnerabilities in the system's software or configuration.
        MONITORING When there is no monitoring in a system, several negative consequences can occur, leading to operational inefficiencies, increased risk exposure, and potential disruptions to services. Here are some of the key impacts of lacking monitoring:

    Undetected Issues: Without monitoring, issues within the system may go unnoticed for extended periods. This includes performance degradation, resource constraints, software bugs, security breaches, and hardware failures. Without timely detection, these issues can escalate and cause significant problems.

    Reduced Availability: Monitoring plays a critical role in maintaining system availability. Without monitoring, there is no proactive alerting of potential problems or impending failures. As a result, downtime may occur unexpectedly, leading to service disruptions, loss of productivity, and negative impacts on users or customers.

    Increased Mean Time to Repair (MTTR): When issues arise without monitoring, the time to identify and resolve them increases significantly. Without real-time visibility into system health and performance metrics, troubleshooting becomes more challenging and time-consuming, resulting in a higher mean time to repair (MTTR) for incidents.

    Security Vulnerabilities: Monitoring is essential for detecting security incidents, such as unauthorized access attempts, malware infections, or unusual network activity. Without monitoring, security breaches may go unnoticed, allowing attackers to exploit vulnerabilities and compromise the integrity, confidentiality, or availability of systems and data.

    Missed Performance Optimization Opportunities: Monitoring provides valuable insights into system performance and resource utilization. Without monitoring, opportunities to optimize performance, streamline processes, and allocate resources efficiently may be missed. This can result in suboptimal system performance, increased operational costs, and wasted resources.

    Inefficient Resource Management: Monitoring helps in identifying resource bottlenecks and capacity constraints. Without monitoring, it's challenging to accurately assess resource usage and plan for future growth or scaling requirements. This may lead to over-provisioning or under-provisioning of resources, resulting in inefficient resource utilization and increased costs.

    Lack of Compliance: Many industries have regulatory requirements or compliance standards that mandate monitoring and reporting of system activity, performance, and security incidents. Without monitoring, organizations may fail to meet these compliance requirements, risking fines, legal consequences, and damage to their reputation.


