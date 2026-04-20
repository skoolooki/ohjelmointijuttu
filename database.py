import sqlite3

DB_NAME = "employees.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    try:
        with get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    department TEXT NOT NULL,
                    role TEXT NOT NULL,
                    salary REAL NOT NULL CHECK (salary >= 0)
                )
            """)
        return True, "Database initialized successfully."
    except sqlite3.Error as e:
        return False, f"Database initialization error: {e}"


def add_employee(emp_id, name, department, role, salary):
    try:
        emp_id = int(emp_id)
        if emp_id <= 0:
            return False, "Employee ID must be a positive number."

        if not str(name).strip():
            return False, "Name cannot be empty."
        if not str(department).strip():
            return False, "Department cannot be empty."
        if not str(role).strip():
            return False, "Role cannot be empty."

        salary = float(salary)
        if salary < 0:
            return False, "Salary cannot be negative."

        with get_connection() as conn:
            conn.execute("""
                INSERT INTO employees (id, name, department, role, salary)
                VALUES (?, ?, ?, ?, ?)
            """, (emp_id, name.strip(), department.strip(), role.strip(), salary))

        return True, "Employee added successfully."

    except ValueError:
        return False, "Employee ID and salary must be valid numbers."
    except sqlite3.IntegrityError:
        return False, "Employee ID already exists."
    except sqlite3.Error as e:
        return False, f"Database error: {e}"


def get_all_employees():
    try:
        with get_connection() as conn:
            rows = conn.execute("SELECT * FROM employees ORDER BY id").fetchall()
            return True, rows
    except sqlite3.Error as e:
        return False, f"Database error: {e}"


def update_employee(emp_id, new_role=None, new_salary=None):
    """
    Keeps your original update function for role + salary updates.
    """
    try:
        emp_id = int(emp_id)

        updates = []
        values = []

        if new_role is not None and str(new_role).strip():
            updates.append("role = ?")
            values.append(str(new_role).strip())

        if new_salary is not None and str(new_salary) != "":
            salary = float(new_salary)
            if salary < 0:
                return False, "Salary cannot be negative."
            updates.append("salary = ?")
            values.append(salary)

        if not updates:
            return False, "No update values provided."

        values.append(emp_id)

        with get_connection() as conn:
            cursor = conn.execute(
                f"UPDATE employees SET {', '.join(updates)} WHERE id = ?",
                values
            )

            if cursor.rowcount == 0:
                return False, "Employee not found."

        return True, "Employee updated successfully."

    except ValueError:
        return False, "Employee ID and salary must be valid numbers."
    except sqlite3.Error as e:
        return False, f"Database error: {e}"


def update_employee_detail(emp_id, detail, new_value):
    """
    Extra helper so your old update.py can still update one field at a time
    with very small changes.
    """
    try:
        emp_id = int(emp_id)
        detail = str(detail).strip().lower()

        allowed_fields = {"name", "department", "role", "salary"}
        if detail not in allowed_fields:
            return False, "Invalid detail."

        if detail == "salary":
            new_value = float(new_value)
            if new_value < 0:
                return False, "Salary cannot be negative."
        else:
            new_value = str(new_value).strip()
            if not new_value:
                return False, f"{detail.capitalize()} cannot be empty."

        with get_connection() as conn:
            cursor = conn.execute(
                f"UPDATE employees SET {detail} = ? WHERE id = ?",
                (new_value, emp_id)
            )

            if cursor.rowcount == 0:
                return False, "Employee not found."

        return True, f"Employee {detail} updated successfully."

    except ValueError:
        if str(detail).strip().lower() == "salary":
            return False, "Salary must be a valid number."
        return False, "Employee ID must be a number."
    except sqlite3.Error as e:
        return False, f"Database error: {e}"


def delete_employee(emp_id):
    try:
        emp_id = int(emp_id)

        with get_connection() as conn:
            cursor = conn.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
            if cursor.rowcount == 0:
                return False, "Employee not found."

        return True, "Employee deleted successfully."

    except ValueError:
        return False, "Employee ID must be a number."
    except sqlite3.Error as e:
        return False, f"Database error: {e}"


def search_by_department(department):
    try:
        if not str(department).strip():
            return False, "Department cannot be empty."

        with get_connection() as conn:
            rows = conn.execute("""
                SELECT * FROM employees
                WHERE department = ? COLLATE NOCASE
                ORDER BY id
            """, (department.strip(),)).fetchall()

        return True, rows

    except sqlite3.Error as e:
        return False, f"Database error: {e}"


def get_employee_by_id(emp_id):
    try:
        emp_id = int(emp_id)

        with get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM employees WHERE id = ?",
                (emp_id,)
            ).fetchone()

        if row is None:
            return False, "Employee not found."

        return True, row

    except ValueError:
        return False, "Employee ID must be a number."
    except sqlite3.Error as e:
        return False, f"Database error: {e}"
