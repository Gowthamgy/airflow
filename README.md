
# Airflow + Scrapy + MySQL Data Pipeline Project 🚀

This project demonstrates a complete, containerized data pipeline using:

✅ **Apache Airflow** - Workflow orchestration  
✅ **Scrapy** - Web scraping framework  
✅ **MySQL** - Database for data storage  
✅ **Docker & Docker Compose** - Containerized deployment  

---

## 📁 Project Structure

```
.
├── dags/               # Airflow DAGs
├── scraper/            # Scrapy project with spiders and settings
├── plugins/            # Airflow plugins (optional)
├── logs/               # Airflow logs
├── docker-compose.yaml # Docker Compose configuration
├── Dockerfile          # Docker image setup
├── .env                # Environment variables (DO NOT COMMIT real credentials)
├── scrapy.cfg          # Scrapy configuration file
└── README.md           # Project documentation
```

---

## 📝 About the Project

This project is a fully automated scraping and data pipeline using **Scrapy**, **Apache Airflow**, **MySQL**, and **Docker**, with seamless GitHub integration and development via **VSCode Containers**.

---

## 🛠️ Tech Stack

- **Python**: Data processing and Scrapy framework
- **Scrapy**: Web scraping
- **Apache Airflow**: Workflow orchestration
- **MySQL**: Database
- **Docker**: Containerization
- **VSCode**: Development environment
- **GitHub Actions**: CI/CD automation

---

## ✅ Prerequisites

Ensure the following are installed:

1. **Python**  
   [Download Python](https://www.python.org/downloads/)  
   Install Scrapy:
   ```bash
   pip install scrapy
   ```

2. **Docker Desktop**  
   [Download Docker Desktop](https://www.docker.com/products/docker-desktop)

3. **Apache Airflow**  
   Recommended via Docker. Local installation guide:  
   [Apache Airflow Installation](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html)

4. **MySQL**  
   [Download MySQL](https://dev.mysql.com/downloads/mysql/)

5. **DBeaver (Optional DB GUI)**  
   [Download DBeaver](https://dbeaver.io/download/)

6. **Git & GitHub**  
   - [Install Git](https://git-scm.com/downloads)
   - [GitHub Login](https://github.com/login)

7. **Visual Studio Code (VSCode)**  
   [Download VSCode](https://code.visualstudio.com/download)

   Install the following extensions:
   - GitHub Actions  
     ```bash
     code --install-extension GitHub.vscode-github-actions
     ```
   - Remote - Containers  
     ```bash
     code --install-extension ms-vscode-remote.remote-containers
     ```
   - GitHub Copilot Chat  
     ```bash
     code --install-extension GitHub.copilot-chat
     ```

---

## ⚡ Quick Start Guide

### 1️⃣ Clone the repository
```bash
git clone <your-repository-url>
cd <your-project-directory>
```

### 2️⃣ Build & Run Containers
```bash
docker-compose up --build
```

### 3️⃣ Access Airflow Web Interface
- URL: [http://localhost:8080](http://localhost:8080)
- Default credentials:
  ```
  Username: airflow
  Password: airflow
  ```

---

## 🐍 Scrapy Spider

Your Scrapy spider is located here:
```
scraper/spiders/sample.py
```

**Manual Run Example (inside container):**
```bash
docker exec -it <scraper-container-name> scrapy crawl sample
```

---

## 🗄️ MySQL Database

**Default Configuration:**
- Host: `localhost`
- Port: `3306`
- Username, Password: Configured via `.env` file

**Note:** `.env` file contains sensitive credentials. Do **NOT** push real `.env` to public repositories.

---

## ⏰ Airflow DAG

The DAG is located in:
```
dags/mysql_example_dag.py
```

**Responsibilities:**
- Runs Scrapy spider  
- Processes scraped data  
- Inserts results into MySQL  

---

## 💻 Requirements

Ensure you have:
- Docker  
- Docker Compose  

All services are containerized; no local Python installation required.

---

## 🙋 About Me

- **Name:** Gowtham  
- **LinkedIn:** https://www.linkedin.com/in/gowtham-gy-95ab57155  
- **GitHub:** https://github.com/Gowthamgy
- **Email:** gowthamjohn7@gmail.com.com  

---

## ⚠️ Notes

- Keep `.env` file secure, with real credentials only in your local environment.  
- Adjust configurations like Airflow schedules, MySQL settings as per your needs.  
- Contributions or suggestions are welcome!  

---

## 🚀 Usage

- Run the Airflow scheduler and webserver via Docker.
- Trigger DAGs from the Airflow UI.
- Run Scrapy spiders via Airflow tasks or manually:
  ```bash
  docker exec -it <scraper-container> scrapy crawl your_spider
  ```
- Use DBeaver to view scraped data in MySQL.

---

## 📚 Resources

- [Scrapy Documentation](https://docs.scrapy.org/en/latest/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [Docker Documentation](https://docs.docker.com/)
- [VSCode Extensions Marketplace](https://marketplace.visualstudio.com/VSCode)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to submit a pull request or open an issue.

---

**Thank you for exploring this project!**
