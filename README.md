# Task Manager CLI Application

A lightweight command-line task management application built with Python and SQLite. This application provides essential task management functionality including task creation, viewing, and deletion with persistent data storage.

## Features

- **Task Creation**: Create new tasks with title, description, and completion status
- **Task Viewing**: Display all tasks in a formatted table layout
- **Task Deletion**: Remove tasks by ID
- **Persistent Storage**: SQLite database for reliable data persistence
- **User-Friendly Interface**: Clean command-line interface with formatted output
- **Error Handling**: Comprehensive error handling for robust operation

## Technologies Used

- **Python 3.x**: Core programming language
- **SQLite3**: Lightweight database for data storage
- **Tabulate**: Library for formatted table display

## Installation

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/task-manager-cli.git
   cd task-manager-cli
   ```

2. Install required dependencies:
   ```bash
   pip install tabulate
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Usage

Upon running the application, you will be presented with a menu offering three options:

### 1. Create Task
- Enter a task title (required and unique)
- Provide a task description
- Set completion status (Y for completed, N for incomplete)

### 2. View Tasks
- Displays all tasks in a formatted table
- Shows Task ID, Title, Description, Status, and Creation Time

### 3. Delete Task
- Remove a task by entering its unique Task ID

## Database Schema

The application uses a SQLite database with the following table structure:

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    description TEXT,
    is_completed TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## File Structure

```
task-manager-cli/
│
├── main.py          # Main application file
├── data.db          # SQLite database (created automatically)
└── README.md        # Project documentation
```

## Error Handling

The application includes comprehensive error handling for:
- Database connection issues
- Invalid user input
- Duplicate task titles
- Non-existent task IDs during deletion
- General exception handling with user-friendly messages

## Sample Output

```
Available options:
    1) Create task
    2) View task
    3) Delete task

Enter your choice: 2

╒══════════╤═══════════════╤═══════════════════════╤═══════════╤═════════════════════╕
│   Task ID │ Title         │ Description           │ Status    │ Time                │
╞══════════╪═══════════════╪═══════════════════════╪═══════════╪═════════════════════╡
│        1  │ Sample Task   │ This is a sample task │ Completed │ 2024-01-15 10:30:00 │
╘══════════╧═══════════════╧═══════════════════════╧═══════════╧═════════════════════╛
```

## Future Enhancements

- Task editing functionality
- Priority levels for tasks
- Due date tracking
- Task categories/tags
- Export functionality (CSV, JSON)
- Search and filter capabilities
- Configuration file support

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or suggestions, please open an issue on GitHub or contact the project maintainer.

---

**Note**: This application is designed for educational and personal productivity purposes. For production use, consider implementing additional security measures and data validation.