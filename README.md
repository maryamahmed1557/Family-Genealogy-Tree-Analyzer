# 🌳 Family Genealogy Tree Analyzer

A Python-based application that represents and analyzes a family tree using **Tree Data Structures and Depth-First Search (DFS)**.

The project allows users to explore family relationships and answer different queries about ancestors, descendants, siblings, generations, and common ancestors through an interactive graphical interface.

---

## 📌 Overview

The **Family Genealogy Tree Analyzer** is designed to model a multi-generation family tree and provide useful information about relationships between family members.

The project combines **Data Structures, Algorithms, Object-Oriented Programming, and GUI development** to create an interactive family tree analyzer.

The application supports a family tree containing **30+ members across 4 generations**.

---

## ✨ Key Features

### 🌳 Family Tree Representation

* Represents family members using a tree-based structure.
* Supports multiple generations.
* Stores relationships between parents and children.
* Displays the family structure visually.

### 🔎 DFS-Based Queries

The application uses **Depth-First Search (DFS)** to answer different family relationship queries:

* 👨‍👩‍👧 Find ancestors of a person
* 👶 Find descendants of a person
* 🤝 Find the Lowest Common Ancestor (LCA)
* 👥 Count siblings
* 📊 Determine generation depth
* 🔍 Explore relationships between family members

### 🖥️ Graphical User Interface

The application includes an interactive GUI that allows users to:

* Select family members.
* Choose different queries.
* Display results clearly.
* Visualize the family tree.
* Navigate through the application easily.

---

## 🧠 Data Structure & Algorithm

### 🌳 Tree Data Structure

Each family member is represented as a node containing information about the person and their relationships.

The tree structure allows the application to represent relationships such as:

```text
Grandparent
    │
 ┌──┴──┐
Parent Parent
  │
 ┌┴─┐
Child Child
```

### 🔍 Depth-First Search (DFS)

DFS is used to traverse the family tree and search through relationships.

It is mainly used to:

* Find ancestors.
* Find descendants.
* Explore family relationships.
* Determine paths within the tree.

### 🤝 Lowest Common Ancestor (LCA)

The application can determine the **Lowest Common Ancestor** between two family members by analyzing their paths within the family tree.

---

## 🛠️ Technologies Used

* 🐍 Python
* 🌳 Tree Data Structures
* 🔍 Depth-First Search (DFS)
* 🧱 Object-Oriented Programming (OOP)
* 🖥️ Tkinter
* 🎨 CustomTkinter

---

## 📂 Project Structure

```text
Family-Genealogy-Tree-Analyzer/
│
├── GUI.py
├── Person.py
├── ...
│
└── README.md
```

> The exact files may vary depending on the final project structure.

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_LINK
```

### 2. Open the Project

Open the project folder in your preferred Python IDE.

### 3. Install Requirements

If needed:

```bash
pip install customtkinter
```

### 4. Run the Application

Run the main Python file:

```bash
python GUI.py
```

---

## 📋 Example Queries

The application can answer questions such as:

**Ancestors**

> Who are the ancestors of a selected person?

**Descendants**

> Who are the descendants of a selected person?

**Lowest Common Ancestor**

> What is the lowest common ancestor of two selected people?

**Siblings**

> How many siblings does a selected person have?

**Generation Depth**

> What generation does a selected person belong to?

---

## 🌱 What I Learned

Through this project, I gained practical experience in:

* Implementing **Tree Data Structures**
* Applying **Depth-First Search (DFS)**
* Understanding family relationships as a hierarchical structure
* Implementing the **Lowest Common Ancestor (LCA)** concept
* Applying Object-Oriented Programming
* Building an interactive GUI using Tkinter and CustomTkinter
* Organizing a multi-file Python project
* Improving problem-solving and algorithmic thinking

---

## 👩‍💻 Project

This project was developed as part of my practical programming and data structures learning journey.

It helped me connect theoretical concepts such as **Trees and DFS** with a real-world application.

---

## ⭐ Future Improvements

Possible future improvements include:

* Adding more family members and generations.
* Adding search and filtering features.
* Improving the graphical visualization.
* Adding more relationship queries.
* Saving and loading family trees from external files.

---

### 🌳 Built with Python, Data Structures & Algorithms ❤️
