# Create a RESTful API using Flask to perform CRUD operations on resources like books or movies.
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"},
]
@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = {
            "id": len(books) + 1,
            "title": request.form['title'],
            "author": request.form['author'],
        }
        books.append(new_book)
        return redirect('/')
    return render_template('add.html')

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if not book:
        return redirect('/')
    if request.method == 'POST':
        book['title'] = request.form['title']
        book['author'] = request.form['author']
        return redirect('/')
    return render_template('edit.html', book=book)

@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return redirect('/')
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify({"book": book})
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route('/api/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = {
        "id": len(books) + 1,
        "title": data.get("title"),
        "author": data.get("author"),
    }
    books.append(new_book)
    return jsonify({"book": new_book}), 201

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        book['title'] = data.get('title', book['title'])
        book['author'] = data.get('author', book['author'])
        return jsonify({"book": book})
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book_api(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({"message": "Book deleted successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
