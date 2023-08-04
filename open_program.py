import pygetwindow as gw
import sys

def open_and_activate_window(title):
    try:
        window_to_open = None

        for window in gw.getAllTitles():
            if title in window:
                window_to_open = gw.getWindowsWithTitle(window)[0]
                break

        if window_to_open:
            # Maximize the window, unhide it, and bring it to the front
            window_to_open.maximize()
            window_to_open.activate()
            return True
        else:
            print(f"Window '{title}' not found.")
            return False
    except Exception as e:
        print(f"Erro: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python open_program.py <title_of_program>")
        sys.exit(1)

    program_title = sys.argv[1]
    success = open_and_activate_window(program_title)

    if success:
        sys.exit(0)
    else:
        sys.exit(1)
