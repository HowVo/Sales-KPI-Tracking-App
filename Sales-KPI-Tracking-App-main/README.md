# Sales-KPI-Tracking-App

## Overview

The Sales KPI Tracking App is a tool designed to help manage and evaluate the performance of sales representatives. It allows users to add, update, and remove sales reps, as well as track key performance indicators (KPIs) such as show count, offer count, close count, cash per call, and revenue per call.

## Features

- Add new sales representatives
- Update KPI data for sales representatives
- Remove sales representatives
- Display KPIs for selected sales representatives
- Compare revenue per call among sales representatives
- Data stored using SQLite
- Modular Design: Separate modules for database, sales rep management, and KPI calculations.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/Sales-KPI-Tracking-App.git
   cd Sales-KPI-Tracking-App
   ```

2. Install the required dependencies:

   ```sh
   pip install tk matplotlib sqlite3
   ```

3. Run the application:
   ```sh
   python main.py
   ```

## Usage

1. **Add Sales Rep**: Enter the sales rep ID and name, then click "Add Sales Rep".
2. **Update KPI Data**: Select a sales rep from the list, enter the KPI data, and click "Update KPI Data".
3. **Remove Sales Rep**: Select a sales rep from the list and click "Remove Sales Rep".
4. **Show KPIs**: Select a sales rep from the list and click "Show KPIs" to display their KPIs.
5. **Draw Revenue Comparison**: Click "Draw Revenue Comparison" to display a bar chart comparing revenue per call among sales reps.

## Dependencies

- Python 3.x
- Tkinter
- Matplotlib
- SQLite3

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
