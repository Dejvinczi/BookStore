import { Book } from '@/types/book';

export interface Cart {
  items: Array<CartItem>;
  totalPrice: number;
}
export interface CartItem {
  id: number;
  quantity: number;
  totalPrice: number;
  book: Book;
}
