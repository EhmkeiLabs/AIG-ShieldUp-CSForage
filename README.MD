# Task 1: Respond to a Zero-Day Vulnerability
## Background
You are an Information Security Analyst in the Cyber & Information Security Team.

A common task and responsibility of information security analysts is to stay on top of emerging vulnerabilities to make sure that the company can remediate them before an attacker can exploit them. 

In this task, you will be asked to review some recent publications from the Cybersecurity & Infrastructure Security Agency (CISA). The Cybersecurity & Infrastructure Security Agency (CISA) is an Agency that has the goal of reducing the nation’s exposure to cyber security threats and risks. 

After reviewing the publications, you will then need to draft an email to inform the relevant infrastructure owner at AIG of the seriousness of the vulnerability that has been reported. 

### Engagement
- Review some recent publications from the Cybersecurity & Infrastructure Security Agency (CISA).
- Research the reported vulnerability.
- Draft an email to affected teams to alert them of the vulnerability, and explain how to remediate.

### Instructions
The CISA has recently published the following two advisories:

The first advisory (Log4j), outlines a serious vulnerability in one of the world’s most popular logging software.
The second advisory explores how ransomware has been increasing and is becoming professionalized - a concern for a large company like AIG.
Your task is to respond to the Apache Log4j zero-day vulnerability that was released to the public by advising affected teams of the vulnerability. 

First, conduct your research on the vulnerability using the “CISA Advisory" resources provided above as a starting point.

Next, analyze the “Infrastructure List” below to find out which infrastructure may be affected by the vulnerability, and which team has ownership.

|Product Team|Product Name |Team Lead|Services Installed|
|---|---|---|---|
|IT|Workstation Management System|Jane Doe (tech@email.com)|OpenSSH dnsmasq lighttpd|
|Product Development|Product Development Staging Environment|John Doe (product@email.com)|	Dovecot pop3d Apache httpd Log4j Dovecot imapd MiniServ|
|Marketing|Marketing Analytics Server|Joe Schmoe (marketing@email.com)|Microsoft ftpd Indy httpd Microsoft Windows RPC Microsoft Windows netbios-ssn Microsoft Windows Server 2008 R2 - 2012 microsoft ds
|HR|Human Resource Information System|Joe Bloggs (hr@email.com)|OpenSSH Apache httpd rpcbind2-4|

## Remediation
Which infrastructure may be affected by the vulnerability?
- `Product Development Staging Environment`

Which team has ownership of the affected infrastructure?
- `Product Development`

#### Draft Email
To finish this task, draft an advisory email to alert the infrastructure owner of the seriousness of this vulnerability. 

From: AIG Cyber & Information Security Team

To: product@email.com

Subject: Security Advisory concerning Product Development Staging Environment Log4j


Body: 
Hello John Doe,

AIG Cyber & Information Security Team would like to inform you that a recent Log4j vulnerability has been discovered in the security community that may affect the Product Development Staging Environment.

The Apache Log4j vulnerability (CVE-2021-44228), also known as "Log4Shell," allows remote code execution (RCE). This flaw enables attackers to send specially crafted requests to exploit systems running affected versions of Log4j, potentially gaining unauthorized access and control over those systems.

This vulnerability is classified as critical with a CVSS score of 10.0. Exploiting this flaw can lead to:

Full system compromise.
Unauthorized access to sensitive data.
Lateral movement within the infrastructure.
Given the presence of Log4j in your staging environment, this poses a significant security risk to AIG’s development infrastructure.



To mitigate this risk, we recommend taking the following steps immediately:

Patch Log4j to the latest version (2.17.1 or higher) where this vulnerability has been resolved.
Apply configuration changes as outlined in the CISA advisory to disable JNDI lookups for older versions if an upgrade is not immediately possible.
Conduct a thorough review of logs for signs of exploitation.



Please confirm once the remediation steps have been completed. If additional support or clarification is required, feel free to reach out to the AIG Cyber & Information Security Team directly.

Your prompt attention to this matter is crucial in safeguarding our systems.

Kind regards,
AIG Cyber & Information Security Team


# Task 2: (Technical) Bypassing Ransomware
## Background
Your advisory email in the last task was great. It provided context to the affected teams on what the vulnerability was, and how to remediate it. 

Unfortunately, an attacker was able to exploit the vulnerability on the affected server and began installing a ransomware virus. Luckily, the Incident Detection & Response team was able to prevent the ransomware virus from completely installing, so it only managed to encrypt one zip file. 

Internally, the Chief Information Security Officer does not want to pay the ransom, because there isn’t any guarantee that the decryption key will be provided or that the attackers won’t strike again in the future. 

Instead, we would like you to bruteforce the decryption key. Based on the attacker’s sloppiness, we don’t expect this to be a complicated encryption key, because they used copy-pasted payloads and immediately tried to use ransomware instead of moving around laterally on the network.

### Engagement
- Write a Python script to bruteforce the decryption key of the encrypted file, to avoid paying a ransom.

### Brute Force Decryption Key
[bruteforce.py](EncryptedFilePack/bruteforce.py)

