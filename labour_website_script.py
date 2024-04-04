import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def download_monthly_progress_report(url):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Open URL
        driver.get(url)

        # Find and click on the "Documents" menu
        documents_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Documents')]")))
        documents_menu.click()

        # Find and download the Monthly Progress Report
        monthly_progress_report_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Monthly Progress Report")))
        monthly_progress_report_link.click()

    finally:
        # Close the browser
        driver.quit()

def download_photo_gallery_images(url, num_images):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Open URL
        driver.get(url)

        # Find and click on the "Media" menu
        media_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Media')]")))
        media_menu.click()

        # Find and click on the "Photo Gallery" submenu
        photo_gallery_submenu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Photo Gallery')]")))
        photo_gallery_submenu.click()

        # Create a folder to store downloaded images
        folder_name = "photo_gallery_images"
        os.makedirs(folder_name, exist_ok=True)

        # Find and download the images
        image_links = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='gallery-images']//img")))
        for i, link in enumerate(image_links[:num_images]):
            image_src = link.get_attribute("src")
            image_name = f"image_{i+1}.jpg"
            image_path = os.path.join(folder_name, image_name)

            # Download image
            driver.execute_script(f"window.open('{image_src}', '_blank');")
            time.sleep(1)  # Add a delay to ensure the new window is loaded
            driver.switch_to.window(driver.window_handles[-1])
            with open(image_path, "wb") as file:
                file.write(driver.find_element(By.TAG_NAME, "img").screenshot_as_png)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    # Task 1: Download Monthly Progress Report
    print("Task 1:")
    download_monthly_progress_report("https://labour.gov.in/")
    print("\nMonthly Progress Report downloaded successfully.")

    # Task 2: Download 10 photos from Photo Gallery
    print("Task 2:")
    download_photo_gallery_images("https://labour.gov.in/", num_images=10)
    print("\n10 photos downloaded from Photo Gallery.")
