import { CartItem } from '@/types/cart';
import CartItemCard from './CartItem';

interface CartItemListProps {
  cartItems: Array<CartItem>;
  changeQuantity: (id: number, quantity: number) => void;
}

export const CartItemList = ({ cartItems, changeQuantity }: CartItemListProps) => {
  return (
    <div className="flex flex-col gap-4">
      {cartItems.map((cartItem) => (
        <CartItemCard key={cartItem.id} cartItem={cartItem} changeQuantity={changeQuantity} />
      ))}
    </div>
  );
};
