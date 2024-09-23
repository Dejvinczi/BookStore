"use client";
import { useEffect, useState } from "react";
import Image from "next/image";
import { Book, BookApiResponse } from "@/types/book";
import api from "@/utils/axios";

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
      <h1 className='text-3xl sm:text-4xl font-bold mb-6 text-stone-700'>
        Available Books
      </h1>
      <div className='grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6'>
        {books.map((book) => (
          <div
            key={book.id}
            className='bg-cream-100 shadow-md rounded-lg p-4 flex flex-col'
          >
            <Image
              src={book.image || ""}
              alt={book.title}
              width={300}
              height={300}
              unoptimized
              className='w-full h-48 object-cover rounded-lg mb-4'
            />
            <h2 className='text-xl font-bold text-stone-700 mb-2'>
              {book.title}
            </h2>
            <p className='text-sm text-stone-600 mb-1'>
              {book.genres.join(", ")}
            </p>
            <p className='text-sm text-stone-600 mb-1'>
              {book.publicationDate}
            </p>
            <p className='text-sm text-stone-600 mb-2'>
              {book.authors.join(", ")}
            </p>
            <div className='mt-auto flex justify-between items-center'>
              <p className='text-xl font-bold text-azure-600'>${book.price}</p>
              <button
                onClick={() => {}}
                className='bg-azure-500 hover:bg-azure-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300'
              >
                Add to Cart
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
