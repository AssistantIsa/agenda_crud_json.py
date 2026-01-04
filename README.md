# agenda_crud_json.py
Learning Project: CRUD system for managing a contact list using Python and JSON. It allows you to easily add, edit, delete, and list contacts. Ideal for practicing JSON file handling and basic database operations in Python. It can be used for both personal and professional purposes.

# 📇 Agenda CRUD JSON

A simple yet powerful contact management system built with Python. This project demonstrates CRUD operations (Create, Read, Update, Delete) with JSON file persistence.

## 🎯 Project Overview

**Project Name:** agenda_crud_json.py
**Level:** Intermediate  
**Duration:** 5-7 days  
**Language:** Python 3.x

This is **Project 3** in the learning pathway, designed to teach:
- File handling and persistence
- CRUD operations
- Data structures (dictionaries and lists)
- JSON serialization/deserialization
- Input validation
- Menu-driven applications

## ✨ Features

- ✅ **Create** new contacts with multiple fields
- 📖 **Read** and display all contacts or search specific ones
- ✏️ **Update** existing contact information
- 🗑️ **Delete** contacts from the agenda
- 💾 **Persistent storage** using JSON files
- 🔍 **Search functionality** by name, phone, or email
- 📊 **Contact statistics** and summaries
- ✔️ **Input validation** for emails and phone numbers

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies (uses standard library only)

## 🚀 Getting Started

### Installation

1. Clone or download the project:
```bash
git clone <repository-url>
cd agenda_crud_json
```

2. Run the program:
```bash
python agenda_crud_json.py
```

### First Run

On first run, the program will automatically create a `contacts.json` file to store your contact data.

## 💻 Usage

### Main Menu

```
================================
        CONTACT AGENDA
================================
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. View Statistics
7. Exit
================================
```

### Adding a Contact

The system will prompt you for:
- Full Name (required)
- Phone Number (validated format)
- Email Address (validated format)
- Address (optional)
- Notes (optional)

### Searching Contacts

Search by:
- Name (partial match)
- Phone number
- Email address

### Updating Contacts

- Select a contact from the list
- Choose which field to update
- Enter new information

### Deleting Contacts

- Search and select the contact to delete
- Confirm deletion
- Contact is permanently removed

## 📁 Project Structure

```
agenda_crud_json/
│
├── agenda_crud_json.py      # Main program file
├── contacts.json          # Data storage (auto-generated)
└── README.md             # This file
```

## 🗂️ Data Structure

Contacts are stored in JSON format:

```json
{
  "contacts": [
    {
      "id": 1,
      "name": "John Doe",
      "phone": "+1-555-0123",
      "email": "john.doe@example.com",
      "address": "123 Main St, City, State",
      "notes": "College friend",
      "created_at": "2026-01-04 10:30:00",
      "updated_at": "2026-01-04 10:30:00"
    }
  ]
}
```

## 🎓 Learning Objectives

This project teaches:

1. **File I/O Operations**
   - Reading from files
   - Writing to files
   - File existence checking

2. **JSON Handling**
   - Serialization (`json.dumps()`)
   - Deserialization (`json.loads()`)
   - Pretty printing

3. **CRUD Operations**
   - Create: Add new records
   - Read: Display and search records
   - Update: Modify existing records
   - Delete: Remove records

4. **Data Validation**
   - Email format validation
   - Phone number validation
   - Required field checking

5. **Error Handling**
   - Try-except blocks
   - File operation errors
   - User input validation

## 🔧 Code Structure

### Main Functions

- `load_contacts()` - Load contacts from JSON file
- `save_contacts()` - Save contacts to JSON file
- `create_contact()` - Add new contact
- `read_contacts()` - Display all contacts
- `search_contact()` - Find specific contacts
- `update_contact()` - Modify contact information
- `delete_contact()` - Remove contact
- `validate_email()` - Email format validation
- `validate_phone()` - Phone number validation

## 📈 Future Enhancements

Potential features to add:

- [ ] Import/Export contacts (CSV format)
- [ ] Birthday reminders
- [ ] Contact groups/categories
- [ ] Backup and restore functionality
- [ ] Multiple phone numbers per contact
- [ ] Photo/avatar support
- [ ] Contact merge functionality
- [ ] Export to vCard format

## 🐛 Known Issues

- Phone number validation is basic (can be enhanced with regex)
- No duplicate contact detection
- Large datasets may require pagination

## 🤝 Contributing

This is a learning project. Feel free to:
- Fork the repository
- Add new features
- Fix bugs
- Improve documentation
- Share feedback

## 📝 License

This project is created for educational purposes.

## 👨‍💻 Author

Created as part of a structured learning path from beginner to senior developer.

## 🙏 Acknowledgments

- Part of the progressive learning curriculum
- Builds upon concepts from previous projects:
  - Project 1: Simple Calculator
  - Project 2: Number Guessing Game

## 📚 Related Projects

- **Previous:** Number Guessing Game (loops, conditionals, random)
- **Next:** Task Management System (databases, OOP)

---

**Happy Coding! 🚀**

For questions or suggestions, please open an issue or submit a pull request.
