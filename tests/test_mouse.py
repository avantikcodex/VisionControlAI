from automation.mouse_controller import MouseController


def main():

    mouse = MouseController()

    print("=" * 60)
    print("MOUSE CONTROLLER TEST")
    print("=" * 60)

    print("\nChecking screen...")

    mouse.screen_size()

    print("\nChecking current mouse position...")

    mouse.position()

    print("\nMove the mouse to the center of the screen.")

    width, height = mouse.screen_size()

    if width and height:

        mouse.move(
            width // 2,
            height // 2,
            duration=0.5
        )

    mouse.wait(1)

    print("\nTesting left click...")

    mouse.click()

    mouse.wait(1)

    print("\nTesting right click...")

    mouse.right_click()

    mouse.wait(1)

    print("\nTesting double click...")

    mouse.double_click()

    mouse.wait(1)

    print("\nTesting scroll up...")

    mouse.scroll_up(3)

    mouse.wait(1)

    print("\nTesting scroll down...")

    mouse.scroll_down(3)

    print("\nMOUSE CONTROLLER TEST FINISHED")


if __name__ == "__main__":
    main()