import java.util.ArrayList;

public class Borrower {

    private ArrayList<Book> books;

    public Borrower(){
        this.books = new ArrayList<>();
    }

    public void takeBookFromLibrary(Library library) {
        Book book = library.takeBookFromLibrary();
    }

    public int bookCount() {
        return this.books.size();
    }

    public void addBook(Book book) {
        this.books.add(book);
    }
}
