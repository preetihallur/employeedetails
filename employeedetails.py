def get_employee_details(name: str, emp_id: str, department: str, salary: float) -> str:
    """
    Returns a formatted string containing employee details.
    """
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )


# Example usage (optional):
if __name__ == "__main__":
    print(get_employee_details("John Doe", "E123", "HR", 50000))
