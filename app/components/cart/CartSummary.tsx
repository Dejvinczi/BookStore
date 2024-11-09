'use client';

import Button from '@/components/shared/Button';
import Input from '@/components/shared/Input';
import { ApiError } from '@/types/api';
import { Cart } from '@/types/cart';
import api from '@/utils/axios';
import { useRouter } from 'next/navigation';
import { useState } from 'react';

export interface CartSummaryProps {
  cart: Cart;
}

interface FormErrors {
  address: string;
  general: string;
}

const CartSummary = ({ cart }: CartSummaryProps) => {
  const [address, setAddress] = useState<string>('');
  const [errors, setErrors] = useState<FormErrors>({} as FormErrors);
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setErrors({} as FormErrors);

    try {
      await api.post('/orders', {
        address,
      });

      router.push('/orders');
    } catch (error) {
      const err = error as ApiError;
      if (err.response) {
        if (err.response.status === 400) {
          if (err.response.data.detail) {
            setErrors({ ...errors, general: err.response.data.detail });
          } else {
            setErrors({ ...errors, ...err.response.data });
          }
        }
      } else {
        setErrors({
          ...errors,
          general: 'An unexpected error occurred. Please try again.',
        });
      }
      console.error('Login failed', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-4">
      {errors.general && <div className="text-red-500 text-sm">{errors.general}</div>}
      <Input
        label="Address"
        className="w-full px-3 py-2 rounded-md bg-secondary placeholder-grey-400 focus:ring-4 focus:ring-accent"
        type="text"
        id="address"
        value={address}
        onChange={(e) => setAddress(e.target.value)}
        disabled={!cart.items.length}
        error={errors.address}
      />
      <div className="flex justify-between items-center">
        <span className="text-lg font-bold text-light">Total: {cart.totalPrice}</span>
        <Button
          type="submit"
          className="font-bold py-2 px-4 rounded-lg transition duration-300"
          disabled={!cart.items.length}
        >
          Submit Order
        </Button>
      </div>
    </form>
  );
};

export default CartSummary;
