from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class TestYouTube():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    
    def teardown_method(self, method):
        self.driver.quit()

    def test_youtube(self):
        self.driver.get("https://www.youtube.com")
        
        assert "YouTube" in self.driver.title
        print("YouTube opened successfully!")
        
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.send_keys("Selenium Python Tutorial")
        search_box.send_keys(Keys.RETURN)
        print("Search performed successfully!")

        wait = WebDriverWait(self.driver, 10)
        first_video = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ytd-video-renderer")))
        first_video.click()
        print("Clicked the first video!")

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "html5-video-player")))
        print("Video is playing successfully!")

        self.driver.save_screenshot("youtube_test.png")
        print("Screenshot taken!")
        
def convert_selenium_script(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        converted_script = []
        converted_script.append("# Converted Selenium Test Report\n")
        converted_script.append("### Test Steps:\n")

        for line in lines:
            line = line.strip()
            if "driver.get(" in line:
                url = line.split('"')[1]
                converted_script.append(f"- Open website: {url}\n")
            elif ".find_element" in line:
                if "By.ID" in line:
                    element = line.split('"')[1]
                    converted_script.append(f"- Locate element by ID: {element}\n")
                elif "By.CLASS_NAME" in line:
                    element = line.split('"')[1]
                    converted_script.append(f"- Locate element by Class Name: {element}\n")
            elif "assert" in line:
                converted_script.append(f"- Assertion: {line}\n")
            elif ".click()" in line:
                converted_script.append(f"- Click action performed on an element\n")
        
        with open(output_file, 'w') as f:
            f.writelines(converted_script)
        
        print(f"Conversion complete! Output saved in {output_file}")
    
    except Exception as e:
        print(f"Error: {e}")

convert_selenium_script("test_script.py", "converted_test_report.txt")


