from __future__ import print_function, absolute_import, division
from flask import redirect
import connexion
import sys

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# create a URL route in our application for "/"
@app.route('/')
def home():
    """
    Home page
    """
    return redirect('api/ui')


def main():
    if len(sys.argv) == 2:
        port = sys.argv[1]
    else:
        port = 5000
    print('Using port:', port)
    app.run(debug=True, port=port)


if __name__ == '__main__':
    main()
