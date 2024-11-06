"use client";

import { Button } from "@/components/shared/Button";
import { Book } from "@/types/book";
import api from "@/utils/axios";
import Image from "next/image";

interface BookCardProps {
  book: Book;
}

export function BookCard({ book }: BookCardProps) {
  const addToCart = async (book: Book) => {
    const response = await api.post("/cart/items", {
      book: book.id,
    });
    console.log(response.data);
  };

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
        <span className='text-lg font-bold text-accent'>{book.price}</span>
        <Button
          onClick={() => addToCart(book)}
          className='font-bold py-2 px-4 rounded-lg transition duration-300'
        >
          Add to Cart
        </Button>
      </div>
    </div>
  );
}
