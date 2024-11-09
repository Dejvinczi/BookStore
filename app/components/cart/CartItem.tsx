import Button from '@/components/shared/Button';
import { CartItem } from '@/types/cart';
import Image from 'next/image';

interface CartItemCardProps {
  cartItem: CartItem;
  changeQuantity: (id: number, quantity: number) => void;
}

const CartItemCard = ({ cartItem, changeQuantity }: CartItemCardProps) => {
  return (
    <div className="flex items-center justify-between p-4 border-b">
      <Image
        src={cartItem.book.image || ''}
        alt={cartItem.book.title}
        width={100}
        height={100}
        unoptimized
        className="w-16 h-16 object-cover rounded-lg"
      />
      <div className="flex-1 px-4">
        <h2 className="text-lg font-bold">{cartItem.book.title}</h2>
        <p className="text-gray-600 text-sm">{cartItem.book.genres.join(', ')}</p>
        <p className="text-gray-500 text-sm">{cartItem.book.publicationDate}</p>
      </div>
      <div className="flex flex-col items-end gap-2">
        <p className="font-semibold text-lg text-accent">{cartItem.totalPrice}</p>
        <div className="flex items-center rounded-lg overflow-hidden">
          <Button
            onClick={() => changeQuantity(cartItem.id, cartItem.quantity - 1)}
            disabled={cartItem.quantity <= 0}
            className="w-8 h-8 flex items-center justify-center"
          >
            <span className="text-lg font-bold">−</span>
          </Button>
          <p className="text-lg font-semibold px-2">{cartItem.quantity}</p>
          <Button
            onClick={() => changeQuantity(cartItem.id, cartItem.quantity + 1)}
            className="w-8 h-8 flex items-center justify-center"
          >
            <span className="text-lg font-bold">+</span>
          </Button>
        </div>
      </div>
    </div>
  );
};

export default CartItemCard;
