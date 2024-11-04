"use client";

import BookList from "@/components/books/BookList";
import { Pagination } from "@/components/shared/Pagination";
import { Book, BookApiResponse } from "@/types/book";
import api from "@/utils/axios";
import { useEffect, useState } from "react";

export default function BooksPage() {
  const [books, setBooks] = useState<Book[]>([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalItems, setTotalItems] = useState(0);
  const [hasNext, setHasNext] = useState(false);
  const [hasPrevious, setHasPrevious] = useState(false);
  const ITEMS_PER_PAGE = 8;

  useEffect(() => {
    fetchBooks(currentPage);
  }, [currentPage]);

  const fetchBooks = async (page: number) => {
    try {
      const response = await api.get<BookApiResponse>("/books", {
        params: {
          limit: ITEMS_PER_PAGE,
          offset: (page - 1) * ITEMS_PER_PAGE,
        },
      });

      setBooks(response.data.results);
      setTotalItems(response.data.count);
      setHasNext(!!response.data.next);
      setHasPrevious(!!response.data.previous);
    } catch (error) {
      console.error("Failed to fetch books:", error);
    }
  };

  const totalPages = Math.ceil(totalItems / ITEMS_PER_PAGE);

  const handlePageChange = (page: number) => {
    setCurrentPage(page);
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return (
    <div className='container mx-auto py-8 px-4'>
      <BookList books={books} />
      {totalPages > 1 && (
        <Pagination
          currentPage={currentPage}
          totalPages={totalPages}
          onPageChange={handlePageChange}
          hasNext={hasNext}
          hasPrevious={hasPrevious}
        />
      )}
    </div>
  );
}
