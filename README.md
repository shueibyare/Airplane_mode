### Airplane Mode

Airplane Mode – Airline Management System
Project Overview
Airplane Mode is a Frappe-based airline management system that simulates real-world flight booking and operations. It manages airplanes, flights, passengers, tickets, and add-ons while demonstrating core ERP concepts such as document modeling, workflows, and server-side business logic.
The project was built as part of a Frappe development exercise to demonstrate practical backend engineering skills, data modeling, and business process automation.
---
Features
Flight Management
- Create and manage airplanes and flight schedules
- Track flight source, destination, and timings
- Flight status workflow (Draft → Boarded → Completed)
Ticket Booking System
- Book tickets linked to specific flights
- Automatic seat assignment (e.g. `21A`, `88E`)
- Passenger management
Add-ons System
- Support for multiple add-ons per ticket (e.g. meals, seat selection)
- Dynamic pricing based on selected add-ons
- Child table implementation for flexible add-ons
Pricing Logic
- Flight price + add-ons = total ticket amount
- Automatic recalculation using server-side controllers
Business Rules
- Prevent invalid ticket submission based on flight status
- Ensure data consistency using validation hooks
- Remove duplicate add-ons per ticket
Data Migration
- Patch system to populate missing seat data for existing tickets
---
Tech Stack

- Frappe Framework (v15)
- Python
- MariaDB
- JavaScript (Frappe Client Scripts)
- Bench CLI
---
System Architecture

```text
Airplane
   ↓
Airplane Flight
   ↓
Airplane Ticket
   ↓
Add-ons (Child Table)

Working with DocTypes

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app airplane_mode
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/airplane_mode
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
