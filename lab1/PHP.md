---
layout: page
title: PHP
---
 

-  [Home](https://www.techtarget.com/whatis/) 
-  [Internet technologies](https://www.techtarget.com/whatis/glossary/Internet-Technologies) 
Definition
# PHP (Hypertext Preprocessor)
By

-  [Robert Sheldon](https://www.techtarget.com/contributor/Robert-Sheldon) 

## What is PHP (Hypertext Preprocessor)?


PHP (Hypertext Processor) is a general-purpose  and interpreter that is freely available and widely used for web development. The language is used primarily for server-side scripting, although it can also be used for command-line scripting and, to a limited degree,  [desktop](https://www.techtarget.com/searchenterprisedesktop/definition/desktop)  applications. The acronym PHP was originally derived from Personal Home Page Tools, but it now stands for PHP: Hypertext Preprocessor*,*  which the PHP Group's documentation describes as a "recursive acronym."

When used for server-side scripting, PHP is added to a webpage for the purpose of generating  [dynamic](https://www.techtarget.com/searchnetworking/definition/dynamic-and-static)  content when the page is accessed through a client browser. The web server runs the script before transmitting the page to the browser. To support this process, the web server requires PHP to be installed on the server, along with a PHP  [parser](https://www.techtarget.com/searchapparchitecture/definition/parser)  -- either a Common Gateway Interface (CGI) parser or a server module.

When a user requests a webpage from the server, the parser interprets the PHP portion of the page, performs the operations called for in the PHP script, and generates the Hypertext Markup Language (HTML) that results from those operations. The HTML is then sent to the client browser, along with any other HTML on the page, providing a seamless rendering of the content. Webpages that contain PHP script are considered to be dynamic HTML pages because content varies based on the results of interpreting the script.
## Working with PHP for server-side scripting


A webpage might be made up entirely of a PHP script, or it might contain one or more PHP scripts that are embedded within standard HTML elements. In either case, the webpage itself typically is assigned the .php  [file extension](https://www.techtarget.com/whatis/definition/file-format) , which informs the web server that the page contains PHP script. The following code provides an example of a simple HTML page named *test.php*  that contains an embedded PHP script that presents the day's date:<!DOCTYPE html>

<html>



<head>

  <title>HTML example</title>

</head>



<body>

  <h2>Example of HTML in action</h2>

  <?php

    $text =  "This is a test HTML script.";

    $date = date("M j, Y") ;

echo $text." Today's date is <b>".$date."</b>."

  ?>

</body>



</html>

Most of the page's content is basic HTML that includes standard <head> and <body> elements. However, the <body> section also contains a PHP script, which is enclosed in the PHP start and end tags -- <?php and ?>, respectively. PHP scripts must always be enclosed in these tags, whether they take up the entire page or are embedded as the one shown here.

The script in this example defines the $text variable, which is assigned a string value, and the $date variable, which is assigned the current date retrieved through the date function. The two variable definitions are followed by an echo statement that concatenates the variables, along with additional text. PHP uses a period (.) to concatenate multiple elements. The echo statement also incorporates standard HTML markup -- <b> and </b> -- which specifies that the date should be displayed in bold text.

When a client browser accesses the *test.php*  page, the web server and PHP parser read the PHP script and return regular HTML. This figure shows the webpage as it is displayed in the  [Google Chrome browser](https://www.techtarget.com/searchmobilecomputing/definition/Google-Chrome-browser) . The text beneath the main heading has been generated by the PHP script.![Image is supposed to be here!](https://www.techtarget.com/) ** Test webpage displayed in Google Chrome with the text beneath the main heading generated by the PHP script


Most major operating systems support PHP, including Linux, macOS, Windows and many Unix variants, as do most of today's web servers, such as  [Apache](https://www.techtarget.com/whatis/definition/Apache)  and  [Microsoft Internet Information Services](https://www.techtarget.com/searchwindowsserver/definition/IIS) . PHP can also interface with a wide range of database platforms, including MySQL, SQLite3, MongoDB, dBase, PostgreSQL and IBM Db2. In addition, PHP can communicate with other services through its support for protocols such as  [Lightweight Directory Access Protocol](https://www.techtarget.com/searchmobilecomputing/definition/LDAP) ,  [Internet Message Access Protocol](https://www.techtarget.com/whatis/definition/IMAP-Internet-Message-Access-Protocol)  and  [Simple Network Management Protocol](https://www.techtarget.com/searchnetworking/definition/SNMP) .

PHP is often contrasted with Microsoft's ASP.NET, an open source web framework. As with ASP.NET, a PHP script can be embedded within a webpage along with HTML elements.

PHP is free and open source. Developers can find the source code on GitHub. PHP is currently licensed under the PHP License, version 3.01, which provides for its use in both source and binary forms, with or without modifications. The license also outlines specific conditions that must be met in order to use PHP. These mostly have to do with  [copyright](https://www.techtarget.com/searchsecurity/definition/copyright)  notices, the use of the PHP name and general acknowledgements. The latest release of PHP is 8.2.3, which became available in February 2023.

*See eight PHP features that prove it's for more than just the web* *.* 
This was last updated in April 2023
#### Continue Reading About PHP (Hypertext Preprocessor)


-  [How to set up PHP on Nginx with fastCGI (PHP-FPM) example](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/Nginx-PHP-FPM-config-example) 


-  [Create an HTML5 and PHP file upload form for Apache example](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/HTML5-PHP-File-Upload-Example-Apache-Server) 


-  [7 key stages of enterprise content lifecycle management](https://www.techtarget.com/searchcontentmanagement/tip/7-key-stages-of-enterprise-content-lifecycle-management) 


-  [3 steps to secure codebase updates, prevent vulnerabilities](https://www.techtarget.com/searchsecurity/tip/3-steps-to-secure-codebase-updates-prevent-vulnerabilities) 


-  [5 tips for reaching full-stack observability](https://www.techtarget.com/searchitoperations/tip/Tips-for-reaching-full-stack-observability) 

#### Related Terms
 [API management](https://www.techtarget.com/searchapparchitecture/definition/API-management) API management is the process by which an organization creates, oversees and controls application programming interfaces (APIs) ... [See complete definition](https://www.techtarget.com/searchapparchitecture/definition/API-management)  [cloud access security broker (CASB)](https://www.techtarget.com/searchcloudcomputing/definition/cloud-access-security-broker-CASB) A cloud access security broker (CASB) is a software tool or service that sits between an organization's on-premises ... [See complete definition](https://www.techtarget.com/searchcloudcomputing/definition/cloud-access-security-broker-CASB)  [vector embeddings](https://www.techtarget.com/searchenterpriseai/definition/vector-embeddings) Vector embeddings are numerical representations that capture the relationships and meaning of words, phrases and other data types. [See complete definition](https://www.techtarget.com/searchenterpriseai/definition/vector-embeddings) Latest TechTarget resources

-  [Networking](https://www.techtarget.com/#) 
-  [Security](https://www.techtarget.com/#) 
-  [CIO](https://www.techtarget.com/#) 
-  [HR Software](https://www.techtarget.com/#) 
-  [Customer Experience](https://www.techtarget.com/#) 
 [Networking](https://www.techtarget.com/searchnetworking/) 

- **  [firewall as a service (FWaaS)](https://www.techtarget.com/searchnetworking/definition/firewall-as-a-service-FWaaS) 

Firewall as a service (FWaaS), also known as a cloud firewall, is a service that provides cloud-based network traffic analysis ...
- **  [private 5G](https://www.techtarget.com/searchnetworking/definition/private-5G) 

Private 5G is a wireless network technology that delivers 5G cellular connectivity for private network use cases.
- **  [NFVi (network functions virtualization infrastructure)](https://www.techtarget.com/searchnetworking/definition/NFVi-network-functions-virtualization-infrastructure) 

NFVi (network functions virtualization infrastructure) encompasses all of the networking hardware and software needed to support ...
 [Security](https://www.techtarget.com/searchsecurity/) 

- **  [phishing](https://www.techtarget.com/searchsecurity/definition/phishing) 

Phishing is a fraudulent practice in which an attacker masquerades as a reputable entity or person in an email or other form of ...
- **  [computer forensics (cyber forensics)](https://www.techtarget.com/searchsecurity/definition/computer-forensics) 

Computer forensics is the application of investigation and analysis techniques to gather and preserve evidence from a particular ...
- **  [cybersecurity](https://www.techtarget.com/searchsecurity/definition/cybersecurity) 

Cybersecurity is the practice of protecting internet-connected systems such as hardware, software and data from cyberthreats.
 [CIO](https://www.techtarget.com/searchcio/) 

- **  [conflict-free replicated data type (CRDT)](https://www.techtarget.com/searchcio/definition/conflict-free-replicated-data-type-CRDT) 

A conflict-free replicated data type (CRDT) is a data structure that lets multiple people or applications make changes to the ...
- **  [Risk Management Framework (RMF)](https://www.techtarget.com/searchcio/definition/Risk-Management-Framework-RMF) 

The Risk Management Framework (RMF) is a template and guideline used by companies to identify, eliminate and minimize risks.
- **  [robotic process automation (RPA)](https://www.techtarget.com/searchcio/definition/RPA) 

Robotic process automation (RPA) is a technology that mimics the way humans interact with software to perform high-volume, ...
 [HRSoftware](https://www.techtarget.com/searchhrsoftware/) 

- **  [OKRs (Objectives and Key Results)](https://www.techtarget.com/searchhrsoftware/definition/OKRs-Objectives-and-Key-Results) 

OKRs (Objectives and Key Results) encourage companies to set, communicate and monitor organizational goals and results in an ...
- **  [cognitive diversity](https://www.techtarget.com/searchhrsoftware/definition/cognitive-diversity) 

Cognitive diversity is the inclusion of people who have different styles of problem-solving and can offer unique perspectives ...
- **  [reference checking software](https://www.techtarget.com/searchhrsoftware/definition/reference-checking-software) 

Reference checking software is programming that automates the process of contacting and questioning the references of job ...
 [Customer Experience](https://www.techtarget.com/searchcustomerexperience/) 

- **  [martech (marketing technology)](https://www.techtarget.com/searchcustomerexperience/definition/martech-marketing-technology) 

Martech (marketing technology) refers to the integration of software tools, platforms, and applications designed to streamline ...
- **  [transactional marketing](https://www.techtarget.com/searchcustomerexperience/definition/transactional-marketing) 

Transactional marketing is a business strategy that focuses on single, point-of-sale transactions.
- **  [customer profiling](https://www.techtarget.com/searchcustomerexperience/definition/customer-profiling) 

Customer profiling is the detailed and systematic process of constructing a clear portrait of a company's ideal customer by ...


-  [Browse by Topic](https://www.techtarget.com/whatis/glossaries) 
-  [Browse Resources](https://www.techtarget.com/whatis/resources) 


-  [About Us](https://www.techtarget.com/editorial/) 
-  [Meet The Editors](https://www.techtarget.com/whatis/about/Meet-the-Editors) 
-  [Editorial Ethics Policy](https://www.techtarget.com/techtarget-editorial-ethics-policy/) 
-  [Contact Us](https://www.techtarget.com/contact-us/) 
-  [Advertisers](https://www.techtarget.com/for-advertisers/) 
-  [Business Partners](https://www.techtarget.com/partner-with-us/) 
-  [Events](https://www.brighttalk.com/summits) 
-  [Media Kit](https://www.techtarget.com/wp-content/uploads/2023/09/TechTarget-Media-Kit-Handout-with-product-descriptions.pdf) 
-  [Corporate Site](https://www.techtarget.com) 
-  [Reprints](https://licensing.ygsgroup.com/ygspublishersolutions/) 


All Rights Reserved,  [Copyright 1999 - 2024](https://www.techtarget.com/whatis/about/copyright) , TechTarget

Close