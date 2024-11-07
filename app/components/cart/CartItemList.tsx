import { CartItem } from "@/types/cart";
import React from "react";
import CartItemCard from "./CartItem";

interface CartItemListProps {
  cartItems: Array<CartItem>;
  changeQuantity: (id: number, quantity: number) => void;
}

export const CartItemList: React.FC<CartItemListProps> = ({
  cartItems,
  changeQuantity,
}) => {
  return (
    <div className='flex flex-col gap-4'>
      {cartItems.map((cartItem) => (
        <CartItemCard
          key={cartItem.id}
          cartItem={cartItem}
          changeQuantity={changeQuantity}
        />
      ))}
    </div>
  );
};
