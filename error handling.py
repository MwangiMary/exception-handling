def file_read_write():
    try:
        # Open "outputfile.txt"
        with open("outputfile.txt", "r", encoding="utf-8") as f:
            content = f.read()

        # Print the contents
        print(content)

    except FileNotFoundError:
        print("❌ File not found.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


file_read_write()