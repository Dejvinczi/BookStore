import { Author } from "./author";
import { Genre } from "./genre";

export interface Book {
  id: number;
  title: string;
  authors: string[];
  genres: string[];
  publicationDate: string;
  image: string | null;
  price: string;
}

export interface BookDetail extends Omit<Book, "authors" | "genres"> {
  authors: Author[];
  genres: Genre[];
}

export interface BookApiResponse {
  count: number;
  previous: string | null;
  next: string | null;
  results: Array<Book>;
}

export interface BookDetailApiResponse extends BookDetail {}
