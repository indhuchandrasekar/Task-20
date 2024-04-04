from selenium import webdriver

def open_and_display_window_ids(url):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Open URL
        driver.get(url)

        # Get current window handle
        original_window = driver.current_window_handle

        # Click on "FAQ" anchor tag to open new window
        faq_link = driver.find_element_by_link_text("FAQ")
        faq_link.click()

        # Click on "Partners" anchor tag to open new window
        partners_link = driver.find_element_by_link_text("Partners")
        partners_link.click()

        # Get handles of all opened windows
        all_windows = driver.window_handles

        # Display window IDs
        print("Window IDs:")
        for window in all_windows:
            print(window)

        # Close the new windows and switch back to the original window
        for window in all_windows:
            if window != original_window:
                driver.switch_to.window(window)
                driver.close()

        driver.switch_to.window(original_window)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    # Task 1: Open and display window IDs
    print("Task 1:")
    open_and_display_window_ids("https://www.cowin.gov.in/")
