---
layout: page
title: SQL
---
 

-  [Home](https://www.techtarget.com/searchdatamanagement/) 
-  [Database management](https://www.techtarget.com/searchdatamanagement/resources/Database-management) 
Definition
# Structured Query Language (SQL)
By

-  [Peter Loshin,](https://www.techtarget.com/contributor/Peter-Loshin) Former Senior Technology Editor
-  [Jessica Sirkin](https://www.techtarget.com/contributor/Jessica-Sirkin) 

## What is Structured Query Language (SQL)?


Structured Query Language (SQL) is a standardized programming language that is used to manage  [relational databases](https://www.techtarget.com/searchdatamanagement/definition/relational-database)  and perform various operations on the data in them. Initially created in the 1970s, SQL is regularly used not only by database administrators, but also by developers writing data integration scripts and data analysts looking to set up and run analytical queries.

The term *SQL*  is pronounced *ess-kew-ell* or *sequel* .

SQL is used for the following:

- modifying database table and index structures;
- adding, updating and deleting rows of data; and
- retrieving subsets of information from within relational database management systems ( [RDBMSes](https://www.techtarget.com/searchdatamanagement/definition/RDBMS-relational-database-management-system) ) -- this information can be used for transaction processing, analytics applications and other applications that require communicating with a relational database.


SQL queries and other operations take the form of commands written as statements and are aggregated into programs that enable users to add, modify or retrieve data from database tables.

A table is the most basic unit of a database and consists of rows and columns of data. A single table holds records, and each record is stored in a row of the table. Tables are the most used type of database objects, or structures that hold or reference data in a relational database. Other types of database objects include the following:

- **Views** are logical representations of data assembled from one or more database tables.
- **Indexes** are lookup tables that help speed up database lookup functions.
- **Reports** consist of data retrieved from one or more tables, usually a subset of that data that is selected based on search criteria.


Each column in a table corresponds to a category of data -- for example, customer name or address -- while each row contains a data value for the intersecting column.

Relational databases are relational because they are composed of tables that relate to each other. For example, a SQL database used for customer service can have one table for customer names and addresses and other tables that hold information about specific purchases, product codes and customer contacts. A table used to track customer contacts usually uses a unique customer identifier called a *key*  or *primary key*  to reference the customer's record in a separate table used to store customer data, such as name and contact information.

SQL became the de facto standard programming language for relational databases after they emerged in the late 1970s and early 1980s.![Image is supposed to be here!](https://www.techtarget.com/) ** The SQL query language can be used for relational or nonrelational databases, but it offers advantages for relational databases.

## SQL standard and proprietary extensions


An official SQL standard was adopted by the American National Standards Institute ( [ANSI](https://www.techtarget.com/searchdatacenter/definition/ANSI) ) in 1986, with the International Organization for Standardization ( [ISO](https://www.techtarget.com/searchdatacenter/definition/ISO) ) adopting the standard in 1987. New versions of the SQL standard are published every few years, the most recent in 2016.

ISO/IEC 9075 is the ISO SQL standard developed jointly by ISO and the International Electrotechnical Commission. The standard way of referring to an ISO standard version is to use the standards organizations -- ISO/IEC -- followed by the ISO standard number, a colon and the publication year. The current ISO standard for SQL is ISO/IEC 9075:2016.

Both proprietary and open source RDBMSes built around SQL are available for use by organizations. SQL-compliant database server products include the following:

-  [Microsoft SQL Server](https://www.techtarget.com/searchdatamanagement/definition/SQL-Server) 
- Oracle Database
- IBM [Db2](https://www.techtarget.com/searchdatamanagement/definition/Db2) 
- SAP HANA
- SAP Adaptive Server
- Oracle [MySQL](https://www.techtarget.com/searchoracle/definition/MySQL) 
- open source postgreSQL


Some versions of SQL include proprietary extensions to the standard language for procedural programming and other functions. For example, Microsoft offers a set of extensions called  [Transact-SQL](https://www.techtarget.com/searchdatamanagement/definition/T-SQL) , while Oracle's extended version of the standard is  [Procedural Language for SQL](https://www.techtarget.com/searchoracle/definition/PL/SQL) . Commercial vendors offer proprietary extensions to differentiate their product offerings by giving customers additional features and functions. As a result, the different variants of extended SQL offered by vendors are not fully compatible with one another.
## SQL commands and syntax


SQL is, fundamentally, a programming language designed for accessing, modifying and extracting information from relational databases. As a programming language, SQL has commands and a syntax for issuing those commands.

SQL commands are divided into several different types, including the following:

- **Data Definition Language (**  [DDL](https://www.techtarget.com/whatis/definition/Data-Definition-Language-DDL) **)** commands are also called*data definition commands* because they are used to define data tables.
- **Data Manipulation Language (DML)** commands are used to manipulate data in existing tables by adding, changing or removing data. Unlike DDL commands that define how data is stored, DML commands operate in the tables defined with DDL commands.
- **Data Query Language** consists of just one command,SELECT, used to get specific data from tables. This command is sometimes grouped with the DML commands.
- **Data Control Language** commands are used to grant or revoke user access privileges.
- **Transaction Control Language** commands are used to change the state of some data -- for example, toCOMMITtransaction changes or toROLLBACKtransaction changes.


SQL syntax, the set of rules for how SQL statements are written and formatted, is similar to other programming languages. Some components of SQL syntax include the following:

- SQL statements start with a SQL command and end with a semicolon (**;** ), for example:

SELECT * FROM customers;ThisSELECTstatement extracts all of the contents of a table calledcustomers.


- SQL statements are case-insensitive, meaning that they can be written using lowercase, uppercase or a combination. However, it is customary to write out SQL keywords -- commands or control operators -- in all-caps and table/column names in lowercase. Words in the statement can be treated as case-sensitive using quotes, so the following two statements produce identical results.

SELECT * FROM customers;

select * from CUSTOMERS;These two statements are different:

SELECT * FROM customers;

SELECT * FROM "Customers";


- SQL statements are terminated only by the semicolon, meaning that more complex statements can be rendered across multiple lines, like this one:

SELECT name, telephone, age

FROM customers;This command selects the contents of the columnsname,telephoneandagein the tablecustomers.


- SQL statements can incorporate program flow controls, meaning that a statement can incorporate table and row selection -- as in the previous example -- and then operate on the data contained in those columns. For example, the following command selects the name, telephone number and birthdate for all customers whose age is over 21:

SELECT name, telephone, age

FROM customers

WHERE age > 21;


Most SQL implementations include support for issuing statements at the command line, through a graphical user interface, by using SQL programs or through application programming interfaces to access SQL databases using other programming languages.
## Commonly used SQL commands with examples


Most SQL commands are used with operators to modify or reduce the scope of data operated on by the statement. Some commonly used SQL commands, along with examples of SQL statements using those commands, follow.

**SQL** **SELECT.**  The SELECT command is used to get some or all data in a table. SELECT can be used with operators to narrow down the amount of data selected:SELECT title, author, pub_date

FROM catalog

WHERE pub_date = 2021;

This example could be used by a publisher to select the title, author and publication date columns from a table named catalog.

**SQL** **CREATE.**  The CREATE command is used to create a new SQL database or SQL table. Most versions of SQL create a new database by creating a new directory, in which tables and other database objects are stored as files.

The following CREATE DATABASE statement creates a new SQL database named Human_Resources:CREATE DATABASE Human_Resources;

The CREATE TABLE command is used create a table in SQL. The following statement creates a table named Employees that has three columns: employee_ID, last_name and first_name, with the first column storing integer (int) data and the other columns storing variable character data of type varchar and a maximum of 255 characters.CREATE TABLE Employees (

    employee_ID int,

    last_name varchar(255),

    first_name varchar(255)

);

**SQL** **DELETE.**  The DELETE command removes rows from a named table. In this example, all records of employees with the last name Smithee are deleted:DELETE FROM Employees WHERE last_name='Smithee';

This statement returns the number of rows deleted when it finishes running.

**SQL** **INSERT INTO.**  The INSERT INTO command is used to add records into a database table. The following statement adds a new record into the Employees table:INSERT INTO Employees (

    last_name,

    first_name

)

VALUES (

    'Alan',

    'Smithee'

);

**SQL** **UPDATE.**  The UPDATE command is used to make changes to rows or records in a specific table. For example, the following statement updates all records that include a last_name value of Smithee by changing the name to Smith:UPDATE Employees

SET last_name = 'Smith',

WHERE last_name = 'Smithee';

SQL statements can use loops, variables and other components of a programming language to update records based on different criteria.
## SQL-on-Hadoop tools


SQL-on-Hadoop query engines are a newer offshoot of SQL that enable organizations with big data architectures built around  [Hadoop](https://www.techtarget.com/searchdatamanagement/definition/Hadoop)  data stores to use SQL as a querying language and enable database professionals to use a familiar query language instead of having to use more complex and less familiar languages -- in particular, the  [MapReduce](https://www.techtarget.com/searchcloudcomputing/definition/MapReduce)  programming environment for developing batch processing applications.

More than a dozen SQL-on-Hadoop tools are available from Hadoop distribution providers and other vendors; many of them are open source software or commercial versions. In addition, the  [Apache Spark](https://www.techtarget.com/searchdatamanagement/definition/Apache-Spark)  processing engine, which is often used in conjunction with Hadoop, includes a Spark SQL module that similarly supports SQL-based programming.

Not all SQL-on-Hadoop tools support all of the functionality offered in relational implementations of SQL. But SQL-on-Hadoop tools are a regular component of Hadoop deployments, as companies look to get developers and data analysts with SQL skills involved in programming big data applications.
## SQL security


SQL servers are subject to most of the same vulnerabilities as any other enterprise application, including weak authentication, insecure design, misconfiguration and other  [application security](https://www.techtarget.com/searchsoftwarequality/definition/application-security)  issues. However,  [SQL injection](https://www.techtarget.com/searchsoftwarequality/definition/SQL-injection) , first reported in 1998, continues to dominate security issues for SQL systems.

 [SQL injection attacks](https://www.techtarget.com/searchsecurity/feature/How-to-prevent-SQL-injection-with-prepared-statements)  usually exploit weaknesses in systems where data submissions are not scanned and sanitized to remove potentially malicious code incorporated or injected into data.

The best-known example of a SQL injection exploit is documented in the "Little Bobby Tables"  [comic](https://xkcd.com/327/)  by Randall Munroe, in which a SQL injection is perpetrated by a mom who filled out a SQL form with her son's name followed by malicious SQL code.

In the comic, the son's name is entered as the following:Robert'); DROP TABLE Students; --

Following the valid data (Robert), the name continues with characters that SQL servers interpret as ending the data -- single quote, close parenthesis and semicolon -- followed by the DROP TABLE command.

Use of  [best practices for database security](https://www.techtarget.com/searchsecurity/tip/4-enterprise-database-security-best-practices)  can help protect an organization's most valuable digital assets.
## History of SQL


With roots going back to the early 1970s, SQL continues to make key milestones in history as one of the most successful ideas in computing history.

- **1970.** "A Relational Model of Data for Large Shared Data Banks" by E.F. Codd publishes in*Communications of the ACM* , laying the basis for RDBMSes.
- **1974.** IBM researchers publish an article introducing Structured Query Language, first called SEQUEL or Structured English Query Language. The name was changed for trademark purposes.
- **1977.** Relational Software Inc., the company that eventually became Oracle, begins building a commercial RDBMS.
- **1979.** Oracle ships first commercially available RDBMS for Digital Equipment Corp.'s minicomputer systems.
- **1982.** IBM ships SQL/Data System, a SQL RDBMS for IBM mainframes.
- **1985.** IBM ships Database 2, a SQL RDBMS for IBM's Multiple Virtual Storage mainframe operating system.
- **1986.** An ANSI committee and then ISO adopt SQL as a standard.
- **1989.** First revision of the ISO SQL standard, SQL-89, publishes.
- **1992.** First major revision of ISQ SQL standard, SQL-92, publishes.
- **1999.** First version to be named in accordance with ISO naming standards, ISO/IEC SQL:1999, adds programming functionality and support for Java.
- **2003.** ISO/IEC SQL:2003 adds support for a predefined data type for Extensible Markup Language (XML) objects.
- **2006.** ISO/IEC SQL:2006 expands XML-related functionality.
- **2008.** ISO/IEC SQL:2008 adds support for partitioned JOINs, a method for linking two or more tables that treats the joined tables as a single table.
- **2011.** ISO/IEC SQL:2011 improves support for relational databases containing time-related data.
- **2016.** ISO/IEC SQL:2016 adds optional new features, including JavaScript Object Notation-related changes, support for polymorphic table functions and row pattern matching.

## SQL skills and related careers


SQL skills can boost many careers, not just those of database administrators, data warehouse architects, database programmers and others whose roles directly use SQL.

Some other roles that can benefit from SQL experience include the following:

- **Data scientists** working with thousands of tables spread across thousands of databases need [strong SQL skills](https://www.techtarget.com/searchenterpriseai/feature/Advanced-SQL-skills-boost-data-scientists-value) .
- **Business intelligence analysts** also must have strong SQL skills for working with data warehouses and structured databases.
- **Data analysts** are expected to have [experience with SQL](https://www.techtarget.com/whatis/feature/Top-8-must-have-data-analyst-skills) .
- **Cloud engineers** are expected to be proficient in SQL.


SQL skills can be helpful in a surprisingly broad range of disciplines. For example, journalists who reported in  [2013 on offshore tax dodgers](https://www.computerweekly.com/news/2240202669/Big-data-journalism-exposes-offshore-tax-dodgers)  and money laundering had to learn SQL to help them understand the significance of the millions of emails and files that were leaked.

*Given its longevity and importance to so many different applications, learning SQL can be an important career goal. One first step is understanding the*  [difference between SQL DML and DDL commands](https://www.techtarget.com/searchdatamanagement/answer/Whats-the-difference-between-DDL-and-DML) *.* 
This was last updated in February 2022
#### Next Steps


 [SAP HANA in-memory DBMS overview](https://www.techtarget.com/searchdatamanagement/feature/SAP-HANA-in-memory-DBMS-overview) 
#### Continue Reading About Structured Query Language (SQL)


-  [Open source database comparison to choose the right tool](https://searchdatamanagement.techtarget.com/feature/Open-source-database-comparison-to-choose-the-right-tool) 


-  [SQL vs. NoSQL vs. NewSQL: How do they compare?](https://whatis.techtarget.com/feature/SQL-vs-NoSQL-vs-NewSQL-How-do-they-compare) 


-  [Key features to create a SQL Server audit trail in databases](https://searchsqlserver.techtarget.com/tip/Key-features-to-create-a-SQL-Server-audit-trail-in-databases) 


-  [NoSQL database types explained: Document-based databases](https://searchdatamanagement.techtarget.com/tip/NoSQL-database-types-explained-Document-based-databases) 


-  [Quiz: Test your understanding of the Hadoop ecosystem](https://searchdatamanagement.techtarget.com/quiz/Quiz-Test-your-understanding-of-the-Hadoop-ecosystem) 

#### Related Terms
 [Amazon RDS (Relational Database Service)](https://www.techtarget.com/searchaws/definition/Amazon-Relational-Database-Service-RDS) Amazon Relational Database Service (RDS) is a managed database service provided by Amazon Web Services (AWS). It makes it easy to... [See complete definition](https://www.techtarget.com/searchaws/definition/Amazon-Relational-Database-Service-RDS)  [Google Bigtable](https://www.techtarget.com/searchdatamanagement/definition/Google-BigTable) Google Bigtable is a distributed, column-oriented data store created by Google Inc. to handle very large amounts of structured ... [See complete definition](https://www.techtarget.com/searchdatamanagement/definition/Google-BigTable) Masked language models (MLMs) are used in natural language processing (NLP) tasks for training language models.
#### Dig Deeper on Database management


-  [Introduction to JDBC with HSQLDB tutorialBy: Cameron McKenzie](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/Introduction-to-JDBC-with-HSQLDB-tutorial) 
-  [foreign keyBy: Ben Lutkevich](https://www.techtarget.com/searchoracle/definition/foreign-key) 
-  [Data Definition Language (DDL)By: Rahul Awati](https://www.techtarget.com/whatis/definition/Data-Definition-Language-DDL) 
-  [How to set up a MySQL database in LinuxBy: Jack Wallen](https://www.techtarget.com/searchdatacenter/tip/How-to-set-up-a-MySQL-database-in-Linux) 
Latest TechTarget resources

-  [Business Analytics](https://www.techtarget.com/#) 
-  [AWS](https://www.techtarget.com/#) 
-  [Content Management](https://www.techtarget.com/#) 
-  [Oracle](https://www.techtarget.com/#) 
-  [SAP](https://www.techtarget.com/#) 
 [Business Analytics](https://www.techtarget.com/searchbusinessanalytics/) 

- **  [Google Cloud unveils new GenAI-fueled data, analytics tools](https://www.techtarget.com/searchbusinessanalytics/news/366571639/Google-Cloud-unveils-new-GenAI-fueled-data-analytics-tools) 

The tech giant introduced extensive support for vector search and improved access to unstructured data while also making a pair ...
- **  [Snowflake CEO Slootman steps down, Ramaswamy takes over](https://www.techtarget.com/searchbusinessanalytics/news/366571855/Snowflake-CEO-Slootman-steps-down-Ramaswamy-takes-over) 

Slootman resigns after five years at the helm of the data cloud vendor. Revenues grew fivefold under him and the company went ...
- **  [Generative AI can improve -- not replace -- predictive analytics](https://www.techtarget.com/searchbusinessanalytics/tip/Generative-AI-can-improve-not-replace-predictive-analytics) 

Generative AI improves predictive analytics through synthetic data generation. Managing data bias and ethical AI risks can enable...
 [SearchAWS](https://www.techtarget.com/searchaws/) 

- **  [AWS Control Tower aims to simplify multi-account management](https://www.techtarget.com/searchaws/tip/AWS-Control-Tower-aims-to-simplify-multi-account-management) 

Many organizations struggle to manage their vast collection of AWS accounts, but Control Tower can help. The service automates ...
- **  [Break down the Amazon EKS pricing model](https://www.techtarget.com/searchaws/tip/Compare-EKS-pricing-to-other-managed-Kubernetes-services) 

There are several important variables within the Amazon EKS pricing model. Dig into the numbers to ensure you deploy the service ...
- **  [Compare EKS vs. self-managed Kubernetes on AWS](https://www.techtarget.com/searchaws/tip/2-options-to-deploy-Kubernetes-on-AWS-EKS-vs-self-managed) 

AWS users face a choice when deploying Kubernetes: run it themselves on EC2 or let Amazon do the heavy lifting with EKS. See ...
 [Content Management](https://www.techtarget.com/searchcontentmanagement/) 

- **  [How businesses should deal with enterprise search issues](https://www.techtarget.com/searchcontentmanagement/tip/How-businesses-should-deal-with-enterprise-search-issues) 

Enterprise search issues frequently complicate user experience with CMSes. However, these challenges have various solutions to ...
- **  [Reading long PDFs less painful with Adobe AI Assistant tool](https://www.techtarget.com/searchcontentmanagement/news/366571023/Reading-long-PDFs-less-painful-with-Adobe-AI-Assistant-tool) 

The first beta version of Adobe's generative AI tools for search, summary, attribution and copy-pasting is available for Acrobat,...
- **  [What does a knowledge manager do?](https://www.techtarget.com/searchcontentmanagement/feature/What-does-a-knowledge-manager-do) 

Knowledge managers use technical skills to maintain knowledge base software and interpersonal skills to encourage employees to ...
 [SearchOracle](https://www.techtarget.com/searchoracle/) 

- **  [Oracle sets lofty national EHR goal with Cerner acquisition](https://www.techtarget.com/searchoracle/news/252521391/Oracle-sets-lofty-national-EHR-goal-with-Cerner-acquisition) 

With its Cerner acquisition, Oracle sets its sights on creating a national, anonymized patient database -- a road filled with ...
- **  [With Cerner, Oracle Cloud Infrastructure gets a boost](https://www.techtarget.com/searchoracle/news/252511240/With-Cerner-Oracle-cloud-infrastructure-gets-a-boost) 

Oracle plans to acquire Cerner in a deal valued at about $30B. The second-largest EHR vendor in the U.S. could inject new life ...
- **  [Supreme Court sides with Google in Oracle API copyright suit](https://www.techtarget.com/searchoracle/news/252498837/Supreme-Court-sides-with-Google-in-Oracle-API-copyright-case) 

The Supreme Court ruled 6-2 that Java APIs used in Android phones are not subject to American copyright law, ending a ...
 [SearchSAP](https://www.techtarget.com/searchsap/) 

- ** 

The Rise with SAP Migration and Modernization program includes cost incentives and services aimed at on-premises customers ...
- **  [SAP restructuring focuses on AI, affects 8,000 employees](https://www.techtarget.com/searchsap/news/366567592/SAP-restructuring-focuses-on-AI-affects-8000-employees) 

Amidst strong earnings results, SAP announced a restructuring plan that focuses the company on AI-based growth, with 8,000 ...
- **  [SAP debuts 4 AI-based retail capabilities](https://www.techtarget.com/searchsap/news/366566212/SAP-debuts-4-AI-based-retail-capabilities) 

At the National Retail Federation 2024 conference, SAP will feature new retail capabilities for predictive demand planning, ...


-  [About Us](https://www.techtarget.com/editorial/) 
-  [Editorial Ethics Policy](https://www.techtarget.com/techtarget-editorial-ethics-policy/) 
-  [Meet The Editors](https://www.techtarget.com/editorial-contacts/) 
-  [Contact Us](https://www.techtarget.com/contact-us/) 
-  [Advertisers](https://www.techtarget.com/for-advertisers/) 
-  [Partner with Us](https://www.techtarget.com/partner-with-us/) 
-  [Media Kit](https://www.techtarget.com/wp-content/uploads/2023/09/TechTarget-Media-Kit-Handout-with-product-descriptions.pdf) 
-  [Corporate Site](https://www.techtarget.com) 


-  [Contributors](https://www.techtarget.com/searchdatamanagement/contributors) 
-  [Reprints](https://licensing.ygsgroup.com/ygspublishersolutions/) 
-  [Answers](https://www.techtarget.com/searchdatamanagement/answers) 
-  [Definitions](https://www.techtarget.com/searchdatamanagement/definitions) 
-  [E-Products](https://www.techtarget.com/searchdatamanagement/eproducts) 
-  [Events](https://www.brighttalk.com/summits) 
-  [Features](https://www.techtarget.com/searchdatamanagement/features) 


-  [Guides](https://www.techtarget.com/searchdatamanagement/guides) 
-  [Opinions](https://www.techtarget.com/searchdatamanagement/opinions) 
-  [Photo Stories](https://www.techtarget.com/searchdatamanagement/photostories) 
-  [Quizzes](https://www.techtarget.com/searchdatamanagement/quizzes) 
-  [Tips](https://www.techtarget.com/searchdatamanagement/tips) 
-  [Tutorials](https://www.techtarget.com/searchdatamanagement/tutorials) 
-  [Videos](https://www.techtarget.com/searchdatamanagement/videos) 


All Rights Reserved,  [Copyright 2005 - 2024](https://www.techtarget.com/searchdatamanagement/about/copyright) , TechTarget

Close