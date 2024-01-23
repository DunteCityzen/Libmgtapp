from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wasomi.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='Available')

    def __repr__(self):
        return '<Book %r>' % self.id


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    debt = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Member %r>' % self.id


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrow_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime, nullable=True)
    fee = db.Column(db.Integer)
    #Foreign Keys
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    #Relationships
    member = db.relationship('Member', backref='transactions')
    book = db.relationship('Book', backref='transactions')

    def __repr__(self):
        return '<Transaction %r>' % self.id
    
    def calc_fee(self):
        if self.return_date is not None:
            calculated_fee = (self.return_date - self.borrow_date).days * 50
            self.fee = calculated_fee
            db.session.commit()
            return calculated_fee
        else:
            current_date = datetime.utcnow()
            calculated_fee = (current_date - self.borrow_date).days * 50
            self.fee = calculated_fee
            db.session.commit()
            return calculated_fee

def drop_tables():
    with app.app_context():
        db.drop_all()

def create_tables():
    with app.app_context():
        db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        booktitle = request.form['title']
        bookauthor = request.form['author']
        #create new book object
        new_book = Book(title=booktitle, author=bookauthor)

        try:
            db.session.add(new_book)
            db.session.commit()
        except:
            return 'An error occurred when creating new book'
        return redirect('/')
    
    elif request.method == 'GET':
        books = Book.query.order_by(Book.id).all()
        return render_template('index.html', books=books)
    else:
        return 'HTTP request Method Not Allowed'
    

@app.route('/members', methods=['GET', 'POST'])
def members():
    if request.method == 'POST':
        member_name = request.form['name']
        #create new member object
        new_member = Member(name=member_name)
        
        try:
            db.session.add(new_member)
            db.session.commit()
        except:
            return 'An error occured while creating new member'
        return redirect('/members')
        
    elif request.method == 'GET':
        members = Member.query.order_by(Member.id).all()
        for member in members:
            leases = Transaction.query.where(Transaction.member_id == member.id).all()
            for lease in leases:
                member.debt += lease.fee
        return render_template('members.html', members=members)
    else:
        return 'HTTP request Method Not Allowed'
    

@app.route('/transactions', methods=['GET', 'POST'])
def transactions():
    if request.method == 'POST':
        memberid = request.form['member_id']
        bookid = request.form['book_id']

        member_exists = Member.query.where(Member.id == memberid).first()
        book_exists = Book.query.where(Book.id == bookid).first()
        
        if (member_exists and book_exists):
            if member_exists.debt <= 500:
                if book_exists.status == 'Rented out':
                    return 'Book is already rented out'
                #create new transaction object
                new_transaction = Transaction(member_id=memberid, book_id=bookid)

                try:
                    book_exists.status = 'Rented out'
                    db.session.add(new_transaction)
                    db.session.commit()
                    return redirect('/transactions')
                except:
                    return 'An error occured while leasing the book'
            else:
                return 'Member passed debt limit'
        else:
            return 'MemberId or BookId does not exist'

    elif request.method == 'GET':
        transactions = Transaction.query.order_by(Transaction.borrow_date).all()
        return render_template('transactions.html', transactions=transactions)
    
    else:
        return 'HTTP request Method Not Allowed'
    
@app.route('/books/<int:id>/delete')
def deleteBook(id):
    book_to_delete = Book.query.get_or_404(id)

    try:
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'An error occured deleting the task'
    
@app.route('/members/<int:id>/delete')
def deleteMember(id):
    member_to_delete = Member.query.get_or_404(id)

    try:
        db.session.delete(member_to_delete)
        db.session.commit()
        return redirect('/members')
    except:
        return 'An error occured deleting the member'
    
@app.route('/transactions/<int:id>/update')
def updateTransaction(id):
    transaction = Transaction.query.get_or_404(id)
    member = Member.query.where(Member.id == transaction.member_id).first()
    book = Book.query.where(Book.id == transaction.book_id).first()

    try:
        member.debt = 0
        book.status = 'available'
        transaction.return_date = datetime.utcnow()
        db.session.commit()
        return redirect('/transactions')
    except:
        return 'An error occured updating the transaction'
    


if __name__ == '__main__':
    create_tables()
    app.run(debug=True)