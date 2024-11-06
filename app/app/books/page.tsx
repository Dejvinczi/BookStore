"use client";

import BookFilters from "@/components/books/BookFilters";
import BookList from "@/components/books/BookList";
import { Pagination } from "@/components/shared/Pagination";
import { Book, BookApiResponse } from "@/types/book";
import api from "@/utils/axios";
import { useEffect, useState } from "react";

interface BookFilters {
  title: string;
  ordering: string;
  publicationDateAfter: string;
  publicationDateBefore: string;
}

export default function BooksPage() {
  const [books, setBooks] = useState<Book[]>([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalItems, setTotalItems] = useState(0);
  const [hasNext, setHasNext] = useState(false);
  const [hasPrevious, setHasPrevious] = useState(false);
  const [filters, setFilters] = useState<BookFilters>({
    title: "",
    ordering: "title",
    publicationDateAfter: "",
    publicationDateBefore: "",
  });

  const ITEMS_PER_PAGE = 8;

  useEffect(() => {
    const fetchBooks = async (page: number) => {
      try {
        const response = await api.get<BookApiResponse>("/books", {
          params: {
            limit: ITEMS_PER_PAGE,
            offset: (page - 1) * ITEMS_PER_PAGE,
            title: filters.title || undefined,
            ordering: filters.ordering || undefined,
            publication_date_after: filters.publicationDateAfter || undefined,
            publication_date_before: filters.publicationDateBefore || undefined,
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

    fetchBooks(currentPage);
  }, [currentPage, filters]);

  const totalPages = Math.ceil(totalItems / ITEMS_PER_PAGE);

  const handlePageChange = (page: number) => {
    setCurrentPage(page);
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const handleFiltersChange = (newFilters: BookFilters) => {
    setFilters(newFilters);
    setCurrentPage(1);
  };

  return (
    <div className='container mx-auto px 4'>
      <BookFilters onFiltersChange={handleFiltersChange} />
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
