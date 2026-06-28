from fastapi import FastAPI

app = FastAPI()

books = [
    {"id": 1, "title": "Python Basic", "quantity": 12},
    {"id": 2, "title": "FastAPI Beginner", "quantity": 3},
    {"id": 3, "title": "Clean Code", "quantity": 5},
    {"id": 4, "title": "Database Design", "quantity": 0},
    {"id": 5, "title": "Web API Design", "quantity": 20}
]

@app.get("/books/low-stock")
def get_LowStock():
    book_LowStock = []
   
    for bk in books:
        if bk["quantity"] <= 5:
            book_LowStock.append(bk)

    if not book_LowStock:
        return{
    "message": "Không có sách nào sắp hết hàng",
    "data": book_LowStock
}
    else:
        return {
            "books" : book_LowStock
        }