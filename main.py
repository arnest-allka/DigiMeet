from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host=app.config['SERVER_HOST'], port=app.config['SERVER_PORT'])