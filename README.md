# Email Project

This project demonstrates how to send an email using Gmail's SMTP server in Python. It uses the `smtplib` library to establish a connection with the SMTP server and send the email.

## Prerequisites

- Python 3.x
- `smtplib` library

## Setup

1. Clone the repository or download the project files.
2. Install the required dependencies by running the following command:

3. Update the `config.py` file with your Gmail account details:
- `USER`: Your Gmail email address.
- `APP_PASS`: Your Gmail app password.
- `HOST`: SMTP server hostname (default is `smtp.gmail.com`).
- `PORT`: SMTP server port (default is `587`).
- `REC_EMAIL`: Email address of the recipient.
4. Update the email content:
- Place your email content files in the `email_content` directory.
- Modify the `email_content` variable in the `send_email_from_gmail` function to specify the email content file you want to send.
5. Run the script:

## Usage

The `send_email_from_gmail` function in `send_email.py` is responsible for sending the email. It reads the content of the specified file and sends it as the body of the email.

You can customize the subject, recipient, and content directory by modifying the corresponding variables in the `send_email_from_gmail` function.

Make sure to enable access for less secure apps in your Gmail account settings or use an app password if two-factor authentication is enabled.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
