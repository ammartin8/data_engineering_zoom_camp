# ⚙️ Data Engineering Portfolio & Course Capstone

> Building robust, scalable data infrastructures from the ground up.

Welcome to my public repository showcasing the comprehensive **Data Engineering Bootcamp** I have completed. This project encapsulates my journey through a rigorous curriculum designed to bridge the gap between theory and production-grade data pipelines.

By completing all 7 core modules, one hands-on workshop, and an end-to-end final project, I have solidified my skills in cloud infrastructure, analytics engineering, and real-time data processing.

---

## 📚 What I Learned

Throughout this intensive program, I moved beyond basic scripting to architecting full-stack data solutions. Here is a breakdown of the core competencies I developed:

- **Infrastructure & Deployment:** Mastered provisioning scalable environments using Infrastructure as Code (IaC) and containerization techniques to ensure reproducibility.
- **Analytics Engineering:** Learned how to model data effectively, enforce quality standards, and automate transformations using modern tools like dbt.
- **Data Warehousing:** Gained deep proficiency in cloud-native warehousing solutions, specifically optimizing for cost and performance through partitioning and clustering.
- **Batch & Stream Processing:** Implemented batch logic with Spark for large-scale datasets and built real-time streaming pipelines using Kafka for event-driven architectures.
- **Orchestration:** Automated complex workflows to handle dependencies, retries, and monitoring without manual intervention.

---

## 🛠️ Tech Stack & Tools Used

I built these projects using a modern data stack focused on the **Cloud-Native** ecosystem.

| Category                      | Technologies & Frameworks                                      |
| :---------------------------- | :------------------------------------------------------------- |
| **Infrastructure**            | Google Cloud Platform (GCP), Terraform, Docker, Docker Compose |
| **Databases**                 | PostgreSQL (Dockerized), BigQuery, DuckDB                      |
| **Transformation & Modeling** | dbt (Data Build Tool), SQL, Python                             |
| **Orchestration**             | Kestra                                                         |
| **Batch Processing**          | Apache Spark, PySpark                                          |
| **Streaming**                 | Apache Kafka, Kafka Streams, KSQL                              |

---

## 📂 Repository Structure

This repository contains the code artifacts and documentation for each stage of the course:

├── [01-Infrastructure/](modules/module_1/project_01/README.md)    # GCP setup, Terraform configs, Docker Compose \
├── [02-Orchestration/](modules/module_2/project_02/README.md)     # Kestra workflows and schedules \
├── [03-Warehousing/](modules/module_3/project_03/README.md)         # BigQuery partitioning strategies & Data Modeling \
├── [04-Analytics/](modules/module_4/project_04/README.md)           # dbt projects, DuckDB local transforms \
├── [05-Data-Platform/](workshops/dlt_project/taxi-pipeline/README.md)           # End-to-end pipeline definitions on dltHub \
├── [06-Batch-Processing/](modules/module_6/project_06/README.md)       # Batch data processing with Apache Spark and Spark Dataframe Transformations \
├── [07-Batch-and-Stream/](modules/module_7/project_07/README.md)    # Kafka Streams implementations with PyFlink and RedPanda \
└── Final_Project/          # Capstone project: In-Progress

## 🏆 Key Highlights from the Course
1. CI/CD for Data: I learned how to test, document, and deploy data models using dbt, ensuring reliability before hitting production.
2. Scalable Architecture: Unlike simple scripts, I built pipelines capable of handling incremental loads and API scalability challenges.
3. Data Quality: Integrated quality checks directly into the pipeline (Module 5) to ensure downstream analytics are never compromised by dirty data.
4. Cloud Optimization: Implemented partitioning and clustering strategies in BigQuery to reduce costs and improve query latency.


## 🚀 Ready for a Data Engineering Challenge!
I am passionate about building scalable, reliable, and efficient data systems that empower business intelligence. This project demonstrates my ability to handle the full lifecycle of data—from ingestion to production deployment on GCP.

## 💼 Connect With Me
LinkedIn: [Linkedin Profile](https://www.linkedin.com/in/amahmartin) \
GitHub: [Github Profile](https://github.com/ammartin8)

"The best pipelines are invisible, allowing the business to focus on the value derived from the data."

## ❤️ Acknowledgments

A sincere thank you to Alexey Grigorev and the Data Engineering Zoom Camp Instructors at [DataTalks Club](https://datatalks.club/) for providing tutorials and guidance on building real world data engineering projects!