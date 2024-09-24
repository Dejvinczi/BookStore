"use client";

import { useEffect, useState } from "react";
import { Book, BookApiResponse } from "@/types/book";
import api from "@/utils/axios";
import BookList from "@/components/books/BookList";

export default function BooksPage() {
  const [books, setBooks] = useState<Book[]>([]);

  useEffect(() => {
    fetchBooks();
  }, []);

  const fetchBooks = async () => {
    try {
      const response = await api.get<BookApiResponse>("/books");
      setBooks(response.data.results);
    } catch (error) {
      console.error("Failed to fetch books:", error);
    }
  };

  return (
    <div className='container mx-auto py-8 px-4'>
      <h1 className='text-3xl sm:text-4xl font-bold mb-6 text-light'>
        Available Books
      </h1>
      <BookList books={books} />
    </div>
  );
}
