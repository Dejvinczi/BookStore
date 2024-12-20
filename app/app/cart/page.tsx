'use client';

import { CartItemList } from '@/components/cart/CartItemList';
import CartSummary from '@/components/cart/CartSummary';
import { Cart } from '@/types/cart';
import api from '@/utils/axios';
import { useEffect, useState } from 'react';

const CartPage = () => {
  const [cart, setCart] = useState<Cart>({
    items: [],
    totalPrice: 0,
  });

  useEffect(() => {
    fetchCart();
  }, []);

  const fetchCart = async () => {
    const response = await api.get('/cart');
    setCart(response.data);
  };

  const handleChangeQuantity = async (bookId: number, quantity: number) => {
    if (quantity <= 0) {
      await api.delete(`/cart/items/${bookId}`);
    } else {
      await api.patch(`/cart/items/${bookId}`, {
        quantity,
      });
    }
    fetchCart();
  };

  return (
    <div className="flex flex-col flex-1">
      <div className="flex flex-1">
        <div className="grid grid-cols-3 gap-4 w-full">
          <div className="col-span-2 flex flex-col rounded-xl p-4 bg-primary">
            <CartItemList cartItems={cart.items} changeQuantity={handleChangeQuantity} />
          </div>
          <div className="flex flex-col rounded-xl p-4 bg-primary">
            <CartSummary cart={cart} />
          </div>
        </div>
      </div>
    </div>
  );
};
export default CartPage;
