## Server Connectivity Monitor

### Project Description

This Python project monitors the connectivity of specified servers and sends email alerts when high-priority servers are down, allowing for quick response and resolution. The script also provides uptime statistics for each monitored server.

### Features

- **Server Monitoring**: Checks the connectivity of specified servers (both HTTP and HTTPS/SSL).
- **Ping Functionality**: Uses ping as an additional method to verify server availability.
- **Email Alerts**: Sends email notifications for connectivity issues with high-priority servers.
- **Uptime Statistics**: Maintains a history of server status to provide uptime statistics.

### Prerequisites

- Python 3.11
- `python-dotenv` package
- A Gmail account with an App Password enabled

### Setup

1. **Clone the repository**:

   ```sh
   git clone https://github.com/Nelly-ayebale/Python-Server-Monitoring-Script.git
   cd Python-Server-Monitoring-Script
   ```

2. **Install required packages**:

   ```sh
   pip install python-dotenv
   ```

3. **Create a `.env` file** in the project directory with your Gmail credentials:

   ```plaintext
   GMAIL_USER=your-email@gmail.com
   GMAIL_PASSWORD=your-app-password
   ```

4. **Ensure your Gmail account has 2FA enabled and create an App Password**. Use this password in the `.env` file.

### Usage

1. **Define the servers to monitor**:

   - Edit the list of servers in the `CheckServer.py` file or load them from a pickle file.

   ```python
   servers = [
       Server("reddit.com", 80, "plain", "high"),
       Server("msn.com", 80, "plain", "high"),
       Server("smtp.gmail.com", 465, "ssl", "high"),
       Server("192.168.1.164", 80, "plain", "high"),
   ]
   ```

2. **Run the script**:

   ```sh
   python CheckServer.py
   ```

3. **Email alerts**:
   - The script will send an email alert to `abigailnelly061@gmail.com` (this can be changed) if any high-priority server is down.

### Example

```python
if __name__ == "__main__":
    try:
        servers = pickle.load(open("servers.pickle", "rb"))
    except:
        servers = [
            Server("reddit.com", 80, "plain", "high"),
            Server("msn.com", 80, "plain", "high"),
            Server("smtp.gmail.com", 465, "ssl", "high"),
            Server("192.168.1.164", 80, "plain", "high"),
        ]

    for server in servers:
        server.check_connection()
        print(len(server.history))
        print(server.history[-1])

    pickle.dump(servers, open("servers.pickle", "wb"))
```

### Author

- ayebalenelly26@gmail.com
