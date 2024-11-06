import React from "react";
import CartItemCard, { CartItemCardProps } from "./CartItem";

type CartItemListProps = {
  items: CartItemCardProps[];
  changeQuantity: (id: number, quantity: number) => void;
};

export const CartItemList: React.FC<CartItemListProps> = ({
  items,
  changeQuantity,
}) => {
  return (
    <div className='flex flex-col gap-4'>
      {items.map((item) => (
        <CartItemCard key={item.id} {...item} changeQuantity={changeQuantity} />
      ))}
    </div>
  );
};
