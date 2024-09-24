"use client";

import Image from "next/image";
import { Book } from "@/types/book";

interface BookCardProps {
  book: Book;
}

export function BookCard({ book }: BookCardProps) {
  return (
    <div className='bg-primary border-4 border-primary shadow-md rounded-lg p-4 flex flex-col'>
      <Image
        src={book.image || ""}
        alt={book.title}
        width={300}
        height={300}
        unoptimized
        className='w-full h-48 object-cover rounded-lg mb-4'
      />
      <h2 className='text-xl font-bold text-accent mb-2'>{book.title}</h2>
      <p className='text-sm text-light mb-1'>{book.genres.join(", ")}</p>
      <p className='text-sm text-light mb-1'>{book.publicationDate}</p>
      <p className='text-sm text-light mb-2'>{book.authors.join(", ")}</p>
      <div className='mt-auto flex justify-between items-center'>
        <span className='text-lg font-bold text-accent'>${book.price}</span>
        <button className='bg-accent text-primary hover:bg-secondary hover:text-accent font-bold py-2 px-4 rounded-lg transition duration-300'>
          Add to Cart
        </button>
      </div>
    </div>
  );
}
