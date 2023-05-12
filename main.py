import os
import keyboard
import pyperclip3

right_align: bool = False  # if true then left, if false then right
terminal_size = os.get_terminal_size()
user_inputs = []
# [{
# "right_align": false
# "message": string
# }, ...]


def echoLeft(message: str):
    appendAndClear(message)
    leftFormatter(message)


def leftFormatter(message: str):
    print(message)


def echoRight(message: str):
    appendAndClear(message)
    rightFormatter(message)


def rightFormatter(message: str):
    half_width = int(terminal_size.columns / 2)
    print(f"{f'{message}' : >{half_width}}")


def appendAndClear(message: str):
    global right_align
    user_inputs.append({"message": message, "right_align": right_align})
    clearScreen()
    for line in user_inputs:
        if line["right_align"] == True:
            rightFormatter(line["message"])
        else:
            leftFormatter(line["message"])


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    clearScreen()
    global right_align
    global user_inputs
    message = ""
    print(
        "Type some text. Press TAB to toggle alignment. Press CTRL-S to write to output.txt\n\n"
    )

    while True:
        # try:

        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key: str = str(event.name)
            if key == "tab":
                right_align = not right_align
            elif key == "enter":
                if right_align == True:
                    echoRight(message)
                elif right_align == False:
                    echoLeft(message)
                message = ""
            elif key == "ctrl+s":
                with open("output.txt", "a") as f:
                    for line in user_inputs:
                        if line["right_align"]:
                            print(f"\t{line['message']}", file=f)
                        else:
                            print(line["message"], file=f)
                print("Successfully saved file")
            else:
                if len(key) > 1:
                    continue

                clearScreen()
                message += str(key)

    # except ValueError:
    #   print('skipped')


if __name__ == "__main__":
    main()
