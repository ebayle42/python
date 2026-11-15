def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10/0
    elif operation_number == 2:
        open('/non/existent/file')
    elif operation_number == 3:
        "garden" + 1
    return


def test_error_types() -> None:
    operations = 0
    while operations <= 4:
        print(f"Testing operation {operations}...")
        try:
            garden_operations(operations)
            print("Operation completed successfully")
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")
        operations += 1
        try:
            garden_operations(0)
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError):
            pass


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print()
    print("All error types tested successfully!")
