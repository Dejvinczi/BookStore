import { Button } from "@/components/shared/Button";
import { Book } from "@/types/book";
import Image from "next/image";

export interface CartItemCardProps {
  id: number;
  book: Book;
  quantity: number;
  totalPrice: number;
  changeQuantity: (id: number, quantity: number) => void;
}

const CartItemCard: React.FC<CartItemCardProps> = ({
  id,
  book,
  quantity,
  totalPrice,
  changeQuantity,
}) => {
  return (
    <div className='flex items-center justify-between p-4 border-b'>
      <Image
        src={book.image || ""}
        alt={book.title}
        width={100}
        height={100}
        unoptimized
        className='w-16 h-16 object-cover rounded-lg'
      />
      <div className='flex-1 px-4'>
        <h2 className='text-lg font-bold'>{book.title}</h2>
        <p className='text-gray-600 text-sm'>{book.genres.join(", ")}</p>
        <p className='text-gray-500 text-sm'>{book.publicationDate}</p>
      </div>
      <div className='flex flex-col items-end gap-2'>
        <p className='font-semibold text-lg text-accent'>{totalPrice}</p>
        <div className='flex items-center rounded-lg overflow-hidden'>
          <Button
            onClick={() => changeQuantity(id, quantity - 1)}
            disabled={quantity <= 0}
            className='w-8 h-8 flex items-center justify-center'
          >
            <span className='text-lg font-bold'>−</span>
          </Button>
          <p className='text-lg font-semibold px-2'>{quantity}</p>
          <Button
            onClick={() => changeQuantity(id, quantity + 1)}
            className='w-8 h-8 flex items-center justify-center'
          >
            <span className='text-lg font-bold'>+</span>
          </Button>
        </div>
      </div>
    </div>
  );
};

export default CartItemCard;
