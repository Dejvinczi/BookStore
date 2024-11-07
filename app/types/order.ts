import { Book } from "@/types/book";

export interface Order {
  id: number;
  no: string;
  address: string;
  status: string;
  totalPrice: string;
}

export interface OrderItem {
  id: number;
  book: Book;
  quantity: number;
  price: string;
}

export interface OrderDetail extends Order {
  items: Array<OrderItem>;
}

export interface OrderApiResponse {
  count: number;
  previous: string | null;
  next: string | null;
  results: Array<Order>;
}

export interface OrderDetailResponse extends OrderDetail {}
