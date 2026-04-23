# Student Task Management System with API Integration

A Python-based command-line application designed to manage daily tasks while demonstrating real-world system design and REST API communication.

---

## Project Overview

The Student Task Management System bridges the gap between basic scripting and system architecture. It allows users to track tasks locally while simulating cloud synchronization through an external API. This project introduces students to:
- **Client-Server Interaction** - How your app (client) talks to a server.
- **Dynamic Data Flow** - How data moves from user input to logic, then to the cloud.
- **CRUD Operations** - Create, Read, Update, and Delete functionalities.

---

## How It Works

```
User enters a task manually
        |
        v
Task is stored in a local list          ← Task Module
        |
        v
Task is sent via POST request to API    ← API Module
        |
        v
Local list is re-indexed dynamically    ← Processing Module
        |
        v
Structured list (1. Mango) is shown     ← Display Module

```

---

## Key Features

- ** Manual Task Entry ** : Full control over your task list; no automated cloud clutter.
- ** Dynamic Re-indexing ** : When a task is deleted, the list automatically shifts to maintain a perfect series (e.g., if you delete #2, the old #3 becomes the new #2).
- ** Cloud Sync Integration** : Every manual entry triggers a POST request to a mock server (JSONPlaceholder) to simulate real-world data persistence.
- ** Clean CLI UI ** : Minimalist output format showing only the number and task name.

--- 

## Prerequisites

- Python 3.8 or higher

--- 

## Installation & Setup

**1. Clone or download this project**

```bash
git clone https://github.com/mohammedanas08/Student-Task-Manager.git
cd Student-Task-Manager
```

**2. Install dependencies**

```bash
pip install requests
```

## Running the App

```bash
python main.py
```

---

## Usage Guide

When you run the script, the following menu will appear:

--- 

```
--- MENU ---
  1. View Tasks
  2. Add Task 
  3. Delete Task
  4. Exit
```
--- 

## Dynamic Series Example

You add: Mango, Apple, Banana.

View list:

1. Mango

2. Apple

3. Banana

Delete 2. Apple.

View list again:

1. Mango

2. Banana (Automatically re-indexed!)

---

## Project Structure

```
Student-Task-Manager/
├── main.py            # Main Interface & Display Module
├── task_manager.py    # Logic Module (CRUD operations)
├── api_module.py      # Cloud Communication Module
└── README.md          # Project Documentation
```

--- 

## Notes

- API Simulation : Since we use JSONPlaceholder, the server will "accept" your tasks, but it won't store them forever. This is purely for demonstrating how a POST request works.
- Git Safety: If you add a .env file for real API keys later, ensure it is added to your .gitignore.
