# sport-booker
SportBooker is your ultimate solution for hassle-free sports facility reservations. 
Easily find and book sports venues based on location, availability, and activity type. 
With secure payment options and convenient notifications, managing your sports bookings has never been easier. Join the community of active individuals and facilities today with SportBooker!

## Project Metadata

- **Name**: sport-booker
- **Version**: 0.0.1
- **Authors**: Raf, Bert
- **License**: GNU General Public License v3.0
- **Requires Python**: >=3.11
- **Dependencies**:
  - sqlalchemy
  - sqlalchemy-utils
- **Optional Dependencies**:
  - mysql: mysqlclient

## Installation

To install this project, follow these steps:
1. Make sure Python 3 is installed on your system. If not, you can download and install Python from [python.org](https://www.python.org/).
2. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/bert-pxl/sport-booker.git
    ```
3. Navigate to the cloned directory:
    ```bash
    cd sport-booker
    ```
4. Install the required dependencies using pip:

   ```bash
   pip install -e .
   ```
5. Optional when using mysal
    ```bash
    pip install -e .[mysql]
    ```
## Usage

To run the project, execute the following command:
```bash
python main.py
```
This will start the application with the configured settings.

## Database

The project is compatible with mysql

![Database Schema](/docs/database/schema.png)

## Analyse

During the initial analysis phase, the project requirements and features were prioritized using the MoSCoW method (Must-have, Should-have, Could-have, Won't-have). This prioritization helped in defining the project scope and determining the essential features for the initial release.

[MoSCoW analysis](/docs/Moscow.md)

## Contributing

Contributions to this project are welcome. You can fork this repository and then submit a pull request with your changes.

## Issues

If you encounter any issues with Sport Booker, please report them on the [issues page](https://github.com/bert-pxl/sport-booker/issues) of this repository.

## License

Sport Booker is licensed under the [GNU General Public License v3.0](https://opensource.org/licenses/GPL-3.0). See the `LICENSE` file for more information.

## Project Information

- **Homepage**: [https://github.com/bert-pxl/sport-booker](https://github.com/bert-pxl/sport-booker)
- **Issues**: [https://github.com/bert-pxl/sport-booker/issues](https://github.com/bert-pxl/sport-booker/issues)
