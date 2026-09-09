# CyberShield Viva — 35 Questions and Simple Answers

1. **What is an IDS?**  
An Intrusion Detection System monitors activity and identifies suspicious behavior or security events.

2. **IDS vs IPS?**  
IDS detects and alerts. IPS is designed to prevent or block traffic. CyberShield is an IDS.

3. **What is network traffic?**  
It is data exchanged between devices over a network.

4. **What is packet sniffing?**  
Observing network packets for analysis. CyberShield uses it only for authorized monitoring.

5. **Why Scapy?**  
Scapy is a Python packet-processing library that can read packet metadata and PCAP files.

6. **What is TCP?**  
A connection-oriented transport protocol that provides reliable delivery.

7. **What is UDP?**  
A connectionless transport protocol with low overhead.

8. **What is ICMP?**  
A network-layer protocol used for diagnostics and control messages.

9. **What is DNS?**  
The Domain Name System maps domain names to IP addresses and supports other naming functions.

10. **What is a port?**  
A logical endpoint used by transport-layer applications.

11. **What is a port scan?**  
A pattern where one source attempts connections to many ports to discover reachable services.

12. **What is anomaly detection?**  
Finding activity that significantly differs from a learned or configured baseline.

13. **Signature/rule-based detection?**  
Known patterns are represented as rules and matching traffic produces alerts.

14. **What is a false positive?**  
Normal activity incorrectly classified as suspicious.

15. **What is a false negative?**  
Suspicious activity that the detector fails to identify.

16. **Why SQLite?**  
It is lightweight, file-based, and easy for a BCA project.

17. **Why Flask?**  
Flask is a lightweight Python web framework suitable for APIs and dashboards.

18. **How are passwords protected?**  
Only password hashes are stored using Werkzeug's password-hashing functions.

19. **How does the detection engine work?**  
It maintains short time windows of metadata, calculates rule metrics, and creates alerts when enabled thresholds are crossed.

20. **How does real-time monitoring work?**  
Scapy runs in a background thread, parses each observed packet into metadata, stores it, and invokes detection.

21. **What is PCAP?**  
A file format used to store captured network packets for later analysis.

22. **What are TCP flags?**  
Control bits such as SYN and ACK that describe TCP connection state.

23. **What is SYN?**  
A TCP flag used to begin a connection handshake.

24. **How are alerts generated?**  
The detection engine compares observed metadata with configured rules.

25. **Why thresholds?**  
Thresholds convert a measurable behavior into a configurable detection condition.

26. **What are the project limitations?**  
Heuristic rules may create false positives, and live capture depends on OS permissions/drivers.

27. **How can ML improve it?**  
ML could learn traffic baselines and identify more complex patterns.

28. **Can it become an IPS?**  
Conceptually yes, but that requires carefully governed active controls. This project intentionally does not block traffic.

29. **What ethical issues exist?**  
Monitoring must have authorization, minimize data collection, protect logs, and comply with applicable laws and policies.

30. **What future improvements are possible?**  
SIEM integration, RBAC, PostgreSQL, threat intelligence, ML, and better visualization.

31. **What is CSRF protection?**  
A security control that helps prevent unauthorized state-changing requests from another site.

32. **Why SQLAlchemy ORM?**  
It provides structured database access and reduces direct SQL handling.

33. **Why run capture in a background thread?**  
Packet capture can be continuous; a background thread keeps Flask request handling responsive.

34. **Why do we avoid packet payloads?**  
Payloads may contain sensitive information. Metadata is sufficient for this academic detection scope.

35. **What is Demo Mode?**  
A safe demonstration feature that creates synthetic metadata without transmitting attack traffic.
