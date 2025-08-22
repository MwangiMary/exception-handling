def file_read_write():
    try:
        # Just a simple risky operation
        with open("output file.py", "r", encoding="utf-8") as f:
            content = f.read()

        print(content)

    except FileNotFoundError:
        print(" File not found.")
    except Exception as e:
        print(f" Unexpected error: {e}")


file_read_write()
