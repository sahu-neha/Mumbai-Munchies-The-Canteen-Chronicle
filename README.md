## Mumbai Munchies: The Canteen Chronicle

The Mumbai Munchies application is designed to automate the snack inventory management and sales tracking system for the canteen of Mumbai University. It provides a command-line interface for canteen staff to perform various tasks efficiently.

### Features

1. **Snack Inventory**: Staff can add snacks to the inventory by providing the snack ID, name, price, and availability. The snack details are stored in memory using a list of dictionaries.

2. **Remove Snack**: Staff can remove a snack from the inventory by specifying the snack ID. If the snack is found, it is removed from the inventory.

3. **Update Snack Availability**: Staff can update the availability of a snack by providing the snack ID. They can specify whether the snack is available or not (using "yes" or "no"). The availability status of the snack is updated accordingly.

4. **Sell Snack**: Staff can sell a snack by entering the snack ID. If the snack is available, it is marked as sold by updating its availability status. If the snack is unavailable, a corresponding message is displayed.

5. **List All Snacks**: Staff can view the complete snack inventory, including the snack ID, name, price, and availability. If the inventory is empty, a relevant message is displayed.

6. **Error Handling**: The application handles invalid user inputs, such as entering an incorrect snack ID or choosing an invalid menu option. Appropriate error messages are displayed to guide the user.

### Getting Started

1. Make sure you have Python installed on your system (version 3.6 or above).

2. Clone the project repository or download the source code files.

3. Open a terminal or command prompt and navigate to the project directory.

4. Run the following command to start the application:

   ```
   python mumbai_munchies.py
   ```

5. Follow the on-screen instructions to interact with the application and manage the snack inventory.

### Usage

1. **Add a Snack**:

   - Enter the snack ID, name, price, and availability when prompted.
   - The snack will be added to the inventory.

2. **Remove a Snack**:

   - Enter the snack ID of the snack you want to remove.
   - If the snack is found in the inventory, it will be removed.

3. **Update Snack Availability**:

   - Enter the snack ID of the snack you want to update.
   - Specify whether the snack is available or not (using "yes" or "no").
   - The availability status of the snack will be updated.

4. **Sell a Snack**:

   - Enter the snack ID of the snack you want to sell.
   - If the snack is available, it will be marked as sold.
   - If the snack is unavailable, a corresponding message will be displayed.

5. **List All Snacks**:

   - Choose the option to list all snacks in the inventory.
   - The snack ID, name, price, and availability of each snack will be displayed.
   - If the inventory is empty, a message indicating no snacks are available will be shown.

6. **Exit**:
   - Choose the option to exit the application.

### Contribution

Contributions to the Mumbai Munchies project are welcome! If you find any issues or have ideas to enhance the functionality, feel free to open an issue or submit a pull request on the project repository.

### License

This project is licensed under the MIT License. You can find more information in the [LICENSE](LICENSE) file.

---

With Mumbai Munchies: The Canteen Chronicle, canteen staff at Mumbai University can streamline their snack inventory management and sales tracking. This Python
