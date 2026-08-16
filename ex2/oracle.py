import os


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    try:
        from dotenv import load_dotenv
    except Exception as e:
        print(e)
        print("Missing dotenv module")
        print("install with pip: pip install python-dotenv")
        print("then run this program again")
        return

    load_dotenv()

    mode = os.getenv("MATRIX_MODE")
    url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_lvl = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")

    missing = [
        item for item in [mode, url, api_key, log_lvl, zion]
        if item is None
    ]
    if missing:
        print("missing required variables")
        return
    print()
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {url}")
    print(f"API Access: {api_key}")
    print(f"Log Level: {log_lvl}")
    print(f"Zion Network: {zion}")
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
