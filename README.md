# agenda_crud_json.py
Learning Project: CRUD system for managing contacts with Python and JSON. It allows you to easily add, edit, delete, and list contacts. Ideal for practicing JSON file handling and basic database operations in Python. It can be used for both personal and professional purposes.

Learning Project: 

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

✅ Create, Read, Update, Delete contacts
- 💾 Persistent JSON storage
- 🔍 Search by name, phone, or email
- ✏️ Edit all contact fields (including website)
- 🗑️ Safe deletion with confirmation
- 📊 Statistics and analytics
- ⚠️ Input validation (phone, email, website)
- 🚫 Cancel operations at any time with 'c'
- 🌐 Compatible with Google Colab + Drive
- 💻 Works on local environments (Ubuntu, Windows, Mac)
- 
## 📋 Requirements

- Python 3.6 or higher
- No external dependencies (uses standard library only)

## 🚀 Quick Start
```bash
# Clone repository
git clone https://github.com/tu-usuario/agenda_crud_json.git
cd agenda_crud_json

# Run locally
python3 agenda_crud_json.py

# Or in Google Colab
# Upload the .py file and run
```

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
├── agenda_crud_json.py      # Main program
├── README.md                # Documentation
├── .gitignore               # Git ignore rules
└── contactos.json           # Created on first run (not in repo)
```

## 🗂️ Data Structure

Contacts are stored in JSON format:

```json
{
  "contacts": [
    {
      "id": 1,
      "name": "John Doe",
      "phone": "+49-123-45678901",
      "email": "john.doe@example.com",
      "pageweb":"paginaweb.de",
      "address": "123 Main St, City, State",
      "notes": "College friend",
      "created_at": "2026-01-04 10:30:00",
      "updated_at": "2026-01-04 10:30:00"
    }
  ]
}
```
## 📊 Contact Fields

- 📛 Name (required)
- 💝 Nickname (optional)
- 📱 Phone (optional, validated)
- 📧 Email (optional, validated)
- 🌐 Website (optional, validated)
- 🎂 Birthday (optional)
- 🎯 Category (optional)
- 📝 Notes (optional)

*Note: At least phone OR email is required*

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
6. **Menu-driven interfaces**
7. **Google Drive integration (Colab)**


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

## Known Issues

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

## 🔒 Privacy Note

The `contactos.json` file is excluded from the repository (via `.gitignore`) to protect your personal data.

## 👨‍💻 Author

Created as part of a structured learning curriculum.

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
