
# Selenium Web Testing Project

This project demonstrates a basic setup for automated web testing using Selenium WebDriver with Firefox in headless mode. It's designed to run automated browser tests in a cloud environment.

## Overview

The project consists of two main components:

1. A WebDriver setup function (`create_webdriver()`)
2. A test function (`test_webdriver()`)

### Key Features

- Headless Firefox browser automation
- Configured for cloud environment compatibility
- Basic website testing functionality

## How It Works

The `main.py` script contains:

1. `create_webdriver()`: Configures Firefox WebDriver with the following options:
   - Headless mode (runs without GUI)
   - GPU disabled
   - Sandbox disabled for cloud compatibility

2. `test_webdriver()`: Demonstrates basic WebDriver functionality by:
   - Creating a new WebDriver instance
   - Navigating to example.com
   - Printing the page title
   - Properly closing the browser

## Dependencies

The project uses:
- selenium (4.24.0): For browser automation
- webdriver-manager (4.0.2): For managing WebDriver binaries

## Running the Project

The code will automatically run when you click the Run button, which will:
1. Launch a headless Firefox instance
2. Navigate to example.com
3. Print the page title
4. Close the browser

## Note

This setup is specifically configured for Replit's cloud environment and includes the necessary configurations to run Selenium with Firefox in headless mode.
